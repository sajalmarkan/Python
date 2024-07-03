arr=[]
a= int(input("Enter the number of the elements: "))

print("Enter the Elements")
for i in range(a):
    element = int(input())
    arr.append(element)

print("Array is:",arr)
sum=0
for num in arr:
    sum += num
print("Sum of the array is :", sum)