# Day 05: Plotting Monte Carlo simulation results
# Topic: Visualizing rare egg probabilities in Rock Kingdom

import random
import matplotlib.pyplot as plt


def simulate_one_player(days, eggs_per_day, rare_probability):
  
    rare_count = 0

    for day in range(days):
        for egg in range(eggs_per_day):
            if random.random() < rare_probability:
                rare_count += 1

    return rare_count


def simulate_many_players(number_of_players, days, eggs_per_day, rare_probability):
  
    results = []

    for player in range(number_of_players):
        rare_eggs = simulate_one_player(days, eggs_per_day, rare_probability)
        results.append(rare_eggs)

    return results


def count_results(results):
    
    counts = {}

    for rare_eggs in results:
        if rare_eggs not in counts:
            counts[rare_eggs] = 0

        counts[rare_eggs] += 1

    return counts


def plot_results(counts, number_of_players):
   
    rare_egg_numbers = sorted(counts.keys())
    player_counts = []

    for number in rare_egg_numbers:
        player_counts.append(counts[number])

    plt.figure(figsize=(8, 5))
    plt.bar(rare_egg_numbers, player_counts)

    plt.title("Monte Carlo Simulation: Rare Egg Results")
    plt.xlabel("Number of rare eggs obtained")
    plt.ylabel("Number of simulated players")

    plt.xticks(rare_egg_numbers)
    plt.tight_layout()

    plt.savefig("rare_egg_distribution.png")
    plt.show()


def print_summary(results, number_of_players):
   
    zero_rare = 0

    for result in results:
        if result == 0:
            zero_rare += 1

    probability_zero = zero_rare / number_of_players
    average_rare = sum(results) / number_of_players

    print("Roco Kingdom Rare Egg Visualization")
    print("-----------------------------------")
    print("Number of simulated players:", number_of_players)
    print("Players with zero rare eggs:", zero_rare)
    print("Probability of zero rare eggs:", round(probability_zero * 100, 2), "%")
    print("Average rare eggs per player:", round(average_rare, 3))
    print("Plot saved as rare_egg_distribution.png")


# Main program

number_of_players = 10000
days = 60
eggs_per_day = 5
rare_probability = 0.01

results = simulate_many_players(
    number_of_players,
    days,
    eggs_per_day,
    rare_probability
)

counts = count_results(results)

print_summary(results, number_of_players)

plot_results(counts, number_of_players)
