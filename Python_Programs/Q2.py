def hide(a):
    n=len(a)
    s=""
    for i in range(0,n):
        if(i<n-4):
            s=s+"*"
        else:
            s=s+a[i]
    
    return(s)

n=input("Enter card number: ")
print(hide(n))



