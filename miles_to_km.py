from tkinter import *

FONT = ("Arial", 14, "normal")

# Conversion function
def miles_to_km():
    try:
        miles = float(entry.get())
        km = miles * 1.60934  # Conversion factor
        result_label.config(text=f"{km:.2f} km")
    except ValueError:
        result_label.config(text="Invalid input")

# Window
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

# Miles entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# "is equal to" label
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

# Result label
result_label = Label(text="0 km", font=FONT)
result_label.grid(column=1, row=1)

# Convert button
button = Button(text="Convert", command=miles_to_km, font=FONT)
button.grid(column=1, row=2)

window.mainloop()
