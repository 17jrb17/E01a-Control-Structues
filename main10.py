#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')  #prints "greetings"
colors = ['red','orange','yellow','green','blue','violet','purple'] #assigns colors an array of values
play_again = '' #creates the play_again value
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #loops the program while play_again doesn't equal n or no
    match_color = random.choice(colors) #assigns a random color
    count = 0 #creates count value equal to zero for now
    color = '' #creates color value equal to nothing for now
    while (color != match_color): #loops program while color and match_color don't equal eachother 
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #allows the value to be assigned a string with spaces and any capitalization
        count += 1 #adds 1 to the count value
        if (color == match_color): #if statement that runs if color and match_color equal eachother 
            print('Correct!') #prints "correct!"
        else: #if the "if" statement isn't met this runs
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #prints "sorry try again" as well as the count value which acts as number of tries
    print('\nYou guessed it in {0} tries!'.format(count)) #prints new line stating the user is correct with number of tries (count value)
    if (count < best_count): #if statement allowing for a high score element
        print('This was your best guess so far!') #prints this statement in terminal
        best_count = count #assigns best_count a new value
    play_again = input("\nWould you like to play again? ").lower().strip() #asks if user wants to play again and if it is yes the program runs again
print('Thanks for playing!') #printed when the program finally ends (user types n or no)