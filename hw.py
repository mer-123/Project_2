# Getting Input from User
name = input('What is your name? ')
print ('Hi '+ name)

#Ask two question: person's name and favorite color. Then print a message like lee likes red
name = input('What is your name? ')
color = input('What is your favorite color? ')
print ( name +  ' likes '  + color)

#Type Conversion: Calculate age with only birth year as input
#birth_year = input('Birth year: ')   #This is string
#age = 2019 - birth_year     #This is integer
#print (age)   # integer - string, an error will show
#So, we must convert the string into integer. int() for converting a string into integer.
# float() for converting a string to float, with a decimal point.
# bool() for converting a string into a boolean
#Solution
birth_year = input('Birth_year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

# Ask the User their weight(in pounds), convert it into kilograms and print on the terminal
weight_lbs = input('What is your weight in lbs: ')
weight_kgs = int(weight_lbs) * 0.45
print(weight_kgs)

