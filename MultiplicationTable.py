a= int(input("Enter the number: "))

print(f"Multiplication Table of {a} is :\n")

for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a*i)}")
