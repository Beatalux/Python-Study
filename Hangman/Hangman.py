from random import randint


try:
    words=open("Hangman/sowpods.txt","r")
except FileNotFoundError as err:
    print(err)

i=randint(1,267752)
anl=words.readlines()
an=anl[i]
ans=list(an)
length=len(ans)
print("The word has "+str(length-1)+" letter")


stri=[]
for i in range(length-1):
        #stri[i]="_ "       error!!
        stri.append("_ ")

for guess in range(5,-1,-1):
    user=input("guess the letter (To type answer, type 0) ")
    if(user == '0' ):
        answer=input("full word : ")
        if(an.rstrip().upper()==answer.upper()):
            print("correct!")
            break
        else:
            print("wrong.")
            continue

    if(user.upper() in ans):
        for i in range(length-1):
            if(user.upper()==ans[i]):
                stri[i]=user
        print(' '.join(stri))
    
    else:
        print("The word doesn't have "+user)
    if(guess==1):
        print("last chance!")
    elif(guess==0):
        print("The answer is "+an)
        print("game over")
    else:
        print(str(guess)+" chances left")