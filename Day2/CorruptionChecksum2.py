N=int(input())
dec=1
mon=[]
number=N
while(number>0):
    mon.append(number%10)
    number=int(number/10)
    