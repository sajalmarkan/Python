def SI(p,r,t):
    print("Principle is:",p)
    print("Rate of interest is:",r)
    print("time period is:",t)

    si=(p*r*t)/100
    print("Simple interest is",si)
    return si

p= int(input("Enter the principle amount"))
r= int(input("Enter the rate of interest of the amount"))
t= int(input("Enter the time period"))

SI(p,r,t)