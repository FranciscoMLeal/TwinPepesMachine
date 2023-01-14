import time
import RLBB as pepesmachine
import random

tempo = 1
temporale = 0

PepesMachina = pepesmachine
PepesMachina.StartPepeFunction()

def get_width_height():
    with open("twin_text.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if "height" in line:
            height = int(line.split("=")[1])
        if "width" in line:
            width = int(line.split("=")[1])
    return width, height


while True:
    PepesMachina = pepesmachine
    with open("twin_text.txt", "r") as f:
        lines = f.readlines()
    true_vars = []
    for line in lines[:-1]: ### essenctial para usar as pepecolors //// lines[:-1] é pq conta a ultima linha como excepção
        var, value = line.strip().split(" = ")
        if value == "True":
            true_vars.append(var)
        if value == "True" and var == "A" and temporale == 4:
            PepesMachina.set_new_colors(5)
            PepesMachina.StartPepeFunction()
        if value == "True" and var == "B" and (temporale == 2 or temporale == 0):
            print("FIX THIS")
            PepesMachina.ADNprocessor.colorChanger()
        if value == "True" and var == "C" and (temporale == 3 or temporale == 1):
            PepesMachina.ADNprocessor.colorChangeReverse()
            print("MAKE THE MONEY")
        if value == "True" and var == "D":
            width, height = get_width_height()
            i = 0
            while i < random.randrange(1,7):
                x = random.randrange(0,width)
                y = random.randrange(0,height)
                PepesMachina.ClicktoChangePP(x,y)
                i = i + 1
        if var == "tempo":
            tempo = float(value)
    temporale = temporale + 1
    if temporale >= 5:
        temporale = 0
    print(f"Active Buttons = {', '.join(true_vars)}")
    time.sleep(tempo)


