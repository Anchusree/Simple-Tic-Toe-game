from tkinter import *

tc = Tk()
tc.title("Tic Tac Toe")

button1 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button2 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button3 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button4 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button5 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button6 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button7 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button8 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))
button9 = Button(tc,text=" ", width=8,height = 4, command = lambda:checker(Button1))

button1.grid(row=1, column = 0)
button2.grid(row=1, column = 1)
button3.grid(row=1, column = 2)
button4.grid(row=2, column = 0)
button5.grid(row=2, column = 1)
button6.grid(row=2, column = 2)
button7.grid(row=3, column = 0)
button8.grid(row=3, column = 1)
button9.grid(row=3, column = 2)





tc.mainloop()
