
#David Leisse
#07.08.2011
#Zwei kleine Spiele

import random

guessesTaken = 0
rightAnswers = 0

print ("Hey! What is your name?")
Name = input()
print ("And how old are you?")
Alter = input()

# up 17
if Alter > "17":
    runGame = 't'
    while runGame == 't':
        number = random.randint(1, 100)
        print("Well," + Name + """ let's play a game! You can choose: a) Guess a number
        b) Quiz c) hm no. Please choose the letter!""")
        oletter = input()
        oletter = str(oletter)

## Guess
        if oletter == "a":
            print("Well then guess a number between 1 and 100!")

            while guessesTaken < 13:
                guess = input()
                guess = int(guess)

                guessesTaken = guessesTaken + 1

                if guess < number:
                    print("Thats not my number, my number is higher!")

                if guess > number:
                    print("Thats not my number, my number is lower!")

                if guess == number:
                    break

            if guess == number:
                print("Good job," + Name + " you guessed my number in " + str(guessesTaken) + " guesses!")
                input()

            if guess != number:
                print("Nope that's not my number, my number was " + str(number) + ".")
                input()

## Quiz
        if oletter == "b":
            print("Well then I ask you some questions.")
            input()
            random.choice('What is 10 + 10''What is 1+1')

            if rightAnswers > 0:   
                    print("Good Job," + Name + " , you have " + str(rightAnswers) + " right answers!")
                    input()

            if rightAnswers == 0:
                    print("Hm," + Name + " that was not so good. You have " + str(rightAnswers) + " right answers")
                    input()

## hm NO
        if oletter == "c":
                break

    if oletter == "c":
            print("Ok, Bye " + Name + " nice to met you!")
            runGame = 'f'     
    

######################################## below 18 ##############################
if Alter < "18":
    runGame = 't'
    while runGame == 't':
        number = random.randint(1, 20)
        print ("Well," + Name + """ let's play a game! You can choose: a) Guess a number
        b) Quiz c) hm no. Please choose the letter!""")
        letter = input()
        letter = str(letter)

## Guess 
        if letter == "a":
            print("Well then guess a number between 1 and 20!")

            while guessesTaken < 6:
                guess = input()
                guess = int(guess)

                guessesTaken = guessesTaken + 1

                if guess < number:
                    print("Thats not my number, my number is higher!")

                if guess > number:
                    print("Thats not my number, my number is lower!")

                if guess == number:
                    break

            if guess == number:
                print("Good job," + Name + " you guessed my number in " + str(guessesTaken) + " guesses!")
                input()

            if guess != number:
                print("Nope that's not my number, my number was " + str(number) + ".")
                input()

## Quiz
        if letter == "b":
            print("Well then I ask you some questions.")
            input()
####

            if rightAnswers > 0:   
                print("Good Job," + Name + " , you have " + str(rightAnswers) + "right answers!")
                input()

            if rightAnswers == 0:
                print("Hm," + Name + " that was not so good. You have " + str(rightAnswers) + " right answers")
                input()

## hm No
        if letter == "c":
                break
            
            
        
    if letter == "c":
            print("Ok, Bye" + Name + ", it was nice to meet you!")
            runGame = 'f'     
