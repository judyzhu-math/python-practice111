# Day 03: Functions and a cleaner shiny egg simulator
# Topic: Roco Kingdom rare egg probability

import random


def simulate_one_day(eggs_today, rare_probability):
    rare_count = 0

    for egg in range(eggs_today):
        if random.random() < rare_probability:
            rare_count += 1

    return rare_count


def simulate_many_days(eggs_per_day, rare_probability):
    daily_rare_counts = []

    for eggs_today in eggs_per_day:
        rare_today = simulate_one_day(eggs_today, rare_probability)
        daily_rare_counts.append(rare_today)

    return daily_rare_counts


def calculate_total_eggs(eggs_per_day):
    total = 0

    for eggs_today in eggs_per_day:
        total += eggs_today

    return total


def theoretical_probability_at_least_one(total_eggs, rare_probability):
    probability_no_rare = (1 - rare_probability) ** total_eggs
    probability_at_least_one = 1 - probability_no_rare

    return probability_at_least_one


def print_results(eggs_per_day, daily_rare_counts, rare_probability):
    total_eggs = calculate_total_eggs(eggs_per_day)
    total_rare = sum(daily_rare_counts)

    probability_at_least_one = theoretical_probability_at_least_one(
        total_eggs,
        rare_probability
    )

    print("Roco Kingdom Rare Egg Simulation")
    print("--------------------------------")
    print("Total days:", len(eggs_per_day))
    print("Total eggs:", total_eggs)
    print("Rare probability per egg:", rare_probability)
    print("Total rare eggs from simulation:", total_rare)

    print("\nDaily rare egg results:")
    for day in range(len(daily_rare_counts)):
        print("Day", day + 1, "- rare eggs:", daily_rare_counts[day])

    print("\nTheoretical probability:")
    print(
        "Probability of getting at least one rare egg:",
        round(probability_at_least_one * 100, 2),
        "%"
    )

    if total_rare == 0:
        print("\nConclusion: No rare eggs. The unlucky curse continues.")
    else:
        print("\nConclusion: Finally! The nest gods have shown mercy.")


# Main program
# Example: 21 days of egg production
# First week: 2 eggs/day
# Second week: 3 eggs/day
# Third week: 5 eggs/day

eggs_per_day = [
    2, 2, 2, 2, 2, 2, 2,
    3, 3, 3, 3, 3, 3, 3,
    5, 5, 5, 5, 5, 5, 5
]

rare_probability = 0.01

daily_rare_counts = simulate_many_days(eggs_per_day, rare_probability)

print_results(eggs_per_day, daily_rare_counts, rare_probability)
