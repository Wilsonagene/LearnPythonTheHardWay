# AYEJUYOLE BENJAMIN EU240102-4167

# =====================
# EXERCISE 6 - STRINGS AND TEXT
# =====================

# x stores a string with %d formatting for numbers
x = "There are %d types of people." % 10

# binary stores a string
binary = "binary"

# do_not stores a string containing an apostrophe

do_not = "don't"

# y stores a formatted string using binary and do_not

y = "Those who know %s and those who %s." % (binary, do_not)

# print the value of x
print(x)

# print the value of y
print(y)

# print x using raw representation
print("I said: %r." % x)

# print y using %s formatting
print("I also said: '%s'." % y)

# hilarious stores a boolean value
hilarious = False

# joke_evaluation stores a format string
joke_evaluation = "Isn't that joke so funny?! %r"

# print the joke evaluation with hilarious inserted
print(joke_evaluation % hilarious)

# w stores a string
w = "This is the left side of..."

# e stores another string

e = "a string with a right side."

# print the two strings combined
print(w + e)


# =====================
# EXERCISE 7 - MORE PRINTING
# =====================

# print a simple string
print("Mary had a little lamb.")

# print using string formatting with a string literal
print("Its fleece was white as %s." % 'snow')

# another simple print
print("And everywhere that Mary went.")

# print a dot repeated 10 times
print("." * 10)

# each variable stores a single character
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# print the first word on one line (comma prevents newline)
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")

# print the second word
print(end7 + end8 + end9 + end10 + end11 + end12)
