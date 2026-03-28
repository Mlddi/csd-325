#|Maddison Montijo | 3.25.2026 | 1.3 Assignment

#|The Purpose of this Program is to :
#|Enter Input for how many beers on the wall
#|Countdown every amount of beers until zero
#|When the program hits zero, print "No more beers on the wall"
#|Ask user how many beers they want to buy, to start the countdown again
#|Repeat unless user exits with zero

import sys

def countdown(n):
    while n > -1:
    
        print(f"{n} bottle(s) of beer on the wall, {n} bottle(s) of beer.")
        
        n -= 1

        print(f"Take one down, pass it around, {n} more bottle(s) of beer on the wall.\n")

        if n == 0:
            print("Time to buy more bottle(s) of beer.")
            break

       
        
    
exitcode = 1

while exitcode > 0:

    
    bottles = int(input((f"Enter the number of bottles:")))
    countdown(bottles)

    sys.exit(0)



   
