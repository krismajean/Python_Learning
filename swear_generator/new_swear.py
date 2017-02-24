import random
import csv

def textStrip(file):
    with open(file,"r") as f:
        filelist = [line.strip() for line in f]
    return (filelist)

body_parts = textStrip("body_list.txt")
swears = textStrip("swear_list.txt")    #http://www.bannedwordlist.com/

def swear():
    swear = random.choice(body_parts) + " " + random.choice(swears)
    return(swear)

for x in range(0,20):
    print(swear())
