from math import sqrt
def prime(m):
    c=0
    for i in range(2,int(sqrt(m))+1):
        if(m%i==0):
            c+=1
            return(False)
    if(c==0):
        return(True)
arr=[]
m=2
q=int(input("Enter no.of test cases: "))
for i in range(0,q):
    n=int(input("\nEnter n: "))
    if(len(arr)>=n):
        for j in range(0,n):
            print(arr[j],end=" ")
    else:
        for k in range(0,len(arr)):
            print(arr[k],end=" ")
        c=len(arr)
        while(c<n):
            if(prime(m)):
                c+=1
                print(m,end=" ")
                arr.append(m)
            m+=1



    