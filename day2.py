import sys, re


def policy_check(policy):
    m = re.search('(\d+)-(\d+) (\w): (\w+)', policy)
    lwr,upr,ltr,pwd = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    count = len(re.sub('[^'+ltr+"]", "", pwd))
    if count >= lwr and count <= upr:
        return True
    return False

if __name__=="__main__":
    f = open("day2_input.txt")
   
    valid = 0
    for line in f.read().split('\n'):
        if (policy_check(line)):
            valid +=1
    
    print(valid)