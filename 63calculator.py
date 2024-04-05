from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def btnAllClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

# Styling
background_color = '#f2f2f2'  # Light gray background
button_color = '#d9d9d9'  # Lighter gray for buttons
text_color = 'black'  # Black text color
button_font = ('Arial', 14, 'bold')  # Font for buttons

# Calculator display
textDisplay = Entry(cal, font=('Arial', 20, 'bold'), textvariable=text_Input, bd=10, insertwidth=4,
                    bg=background_color, justify='right')
textDisplay.grid(row=0, column=0, columnspan=4, pady=10)

# Button styling
button_width = 8
button_height = 3
button_padx = 1
button_pady = 1
button_borderwidth = 1
button_relief = 'raised'  # 'raised' border style for 3D effect

# Button layout
button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('AC', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Creating and placing buttons
for (text, row, col) in button_layout:
    button = Button(cal, text=text, padx=button_padx, pady=button_pady, bd=button_borderwidth,
                    fg=text_color, bg=button_color, font=button_font, width=button_width, height=button_height,
                    relief=button_relief,
                    command=lambda t=text: btnClick(t) if t.isdigit() or t in ['+', '-', '*', '/'] else (
                        btnAllClearDisplay() if t == 'AC' else btnEqualsInput()))
    button.grid(row=row, column=col, padx=5, pady=5)

cal.configure(bg=background_color)
cal.mainloop()
