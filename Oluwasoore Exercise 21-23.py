# Excercise 21 Functions for performing basic mathematical operations

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some matg with just functions!")

age= add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print(f"Age : {age},Height: {height}, Weight : {weight}")


 
print("Here is a puzzle." )

what = add(age, subtract(height, multiply(weight,divide))
           
print(That becomes:, what, "can you do it by hand?")




#Exercise 22 a puzzle for extra credit
import sys
script, input_encoding, error = sys.argv


def main(language, encoding errors):
     line = language_file.readline()

if line:
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)

def print_line(line, encoding, errors)
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    def print_line(line, encoding errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)

    print(raw_bytes, "<===>, cooked_string")

    languages = open("languages.txt", encoding="utf-8")

    main(languages, input_encoding, error)


#Exercise 23 Dictionaries for different things

fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, '8'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]


Cars = [
    ['cadillac', ['Black', 'Big', 34500]],
    ['corvette',['Red', 'Little', 1000000]],
    ['Ford',['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['Javascript', ['Moderate', ['Alright', 'Bizzare']]]
    ['Per16', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying' 'Dangerous']]],
    ['Fourth', ['Fast',  ['Fun', 'Difficult']]],
]