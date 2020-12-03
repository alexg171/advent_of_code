import sys
f = open("expense_report.txt")


fs = f.read().split('\n')
i = 0
for x in fs:
    for y in fs:
        x = int(x)
        y = int(y)
        sum = x+y
        if sum == 2020:
            print(x*y)
            sys.exit()
