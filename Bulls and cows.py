print("""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Mikešová
email: veronikamikesova@gmail.com
discord: Veronika M.#2692
""")

# výběr náhodného 4ciferného čísla ze seznamu čísel v jiném souboru
from random import choice
from  cisla import random_cisla as cislo
cislo = str(choice(cislo))

cara = "-" * 35 

print(cislo) # při hraní hry jen nutné skrýt

print("Zadej číslo. Číslo musí být 4ciferné, nesmí začínat nulou a číslice se nesmí opakovat")
zadane_cislo = input("Enter a number:") # hráč zadá svůj tip

seznam_cisel = list(zadane_cislo)

 
print (cara)


# kontrola zadaného čísla
def kontrola_cisla (hodnota) -> True:
    mnozina_cisel = set(seznam_cisel) # pokud se množina zmenší, tak se v hadanem_cisle číslo opakuje, což nesmí
    if hodnota.isnumeric() and len(hodnota) == 4 and hodnota[0] != "0" and len(seznam_cisel) == len(mnozina_cisel):
       return True
    else:
        print ("Číslo zadáno chybně, ukončuji hru!")
        return False


# prověřit, zda ve náhodně vybraném čísle se nachází některá číslice ze zadaného čísla a na kterém místě
def existence_cislice(cislice):
   nahodny_seznam = list(cislo)    # z náhodně vybraného čísla ze seznamu čísel se udělá seznam číslic
   vysledek = {"cows":0, "bulls":0}
   
   for cislice in seznam_cisel:
        if cislice in nahodny_seznam:
            vysledek["cows"] += 1
            if seznam_cisel.index(cislice) == nahodny_seznam.index(cislice):
                vysledek["bulls"] += 1
   return vysledek

def zpusob_tisku(vysledek): # nepřišla jsem na to, zda lze využít obecné pravidlo pomocí nějakých proměnných, abych nemusela vypisovat všechny situace, které mohou vzniknout
    if vysledek["cows"] == 1:
        if vysledek["bulls"] == 1:
            print(vysledek["cows"], "cow", vysledek["bulls"], "bull")
        else: 
            print(vysledek["cows"], "cow", vysledek["bulls"], "bulls")
           
    elif vysledek["bulls"] == 1:
        print(vysledek["cows"], "cow", vysledek["bulls"], "bull")

    else:
        print(vysledek["cows"], "cows", vysledek["bulls"], "bulls")

    
        
 
# zavolání funkcí
if kontrola_cisla (zadane_cislo) is True:
    existence_cislice(zadane_cislo)
    zpusob_tisku(existence_cislice(zadane_cislo))





