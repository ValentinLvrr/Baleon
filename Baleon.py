import os
import time

def main():

    try:
        from pyfade import Fade, Colors
    except:
        print("Installation du module pyfade")
        try:
            os.system("pip3 install pyfade")
            time.sleep(1)
            from pyfade import Fade, Colors
        except:
            os.system("pip install pyfade")
            time.sleep(1)
            from pyfade import Fade, Colors

    try:
        from pycenter import center
    except:
        print("Installation du module PyCenter")
        try:
            os.system("pip3 install pycenter")
            time.sleep(1)
            from pycenter import center
        except:
            os.system("pip install pycenter")
            time.sleep(1)
            from pycenter import center

    try:
        import cv2
    except:
        print("Installation du module OpenCV")
        try:
            os.system("pip3 install opencv-python")
            time.sleep(1)
            import cv2
        except:
            os.system("pip install opencv-python")
            time.sleep(1)
            import cv2
    
    try:
        import qrcode
    except:
        print("Installation du module QrCode")
        try:
            os.system("pip3 install qrcode[pil]")
            time.sleep(1)
            import qrcode
        except:
            os.system("pip install qrcode[pil]")
            time.sleep(1)
            import qrcode

    os.system("mode 150, 50")
    os.system("title Baleon - Valentin.Lvr")

    def clear():
        os.system("cls")

    def read():
        os.system("title Baleon - Lecture")
        d = cv2.QRCodeDetector()
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        name = input(Col.orange+"Nom > "+Col.white)
        name_png = name + ".png"
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        print(Col.orange+"Lecture ...")
        try:
            val, points, qrcode = d.detectAndDecode(cv2.imread(name_png))
            print(Col.orange+"Valeure decodée :", Col.yellow+val)
            print(Col.orange+"Entrez", Col.yellow+"copy", Col.orange+"pour copier la valeure.\n")
        except:
            print(Col.orange+f"Aucun QR Code trouvé avec le nom {name}", Col.yellow+val)
        c = input(Col.orange+"Choix > "+Col.white)
        if c == "copy":
            import pyperclip
            pyperclip.copy(val)
            print(Col.yellow+"Valeure Copiée")
            input()
            main()
        else:
            main()
    
    def write():
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
        try:
            img = qrcode.make(data)
            img.save(name_png)
            clear()
            title()
            print("\n\n\n\n\n\n\n") #Saut de ligne
            print(Col.yellow+"QR-Code généré !!!")
            input()
            main()
        except:
            clear()
            title()
            print("\n\n\n\n\n\n\n") #Saut de ligne
            print(Col.yellow+"Le QR Code n'a pas pu être généré :(")
            input()
            main()
    
    def delete():

        os.system("title Baleon - Suppression")
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        name = input(Col.orange+"Nom > "+Col.white)
        name_png = name + ".png"
        clear()
        title()
        print("\n\n\n\n\n\n\n") #Saut de ligne
        try:
            os.remove(name_png)
            print(Col.yellow+"QR-Code Suprimé !!!")
            input()
            main()
        except:
            print(Col.yellow+"Le QR Code n'a pas pu être supprimé !!!")
            input()
            main()

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

    print(Fade.Horizontal(Colors.yellow_to_red, center("\n1 | Lire un QR Code\n2 | Ecrire un QR Code\n3 | Supprimer un QR\n4 | Fermer Baleon")))

    print("\n\n\n") #Saut de ligne


    c = input(Col.orange+"Choix > "+Col.white)

    if c == "1":
        read()
    if c == "2":
        write()
    if c == "3":
        delete()
    if c == "4":
        quit()

    else:
        clear()
        print(Fade.Vertical(Colors.red_to_yellow, center(baleon)))
        print(Fade.Horizontal(Colors.yellow_to_red, center("\nChoix Invalide")))
        input()
        main()

if __name__ == "__main__":
    main()
