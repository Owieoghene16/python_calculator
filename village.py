from tkinter import *

window = Tk()
window.geometry("312x324")
window.resizable(0, 0)
window.title("Owie Invented Calculator")


arithmetic_value = ""
def screen_display(value):
    global arithmetic_value
    arithmetic_value += value
    but_entry.insert(END, value)
    print(arithmetic_value)
    
def clear_button():
    global arithmetic_value
    but_entry.delete(0, len(arithmetic_value))
    but_entry.insert(0, "0")
    arithmetic_value = "0"

def delete_button():
    global arithmetic_value
    but_entry.delete(len(arithmetic_value) - 1)
    arithmetic_value = arithmetic_value[0: -1]
    print(arithmetic_value)


def equalpress():
    global arithmetic_value
    total = str(eval(arithmetic_value))
    print(total)
    but_entry.delete(0, len(arithmetic_value))
    but_entry.insert(END, total)
    

Sample_entry_text = StringVar()

Buttonframe = Frame(window, width=312, height=50)
Buttonframe.pack(side=TOP)


but_entry = Entry(Buttonframe,textvariable="StringVar()", justify=RIGHT, width=50)
but_entry.grid(row=0, column=0 ,ipady=10)
        

frame = Frame(window, width = 312, height= 50)
frame.pack()




    ## for row 0
all_clear = Button(frame, text="C", width = 22, height=3, bg="#000fff000", fg="red", command=clear_button)
all_clear.grid(row=0, column=0, columnspan=2, padx=1, pady=1)


Delete_button = Button(frame, text="(x)", width=10, height=3, bg="grey", fg="cyan", command=delete_button)
Delete_button.grid(row=0, column=2, pady=1, padx=1)


Divide = Button(frame, text="/", width=10, height=3, bg="red", fg="green", command=lambda:screen_display("/"))
Divide.grid(row=0, column=3, pady=1,padx=1)
# for row 0

#for row 1
seven = Button(frame, text="7", width=10, height=3,command=lambda:screen_display("7"))
seven.grid(row=1, column=0, pady=1, padx=1)


eight = Button(frame, text="8", width=10, height=3,command=lambda:screen_display("8"))
eight.grid(row=1, column=1, pady=1,padx=1)


nine = Button(frame, text="9", width=10, height=3, command=lambda:screen_display("9"))
nine.grid(row=1, column=2, pady=1,padx=1)


multiply = Button(frame, text="*", width=10, height=3, bg="green", fg="red", command=lambda:screen_display("*"))
multiply.grid(row=1, column=3, pady=1,padx=1)
#for row 1

# for row 2
four = Button(frame, text="4", width=10, height=3, command=lambda:screen_display("4"))
four.grid(row=2, column=0, pady=1,padx=1)


five = Button(frame, text="5", width=10, height=3, command=lambda:screen_display("5"))
five.grid(row=2, column=1, pady=1,padx=1)


six = Button(frame, text="6", width=10, height=3, command=lambda:screen_display("6"))
six.grid(row=2, column=2, pady=1,padx=1)


add = Button(frame, text="+", width=10, height=3, bg="yellow", fg="blue", command=lambda:screen_display("+"))
add.grid(row=2, column=3, pady=1,padx=1)
# for row 2

# for row 3                             
one = Button(frame, text="1", width=10, height=3, command=lambda:screen_display("1"))
one.grid(row=3, column=0, pady=1,padx=1)


two = Button(frame, text="2", width=10, height=3, command=lambda:screen_display("2"))
two.grid(row=3, column=1, pady=1,padx=1)


three = Button(frame, text="3", width=10, height=3, command=lambda:screen_display("3"))
three.grid(row=3, column=2, pady=1,padx=1)


subtract = Button(frame,  text="-", width=10, height=3, bg="cyan", fg="black", command=lambda:screen_display("-"))
subtract.grid(row=3, column=3, pady=1,padx=1)
# for row 3

# for row 4
dot = Button(frame, text=".", width=22, height=3, bg= "blue", fg="magenta", command=lambda:screen_display("."))
dot.grid(row=4, column=0,columnspan=2, pady=1,padx=1)


zero = Button(frame, text="0", width=10, height=3, command=lambda:screen_display("0"))
zero.grid(row=4, column=2, pady=1,padx=1)


equal = Button(frame, text="=", width=10, height=3, bg="black", fg="red", command=equalpress)
equal.grid(row=4, column=3, pady=1, padx=1)
## for row 4
window.mainloop()


##But_entry(END, result)
##Sample_entry_text.set(result)   self.e.result()#

#arithmetic_value = ""#
    #self.e.delete(0, END)#


    

    ##def clear_entry(self):
    #global arithmetic_value#    # AC button pressed on form or 'esc" pressed on keyboard
    ##self.delete(0, END)##
    ##self.insert(0, "0")##