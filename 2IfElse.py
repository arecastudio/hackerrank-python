import math
import os
import random
import re
import sys

if __name__=='__main__':
    w="Weird"
    nw="Not Weird"
    n=int(input().strip())
    if n>=1 and n<=100:
        if n%2!=0:
            print(w)
        else:
            if n>=2 and n<=5:
                print(nw)
            elif n>=6 and n<=20:
                print(w)
            elif n>20:
                print(nw)
