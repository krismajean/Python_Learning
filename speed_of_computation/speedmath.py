###############
#
#   Speed of Computation
#
#   This is an exercise to compare how fast you are at computation
#   to your computer
#
#   Author: Brian Broom-Peltz
#   Date: 2017.03.27
#
################
import time
import random as rand
import sys
import argparse

parser = argparse.ArgumentParser(description='Compare your math speed to your computer.')
parser.add_argument('users', metavar='users', type=int,
                    help='The number of users to create numbers for the experiment (default: 1)', default=1)


users = int(sys.argv[1])

### TODO:
### maybe make the list a dictionry to animals rather than group 0,1,2


print("""
###################################
##                                #
##      SPEED OF COMPUTATION      #
##                                #
###################################

        Let's see how you match up next to me :)

        Select 4 random 2 digit numbers between 10 and 100
        Then let's time how long it takes you to:
            Multiple two of them
            Add the two products

        Eg:	34	82	19	65
                34 x 82 = 2,788	    19 x 65 = 1,235
                2,788 + 1,235 = 4,023

""")
generate = input("Do you want me to pick some random numbers for you? (yes / no) ")

def generate_list():
    numbers = [[rand.randint(10,100) for x in range(4)] for x in range(pairs)]
    for x in range(pairs): print("\nGroup", x, "numbers:", numbers[x])
    return numbers

def check_list(numbers):
    return True

def input_list():
    valid = False
    while(valid == False):
        print("Please enter your four values separated by a space. Press enter after each")
        numbers = [[int(x) for x in input("Enter numbers: ").split(" ")] for x in range(users)]
    ## Check values are valid:
        valid = check_list(numbers)

    print("Let's confirm we have the same numbers:")
    for x in range(users): print("\nUser", x, "numbers:", numbers[x])

if generate == "yes": numbers = generate_list()

else: numbers = input_list()
print("""
        Now that you have your numbers, let's see how fast you are.

        As each of you finish, I'll record the time.

        On your mark

""")
input("Get set ....")
print("Go!")
start_time = time.time()

times = []
while(len(times) < users):
        input()
        mark = time.time()
        duration = mark - start_time
        times.append(duration)
        print(round(duration,3), "seconds")

avg_time = sum(times)/len(times)

input("Now my turn. Ready ... set ...")
print("Go!\n")
start_time = time.time()

# Compute
for x in range(users):
    first = numbers[x][0] * numbers[x][1]
    second = numbers[x][2] * numbers[x][3]
    combine = first + second
    print("Group",x,":\n",numbers[x][0],"x",numbers[x][1],"=",first,"\t",numbers[x][2],"x",numbers[x][3],"=",second,)
    print(first,"+",second,"=",combine,"\n")

computer_time = time.time()-start_time
print("\nComputer Time: ", round(computer_time,6),"seconds")

computers_to_humans = int(avg_time / computer_time)

print("""

    So let's put that time into context:
    If you take the average amount of time it took y'all: %d

    This computer was %d times faster than you all.

    Said another way, there would have to be %d of you working
    simultaneously to equal the performance of this one computer.

""" % (avg_time, computers_to_humans, computers_to_humans))

#print("Time for computation: ", (time.time() - start_time))
