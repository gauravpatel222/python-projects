import turtle as t
import random


def computer():
 def grid_prep():
    t.showturtle()
    t.screensize(1000,1000)
    t.pensize(5)
    t.penup()
    t.goto(-100,0)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.right(90)
    t.goto(0,100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(100,100)
    t.pendown()
    t.forward(300)
    t.hideturtle()
    t.penup()
 def player_name():
    global p1
    global p2
    p1=input("Player 1st name : ")
    p2="computer"
 def character():
    print(p1,", Which character would you like X or O : ")
    global cp1,cp2
    cp1=input()
    if(cp1=="X" or cp1=="x"):
        cp1="X"
        cp2="O"
    elif(cp1=="O" or cp1=="o"):
        cp1="O"
        cp2="X"
    else:
        print("invalid selection!! - try again")
        character()
    print("--------------------------------------------")
    print("%s : %c | %s : %c"%(p1,cp1,p2,cp2))
    print("--------------------------------------------\n")
 def winner_select():
    if(i>=4):
        if(l[1]==l[5]==l[9]!=""):
            if(l[1]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[3]==l[5]==l[7]!=""):
            if(l[3]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[1]==l[2]==l[3]!=""):
            if(l[1]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[4]==l[5]==l[6]!=""):
            if(l[4]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[7]==l[8]==l[9]!=""):
            if(l[7]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[1]==l[4]==l[7]!=""):
            if(l[1]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[2]==l[5]==l[8]!=""):
            if(l[2]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[3]==l[6]==l[9]!=""):
            if(l[3]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(i==8):
            print("It's a tie")
            return(True)
        else:
            return(False)
 def entering():
    a=True
    while(a):
        r=int(input("Enter the space you want to enter :"))
        if(r>=1 and r<=9):
            if(l[r]==""):
                l.update({r:ch})
                a=False
                print("--------------------------------------------")
            else:
                print(" Already occupied!! - try again..")
        else:
            print("invalid choice!! - try again")
    return(r)
 def entering1():
    a=True
    while(a):
        r1=random.randint(1,9)
        print("computer chooses",r1)
        if(r1>=1 and r1<=9):
            if(l[r1]==""):
                l.update({r1:ch})
                a=False
                print("--------------------------------------------")
            else:
                print(" Already occupied!! - try again..")
        else:
            print("invalid choice!! - try again")
    return(r1)
 def turn(i):
    global ch
    if(i%2==0):
        ch=cp1
        print("--------------------------------------------")
        print(p1,"'s turn : ")
        return(entering())
    else:
        ch=cp2
        print("--------------------------------------------")
        print(p2,"'s turn : ")
        return(entering1())
 def game():
    global i
    for i in range(9):
        x=turn(i)
        if(x==1):
            t.goto(-50,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==2):
            t.goto(50,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==3):
            t.goto(150,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==4):
            t.goto(-50,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==5):
            t.goto(50,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==6):
            t.goto(150,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==7):
            t.goto(-50,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==8):
            t.goto(50,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==9):
            t.goto(150,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
    exit()
 def exit():
    yorn=input("Do you want to play again or not(Y or N): ")
    if(yorn=="Y" or yorn=="y"):
        t.reset()
        t.color("Black")
        grid_prep()
        global p1
        global p2
        for i in range(1,10):
            l.update({i:""})
        p1,p2=p2,p1
        response=input("Do you want to play with computer or with partener:Y/N")
        if response=="Y" or response=="y":
                    computer()
        else:
                    partener()
        character()
        game()
    elif(yorn=="N" or yorn=="n"):
        print("Thanks for playing..")
    else:
        print("invalid choice!! - try again..")
        exit()

 l={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
 grid_prep()
 player_name()
 character()
 game()
def partener():
 def grid_prep():
    t.showturtle()
    t.screensize(1000,1000)
    t.pensize(5)
    t.penup()
    t.goto(-100,0)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.right(90)
    t.goto(0,100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(100,100)
    t.pendown()
    t.forward(300)
    t.hideturtle()
    t.penup()
 def player_name():
    global p1
    global p2
    p1=input("Player 1st name : ")
    p2=input("Player 2nd name : ")
 def character():
    print(p1,", Which character would you like X or O : ")
    global cp1,cp2
    cp1=input()
    if(cp1=="X" or cp1=="x"):
        cp1="X"
        cp2="O"
    elif(cp1=="O" or cp1=="o"):
        cp1="O"
        cp2="X"
    else:
        print("invalid selection!! - try again")
        character()
    print("--------------------------------------------")
    print("%s : %c | %s : %c"%(p1,cp1,p2,cp2))
    print("--------------------------------------------\n")
 def winner_select():
    if(i>=4):
        if(l[1]==l[5]==l[9]!=""):
            if(l[1]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[3]==l[5]==l[7]!=""):
            if(l[3]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[1]==l[2]==l[3]!=""):
            if(l[1]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[4]==l[5]==l[6]!=""):
            if(l[4]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[7]==l[8]==l[9]!=""):
            if(l[7]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[1]==l[4]==l[7]!=""):
            if(l[1]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[2]==l[5]==l[8]!=""):
            if(l[2]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(l[3]==l[6]==l[9]!=""):
            if(l[3]==cp1):
                print(p1," WON!!")
                return(True)
            else:
                print(p2," WON!!")
                return(True)
        elif(i==8):
            print("It's a tie")
            return(True)
        else:
            return(False)
 def entering():
    a=True
    while(a):
        r=int(input("Enter the space you want to enter :"))
        if(r>=1 and r<=9):
            if(l[r]==""):
                l.update({r:ch})
                a=False
                print("--------------------------------------------")
            else:
                print(" Already occupied!! - try again..")
        else:
            print("invalid choice!! - try again")
    return(r)
 def turn(i):
    global ch
    if(i%2==0):
        ch=cp1
        print("--------------------------------------------")
        print(p1,"'s turn : ")
        return(entering())
    else:
        ch=cp2
        print("--------------------------------------------")
        print(p2,"'s turn : ")
        return(entering())
 def game():
    global i
    for i in range(9):
        x=turn(i)
        if(x==1):
            t.goto(-50,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==2):
            t.goto(50,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==3):
            t.goto(150,-10)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==4):
            t.goto(-50,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==5):
            t.goto(50,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==6):
            t.goto(150,-115)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==7):
            t.goto(-50,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==8):
            t.goto(50,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
        elif(x==9):
            t.goto(150,-215)
            if(ch=="X"):
                t.color("Red")
            else:
                t.color("Blue")
            t.write(ch,align='center',font=('Comic sans MS',70,'bold'))
            val=winner_select()
            if(val==True):
                break
    exit()
 def exit():
    yorn=input("Do you want to play again or not(Y or N): ")
    if(yorn=="Y" or yorn=="y"):
        t.reset()
        t.color("Black")
        grid_prep()
        global p1
        global p2
        for i in range(1,10):
            l.update({i:""})
        p1,p2=p2,p1
        if response=="Y" or response=="y":
                    computer()
        else:
                    partener()
        character()
        character()
        game()
    elif(yorn=="N" or yorn=="n"):
        print("Thanks for playing..")
    else:
        print("invalid choice!! - try again..")
        exit()

 l={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
 grid_prep()
 player_name()
 character()
 game()
response=input("Do you want to play with computer or with partener:Y/N")
if response=="Y" or response=="y":
    computer()
else:
    partener()

