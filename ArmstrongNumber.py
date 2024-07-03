def Armstrong(n):
    n_str=str(n)
    n_digits=len(n_str)

    sum_of_powers=sum(int(digit)**n_digits for digit in n_str)

    return sum_of_powers == n

n= int(input("enter a number: "))
if Armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")