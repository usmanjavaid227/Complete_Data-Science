import random

l=['rock','scissor','paper']

while True:
    ccount = 0
    ucount = 0
    uc=int(input('''
            Game start........
            1 Yes 
            2 No | exit
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
                1 Rock
                2 scissor
                3 paper
            '''))
            if userInput==1:
                uchoice='rock'
            elif userInput==2:
                uchoice='scissor'
            elif userInput==3:
                uchoice='paper'
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("computer value : ",Cchoice)
                print("User value : ",uchoice)
                print("Game draw : ")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor" )or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("computer value : ",Cchoice)
                print("User value : ",uchoice)
                print("You Win ! ")
                ucount=ucount+1
            else:
                print("computer value : ",Cchoice)
                print("User value : ",uchoice)
                print("Computer win ! ")
                ccount=ccount+1
        print("\n\n")
        if ucount==ccount:
            print("Final Game Draw ... ")
            print("computer score : ",ccount)
            print("User score : ",ucount)
        elif ucount>ccount:
            print("Final You Win the Game  ... ")
            print("computer score : ",ccount)
            print("User score : ",ucount)
        else:
            print("Final computer wins the Game...")
            print("computer score : ",ccount)
            print("User score : ",ucount)
    else:
        break
