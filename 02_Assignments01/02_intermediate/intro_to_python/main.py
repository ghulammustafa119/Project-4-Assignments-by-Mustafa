# Milestone #1: Mars Weight Calculator
# Prompt user for Earth weight


# earth_weight = float(input("Enter a weight on Earth: "))

# # Mars gravity factor
# mars_gravity = 0.378

# # Calculate weight on Mars
# mars_weight = round(earth_weight * mars_gravity, 2)

# # Print result
# print("The equivalent on Mars:", mars_weight)
# ---------------------------------------------


# ✅ Milestone #2: Weight on Any Planet

# Gravity factors relative to Earth
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt user for input
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Get gravity factor for chosen planet
if planet in gravity_factors:
    equivalent_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"The equivalent weight on {planet}: {equivalent_weight}")
else:
    print("Sorry, invalid planet name!")
