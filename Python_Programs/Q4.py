def func(s):
    n=len(s)
    str=""
    for i in range(0,n):
        str=str+s[i]+s[i]
    return(str)

a=input("Enter string: ")
print(func(a))