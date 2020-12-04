import sys, re, numpy

def hits(dx,dy,forest):
    currx = 0
    curry = 0
    length = len(forest[0])
    trees = 0 

    while curry <= len(forest)-1:
        if forest[curry][currx] is '#': trees += 1
        currx = (currx + dx)%length
        curry += dy

    return trees



if __name__=="__main__":

    f = open("day3_input.txt")
    forest = f.read().split('\n')

    
    slope = [(1,1),(3,1),(5,1),(7,1),(1,2)]

    res = []
    for dx,dy in slope:
        res.append(hits(dx,dy,forest))

    print(res) # =

