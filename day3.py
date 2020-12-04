import sys, re

if __name__=="__main__":
    f = open("day3_input.txt")
    
   
    trees = 0
    currx = 0
    dx = 3


    for line in f.read().split('\n'):  
        if line[currx] is '#': trees += 1
        currx = (currx + dx)%len(line)
        #print(currx)
    
    print(trees)