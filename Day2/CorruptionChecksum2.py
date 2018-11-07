d = [[]]
a=open("Testfile.txt") #we read the numbers from a file, and store every line 
for i in a:            #as row in a two dimensional list 
    d=d+[i.split()]  
a.close()
d.remove([]) 
result=0
found=False
rows=len(d)
columns=len(d[0])
for i in range(0,rows):
    for j in range(0,columns):
        d[i][j]=int(d[i][j])   #we convert d into a two-dimensional list of ints
for i in range(0,rows):
    for j in range(0,columns):
        for k in range(j+1,columns):
            if(d[i][j]>d[i][k]): 
                m=d[i][j] 
                n=d[i][k] 
            else: 
                m=d[i][k] 
                n=d[i][j]
            if(m%n==0):        
                result=result+m/n
                found=True
                break
        if(found==True): break 
    found=False
print(result)                  #we prin the sum of all these differences          
