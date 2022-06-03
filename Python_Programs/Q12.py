arr=list(eval(input("Enter the list(1-99): ")))
l=list()
l=[0]*100

for i in range(0,100):
    l[arr[i]]+=1
    if l[arr[i]]==2:
        print(arr[i])
        break

    
