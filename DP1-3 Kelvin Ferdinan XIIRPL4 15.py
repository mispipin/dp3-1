#Kelvin Ferdinan - XII RPL 4 - 15
# Import necessary modules
from tkinter import *
from tkinter import ttk

# Define function to convert string to ASCII
def str_to_ascii(string):
    ascii_list = []
    for char in string:
        ascii_list.append(ord(char))
    return ascii_list

# Define function to convert between binary, decimal, octal, and hexadecimal
def base_conversion(number, from_base, to_base):
    if from_base == "Decimal":
        decimal_num = int(number)
    elif from_base == "Binary":
        decimal_num = int(number, 2)
    elif from_base == "Octal":
        decimal_num = int(number, 8)
    elif from_base == "Hexadecimal":
        decimal_num = int(number, 16)
    else:
        raise ValueError("Invalid input base")

    if to_base == "Decimal":
        return str(decimal_num)
    elif to_base == "Binary":
        return bin(decimal_num)[2:]
    elif to_base == "Octal":
        return oct(decimal_num)[2:]
    elif to_base == "Hexadecimal":
        return hex(decimal_num)[2:]
    else:
        raise ValueError("Invalid output base")

# Define function to convert between binary, decimal, octal, and hexadecimal
def convert_base():
    # Get user input
    number = input_entry.get()
    from_base = from_base_choice.get()
    to_base = to_base_choice.get()

    # Convert number
    converted_number = base_conversion(number, from_base, to_base)

    # Display result
    result_label.config(text=converted_number)

# Define function to convert string to ASCII
def convert_ascii():
    # Get user input
    string = input_entry.get()

    # Convert string to ASCII
    ascii_list = str_to_ascii(string)

    # Display result
    result_label.config(text=str(ascii_list))

# Set up the GUI
root = Tk()
root.title("Kelvin Ferdinan")
root.geometry("700x400")
root['bg']='cyan'



#Create a canvas object
canvas= Canvas(root, width= 1000, height= 750, bg="SpringGreen2")

#Add a text in Canvas
canvas.create_text(370, 50, text="Konversi Bilangan", fill="black", font=('Helvetica 24 bold'))
canvas.pack()

# Create input label and entry box
input_label = ttk.Label(root, text="Masukkan angka atau huruf:")
input_label.pack(pady=10)

input_entry = ttk.Entry(root, width=30)
input_entry.place(x=20, y=100)

input_entry.pack()

# Create "Convert" button
convert_button = ttk.Button(root, text="Convert", command=convert_base)
convert_button.pack(pady=10)

# Create "Convert to ASCII" button
ascii_button = ttk.Button(root, text="Convert ke ASCII", command=convert_ascii)
ascii_button.pack(pady=10)

# Create "From base" dropdown menu
from_base_label = ttk.Label(root, text="Convert dari:")
from_base_label.pack(pady=10)

from_base_choice = ttk.Combobox(root, values=["Decimal", "Binary", "Octal", "Hexadecimal"])
from_base_choice.current(0)
from_base_choice.pack()

# Create "To base" dropdown menu
to_base_label = ttk.Label(root, text="Convert ke:")
to_base_label.pack(pady=10)

to_base_choice = ttk.Combobox(root, values=["Decimal", "Binary", "Octal", "Hexadecimal"])
to_base_choice.current(0)
to_base_choice.pack()

# Create result label
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)


input_label.place(relx=0.4, rely=0.56,)
input_entry.place(relx=0.37, rely=0.63,)
convert_button.place(relx=0.37, rely=0.8)
ascii_button.place(relx=0.5, rely=0.8)
from_base_label.place(relx=0.25,rely=0.3)
from_base_choice.place(relx=0.25,rely=0.39)
to_base_label.place(relx=0.55,rely=0.3)
to_base_choice.place(relx=0.55,rely=0.39)
result_label.place(relx=0.5,rely=0.9)
root.mainloop()
