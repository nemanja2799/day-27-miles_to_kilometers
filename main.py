from tkinter import *

def action():
    miles = float(entry.get())
    km = miles * 1.6
    label_answer.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0,column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label_answer = Label(text="0")
label_answer.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1,column=2)

button = Button(text="Calculate", command=action)
button.grid(row=2,column=1)

window.mainloop()
