print("Vítejte v obchodu s potravinamy")
print("Pro ukončení obchodu zmáčkni číslo 4")

potraviny = []
platba = 0
obchod = True

while obchod:
    print("1. Ovoce")
    print("2. Zelenina")
    print("3. Pečivo")
    print("4. Ukončení obchodu")
    
    a = input("Vyber jaký druh potraviny chceš: ")

    if a == "4":
        obchod = False
    else:
        zvoleni = int(a)

        if zvoleni == 1:
            print("Nyní si v sekci Ovoce")
            print("1. Jablko")
            print("2. Pomeranč")
            print("3. Hroznové víno")
            print("4. Ukončení výběru ovoce")
            while True:
                ovoce_volba = input("Vyber si druh Ovoce: ")
                if ovoce_volba == "4":
                    break
                elif ovoce_volba in ["1", "2", "3"]:
                    if ovoce_volba == "1":
                        potraviny.append("Jablko")
                        platba += 30
                    elif ovoce_volba == "2":
                        potraviny.append("Pomeranč")
                        platba += 40
                    elif ovoce_volba == "3":
                        potraviny.append("Hroznové víno")
                        platba += 25
                else:
                    print("Neplatná volba")

        elif zvoleni == 2:
            print("Nyní si v sekci Zelenina")
            print("1. Okurka")
            print("2. Paprika")
            print("3. Rajče")
            print("4. Ukončení výběru zeleniny")
            while True:
                zelenina_volba = input("Vyber si druh Zeleniny: ")
                if zelenina_volba == "4":
                    break
                elif zelenina_volba in ["1", "2", "3"]:
                    if zelenina_volba == "1":
                        potraviny.append("Okurka")
                        platba += 50
                    elif zelenina_volba == "2":
                        potraviny.append("Paprika")
                        platba += 35
                    elif zelenina_volba == "3":
                        potraviny.append("Rajče")
                        platba += 20
                else:
                    print("Neplatná volba")

        elif zvoleni == 3:
            print("Nyní si v sekci Pečivo")
            print("1. Houska")
            print("2. Croissant")
            print("3. Bageta")
            print("4. Ukončení výběru pečiva")
            while True:
                pecivo_volba = input("Vyber si druh Pečiva: ")
                if pecivo_volba == "4":
                    break
                elif pecivo_volba in ["1", "2", "3"]:
                    if pecivo_volba == "1":
                        potraviny.append("Houska")
                        platba += 5
                    elif pecivo_volba == "2":
                        potraviny.append("Croissant")
                        platba += 7
                    elif pecivo_volba == "3":
                        potraviny.append("Bageta")
                        platba += 10
                else:
                    print("Neplatná volba")

print("Potraviny jsou v košíku:")
print(potraviny)
print("Celková cena k zaplacení:")
print(platba)

                            



        