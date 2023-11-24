from http.server import BaseHTTPRequestHandler
import random #allows use of math modules like sine. square root, cos etc
import math  #allows us to use random modules


#we are taking inputs for :Lower values now
Lower = int(input("Welcome Fellow Human! Insert number to continue: "))

#we are taking inputs for Higher values now
Higher = int(input("Continue and insert number please: "))

# This piece of code creates range from Lower to Higher
# Not only that...it uses an algorithm to assist you with telling you how many chances you have left


y = random.randint(Lower, Higher)

print("\n\tYou have only got ",
      round(math.log(Higher - Lower+1,2)),
      " chances left to guess boyy!\n")

# Initializes variable "count"
count = 0

while count < math.log(Higher-Lower+1,2):
    count +=1 
    
    #input question that places it as an integer
    take_a_guess = int(input("...pick a number to continue: "))
    
#tests condition
    if y == take_a_guess:
        
        print("Congratulations fellow Human...You May Pass!\nYOU DID THIS IN",
              count,
              "TRIES")
        break          #code will stop, unles........
    elif y > take_a_guess:
        print("Oops...guessed too low!")
    elif y < take_a_guess:
        print("Oops...guessed too high!")
        
#If you just suck at this 

if count >= math.log(Higher-Lower+1,2):
    print("\nThe actual number is...%d" % y)
    print("This is a rather unfortunate result. My apologies but you may not advance....")
    print("GAME OVER")