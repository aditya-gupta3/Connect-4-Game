

import Tkinter
from Tkinter import *
import tkMessageBox


x= [[0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0]]
z= [[0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0]]
y=[0,0,0,0,0,0,0]
style=0
z1=0
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
turn=0
row_clicked=0
turn_computer=6
player_num=0
playervsplayer=0
computer=0

def buttons_rules():
# This creates a button.

    for i in range(0, len(y)):
        y[i]= button_1 = Button(main_window, text = str(i+1),command= lambda x1=i:buttonrules_action(x1))


#put this into the window
    for i in range(0, len(y)):
           y[i].grid(row=i, column = 7)



def print_rules():
    print 'The board is going to be sideways'
    print 'Every person gets one chance per move'
    print 'The first to get four in a row wins the game'

def print_board():
    print x
def get_input(player_num):
    global z1,z2,z3,z4
    y=input('Hello Player ' + str(player_num +1 ) + ': Which row do you want to put your coin in ')
    return y
    

def valid():
    global row_clicked
    global z1,z2,z3,z4
    if row_clicked==1 and z1<6:
        return True
    elif row_clicked==2 and z2<6:
        return True
    elif row_clicked==3 and z3<6:
        return True
    elif row_clicked==4 and z4<6:
        return True
    elif row_clicked==5 and z5<6:
        return True
    elif row_clicked==6 and z6<6:
        return True
    elif row_clicked==7 and z7<6:
        return True
    else:
        return False
def update_board_computer():
    global turn
    global row_clicked
    global z1,z2,z3,z4,z5,z6,z7
    global player_num
    player_num=turn%2
    if not valid():
        tkMessageBox.showinfo("Error", "This row is filled")
    elif player_num==0:
        tkMessageBox.showinfo("you pressed", str(row_clicked))

        if row_clicked ==1:
            x[row_clicked-1][z1] = 'x'
        if row_clicked==2:
            x[row_clicked-1][z2] = 'x'
        if row_clicked==3:
            x[row_clicked-1][z3] = 'x'
        if row_clicked==4:
            x[row_clicked-1][z4] = 'x'
        if row_clicked==5:
            x[row_clicked-1][z5] = 'x'
        if row_clicked==6:
            x[row_clicked-1][z6] = 'x'
        if row_clicked==7:
            x[row_clicked-1][z7] = 'x'
        if row_clicked==1:
            z1=z1+1
        if row_clicked==2:
            z2=z2+1

        if row_clicked==3:
            z3=z3+1

        if row_clicked==4:
            z4=z4+1
        if row_clicked==5:
            z5=z5+1
        if row_clicked==6:
            z6=z6+1
        if row_clicked==7:
            z7=z7+1
        update_GUI()
    
        computer_move()
        if row_clicked ==1:
            x[row_clicked-1][z1] = 'y'
        if row_clicked==2:
            x[row_clicked-1][z2] = 'y'
        if row_clicked==3:
            x[row_clicked-1][z3] = 'y'
        if row_clicked==4:
            x[row_clicked-1][z4] = 'y'
        if row_clicked==5:
            x[row_clicked-1][z5] = 'y'
        if row_clicked==6:
            x[row_clicked-1][z6] = 'y'
        if row_clicked==7:
            x[row_clicked-1][z7] = 'y'
        if row_clicked==1:
            z1=z1+1
        if row_clicked==2:
            z2=z2+1

        if row_clicked==3:
            z3=z3+1

        if row_clicked==4:
            z4=z4+1
        if row_clicked==5:
            z5=z5+1
        if row_clicked==6:
            z6=z6+1
        if row_clicked==7:
            z7=z7+1
    if not valid():
        computer_move()

    update_GUI()

    checked()

def update_board():
    global turn
    global row_clicked
    global z1,z2,z3,z4,z5,z6,z7
    global player_num
    player_num=turn%2
    if not valid():
        tkMessageBox.showinfo("Error", "This row is filled")
    elif player_num==0:
        if row_clicked ==1:
            x[row_clicked-1][z1] = 'x'
        if row_clicked==2:
            x[row_clicked-1][z2] = 'x'
        if row_clicked==3:
            x[row_clicked-1][z3] = 'x'
        if row_clicked==4:
            x[row_clicked-1][z4] = 'x'
        if row_clicked==5:
            x[row_clicked-1][z5] = 'x'
        if row_clicked==6:
            x[row_clicked-1][z6] = 'x'
        if row_clicked==7:
            x[row_clicked-1][z7] = 'x'

    elif player_num==1:
       
        if row_clicked ==1:
            x[row_clicked-1][z1] = 'y'
        if row_clicked==2:
            x[row_clicked-1][z2] = 'y'
        if row_clicked==3:
            x[row_clicked-1][z3] = 'y'
        if row_clicked==4:
            x[row_clicked-1][z4] = 'y'
        if row_clicked==5:
            x[row_clicked-1][z5] = 'y'
        if row_clicked==6:
            x[row_clicked-1][z6] = 'y'
        if row_clicked==7:
            x[row_clicked-1][z7] = 'y'
    turn=turn+1
    update_GUI()
    checked()


def playerplayer():
    global style
    style="player"
    print style
    if style=="computer":

        buttons_computer()
        update_GUI()
    else:

        buttons()
        update_GUI()
# This creates a button.

            
def playervscomputer():
    global style
    style="computer"
    print style
    if style=="computer":

        buttons_computer()
        update_GUI()
    else:

        buttons()
        update_GUI()

def main():
    print_rules()
    
    global player_num
    global turn
    button_playervsplayer()
    


    
   





#create a window
main_window = Tkinter.Tk()
#set its attributes
main_window.geometry("500x500")      #size in points
main_window.wm_title("Hello, welcome to connect 4") #the title that you see


#create a button array
def button1_action(r):
    global row_clicked
    global z1,z2,z3,z4,z5,z6,z7
    row_clicked=r+1
    update_board()

    if  valid():
        tkMessageBox.showinfo("you pressed", str(r+1))

        if row_clicked==1:
            z1=z1+1
        if row_clicked==2:
            z2=z2+1

        if row_clicked==3:
            z3=z3+1

        if row_clicked==4:
            z4=z4+1
        if row_clicked==5:
            z5=z5+1

        if row_clicked==6:
            z6=z6+1

        if row_clicked==7:
            z7=z7+1
def button2_action(r):
    global row_clicked
    global z1,z2,z3,z4,z5,z6,z7
    row_clicked=r+1
    update_board_computer()

    
def checked():
    global player_num
    for i in range (0,4):
        if x[i]==["x","x","x","x"]:
            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
        elif x[i]==['y','y','y','y']:
            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    if x[0][0]=='x' and x[1][1]=='x'and x[2][2]=='x'and x[3][3]=='x':
        tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    if x[0][3]=='x' and x[1][2]=='x'and x[2][1]=='x'and x[3][0]=='x':
        tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    if x[0][0]=='y' and x[1][1]=='y'and x[2][2]=='y'and x[3][3]=='y':
        tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    if x[0][3]=='y' and x[1][2]=='y'and x[2][1]=='y'and x[3][0]=='y':
        tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    
    if x[0][0]==["x"] and x[1][0]==["x"] and x[2][0]==["x"] and x[3][0] == ["x"]:
            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    if x[0][1]==["y"] and x[1][1]==["y"] and x[2][1]==["y"] and x[3][1]==['y']:
            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
    
    # this thing above checks one diagonol, make another one for 1. player 2, and 2. for the other diagnols)

def button_playervsplayer():
    buttons()
    update_GUI()

    playervsplayer = Button(main_window, text = "player vs player",command= lambda: playerplayer())


    playervsplayer.grid(row=8, column = 9)
    computer = Button(main_window, text = "player vs computer",command= lambda: playervscomputer())



    computer.grid(row=9, column = 9)

 


    

    
    
##        elif x[0][0]==['y'] and x[1][1]==['y'] and x[2][2]==['y'] and x[3][3]==['y']:
##            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
##        elif  x[0][3]==['x'] and x[1][2]==['x'] and x[2][1]==['x'] and x[3][0]==['x']:
##            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
##        elif  x[0][3]==['y'] and x[1][2]==['y'] and x[2][1]==['y'] and x[3][0]==['y']:
##            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
##        elif x[i][0]=="x":
##            tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
##        elif x[j]==["x","x","x","x"]:
##           tkMessageBox.showinfo("player won",'player '+str(player_num+1)+" won")
##    

    
            
# This creates a button.

            

def buttons():
# This creates a button.

    for i in range(0, len(y)):
        y[i]= button_1 = Button(main_window, text = str(i+1),command= lambda x1=i:button1_action(x1))


#put this into the window
    for i in range(0, len(y)):
           y[i].grid(row=i, column = 10)

        
def buttons_computer():
# This creates a button.

    for i in range(0, len(y)):
        y[i]= button_1 = Button(main_window, text = str(i+1),command= lambda x1=i:button2_action(x1))


#put this into the window
    for i in range(0, len(y)):
           y[i].grid(row=i, column = 10)


def update_GUI():
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            z[i][j]= Label(main_window, text=x[i][j], relief = RAISED)
    for i in range(0, len(z)):
        for j in range(0, len(x[i])):
            z[i][j].grid(row=i, column = j)

def computer_move():
    global turn_computer 
    global row_clicked
    global player_num
    global z1,z2,z3,z4,z5,z6,z7
    row_clicked= turn_computer % 4 +1 # divided by 4 because there are only 4 rows and rows start from 0
    turn_computer=turn_computer+1
    if  valid():
        tkMessageBox.showinfo("Computer Move", "Computer moved in  "+str(row_clicked))
    
main()
main_window.mainloop()



#function that is run when the button is clicked
def button_rules_action():
    tkMessageBox.showinfo("you pressed", "thanks!")
button_rules = Button(main_window, text = "Press",command = button_rules_action )


