d = [[]]
a=open("Testfile.txt") #we read the numbers from a file, and store every line 
for i in a:            #as row in a two dimensional list 
    d=d+[i.split()]  
a.close()
d.remove([]) 
result=0
rows=len(d)
columns=len(d[0])
for i in range(0,rows):
    for j in range(0,columns):
        d[i][j]=int(d[i][j])   #we convert d into a two-dimensional list of ints
    maxdif=max(d[i])-min(d[i]) #calculate the difference between the max and the min element of every row
    result=result+maxdif
print(result)                  #we prin the sum of all these differences          
