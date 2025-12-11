#Exercise 4. Variables and Names
cars = 100
space_in_a_car = 4.0
drivers = 30
passenger = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passenger / cars_driven

print("There are", cars, "cars available.")
print("There are only", driver, "driver available.")
print("There will be", car_not_driven, "empty today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car.")

#Exercise 5. More Varaibles and printing
#varaibles is a container used to store data, like numbers or text
my_name = 'Zed A. Shaw'
my_age = # not a lie
my_height = # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}".)
print(f"He's{my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy")
print("He got {my_eyes} eyes and {my_hair} hair.")
print(f"his teeth are usally {my_teeth} depending on the coffee." % my_teeth)

#this line is tricky, try to get it exactly right 
print(f"if I add {my_age}, {my_height}, and {my_weight}")

#Exercise 6. String and Text
#this exercise explains strings and text and how it is used
types_of_poeple = 10
x = f" There who are {types_of_poeple} types of poeple ."

Binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those {do_not}."

print(x)
print(y)

print(f"I also said:{x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn' that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This ismthe left side of..."
e = "a string with a right side."

print(w + e)