import random

top_of_range = input("Type A Number: ")

#int("") this command will convert a digit which has een entered as a string, into a numerical value

if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print('Please type a number larger than zero next time.')
            quit()
else:
    print('Please print a number next time.')
    quit()
    

#r=random.randrange(-5,11)
#random number within specified range NOT inlcuding upper bound
#r=random.randint(-5,11)
#random number within specified range including upper bound
random_number = random.randint(0,top_of_range)
guesses = 0

while True:
        guesses += 1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
                user_guess = int(user_guess)
        else:
                print("Please type a numer next time")
                continue
        
        if user_guess == random_number:
                print("You got it!")
                break
        elif user_guess > random_number:
                print("You were above the number!")
        else:
                print("You were below the number!")
                #print("You got it wrong!")
                
print("You got it in" , guesses, "guesses")