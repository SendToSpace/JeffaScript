import os
import sys


def main(argv):
    print(replaceStr(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4],sys.argv[5]))

def clear():
    os.system('cls')

def replaceStr(beg,end,str,Newpatt,Oldpatt):
    for x in range(beg,end+1):
        if(Oldpatt == str[x:x+len(Oldpatt)]):
            str = str[:x] + Newpatt + str[x+len(Oldpatt):]

    return str
main(sys.argv[1:])
