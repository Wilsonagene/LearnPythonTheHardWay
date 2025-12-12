#chapter7
print("Mary had a little lamb.") #this line prints Mary had a little lamb
print("Its fleece was white as {}. ".format('snow')) #this line prints its fleece was white as in a snow format
print("And everywhere that Mary went.") #this line prints everywhere that Mary went
print("." * 10) # what'd that do? # this line prints "." * 10

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

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#chapter8
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) #this line prints 1, 2, 3, 4.
print(formatter.format("one", "two", "three", "four")) #this line prints 0ne, two, three, four
print(formatter.format(True, False, False, True)) #this line prints true, false, false, true
print(formatter.format(formatter, formatter,formatter,formatter)) #this line prints formatter, formatter, formatter, formatter
print(formatter.format( #this line prints formatter
     "Try your",
     "Own text here",
     "Maybe a poem",
     "Or a song about fear"
      ))


#chapter9
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJul\nAug"

print("Here are the days: ", days) #this line prints here are the days
print("Here are the months: ", months) #this line prints here are the months
print("""""") #this line prints """"""