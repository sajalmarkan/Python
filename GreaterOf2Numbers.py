def Greater(a, b):
    if a > b:
        return "a"
    elif b > a:
        return "b"
    else:
        return "Both are equal"

# Get user input for a and b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the Greater function with the input values and print the result
result = Greater(a, b)
if result == "Both are equal":
    print(f"In the numbers {a} and {b},\nboth are equal.")
else:
    print(f"In the numbers {a} and {b},\n{result} is greater.")
