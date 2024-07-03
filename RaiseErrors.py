a= int(input("Enter the value between 5 and 9: "))
if a<5 or a>9 :
    raise ValueError("value should be between 5 and 9")
else:
    print(f"The entered value is {a}")