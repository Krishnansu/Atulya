def gcd(n,m):
    r=1
    while(r!=0):
        r=m%n
        m,n=n,r
    return(m)
    




a=int(input("First number: "))
b=int(input("Second number: "))
if(b>a):
    print(gcd(a,b))
else:
    print(gcd(b,a))

