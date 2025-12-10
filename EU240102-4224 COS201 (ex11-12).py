#Ex.11
#This code snippet is part of a Python exercise that prompts the user for their age, height, and weight, and then prints out the information in a formatted string.
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#The same functionality can be achieved in a more concise way as follows:
#Ex.12
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#this version combines the prompt and input into a single line for each question. Its more cleaner and shorter compared to exercise 11