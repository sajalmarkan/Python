sum =0
while(True):
    userInput = input("Enter the price or press q to quit\n")
    if(userInput!="q"):
        sum=sum+int(userInput)
        print(f"Your total so far is: {sum}")
    else:
        print(f"Your total is {sum} thanks for using this program")
        break
    
