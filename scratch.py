from datetime import date

from tkinter import *

from PIL import ImageTk, Image

from tkinter import Entry

window = Tk()
window.geometry("700x500")
window.title("Zodiac and Age Calculator")
photo = ImageTk.PhotoImage(Image.open("zodiacpic.jpg"))
myimage = Label(window, image=photo)
myimage.grid(row=0, column=1)

"""
Originally I had 2 functions, calculateAge() and calculateZodiac(). I tried running them consecutively, it did not work.
Overall I just simplified and made everything more unified (ex. months are all ints now rather than strings for Zodiac)
Removed the zodiac month/day "input" code. It was making the user input info in command line rather than the app window
Added monthEntry.get() as a value for the variable 'month' and dayEntry.get() for 'day'
"""

"""
Originally I had 2 functions, calculateAge() and calculateZodiac(). I tried running them consecutively, it did not work.
Overall I just simplified and made everything more unified (ex. months are all ints now rather than strings for Zodiac)
Removed the zodiac month/day "input" code. It was making the user input info in command line rather than the app window
Added monthEntry.get() as a value for the variable 'month' and dayEntry.get() for 'day'
"""


def calculate_age():
    today = date.today()
    birth_date = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    month = int(monthEntry.get())
    day = int(dayEntry.get())
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    get_zodiac(month, day, age)


def get_zodiac(month, day, age):
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

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
nameEntry = Entry(window, textvariable=nameValue)
yearEntry = Entry(window, textvariable=yearValue)
monthEntry: Entry = Entry(window, textvariable=monthValue)
dayEntry = Entry(window, textvariable=dayValue)
nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

Button(text="Calculate age and Zodiac Sign", fg="purple", command=calculate_age).grid(row=5, column=1, pady=10)

window.mainloop()
