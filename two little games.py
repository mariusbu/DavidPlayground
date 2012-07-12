
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
#            print("Do you want a sport(s), geographie(g), history(h) or a mixed(m) quiz?Please write down the letter")
 #           quizLetter = input()
#            if quizletter = "s":
#               print("Well then I ask you some questions.")
#               input()
#               print("When 
            print("Well then I ask you some questions.")
            input()
            print("What is the square-root of 1369?")
            oanswer1 = input()
    
            if oanswer1 == "37":
                print("Yeah that's right")
                input()
                
                rightAnswers = rightAnswers + 1

            if oanswer1 != "37":
                print(" No that's wrong, the right answer is 37.")
                input()

            print("Which city is the capital of Kamerun?")
            oanswer2 = input()

            if oanswer2 == "Yaounde":
                print("Yeah that's right")
                input()

                rightAnswers = rightAnswers + 1

            if oanswer2 != "Yaounde":
                print("Nope, that's not right. The right answer is Yaounde.")
                input()

            print("Who is the best german table-tennis player?")
            oanswer3 = input()

            if oanswer3 == "Timo Boll":
                    print("Yeah that's right!")
                    input()

                    rightAnswers = rightAnswers + 1
        
            if oanswer3 != "Timo Boll":
                    print("No that's wrong! The right answer is Timo Boll")
                    input()

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
            print("What is the square-root of 144?")
            answer1 = input()
    
            if answer1 == "12":
                print("Yeah that's right")
                input()

                rightAnswers = rightAnswers + 1

            if answer1 != "12":
                print(" No that's wrong, the right answer is 12.")
                input()

            print("And which is the highest mountain?")
            answer2 = input()

            if answer2 == "Mount Everest":
                print("Yeah that's right")
                input()

                rightAnswers = rightAnswers + 1

            if answer2 != "Mount Everest":
                print("Nope, that's not right. The right answer is Mount Everest")
                input()

            print("How long is the sailboat named 470? (__,__m)")
            answer3 = input()

            if answer3 == "4,70m":
                print("Yeah that's right!")
                input()

                rightAnswers = rightAnswers + 1
        
            if answer3 != "4,70m":
                print("No that's wrong! The right answer is 4,70m")
                input()

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
            print("Ok, Bye " + Name + ", it was nice to meet you!")
            runGame = 'f'     
