
from datetime import date

from tkinter import *

from PIL import ImageTk, Image

from tkinter import Entry


root = Tk()
root.geometry("700x500")
root.title("Age Calculator")
photo = ImageTk.PhotoImage(Image.open("zodiacpic.jpg"))
myimage = Label(root, image=photo)
myimage.grid(row=0, column=1)

# Originally I had 2 functions, calculateAge() and calculateZodiac(). I tried running them consecutively, it did not work.
# Overall I just simplified and made everything more unified (ex. months are all ints now rather than strings for Zodiac)
# Removed the zodiac month/day "input" code. It was making the user input info in command line rather than the app window
# Added monthEntry.get() as a value for the variable 'month' and dayEntry.get() for 'day'

"""
Originally I had 2 functions, calculateAge() and calculateZodiac(). I tried running them consecutively, it did not work.
Overall I just simplified and made everything more unified (ex. months are all ints now rather than strings for Zodiac)
Removed the zodiac month/day "input" code. It was making the user input info in command line rather than the app window
Added monthEntry.get() as a value for the variable 'month' and dayEntry.get() for 'day'
"""

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    month = int(monthEntry.get())
    day = int(dayEntry.get())
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
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


    # updated the button to include the Zodiac sign
    # updated the button to include the Zodiac sign

    Label(text=f"{nameValue.get()} your age is {age} and your Zodiac sign is {astro_sign}").grid(row=6, column=1)

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

Button(text="Calculate age and Zodiac Sign", fg="purple", command=calculateAge).grid(row=5, column=1, pady=10)

root.mainloop()