# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:04:20 2019

@author: mixalis
"""

f = open("Input.txt", "r")
result=0
for line in f:
    valid=True
    tokens=line.split()
    freq = nltk.FreqDist(tokens)
    for val in freq.values():
        if(val>1):
            valid=False
    if(valid==True):
        result+=1
print(result)