import math
import random

import pygame
from variables import global_variables
from nn import NeuralNetwork
import numpy as np


class Player(pygame.sprite.Sprite):
    def __init__(self, game_mode):
        super().__init__()

        # loading images
        player_walk1 = pygame.image.load('Graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('Graphics/Player/player_walk_2.png').convert_alpha()

        # rotating -90 degree and scaling by factor of 0.5
        player_walk1 = pygame.transform.rotozoom(player_walk1, -90, 0.5)
        player_walk2 = pygame.transform.rotozoom(player_walk2, -90, 0.5)

        # flipping vertically
        player_walk1 = pygame.transform.flip(player_walk1, flip_x=False, flip_y=True)
        player_walk2 = pygame.transform.flip(player_walk2, flip_x=False, flip_y=True)

        self.player_walk = [player_walk1, player_walk2]

        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midleft=(177, 656))

        self.player_gravity = 'left'
        self.gravity = 10
        self.game_mode = game_mode

        if self.game_mode == "Neuroevolution":
            self.fitness = 0  # Initial fitness

            # TODO (Design your architecture here by changing the values)
            # layer_sizes = [4, 16, 1]
            layer_sizes = [5, 20, 1]

            self.nn = NeuralNetwork(layer_sizes)

    def create_input_vector(self, screen_width, screen_height, obstacles, player_x, player_y):

        if len(obstacles):
            target_position = [obstacles[0]['x'], obstacles[0]['y']]
        else:
            if player_x>380:
                target_position = [410, 660]
            else:
                target_position = [177, 660]
        
        dist = 233
        dist_right = 604 - player_x
        dist_left = player_x        
        left_gap = abs(player_x - dist - target_position[0])
        right_gap = abs(player_x + dist - target_position[0])
        d_distance = math.sqrt((player_x - target_position[0])**2 + (player_y - target_position[1])**2)


        vector_max = max([dist_right, right_gap, d_distance, dist_left, left_gap])

        return [dist_right/vector_max, right_gap/vector_max, d_distance/vector_max, dist_left/vector_max, left_gap/vector_max]


    # def create_input_vector(self, screen_width, screen_height, obstacles, player_x, player_y):

    #     player_x = player_x / screen_width
    #     player_y = player_y / screen_height
    #     obstacle1_x = 0
    #     obstacle1_y = 0
    #     obstacle2_x = 0
    #     obstacle2_y = 0

    #     if len(obstacles) == 1:
    #         obstacle1_x = player_x - obstacles[0]['x'] / screen_width
    #         obstacle1_y = player_y - obstacles[0]['y'] / screen_height
    #     elif len(obstacles) >= 2:
    #         obstacle2_x = player_x - obstacles[1]['x'] / screen_width
    #         obstacle2_y = player_y - obstacles[1]['y'] / screen_height
        
            
            
    #     input_vector = [player_x, player_y, obstacle1_x, obstacle1_y,obstacle2_x, obstacle2_y]
    #     input_vector = np.array(input_vector)

    #     return input_vector

    def think(self, screen_width, screen_height, obstacles, player_x, player_y):
        """
        Creates input vector of the neural network and determines the gravity according to neural network's output.

        :param screen_width: Game's screen width which is 604.
        :param screen_height: Game's screen height which is 800.
        :param obstacles: List of obstacles that are above the player. Each entry is a dictionary having 'x' and 'y' of
        the obstacle as the key. The list is sorted based on the obstacle's 'y' point on the screen. Hence, obstacles[0]
        is the first obstacle on the scene. It is also worthwhile noting that 'y' range is in [-100, 656], such that
        -100 means it is off screen (Topmost point) and 656 means in parallel to our player's 'y' point.
        :param player_x: 'x' position of the player
        :param player_y: 'y' position of the player
        """
        # TODO (change player's gravity here by calling self.change_gravity)

       

        # if output[0][0] < 0.5:
        #     self.change_gravity('right')
        # else:
        #     self.change_gravity('left')

        input = self.create_input_vector(screen_width, screen_height, obstacles, player_x, player_y)
        output = self.nn.forward(input)

        if output[0][0]>0.5:
            self.change_gravity('right')
        else:
            self.change_gravity('left')



    def change_gravity(self, new_gravity):
        """
        Changes the self.player_gravity based on the input parameter.
        :param new_gravity: Either "left" or "right"
        """
        new_gravity = new_gravity.lower()

        if new_gravity != self.player_gravity:
            self.player_gravity = new_gravity
            self.flip_player_horizontally()

    def player_input(self):
        """
        In manual mode: After pressing space from the keyboard toggles player's gravity.
        """
        if global_variables['events']:
            for pygame_event in global_variables['events']:
                if pygame_event.type == pygame.KEYDOWN:
                    if pygame_event.key == pygame.K_SPACE:
                        self.player_gravity = "left" if self.player_gravity == 'right' else 'right'
                        self.flip_player_horizontally()

    def apply_gravity(self):
        if self.player_gravity == 'left':
            self.rect.x -= self.gravity
            if self.rect.left <= 177:
                self.rect.left = 177
        else:
            self.rect.x += self.gravity
            if self.rect.right >= 430:
                self.rect.right = 430

    def animation_state(self):
        """
        Animates the player.
        After each execution, it increases player_index by 0.1. Therefore, after ten execution, it changes the
        player_index and player's frame correspondingly.
        """
        self.player_index += 0.1
        if self.player_index >= len(self.player_walk):
            self.player_index = 0

        self.image = self.player_walk[int(self.player_index)]

    def update(self):
        """
        Updates the player according to the game_mode. If it is "Manual", it listens to the keyboard. Otherwise the
        player changes its location based on `think` method.
        """
        if self.game_mode == "Manual":
            self.player_input()
        if self.game_mode == "Neuroevolution":
            obstacles = []
            for obstacle in global_variables['obstacle_groups']:
                if obstacle.rect.y <= 656:
                    obstacles.append({'x': obstacle.rect.x, 'y': obstacle.rect.y})

            self.think(global_variables['screen_width'],
                       global_variables['screen_height'],
                       obstacles, self.rect.x, self.rect.y)

        self.apply_gravity()
        self.animation_state()

    def flip_player_horizontally(self):
        """
        Flips horizontally to have a better graphic after each jump.
        """
        for i, player_surface in enumerate(self.player_walk):
            self.player_walk[i] = pygame.transform.flip(player_surface, flip_x=True, flip_y=False)
