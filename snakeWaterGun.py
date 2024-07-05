import random

def check(comp,user):
    if comp == user:
        return 0
    if(comp==0 &user ==1):
        return -1
    if(comp==1 &user ==2):
        return -1
    if(comp==2 &user ==0):
        return -1
    
    return 1
comp =random.randint(0,2)

try:
    user = int(input("Enter 0 for snake, 1 for water and 2 for Gun:\n"))
    if user <0 or user>2:
        print("Enter Valid Input")

    else: 
        score = check(comp,user)

        print("You:",user)
        print("Computer:",comp)

        if(score ==0):
            print("Its a draw")

        elif(score ==-1):
            print("You loose")
        else:
            print("You Won")

except ValueError:
    print ("Enter a valid under between 0 and 2")