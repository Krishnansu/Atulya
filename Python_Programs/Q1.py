def sort(a,b):
    if(b=="none"):
        return(a)
    else:
        for i in range(0,len(a)):
            for j in range(0,len(a)-i-1):
                if(a[j]>a[j+1]):
                    a[j],a[j+1]=a[j+1],a[j]
        if(b=="asc"):
            return(a)
        elif(b=="desc"):
            return(a[ : :-1])


l=list(eval(input("Enter the list: ")))

ans=input("Enter sorting order(asc/desc/none): ")
print(sort(l,ans))

