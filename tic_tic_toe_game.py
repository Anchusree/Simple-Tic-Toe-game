from tkinter import *

from tkinter import messagebox 

tc = Tk()
tc.title("Simple Tic Tac Toe Game") 
tc.geometry("1350x750+0+0")
tc.configure(background='Cadet Blue')

Tops = Frame(tc, bg="Cadet Blue",width = 1350, height=100, relief = RIDGE)
Tops.grid(row=0, column = 0)

GameTitle = Label(Tops,font=("arial",40,"bold"), text="Simple Tic Tac Toe Game", bd = 21, bg='Cadet Blue', justify = CENTER)
GameTitle.grid(row=0,column=0)

MainFrame = Frame(tc, bg = "Powder Blue",bd=10, width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500,padx = 10,pady=2 , bg = "Cadet Blue", relief = RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame,bd=10, width=560, height=200,padx = 10,pady=2 , bg = "Cadet Blue", relief = RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, bg = "Cadet Blue",padx = 10,pady=2, width=560, height=200, relief = RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, bg = "Cadet Blue",padx = 10,pady=2, width=560, height=200, relief = RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

Label_PlayerX = Label(RightFrame1,font=('arial',30,'bold'), text = 'Player X: ', padx = 2,pady = 2, bg = 'Cadet Blue')
Label_PlayerX.grid(row=0, column = 0, sticky = S+N+E+W)
txtPlayerX= Entry(RightFrame1,font=('arial',30,'bold'),bd=2,fg= 'black',textvariable = PlayerX, width=14,justify = LEFT).grid(row=0,column=1)

Label_PlayerO = Label(RightFrame1,font=('arial',30,'bold'), text = 'Player O: ', padx = 2,pady = 2, bg = 'Cadet Blue')
Label_PlayerO.grid(row=1, column = 0, sticky = S+N+E+W)
txtPlayerO= Entry(RightFrame1,font=('arial',30,'bold'),bd=2,fg= 'black',textvariable = PlayerO, width=14,justify = LEFT).grid(row=1,column=1)


Reset_bttn = Button(RightFrame2,text="Reset", width=10,height = 4, font=('Times 24 bold'), command = lambda:reset())
NewGame_bttn = Button(RightFrame2,text="New Game", width=10,height = 4,font=('Times 24 bold'), command = lambda:NewGame())

Reset_bttn.grid(row=1, column = 0)
NewGame_bttn.grid(row=1, column = 1)


click = True
buttons = StringVar()


button1 = Button(LeftFrame,text=" ", width=8,height = 4, font=('Times 24 bold'), command = lambda:check(button1),bg = 'light gray', fg="medium blue")
button2 = Button(LeftFrame,text=" ", width=8,height = 4,font=('Times 24 bold'), command = lambda:check(button2),bg = 'light gray', fg="medium blue")
button3 = Button(LeftFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button3),bg = 'light gray', fg="medium blue")
button4 = Button(LeftFrame,text=" ", width=8,height = 4,font=('Times 24 bold'), command = lambda:check(button4),bg = 'light gray', fg="blue")
button5 = Button(LeftFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button5),bg = 'light gray', fg="blue")
button6 = Button(LeftFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button6),bg = 'light gray', fg="blue")
button7 = Button(LeftFrame,text=" ", width=8,height = 4,font=('Times 24 bold'), command = lambda:check(button7),bg = 'light gray', fg="blue")
button8 = Button(LeftFrame,text=" ", width=8,height = 4,font=('Times 24 bold'),command = lambda:check(button8),bg = 'light gray', fg="blue")
button9 = Button(LeftFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button9),bg = 'light gray', fg="blue")

button1.grid(row=1, column = 0, sticky = S+N+E+W)
button2.grid(row=1, column = 1, sticky = S+N+E+W)
button3.grid(row=1, column = 2, sticky = S+N+E+W)
button4.grid(row=2, column = 0, sticky = S+N+E+W)
button5.grid(row=2, column = 1, sticky = S+N+E+W)
button6.grid(row=2, column = 2, sticky = S+N+E+W)
button7.grid(row=3, column = 0, sticky = S+N+E+W)
button8.grid(row=3, column = 1, sticky = S+N+E+W)
button9.grid(row=3, column = 2, sticky = S+N+E+W)


def check(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
        
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

    

def scorekeeper():
    if  button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")
        
    elif  button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.configure(background="powder blue")
        button5.configure(background="powder blue")
        button6.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")
        
        
    elif  button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.configure(background="powder blue")
        button8.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
        
    elif  button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.configure(background="powder blue")
        button4.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
        
    elif  button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.configure(background="powder blue")
        button5.configure(background="powder blue")
        button8.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
        
    elif  button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.configure(background="powder blue")
        button6.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
        
    elif  button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.configure(background="powder blue")
        button5.configure(background="powder blue")
        button7.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
        
    elif  button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.configure(background="powder blue")
        button5.configure(background="powder blue")
        button9.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
        
    elif  button7["text"] == "X" and button5["text"] == "X" and button3["text"] == "X":
        button7.configure(background="powder blue")
        button5.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        messagebox.showinfo("Congratulations", "PlayerX won the game!!!")        
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
       button1.configure(background="powder blue")
       button2.configure(background="powder blue")
       button3.configure(background="powder blue")
       n = float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
           
    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
       button4.configure(background="powder blue")
       button5.configure(background="powder blue")
       button6.configure(background="powder blue")
       n = float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
        
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
       button7.configure(background="powder blue")
       button8.configure(background="powder blue")
       button9.configure(background="powder blue")
       n = float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
        
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
       button1.configure(background="powder blue")
       button4.configure(background="powder blue")
       button7.configure(background="powder blue")
       n = float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
       
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
       button2.configure(background="powder blue")
       button5.configure(background="powder blue")
       button8.configure(background="powder blue")
       n = float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
       
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
       button3.configure(background="powder blue")
       button6.configure(background="powder blue")
       button9.configure(background="powder blue")
       n = float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
           
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
         button3.configure(background="powder blue")
         button5.configure(background="powder blue")
         button7.configure(background="powder blue")
         n = float(PlayerO.get())
         score=(n+1)
         PlayerO.set(score)
         messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
           
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
         button1.configure(background="powder blue")
         button5.configure(background="powder blue")
         button9.configure(background="powder blue")
         n = float(PlayerO.get())
         score=(n+1)
         PlayerO.set(score)
         messagebox.showinfo("Congratulations", "PlayerO won the game!!!")
       
    elif button7["text"] == "O" and button5["text"] == "O" and button3["text"] == "O":
         button7.configure(background="powder blue")
         button5.configure(background="powder blue")
         button3.configure(background="powder blue")
         n = float(PlayerO.get())
         score=(n+1)
         PlayerO.set(score)
         messagebox.showinfo("Congratulations", "PlayerO won the game!!!")

             
            
def reset():
    button1['text' ]= " "
    button2['text' ]= " "
    button3['text' ]= " "
    button4['text' ]= " "
    button5['text' ]= " "
    button6['text' ]= " "
    button7['text' ]= " "
    button8['text' ]= " "
    button9['text' ]= " "

    button1.configure(background ='light gray')
    button2.configure(background ='light gray')
    button3.configure(background ='light gray')
    button4.configure(background ='light gray')
    button5.configure(background ='light gray')
    button6.configure(background ='light gray')
    button7.configure(background ='light gray')
    button8.configure(background ='light gray')
    button9.configure(background ='light gray')
    
    
def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    
    

tc.mainloop()
