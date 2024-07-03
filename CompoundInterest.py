def CI(p,r,t):
    print("Principle is:",p)
    print("Rate of interest is:",r)
    print("time period is:",t)

    amount=p*((1+r/100)**t)
    ci=amount-p
    print(f"Compound interest is: {ci:.2f}")

p= int(input("Enter the principle amount: "))
r= int(input("Enter the rate of interest of the amount: "))
t= int(input("Enter the time period: "))

CI(p,r,t)