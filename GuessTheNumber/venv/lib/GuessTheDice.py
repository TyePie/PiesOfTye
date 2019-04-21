import random
print "rolling..."

import time
time.sleep(2)                                               #Building little suspense

lines = open('Smacktalk.txt').read().splitlines()           #We read this file and are going to print a random smack talking line
myline =random.choice(lines)
print(myline)

time.sleep(2)                                               #Building more suspense
n = random.randint(1,6)

print "guess a number between 1 and 6, then press enter"
uinput = input()                                            #We have the user input a guess

while uinput <> n:
    if uinput > 6 or uinput < 1:                            #If statement cause you do get those people who can't read
        print "Did I stutter? A NUMBER BETWEEN 1 AND 6!"
        uinput = input()
    elif uinput < n:                                        #If it's too low, let the player know and try again
        print "Checking the dice..."
        time.sleep(2)
        print "You're too low, try again"
        uinput = input()
    elif uinput > n:                                        #If it's too high, let the player know and try again
        print "Checking the dice..."
        time.sleep(2)
        print "You're too high, try again"
        uinput = input()

if uinput == n:                                             #When game has been won. Will one day add credits.
    print "Checking the dice..."
    time.sleep(2)
    print "You're correct! You win! Still noob though."
    print n
