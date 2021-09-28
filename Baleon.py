from pyfade import Fade, Colors
from pycenter import center
import os
import cv2
import qrcode


os.system("mode 150, 50")
os.system("title Baleon - Valentin.Lvr")

def main():

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

    print(Fade.Horizontal(Colors.yellow_to_red, center("\n1 | Lecture\n2 | Ecriture\n3 | Fermer")))

    print("\n\n\n") #Saut de ligne


    c = input(Col.orange+"Choix > "+Col.white)

    if c == "1":
        
        os.system("title Baleon - Lecture")
        d = cv2.QRCodeDetector()
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        name = data = input(Col.orange+"Nom > "+Col.white)
        name_png = name + ".png"
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        print(Col.orange+"Lecture ...")
        val, points, qrcode = d.detectAndDecode(cv2.imread(name_png))
        print(Col.orange+"Valeure decodée :", Col.yellow+val)
        input()
        main()

    if c == "2":
        
        os.system("title Baleon - Ecriture")
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        data = input(Col.orange+"Lien > "+Col.white)
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        name = input(Col.orange+"Nom > "+Col.white)
        name_png = name + ".png"
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        print(Col.orange+"Génération ...")
        img = qrcode.make(data)
        img.save(name_png)
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        print(Col.yellow+"QR-Code généré !!!")
        input()
        main()

    if c == "3":
        
        quit()

    else:
        clear()
        print(Fade.Vertical(Colors.red_to_yellow, center(baleon)))
        print(Fade.Horizontal(Colors.yellow_to_red, center("\nChoix Invalide")))
        input()
        main()


if __name__ == "__main__":
    main()
