
arr=list(eval(input("Enter elements: ")))
max=0                                                                         
for j in range(0,len(arr)):
    if(arr[j]>max):
        max=arr[j]

l=[0]*(max+1)
for i in range(0,len(arr)):
    l[arr[i]]+=1

max1=0
c=0
for k in range(0,len(l)):
    if(l[k]>max1):
        max1=l[k]
        c=k

    
print(c)