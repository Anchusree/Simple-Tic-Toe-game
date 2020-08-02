from tkinter import *

from tkinter import messagebox 

tc = Tk()
tc.title("Simple Tic Tac Toe Game")
tc.geometry("700x700")
tc.configure(background='Cadet Blue')

MainFrame = Frame(tc, bg = "Powder Blue", width=700, height=700)
MainFrame.grid(row=0, column=0)

RightFrame = Frame(MainFrame, bd=10, bg = "Powder Blue", width=100, height=100)
RightFrame.grid(row=0, column=0)




click = True
buttons = StringVar()


button1 = Button(MainFrame,text=" ", width=8,height = 4, font=('Times 24 bold'), command = lambda:check(button1))
button2 = Button(MainFrame,text=" ", width=8,height = 4,font=('Times 24 bold'), command = lambda:check(button2))
button3 = Button(MainFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button3))
button4 = Button(MainFrame,text=" ", width=8,height = 4,font=('Times 24 bold'), command = lambda:check(button4))
button5 = Button(MainFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button5))
button6 = Button(MainFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button6))
button7 = Button(MainFrame,text=" ", width=8,height = 4,font=('Times 24 bold'), command = lambda:check(button7))
button8 = Button(MainFrame,text=" ", width=8,height = 4,font=('Times 24 bold'),command = lambda:check(button8))
button9 = Button(MainFrame,text=" ", width=8,height = 4, font=('Times 24 bold'),command = lambda:check(button9))

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
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
    elif (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
          button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
          button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
          button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
          button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
          button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
          button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
          button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
          button7["text"] == "X" and button5["text"] == "X" and button3["text"] == "X"):
          messagebox.showinfo("Congratulations", "You have won the game!!!") 
   
        
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button7["text"] == "O" and button5["text"] == "O" and button3["text"] == "O"):
          messagebox.showinfo("Congratulations", "You have won the game!!!") 
    else:
          messagebox.showinfo("Oops"," Your Game is Over!!!") 
    
            


tc.mainloop()
