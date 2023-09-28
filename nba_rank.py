#Prompt Reply/Rating : input() - Advanced
#simple example of python rating code which provides a specific set of options and then #utilizes user provided input and ranks #responses as defined by user

#welcome user and request name input

print("Welcome to the NBA""\" Top Five \"Ranking System!")
print("Please Enter Your First Name: ")

name = input()

#defines a variable which represents a set of eligible choices

print( name + " Please Rank The Following Top 5 Players from Worst to Greatest, With The Greatest Being Ranked Number 1")

player = {"options":["Luka","Zion","Shaq", "Kyrie", "Lamelo"]}

#displays choices to user

print("*")
print("Luka")
print("Zion")
print("Shaq")
print("Kyrie")
print("Lamelo")
print("*")


#asks for user import for number one choice
#uses .lower() to standardize input string
#else statement ensure that the user has entered one of the 5 choices
#if user doesn’t answer one of the 5 choices, they must enter again
#this was accomplished with “while true” loop function
#the “if” statement assigns the input to a variable called “number1”

while True: 
    number1 = input("Please Enter Your First Choice: ")

    if number1.lower() == "luka" or number1.lower() == "zion" or number1.lower() == "shaq" or number1.lower() == "kyrie" or number1.lower() == "lamelo":
        print("Thank you for your response!")
        break
    else:
        
        print("Please Enter One Of The Five Listed Players")
        
#Repeat “while true” input loop function for second choice. Assign input to “number2” #variable

while True:
    number2 = input("Please Enter Your Second Choice: ")

    if number2.lower() == "luka" or number2.lower() == "zion" or number2.lower() == "shaq" or number2.lower() == "kyrie" or number2.lower() == "lamelo":
        print("Thank you for your response!")
        break
    else:

        print("Please Enter One Of The Five Listed Players")
        
#Repeat “while true” input loop function for third choice. Assign input to “number3” #variable


while True:
    number3 = input("Please Enter Your Third Choice: ")

    if number3.lower() == "luka" or number3.lower() == "zion" or number3.lower() == "shaq" or number3.lower() == "kyrie" or number3.lower() == "lamelo":
        print("Thank you for your response!")
        break
    
    else:
        print("Please Enter One Of The Five Listed Players")
        
#Repeat “while true” input loop function for third choice. Assign input to “number4” #variable

while True:
    number4 = input("Please Enter Your Fourth Choice: ")

    if number4.lower() == "luka" or number4.lower() == "zion" or number4.lower() == "shaq" or number4.lower() == "kyrie" or number4.lower() == "lamelo":
        print("Thank you for your response!")
        break
    
    else:
        print("Please Enter One Of The Five Listed Players")
        
#Repeat “while true” input loop function for fifth choice. Assign input to “number5” #variable


while True:
    number5 = input("Please Enter Your Fifth Choice: ")

    if number5.lower() == "luka" or number5.lower() == "zion" or number5.lower() == "shaq" or number5.lower() == "kyrie" or number5.lower() == "lamelo":
        print("Thank you for your response!")
        break
    
    else:
        print("Please Enter One Of The Five Listed Players")
        
#Relist players in order based on user input and defined variables

print("Your selections have been completed!")

print("In your opinion, the TOP 5 ranking are as follows: ")

print( "1st: " + number1)
print( "2nd: " + number2)
print( "3rd: " + number3)
print( "4th: " + number4)
print( "5th: " + number5)

#use user name for closing statement

print(" Thanks for playing! " + name + "!")
