#******************************************************************************
# barrier.py
#******************************************************************************
# Name: Eduardo Esteves 
#******************************************************************************
# Remarks (optional):
#
#
#

import random

#number of tims to be simulated

trios = 10**5

#create variables for the number of times won and money earned
earned = 0

times_won = 0

#loop

for i in range(trios):
#create random numbers between 50-70 
    a = random.randrange(50,71)

    b = random.randrange(50,71)

    c = random.randrange(50,71)
#define the parameters to win     
    you_win = a < 65 and b < 65 and c < 65
#create an if-statement for every time you are able to make at least a dollar  
    if you_win:
        if c > 55:
            earned += (c - 55)
            times_won += 1
            
            

#Average amount earned           
average_earned = earned/times_won

#probability of winning at least a dollar
prob = times_won/trios

print(f'Average amount earned: {average_earned}')

print(f'Probability of winning at least one dollar: {prob}')


