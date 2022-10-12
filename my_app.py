import random
import tkinter as tk

window = tk.Tk()
window.title("My First App")
window.geometry("400x250")

# Function----------------
def phrase_gen():
    phrases = ["Welcome ", "This is your first time here, ", "Konnichiwa "]
    name = str(entry1.get())
    return phrases[random.randint(0, 2)] + name

def message_display():
    greetings = phrase_gen()

    # This displays the text field
    greet_display = tk.Text(master=window, height=2, width=15)
    greet_display.grid(column=1, row=2)
    greet_display.insert(tk.END, greetings)


# Labels------------------
label1 = tk.Label(text="Welcome to my first app")
label1.grid(column=0, row=0)

label2 = tk.Label(text="What is your name?")
label2.grid(column=0, row=1)

# Entries------------------
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# Buttons------------------
button1 = tk.Button(text="Submit", command=message_display)
button1.grid(column=2, row=1)

window.mainloop()
