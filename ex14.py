# Exercise 14: Prompting and Passing

# This program takes one argument (user_name) from the comman line.

from sys import argv

script, user_name = argv
prompt = '>'

# This greets the user, and asks three questions using input().

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print (f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# This is the summary of the answers to the questions fom line 13-20
# NOTE: one must run like: python ex14.py (user_name) i.e python ex14.py omowunmi.
# when running program in cmd make sure to find file directory, in a case where file is in document,
# use >cd documents

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")