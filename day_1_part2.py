import sys
f = open("expense_report.txt")


fs = f.read().split('\n')
i = 0
for x in fs:
    for y in fs:
        for z in fs:
            x = int(x)
            y = int(y)
            z = int(z)
            sum = x+y+z
            if sum == 2020:
                print(x,y,z,x*y*z)
                sys.exit(0)
