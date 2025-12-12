import ex26
# ================================
# EXERCISE 24 - INTRODUCTORY DICTIONARIES
# ================================

print("height",ex26.height)
print("name",ex26.name)
# ----------- FRUIT DATA -----------
# This list stores information about different fruits
fruit = [
    {"kind": "Apples",  "count": 12, "rating": "AAA"},
    {"kind": "Oranges", "count": 1,  "rating": "B"},
    {"kind": "Pears",   "count": 2,  "rating": "A"},
    {"kind": "Grapes",  "count": 14, "rating": "UR"},
]


# ----------- CARS DATA -----------
# This list stores information about different cars
cars = [
    {"type": "Cadillac", "color": "Black", "size": "Big",    "miles": 34500},
    {"type": "Corvette", "color": "Red",   "size": "Little", "miles": 1000000},
    {"type": "Ford",     "color": "Blue",  "size": "Medium", "miles": 1234},
    {"type": "BMW",      "color": "White", "size": "Baby",   "miles": 7890},
]


# ----------- LANGUAGES DATA -----------
# This list stores information about programming languages
languages = [
    {"name": "Python",     "speed": "Slow",     "opinion": ["Terrible", "Mush"]},
    {"name": "JavaScript", "speed": "Moderate", "opinion": ["Alright", "Bizarre"]},
    {"name": "Perl6",      "speed": "Moderate", "opinion": ["Fun", "Weird"]},
    {"name": "C",          "speed": "Fast",     "opinion": ["Annoying", "Dangerous"]},
    {"name": "Forth",      "speed": "Fast",     "opinion": ["Fun", "Difficult"]},
]


# ================================
# FRUIT CHALLENGE OUTPUT
# ================================

print("\nFRUIT CHALLENGE")

print(fruit[0]["count"])    # 12
print(fruit[0]["rating"])   # AAA
print(fruit[2]["count"])    # 2
print(fruit[1]["kind"])     # Oranges
print(fruit[3]["kind"])     # Grapes
print(fruit[3]["count"])    # 14
print(fruit[0]["kind"])     # Apples


# ================================
# CARS CHALLENGE OUTPUT
# ================================

print("\nCARS CHALLENGE")

print(cars[0]["size"])     # Big
print(cars[1]["color"])    # Red
print(cars[2]["miles"])    # 1234
print(cars[3]["color"])    # White
print(cars[3]["miles"])    # 7890
print(cars[0]["color"])    # Black
print(cars[0]["miles"])    # 34500
print(cars[2]["color"])    # Blue


# ================================
# LANGUAGES CHALLENGE OUTPUT
# ================================

print("\nLANGUAGES CHALLENGE")

print(languages[0]["speed"])         # Slow
print(languages[1]["opinion"][0])    # Alright
print(languages[3]["opinion"][1])    # Dangerous
print(languages[3]["speed"])         # Fast
print(languages[4]["opinion"][1])    # Difficult
print(languages[2]["opinion"][0])    # Fun
print(languages[3]["opinion"][0])    # Annoying
print(languages[2]["opinion"][1])    # Weird
print(languages[1]["speed"])         # Moderate


# ================================
# FINAL CHALLENGE - SONG LYRICS
# ================================

print("\nSONG LYRICS")

lyrics = [
    # Example:
     "Little red corvette",
    "Baby you're too much ehh,",
    "cos your body na meat-pie,",
]

for line in lyrics:   # Loop through each lyric line
    print(line)       # Print each line one by one




#=============================================================================================================#

# ================================
# EXERCISE 25 - DICTIONARIES AND FUNCTIONS
# ================================

# STEP 1: FUNCTION NAMES ARE VARIABLES

# A function's name can be stored in another variable.

def print_number(x):
    print("NUMBER IS", x)

rename_print = print_number   # rename_print now points to the same function

rename_print(100)             # Calls print_number(100) through new name
print_number(100)             # Calls the original name


# --------------------------------
# STEP 2: DICTIONARIES WITH VARIABLES
# --------------------------------
# You can store variables as values inside a dictionary.

color = "Red"     # normal variable

corvette = {
    "color": color   # store the variable inside the dict
}

print("LITTLE", corvette["color"], "CORVETTE")   #This Uses the dict value


# --------------------------------
# STEP 3: DICTIONARIES WITH FUNCTIONS
# --------------------------------
# You can also store a FUNCTION inside a dictionary.

def run():
    print("VROOM")

corvette2 = {
    "color": "Red",
    "run": run      # store the function (without parentheses)
}

print("My", corvette2["color"], "can go")
corvette2["run"]()   # 1) get the function from the dict  2) run it with ()


# --------------------------------
# STEP 4: BREAKING DOWN corvette2["run"]
# --------------------------------


myrun = corvette2["run"]   #this simply get the function out of the dict
myrun()                    # call the function



def make_car(name, color, speed):
    """Create a car dict with data + behavior."""

    def run():
        # This function uses name and speed from the outer function
        print(name, "goes", speed, "km/h")

    def stop():
        print(name, "is stopping.")

    # Return a dictionary that represents the car
    return {
        "name": name,
        "color": color,
        "speed": speed,
        "run": run,    # function stored as a value
        "stop": stop,
    }



# ====================================================================================
# EXERCISE 25 - DICTIONARIES AND MODULES
# ====================================================================================
# This file imports ex26.py and shows that a module works like a dictionary.

# from pprint import pprint   # pretty-printing for easier reading
# import ex26                 # import the module we created

# Step 1: Access values in the module using dot syntax
print("name:", ex26.name)        # prints the name stored in ex26
print("height:", ex26.height)    # prints the height stored in ex26

# Step 2: Show the module's internal dictionary
from pprint import pprint
pprint(ex26.__dict__)            # prints everything inside the module

# Step 3: Change the dict and show it changes the module
print(f"I am currently {ex26.height} inches tall.")

ex26.__dict__['height'] = 1000               # Change height THROUGH dict
print(f"I am now {ex26.height} inches tall.")

ex26.height = 12                             # Change height THROUGH dot syntax
print(f"Oops, now I'm {ex26.__dict__['height']} inches tall")

# Step 5: Dunder example (__doc__)
print(pprint.__doc__)