#part 2 
#same logic as the part 1, but now instead of considering the next digit, it wants you to consider the digit halfway around.
a=input()
n=len(a)
result=0
point=n/2
for i in range(0,n/2):
    if a[i]==a[i+point]:
        result=result+int(a[i])
print(2*result) #print 2*result because we have only calculated the half cycle.
