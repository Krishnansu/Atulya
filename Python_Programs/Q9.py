str=input("Enter string to sort: ")
l=[]
n=len(str)
for i in range(0,n):
    l.append(str[i])

for k in range(0,n):
    for j in range(0,n-k-1):
        if(ord(l[j])>ord(l[j+1])):
            l[j],l[j+1]=l[j+1],l[j]

s=""
for i in range(0,n):
    s=s+l[i]
print(s)