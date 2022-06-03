s=input("Enter string: ")
sum=0
for i in range(0,len(s)):
    if(s[i].isdigit()):
        sum+=int(s[i])
    else:
        continue
print(sum)
