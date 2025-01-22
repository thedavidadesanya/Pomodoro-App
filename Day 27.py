import tkinter


window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Button
def button_clicked():
    my_label.config(text = input.get())

#Label
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "italic"))
#can use pack,place, grid
#you can't mix up grid and pack in the same program
my_label.grid(column=0, row=0)

#two different ways to change the text of a label
my_label["text"] = "New Text"
my_label.config(text = "New Text")



button = tkinter.Button(text = "Click Me", command = button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button", command=button_clicked )
new_button.grid(column=2, row=0)
#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
print(input.get())













window.mainloop()