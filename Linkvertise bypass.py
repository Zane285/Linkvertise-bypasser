import requests
from tkinter import *
from tkinter import messagebox
import pyperclip as pc
import webbrowser

root = Tk()
root.title("Bypasser")
root.configure(bg="black")

a = Entry(root, width=42, fg="white", bg="black", borderwidth=3)
a.insert(0, "Enter Link")
a.grid(row=0, column=0)

def bypass():
    url = a.get()
    try:
        bruh = requests.get(f"https://bypass.bot.nu/bypass2?url={url}").json()
        destination = bruh["destination"]
        question = messagebox.askquestion("Open in browser?", destination)
        if question == "yes":
            webbrowser.open(destination)
        elif question == "no":
            print("sad")
    except:
        messagebox.showerror("Error", "Cannot Bypass")


button = Button(root, text="Bypass link", fg="white", bg="black",width=36 ,command=bypass).grid(row=1, column=0)

root.mainloop()
