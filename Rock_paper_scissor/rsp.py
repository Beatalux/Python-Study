import random

random.seed()

def specific(user,wl):
    which_u=""
    which_c=""
    if(user==1):
        which_u="rock"
        if(wl==0):
            which_c=which_u
        elif(wl==1):
            which_c="scissor"
        elif(wl==-1):   #else essential?-->no
            which_c="paper"
        
    elif(user==2):
        which_u="scissor"
        if(wl==0):
            which_c=which_u
        elif(wl==1):
            which_c="paper"
        else:  
            which_c="rock"

    else:
        which_u="paper"
        if(wl==0):
            which_c=which_u
        elif(wl==1):
            which_c="rock"
        else:  
            which_c="scissor"

    print("You chose "+which_u+", computer chose "+which_c)


user=3

while True:    #str..?
    computer=random.randint(1,4)
    try:
        user=int(input("If you want rock, input 1\nIf you want scissor, input 2\nIf you want paper, input 3\n-->"))
    except ValueError:
        print("invalid input")
        continue

    if user==0:
        break
    
    if user not in range(0,4):  #expression!!!
        print("try again")
        continue

    if(computer == user):
        specific(user,0)
        print("jinx!")
        
    elif(computer > user):
        specific(user,-1)
        print("you lose")
    else:
        specific(user,1)
        print("you win!")

    print("TO finish, type 0:")



