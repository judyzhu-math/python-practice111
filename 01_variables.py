# Day 01: Python variables and basic calculations

# Basic variables
name = "Judy"
major = "Applied Mathematics"
city = "Berlin"

print("Hello, my name is", name)
print("I study", major)
print("I live in", city)

# Simple math
a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

# Applied math example: Euler step
# y' = -2y, y(0) = 1
y = 1
h = 0.1

y_next = y + h * (-2 * y)

print("One Euler step gives y =", y_next)
