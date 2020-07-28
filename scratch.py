from tkinter import *

from datetime import date
from tkinter import Entry

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

def ZodiacSign():

#I changed the month format from strings for months ie "March" to ints to be consistent between age calculator and Zodiac

	month = int(input("Input your month of birth (e.g. 01, 02 etc): "))
	day = int(input("Input your day of birth: "))
	if month == 12:
		astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
	elif month == 1:
		astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
	elif month == 2:
		astro_sign = 'Aquarius' if (day < 19) else 'pisces'
	elif month == 3:
		astro_sign = 'Pisces' if (day < 21) else 'aries'
	elif month == 4:
		astro_sign = 'Aries' if (day < 20) else 'taurus'
	elif month == 5:
		astro_sign = 'Taurus' if (day < 21) else 'gemini'
	elif month == 6:
		astro_sign = 'Gemini' if (day < 21) else 'cancer'
	elif month == 7:
		astro_sign = 'Cancer' if (day < 23) else 'leo'
	elif month == 8:
		astro_sign = 'Leo' if (day < 23) else 'virgo'
	elif month == 9:
		astro_sign = 'Virgo' if (day < 23) else 'libra'
	elif month == 10:
		astro_sign = 'Libra' if (day < 23) else 'scorpio'
	elif month == 11:
		astro_sign = 'scorpio' if (day < 22) else 'sagittarius'

	print("Your Astrological sign is :", astro_sign)

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
monthEntry: Entry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)
nameEntry.grid(row=1, column =1,pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)
#Button(text="Calculate age", fg="red", command=calculateAge).grid(row=5, column=1, pady=10)

#Okay, so here I have added the button for calculating the zodiac sign, but it is not functional yet

Button(text="Zodiac Sign", fg="purple", command=ZodiacSign).grid(row=6, column=1, pady=10)



root.mainloop()

