arr=[]
num=int(input("Enter no of elements to insert"))
for i in range(num):
    print("Enter the",i+1,"element:")
    digit=int(input())
    arr.append(digit)
j=0
t=0
for i in range(num):
    for j in range(0,num-i-1):
        if(arr[j]<=arr[j+1]):
            t=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=t
print("After sorting")
for i in range(num):
    print(arr[i])
