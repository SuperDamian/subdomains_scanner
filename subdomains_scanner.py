import requests
import sys
import colorama

if sys.argv[1] == "-h":
    print("[python3 program.py domena slownik]")
else:
    domena = sys.argv[1]
    slownik1 = sys.argv[2]
    slownik = open(slownik1, "r")
    istnieje = []
    n = 0

    for haslo in slownik.readlines():
        n += 1
        r = requests.get(domena + "/" + haslo)
        kolor_kodu =  "nie wiem co tu napisac"

        if r.status_code == 200:
            kolor = colorama.Fore.GREEN
            istnieje.append(domena + "/" + haslo)
        elif r.status_code == 403:
            kolor = colorama.Fore.BLUE
        elif r.status_code == 404:
            kolor = colorama.Fore.RED


        print(colorama.Fore.CYAN, str(n) + '.',colorama.Fore.WHITE, domena + "/"+ haslo, " " * len(haslo) ,kolor, r.status_code)
    
        print(colorama.Fore.WHITE, "")
    print("poprawne podstrony: ")
    for adres in istnieje:
        print(adres)
    print(colorama.Fore.WHITE, "koniec") 
