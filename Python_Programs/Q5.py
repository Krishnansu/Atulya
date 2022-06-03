ar=list(eval(input("Enter the list(1-99): ")))
l=list()
l=[0]*100

for i in range(0,100):
    l[ar[i]]+=1
    if l[ar[i]]==2:
        print(ar[i])
        break

    
