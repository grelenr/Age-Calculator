from tkinter import *

from datetime import date

from PIL import ImageTk, Image

root = Tk()
root.geometry("700x500")
root.title("Age Calculator")
photo = ImageTk.PhotoImage(Image.open("oldcalculator.jpg"))
myimage = Label(root, image=photo)
myimage.grid(row=0, column=1)

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()),
    int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today. day) < (birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)

Label(text="Name").grid(row=1, column=0, padx=90)
Label(text="Year").grid(row=2, column=0)
Label(text="Month").grid(row=3, column=0)
Label(text="Day").grid(row=4, column=0)
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()
nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)
nameEntry.grid(row=1, column =1,pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)
Button(text="Calculate age", fg="red", command=calculateAge).grid(row=5, column=1, pady=10)

#Okay, so here I have added the button for calculating the zodiac sign, but it is not functional yet

Button(text="Zodiac Sign", fg="purple",).grid(row=6, column=1, pady=10)



root.mainloop()

