import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button click
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to delete the last character
def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Function to perform calculation
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input!")

# Function to perform square root
def square_root():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(value)))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input!")

# Main Tkinter window
app = tk.Tk()
app.title("Calculator")
app.geometry("435x500")  # Medium screen size
app.configure(bg="#f0f0f0")     #light gray
app.resizable(False, False)

# Entry field
entry = tk.Entry(app, width=22, borderwidth=3, font=("Arial", 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout (Buttons resized for visibility)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('√', 5, 0), ('^', 5, 1), ('%', 5, 2), ('=', 5, 3)
]

# Add buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, width=8, height=2, bg="lightgreen", font=("Arial", 14),
                           command=calculate)
    elif text == 'C':
        button = tk.Button(app, text=text, width=8, height=2, bg="red", fg="white", font=("Arial", 14),
                           command=clear)
    elif text == '√':
        button = tk.Button(app, text=text, width=8, height=2, bg="#ffcccb", font=("Arial", 14),
                           command=square_root)
    elif text == '^':
        button = tk.Button(app, text=text, width=8, height=2, font=("Arial", 14),
                           command=lambda: button_click('**'))
    elif text == '%':
        button = tk.Button(app, text=text, width=8, height=2, font=("Arial", 14),
                           command=lambda: button_click('/100'))
    else:
        button = tk.Button(app, text=text, width=8, height=2, font=("Arial", 14),
                           command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Add Delete button
delete_button = tk.Button(app, text="DEL", width=8, height=2, bg="#ffcccb", font=("Arial", 14),
                          command=delete_last)
delete_button.grid(row=6, column=0, padx=5, pady=5, columnspan=4)

# Run the app
app.mainloop()
