a = input("Enter the number: ")

try:
    num = int(a)

    print(f"Multiplication Table of {num}:\n")

    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")


print("\nSome important lines of code")
