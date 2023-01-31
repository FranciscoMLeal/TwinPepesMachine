import tkinter as tk
import pyautogui

width_size, height_size = pyautogui.size()

def change_var(var, value = None):
    with open("twin_text.txt", "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if var in lines[i]:
            lines[i] = f"{var} = {value}\n"
            break
    else:
        lines.append(f"{var} = {value}\n")
    with open("twin_text.txt", "w") as f:
        f.write("".join(lines))
        
def button_click(var):
    with open("twin_text.txt", "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if var in lines[i]:
            value = lines[i].split("=")[1].strip()
            if value == "True":
                lines[i] = f"{var} = False\n"
            elif value == "False":
                lines[i] = f"{var} = True\n"
            break
    else:
        lines.append(f"{var} = True\n")
    with open("twin_text.txt", "w") as f:
        f.write("".join(lines))

def update_height():
    height = int(height_var.get())
    change_var("height", height)

def update_width():
    width = int(width_var.get())
    change_var("width", width)

def update_tempo():
    tempo = float(tempo_var.get())
    change_var("tempo", tempo)

def update_dividend():
    dividend = int(dividend_var.get())
    change_var("canvas_dividend", dividend)
    
def update_nbr_of_colors():
    nbr_of_colors = int(nbr_of_colors_var.get())
    change_var("nbr_of_colors", nbr_of_colors)

root = tk.Tk()

button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, columnspan=2)

button_A = tk.Button(button_frame, text="A", command=lambda: button_click("A"))
button_A.grid(row=1, column=0)

button_B = tk.Button(button_frame, text="B", command=lambda: button_click("B"))
button_B.grid(row=1, column=1)

button_C = tk.Button(button_frame, text="C", command=lambda: button_click("C"))
button_C.grid(row=2, column=0)

button_D = tk.Button(button_frame, text="D", command=lambda: button_click("D"))
button_D.grid(row=2, column=1)

height_var = tk.StringVar()
height_entry = tk.Entry(root, textvariable=height_var)
height_entry.insert(0, height_size)
height_entry.grid(row=2, column=0)
height_button = tk.Button(root, text="Update Height", command=update_height)
height_button.grid(row=2, column=1)

width_var = tk.StringVar()
width_entry = tk.Entry(root, textvariable=width_var)
width_entry.insert(0, width_size)
width_entry.grid(row=3, column=0)
width_button = tk.Button(root, text="Update Width", command=update_width)
width_button.grid(row=3, column=1)

tempo_var = tk.StringVar()
tempo_entry = tk.Entry(root, textvariable=tempo_var)
tempo_entry.insert(0,1)
tempo_entry.grid(row=4, column=0)
tempo_button = tk.Button(root, text="Update Tempo", command=update_tempo)
tempo_button.grid(row=4, column=1)

dividend_var = tk.StringVar()
dividend_entry = tk.Entry(root, textvariable=dividend_var)
dividend_entry.insert(0,25)
dividend_entry.grid(row=5, column=0)
dividend_button = tk.Button(root, text="Update Dividend", command=update_dividend)
dividend_button.grid(row=5, column=1)

nbr_of_colors_var = tk.StringVar()
nbr_of_colors_entry = tk.Entry(root, textvariable=nbr_of_colors_var)
nbr_of_colors_entry.insert(0,10)
nbr_of_colors_entry.grid(row=6, column=0)
nbr_of_colors_button = tk.Button(root, text="Update Nbr of Colors", command=update_nbr_of_colors)
nbr_of_colors_button.grid(row=6, column=1)


button_E = tk.Button(button_frame, text="E", command=lambda: button_click("E"))
button_E.grid(row=0, column=0)

root.mainloop()
