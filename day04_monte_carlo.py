# Day 04: Monte Carlo Simulation
# Topic: Simulating many players in Rock Kingdom

import random


def simulate_one_player(days, eggs_per_day, rare_probability):
    total_rare_eggs = 0

    for day in range(days):
        for egg in range(eggs_per_day):
            if random.random() < rare_probability:
                total_rare_eggs += 1

    return total_rare_eggs


def simulate_many_players(number_of_players, days, eggs_per_day, rare_probability):
    rare_egg_results = []

    for player in range(number_of_players):
        rare_eggs = simulate_one_player(days, eggs_per_day, rare_probability)
        rare_egg_results.append(rare_eggs)

    return rare_egg_results


def count_unlucky_players(rare_egg_results):
    unlucky_count = 0

    for result in rare_egg_results:
        if result == 0:
            unlucky_count += 1

    return unlucky_count


def count_lucky_players(rare_egg_results):
    """
    Count how many players got at least one rare egg.
    """
    lucky_count = 0

    for result in rare_egg_results:
        if result >= 1:
            lucky_count += 1

    return lucky_count


def theoretical_no_rare_probability(total_eggs, rare_probability):
    return (1 - rare_probability) ** total_eggs


def print_summary(
    number_of_players,
    days,
    eggs_per_day,
    rare_probability,
    rare_egg_results
):
    """
    Print a summary of the Monte Carlo simulation.
    """
    total_eggs_per_player = days * eggs_per_day

    unlucky_players = count_unlucky_players(rare_egg_results)
    lucky_players = count_lucky_players(rare_egg_results)

    simulated_no_rare_probability = unlucky_players / number_of_players
    simulated_at_least_one_probability = lucky_players / number_of_players

    theoretical_no_rare = theoretical_no_rare_probability(
        total_eggs_per_player,
        rare_probability
    )
    theoretical_at_least_one = 1 - theoretical_no_rare

    average_rare_eggs = sum(rare_egg_results) / number_of_players
    max_rare_eggs = max(rare_egg_results)

    print("Rock Kingdom Monte Carlo Simulation")
    print("-----------------------------------")
    print("Number of simulated players:", number_of_players)
    print("Days per player:", days)
    print("Eggs per day:", eggs_per_day)
    print("Total eggs per player:", total_eggs_per_player)
    print("Rare probability per egg:", rare_probability)

    print("\nSimulation results:")
    print("Players with zero rare eggs:", unlucky_players)
    print("Players with at least one rare egg:", lucky_players)
    print("Simulated probability of zero rare eggs:", round(simulated_no_rare_probability * 100, 2), "%")
    print("Simulated probability of at least one rare egg:", round(simulated_at_least_one_probability * 100, 2), "%")

    print("\nTheoretical results:")
    print("Theoretical probability of zero rare eggs:", round(theoretical_no_rare * 100, 2), "%")
    print("Theoretical probability of at least one rare egg:", round(theoretical_at_least_one * 100, 2), "%")

    print("\nExtra statistics:")
    print("Average rare eggs per player:", round(average_rare_eggs, 3))
    print("Maximum rare eggs obtained by one player:", max_rare_eggs)

    print("\nConclusion:")
    if simulated_no_rare_probability < 0.05:
        print("Getting zero rare eggs is very unlucky. The nest curse is real.")
    elif simulated_no_rare_probability < 0.20:
        print("Getting zero rare eggs is unlucky, but still possible.")
    else:
        print("Getting zero rare eggs is frustrating, but statistically not that shocking.")


# Main program
# Imagine 10,000 players.
# Each player plays for 60 days.
# Each player gets 5 eggs per day.
# Each egg has a 1% chance to become rare.

number_of_players = 10000
days = 60
eggs_per_day = 5
rare_probability = 0.01

rare_egg_results = simulate_many_players(
    number_of_players,
    days,
    eggs_per_day,
    rare_probability
)

print_summary(
    number_of_players,
    days,
    eggs_per_day,
    rare_probability,
    rare_egg_results
)
