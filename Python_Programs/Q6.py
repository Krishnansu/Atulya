from math import sqrt
def prime(n):
    c=0
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            c+=1
            return(False)
    if(c==0):
        return(True)

l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
for j in range(l,u):
    if(prime(j)):
        print(j)
