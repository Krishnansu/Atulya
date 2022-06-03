def operator(p,a,q):
    if(a=="+"):
        return(p+q)
    elif(a=="-"):
        return(p-q)
    elif(a=="/"):
        return(p/q)
    elif(a=="*"):
        return(p*q)

n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
b=input("Enter operator(+,-,/,*): ")
print(operator(n,b,m))
    