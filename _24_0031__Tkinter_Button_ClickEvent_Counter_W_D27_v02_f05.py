from tkinter import *

count = 1

# 1) we moved the function definition to the top of the code.
def button_clicked():
    global count
    user_input = input.get()
    my_own_label.config(text=f"{user_input}I got clicked {count} time(s).")
    count += 1

window = Tk()
window.title("This is the title for the Window name!!!")
window.minsize(width=500, height=300)

# 2) we also placed ALL of the .pack() methods are at the very bottom/end of each of the widgets.
my_own_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_own_label.config(text="Hello, I am a label.")
my_own_label.pack()

button = Button(text="I'm a Button. Click Me!", command=button_clicked)
button.pack()

input = Entry(width=16)
print(input.get())
input.pack()



window.mainloop()
