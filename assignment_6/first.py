#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.


def intro ():
    print ("Hello User! This program is designed to sort 4 digits number from highest to lowest")
    name = input("what is your name?: ")
    name = name.title()
    print ("""Hello {}, welcome again to this program! enter your answer. Good Luck! """. format(name))
    quest = input ("are you ready? yes or no: ")
    if quest == "yes": 
        print ("Let's play!")
    else:
        print ("that's okay, no pressure")
    print ("please insert the value below")

intro()

first =(input("enter first number: "))
second =(input ("enter second number: "))
third = (input ("enter third number: "))
fourth= (input ("enter fourth number: "))

if (first <= second <= third <= fourth): 
     first, second, third, fourth = fourth, third, second, first
     print("highest=", first)
     print("second =", second)
     print("third  =", third)
     print("lowest =", fourth)

elif (first <= second <= fourth <= third):
    first, second, third, fourth = third, fourth, second, first
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (first <= fourth <= third <= second):
    first, second, third, fourth = second, third, fourth, first
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (first <= fourth <= second <= third):
    first, second, third, fourth = third, second, fourth, first
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("fourth =", fourth)

elif (first <= third <= second <= fourth):
    first, second, third, fourth = fourth, second, third, first
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (first <= third <= fourth <= second):
    first, second, third, fourth = second, fourth, third, first
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (second <= first <= third <= fourth):
    first, second, third, fourth, = fourth, third, first, second
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (second <= first <= fourth <= third):
    first, second, third, fourth, = third, fourth, first, second
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (first <= second <= fourth <= third):
    first, second, third, fourth, = third, fourth, second, first
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (second <= fourth <= first <= third):
    first, second, third, fourth, = fourth, first, fourth, second
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (second <= fourth <= third <= first):
    first, second, third, fourth, = first, third, fourth, second
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (second <= third <= fourth <= first):
    first, second, third, fourth, = first, fourth, third, second
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (second <= third <= first <= fourth):
    first, second, third, fourth, = fourth, first, third, second
    print("first  =", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (third <= first <= second <= fourth ):
    first, second, third, fourth, = fourth, second, first, third
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (third <= first <= fourth <= second ):
    first, second, third, fourth, = second, fourth, first, third
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (third <= fourth <= first <= second ):
    first, second, third, fourth, = second, first, fourth, third
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (third <= fourth <= second <= first ):
    first, second, third, fourth, = first, second, fourth, third
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (third <= second <= fourth <= first ):
    first, second, third, fourth, = first, fourth, second, third
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (third <= second <= first <= fourth ):
    first, second, third, fourth, = fourth, first, second, third
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= first <= second <= third):
    first, second, third, fourth, = third, second, first, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= first <= third <= second):
    first, second, third, fourth, = second, third, first, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= first <= third <= second):
    first, second, third, fourth, = second, third, first, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= second <= first <= third):
    first, second, third, fourth, = second, third, first, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= second <= third <= first):
    first, second, third, fourth, = first, third, second, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= third <= first <= second):
    first, second, third, fourth, = second, first, third, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

elif (fourth <= third <= second <= first ):
    first, second, third, fourth, = first, second, third, fourth
    print("highest=", first)
    print("second =", second)
    print("third  =", third)
    print("lowest =", fourth)

def goodbye ():
    print ("thank you for playing!")

goodbye ()