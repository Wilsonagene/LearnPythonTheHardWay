#Exercise 0 was about installation of python , Anaconda, jupyter, Geany,  Testing setup and some CMD command line
#Excercise 9: Explanation of multi-line Strings 
days = "mon tue wed thurs fri sat sun" #This line of code has a variable name of days and string of days of the week
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # A varable named months and where each month name is separated by a newline character (\n)
print("Here are days: ", days) #This line prints the text 'here are days' and then the varable stored as days and the days of the week
print("Here are the months: ", months) #This line of code prints prints 'here are months' and prints names of the month and moves to the next line to to print the next one because of \n(nextline)
print("""
      There's something going on here.
      with the three double-quotes.
      we'll be able to type as much as we like.
      even 4 lines if we want, 5, or 6.""") #This line of code is a multi-line string or docstring which allows a person to write multiple lines of text without using \n to move to next line

#Excercise 10: Escape codes in strings
"i am 6'2\" tall" # What this code does is that it uses this \ sign to tell python that the double quote inside the code is not the end of that string which can also be known as escape string

tabby_cat = "\tI'm tabbing in." #This line of code has an escape sequence (\t) which basically gives a blank small space at the front of the text before printing the actual text after the space
persian_cat = "i'm split\non a line" #This code uses \n which means "new line" printing the the remainig text after the \n on the next line
backslash_cat = "i'm \\ a \\ cat" # if you want to show an actual backslash in your text you need to escape is by typing \\ in your code
fat_cat = """" 
i'll do a list:
\t* cat food
\t* fishfood
\t* catnip\n\t* grass"""#This starts with a span that can take many line, then the escape sequence \t that gives space at the front and the the \n that moves the text in front of it to the next line.
print(tabby_cat) #this line prints the varable name with tebby_cat
print(persian_cat) #this line prints the varable name with persian_cat
print(backslash_cat) #this line prints the varable name with backslash_cat
print(fat_cat) #this line prints the varable name with fat_cat

#Excercise 11: Asking People Questions
print("how old are you?", end=' ') #normally print ends with a new line but the end changes its behavior. instead of jumping to the next line, it puts space at the end, so the next input or print appears on same line.
age = input() # waits for user to input their age 
print("how tall are you?", end=' ') #prints the next question and still stays on the same line and adds a space insted of jumping to a new line
height = input()  # waits for user to input their height
print("how much do you weigh?", end=' ') #prints the next question and still stays on the same line and adds a space insted of jumping to a new line
weight = input()  # waits for user to input their weight

print(f"so you're {age} old, {height} feets tall and {weight} lbs heavy") # this prints a summary. f" means an f-string, it inserts the value of the varables inside a curly braces