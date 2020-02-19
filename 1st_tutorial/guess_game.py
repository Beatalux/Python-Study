guess_count=0
guess_limit=3
guess=""
guess_bool=True

while guess!="giraffe" and guess_bool:
    if(guess_count<guess_limit):
        guess=input()
        guess_count+=1  # ++ non-exist
    else:
        guess_bool=False


if guess_bool==True:
    print("win")
else:
    print("lose")