import copy
import json
import math
import numpy as np
from player import Player


class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"
        
        self.generation_number = 0

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
        total_fitness = sum([p.fitness for p in players])
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

        crossover_place1 = math.floor(player1.nn.hidden_size / 2)
        crossover_place2 = math.floor(player1.nn.output_size / 2)

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

        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.w1 += np.random.randn(player.nn.hidden_size, player.nn.input_size)
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.w2 += np.random.randn(player.nn.output_size, player.nn.hidden_size)
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.b1 += np.random.randn(player.nn.hidden_size, 1)
        if np.random.uniform(0, 1, 1) < mutation_probability:
            player.nn.b2 += np.random.randn(player.nn.output_size, 1)

        return player

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        
        players_sorted = sorted(players, key=lambda player: player.fitness, reverse=True)
        fitness_list = [player.fitness for player in players]
        best_fitness = float(np.max(fitness_list))
        average_fitness = float(np.mean(fitness_list))
        worst_fitness = float(np.min(fitness_list))
        self.save_fitness_results(best_fitness , worst_fitness , average_fitness)

       
        # return self.roulette_wheel(players, num_players)
        return players_sorted[: num_players]
        

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            print(num_players)
            return [Player(self.game_mode) for _ in range(num_players)]
        else:


            new_players = self.q_tournament(num_players, prev_players, q=10)
            # return players[: num_players]

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

    def save_fitness_results(self , max_fitness , min_fitness , average_fitness):
        if(self.generation_number == 0) :
            generation_results ={
                'best_fitnesses': [max_fitness],
                'worst_fitnesses': [min_fitness],
                'average_fitnesses': [average_fitness]
            }
            with open('generation_results.json', 'w') as file:
                json.dump(generation_results, file)
            file.close()
        else:
            with open('generation_results.json', 'r') as file:
                generation_results = json.load(file)
            file.close()
            generation_results['best_fitnesses'].append(max_fitness)
            generation_results['worst_fitnesses'].append(min_fitness)
            generation_results['average_fitnesses'].append(average_fitness)

            with open('generation_results.json', 'w') as file:
                json.dump(generation_results, file)
            file.close()
        self.generation_number += 1
