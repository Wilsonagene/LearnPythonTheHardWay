# Exercise 15: Reading Files

# This progrsm takes a filename as a command line argument,
# opens that file, prints out its contents,
# then asks the user to retype the filenamr and prints it again.
# NOTE: one must run like: python ex15.py (filename) the filename here is ex15_sample.txt,
# run program in cmd using: python ex15.py ex15_sample.txt.
# when running program in cmd make sure to find file directory, in a case where file is in document,
# use >cd documents

from sys import argv 

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# the ex15_sample.txt is an extra argument created to test the file-reading program.

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())