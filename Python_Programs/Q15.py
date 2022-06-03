str=input("Enter string: ")
alpha,dig,spc=0,0,0
for i in range(0,len(str)):
    if(str[i].isalpha()):
        alpha+=1
    elif(str[i].isdigit()):
        dig+=1
    else:
        spc+=1
print("Alpha= ",alpha,"Digits= ",dig,"Special Characters= ",spc)