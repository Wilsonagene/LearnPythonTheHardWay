# Exercise 13: Parameters, Unpacking, Variables

# This program takes three arguments from the command line and prints them
# It uses sys.argv to collect values typed when runnning the scripts.
# the user must run it with three extra words, e.g as stated in the textbook:
# apple, orange and grapefruit

# NOTE: when running program in cmd make sure to find file directory, in a case where file is in document,
# use >cd documents

from sys import argv
# read the What You Should See Section for how to run the argv
script, first, second, third = argv

print("The script is called:", script)
print("Ypur first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)