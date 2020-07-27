from tkinter import *

from datetime import date

from PIL import ImageTk, Image

root = Tk()
root.geometry("700x500")
root.title("Age Calculator")


month = input("Input month of birth (e.g. march, july etc): ")
day = int(input("Input day of birth: "))

if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'

print("Your Astrological sign is :",astro_sign)


root.geometry("700x500")
root.title("Age Calculator")
photo = ImageTk.PhotoImage(Image.open("mei-featherstone-WlvziDjFkwA-unsplash.jpg"))
myimage = Label(root, image=photo)
myimage.grid(row=0, column=1)
root.mainloop()