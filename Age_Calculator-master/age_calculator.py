# Test connect
# print("Hello World")
''' 
create a calculator that calculates 
the year the user turns 100
'''

# calculate todays date and print it
from datetime import date
today = date.today().year
print("The Year is ", today)

# gather user input change year to int
name = input("Whats your name ")
print("Ok so, Let's calculate the year you turn 100. " )
year = int(input("What year were you born? "))

# concatenate/calculate/print results with message
print("Wow "+ name,",you will be 100 the year", (year + 100),"Live well,😉!!")