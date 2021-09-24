from pyfade import Fade, Colors
from pycenter import center
from requests import get
import os
import cv2
import qrcode
import time

os.system("mode 160, 50")
os.system("title Baleon - Valentin.Lvr")

def clear():
    os.system("cls")

class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "orange" : "\033[38;2;255;100;0m", 
              "yellow" : "\033[38;2;255;255;0m",
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    orange = colors['orange']

    yellow = colors['yellow']
    
    white = colors['white']

clear()





baleon = """
 /$$$$$$$   /$$$$$$  /$$       /$$$$$$$$  /$$$$$$  /$$   /$$
| $$__  $$ /$$__  $$| $$      | $$_____/ /$$__  $$| $$$ | $$
| $$  \ $$| $$  \ $$| $$      | $$      | $$  \ $$| $$$$| $$
| $$$$$$$ | $$$$$$$$| $$      | $$$$$   | $$  | $$| $$ $$ $$
| $$__  $$| $$__  $$| $$      | $$__/   | $$  | $$| $$  $$$$
| $$  \ $$| $$  | $$| $$      | $$      | $$  | $$| $$\  $$$
| $$$$$$$/| $$  | $$| $$$$$$$$| $$$$$$$$|  $$$$$$/| $$ \  $$
|_______/ |__/  |__/|________/|________/ \______/ |__/  \__/
"""


def title():
    print(Fade.Vertical(Colors.red_to_yellow, center(baleon)))
    print(Fade.Horizontal(Colors.yellow_to_red, center("\nValentin.Lvr")))

title()

print(Col.orange+center("   Baleon - Lecture ou Ecriture."))

print("\n\n\n") #Saut de ligne

c = input(Col.yellow+"Choix > "+Col.white)

if c == "Lecture":
    
    d = cv2.QRCodeDetector()
    clear()
    title()
    print("\n\n\n") #Saut de ligne
    name = data = input(Col.yellow+"Nom > "+Col.white)
    name_png = name + ".png"
    clear()
    title()
    print("\n\n\n") #Saut de ligne
    print(Col.yellow+"Lecture ...")
    val, points, qrcode = d.detectAndDecode(cv2.imread(name_png))
    print(Col.yellow+f"Valeure decodée : {val}")
    input()

if c == "Ecriture":
    clear()
    title()
    print("\n\n\n") #Saut de ligne
    data = input(Col.yellow+"Valeure > "+Col.white)
    clear()
    title()
    print("\n\n\n") #Saut de ligne
    name = input(Col.yellow+"Nom > "+Col.white)
    name_png = name + ".png"
    clear()
    title()
    print("\n\n\n") #Saut de ligne
    print(Col.yellow+"Génération ...")
    img = qrcode.make(data)
    img.save(name_png)
    clear()
    title()
    print("\n\n\n") #Saut de ligne
    print(Col.yellow+"QR-Code généré !!!")
    input()

else:
    clear()
    title()
    print(Col.orange+center("   Baleon - Choix invalide."))
    print("\n\n\n") #Saut de ligne
    print(Col.orange+"Appuyer sur ENTER pour fermer")
    input()