from tkinter import *

window = Tk()
window.title("Test App For Shosan")
window.geometry("400x250")
window.configure(background="black")

# Functions-----------------------------------
def click():
    entered_text = text_entry.get()
    print("Hello " + entered_text)

# photo1 = PhotoImage(file="CelebrityArt/1.gif")
Label(window, bg="black", fg="white", font="verdana 12 italic", text="This is a test app").grid(column=0, row=0, sticky=W)
Label(window, bg="black", fg="red", font="verdana 10 italic", text="What is your name?").grid(column=0, row=1, sticky=W)
text_entry = Entry(width=20, bg="black", fg="white", font="verdana 9 italic")
text_entry.grid(column=1, row=1, sticky=E)
Button(height=1, bg="green", fg="white", font="verdana 12", text="Submit", command=click).grid(column=2, row=1, sticky=E)


window.mainloop()
