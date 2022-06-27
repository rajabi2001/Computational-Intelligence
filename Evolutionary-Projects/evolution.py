import copy
import math
import numpy as np
from player import Player


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"
        # options = q_tournament , roulette_wheel , sus
        self.selection_mode = "q_tournament"

    def q_tournament(self, num_players, players, q ):
        selected_players = []
        for i in range(num_players) :
             random_selections = np.random.choice(players, q)
             selected_players.append(max(random_selections, key=lambda player: player.fitness))
        return selected_players

    def roulette_wheel(self , players , num_player):
        fitness_sum = sum([player.fitness for player in players])
        probabilities = [player.fitness / fitness_sum for player in players]
        next_generation = np.random.choice(players, size=num_player, p=probabilities, replace=False)
        return next_generation.tolist()

    def sus(self, players, num_players):
        total_fitness = np.sum([p.fitness for p in players])
        step_size = total_fitness / num_players
        start_point = np.random.uniform(0, step_size)

        ruler = np.arange(num_players) * step_size
        ruler = ruler + start_point

        selected_players = []
        for r in ruler:
            i = 0
            f = 0
            while f < r:
                f += players[i].fitness
                i += 1
            selected_players.append(players[i - 1])
        return selected_players


    def crossover(self, player1, player2):

        crossover_probability = 0.8
        random_number = np.random.uniform(0, 1, 1)
        if(random_number >= crossover_probability) :
            return player1 , player2

        child1 = self.clone_player(player1)
        child2 = self.clone_player(player2)

        crossover_place1 = math.floor(player1.nn.hidden_size[1] / 2)
        crossover_place2 = math.floor(player1.nn.output_size[2] / 2)

        child1.nn.w1 = np.concatenate((player1.nn.w1[:crossover_place1], player2.nn.w1[crossover_place1:]), axis=0)
        child1.nn.b1 = np.concatenate((player1.nn.b1[:crossover_place1], player2.nn.b1[crossover_place1:]), axis=0)
        child1.nn.w2 = np.concatenate((player1.nn.w2[:crossover_place2], player2.nn.w2[crossover_place2:]), axis=0)
        child1.nn.b2 = np.concatenate((player1.nn.b2[:crossover_place2], player2.nn.b2[crossover_place2:]), axis=0)
        child2.nn.w1 = np.concatenate((player2.nn.w1[:crossover_place1], player1.nn.w1[crossover_place1:]), axis=0)
        child2.nn.b1 = np.concatenate((player2.nn.b1[:crossover_place1], player1.nn.b1[crossover_place1:]), axis=0)
        child2.nn.w2 = np.concatenate((player2.nn.w2[:crossover_place2], player1.nn.w2[crossover_place2:]), axis=0)
        child2.nn.b2 = np.concatenate((player2.nn.b2[:crossover_place2], player1.nn.b2[crossover_place2:]), axis=0)

        return child1,child2

    def mutation(self, player):
        mutation_probability = 0.3

        layer_sizes = player.nn.layer_sizes
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.w1 += np.random.randn(layer_sizes[1], layer_sizes[0])
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.w2 += np.random.randn(layer_sizes[2], layer_sizes[1])
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.b1 += np.random.randn(layer_sizes[1], 1)
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.b2 += np.random.randn(layer_sizes[2], 1)
  

        # random_number = np.random.uniform(0, 1, 1)
        # if(random_number <= mutation_probability) :
        #     player.nn.w1 += np.random.normal(0,0.3,size=player.nn.w1.shape)
        #     player.nn.w2 += np.random.normal(0,0.3,size=player.nn.w2.shape)
        #     player.nn.b1 += np.random.normal(0, 0.3, size=player.nn.b1.shape)
        #     player.nn.b2 += np.random.normal(0, 0.3, size=player.nn.b2.shape)

        return player

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)

        # TODO (Additional: Learning curve)
        return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:

            if self.selection_mode == "q_tournament":
                new_players = self.q_tournament(num_players, prev_players, q=3)
            elif self.selection_mode == "roulette_wheel":
                new_players = self.roulette_wheel(prev_players, num_players)
            elif self.selection_mode == "sus":
                new_players = self.sus(prev_players, num_players)

            children = []
            for i in range( 0, len(new_players) , 2) :
                parent1 = new_players[i]
                parent2 = new_players[i+1]
                child1, child2 = self.crossover(parent1,parent2)
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)
                children.append(child1)
                children.append(child2)

            return children


            
            

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
