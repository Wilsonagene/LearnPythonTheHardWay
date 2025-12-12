#Olafusi esther
#python group1
# import the dis function
#ex27
from dis import dis #dis means disassemble (rule1)
dis(""" 
x = 10
y = 20
z = x + y
""") # this is a multi-line string

#rule2 (jumps make the sequence Non-linear).
dis("while True: x = 10")

#rule3
dis('''
x = 1
if x > 0:
    y = 10''')#python wll test if x > 0
#if it is then python would run the line y = 10

#rule4
#ths rile talks about storage control
if 1 < 2:
    print("but....why?")#this is used to store values into memory
#it transforms the data into a new variable

#rule5
from dis import dis
dis("input('Yes? ')")# data is read as input, you then write to output for storage.

# Exercise28
# this exercise talks about the truth terms
#and, or, not, !=(not equal), ==(equal), >=(greater-than-equal), <=(less-than-equal), True, and False.
#not False = True
#not True = False
#True or True = True
#True or False = True
#False or True = True
#True and False = False
#True and True = True
#False and True = False
#False and False = False
#not(True and False) = True
#not(True and True) = False
#not(False and True) = True
#not(False and False) = True
#1 != 0 = True
#1 != 1 = False
#1 == 0 = False
#1 == 1 = True

#ex29 (Boolean Practice)
3 != 4 and not ("testing" != "test" or "Python" == "Python")
#3 != 4 is True
#"testing" != "test" is true
#"Python" == "Python" is true
#replacing with the output we have.....True and not (True or True)
print(3 != 5)
print(3 != 4 and not ("testing" != "test" or "Python" == "Python"))
print(34 <= 45)


    



