coding = int(input("Enter 1 for coding and 0 for decding: "))
st= input("Enter message: ")
words = st.split(" ")
if(coding==1):
    coding = True
elif (coding==0):
    coding= False
else:
    print("Envalid input")
if(coding):
    nwords =[]
    for word in words:
        if(len(word)>=3):
            r1 ='sdk'
            r2 = 'bhj'
            stnew = r1 + word[1:] + word[0] +r2
            nwords.append(stnew)
        else:
            nwords.append(stnew)
    print(" ".join(nwords))

else: 
    nwords =[]
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew =stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[:-1])
    print(" ".join(nwords))