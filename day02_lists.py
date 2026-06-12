# Day 02: Lists, loops, and a simple rare egg simulation
# Topic: Rock Kingdom rare egg probability

import random

# Suppose each egg has a 1% chance to be rare shiny
rare_probability = 0.01

# Number of eggs produced each day for 14 days
eggs_per_day = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]

total_eggs = 0
rare_eggs = 0

daily_results = []

for day in range(len(eggs_per_day)):
    eggs_today = eggs_per_day[day]
    rare_today = 0

    for egg in range(eggs_today):
        total_eggs += 1

        # Generate a random number between 0 and 1
        random_number = random.random()

        # If the random number is smaller than 0.01, we get a rare egg
        if random_number < rare_probability:
            rare_eggs += 1
            rare_today += 1

    daily_results.append(rare_today)

# Print summary
print("Rock Kingdom Egg Simulation")
print("----------------------------")
print("Total days:", len(eggs_per_day))
print("Total eggs:", total_eggs)
print("Rare eggs:", rare_eggs)

if rare_eggs == 0:
    print("Result: No rare eggs. So sad!!!")
else:
    print("Result: Congratulations!!! You got at least one rare egg.")

# Print daily results
print("\nDaily results:")

for day in range(len(daily_results)):
    print("Day", day + 1, "- rare eggs:", daily_results[day])

# Theoretical probability of getting no rare eggs
prob_no_rare = (1 - rare_probability) ** total_eggs
prob_at_least_one = 1 - prob_no_rare

print("\nTheoretical probability:")
print("Probability of no rare eggs:", round(prob_no_rare * 100, 2), "%")
print("Probability of at least one rare egg:", round(prob_at_least_one * 100, 2), "%")
