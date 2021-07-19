a=[]
n=int(input("Enter the size of the array: "))
i=0
while(i<n):
    a.append(int(input()))
    i+=1
a.sort()
max1=int(input("Enter the budget: "))
i=0
sum1=0
count=0
while(i<n):
    if((sum1+a[i])<max1):
        sum1=sum1+a[i]
        count+=1
print(count)
