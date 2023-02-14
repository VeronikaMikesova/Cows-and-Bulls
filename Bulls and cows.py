"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Veronika Mikešová
email: veronikamikesova@gmail.com
discord: Veronika M.#2692
"""

# výběr náhodného 4ciferného čísla ze seznamu čísel v jiném souboru
from random import choice
from  cisla import random_cisla as cislo
cislo = str(choice(cislo))


# kontrola zadaného čísla
def kontrola_cisla (hodnota) -> True:
    mnozina_cisel = set(seznam_cisel) # pokud se množina zmenší, tak se v hadanem_cisle číslo opakuje, což nesmí
    if hodnota.isnumeric() and len(hodnota) == 4 and hodnota[0] != "0" and len(seznam_cisel) == len(mnozina_cisel):
        return True
    else:
        print ("Číslo zadáno chybně, ukončuji hru!")
        return False

# prověřit, zda ve náhodně vybraném čísle se nachází některá číslice ze zadaného čísla a kolikrát se pozice shoduje
def existence_cislice(cislice):
   vysledek = {"cows":0, "bulls":0}
   for cislice in seznam_cisel:
        if cislice in nahodny_seznam:
            vysledek["cows"] = vysledek["cows"] + 1
            if seznam_cisel.index(cislice) == nahodny_seznam.index(cislice):
               vysledek["bulls"] = vysledek["bulls"] + 1
   return vysledek

def zpusob_tisku(vysledek): 
    if vysledek["cows"] == 1:
        if vysledek["bulls"] == 1:
            print(vysledek["cows"], "cow", vysledek["bulls"], "bull")
        else: 
            print(vysledek["cows"], "cow", vysledek["bulls"], "bulls")
    
    elif vysledek["bulls"] == 1:
        print(vysledek["cows"], "cows", vysledek["bulls"], "bull")
    
    else:
        print(vysledek["cows"], "cows", vysledek["bulls"], "bulls") 
    
  
def opakovani(vysledek):
    if vysledek["cows"] == 4 and vysledek["bulls"] == 4:
        print (f"Hledané číslo je", zadane_cislo)
        if pocet_pokusu == 1:
            print (f"Číslo bylo nalezeno po {pocet_pokusu} pokusu")
        else:
            print (f"Číslo bylo nalezeno po {pocet_pokusu} pokusech")
        return False
    else:
        return True

# ZAČÁTEK HRY

cara = "-" * 35
pocet_pokusu = 0
vysledek = {"cows":0, "bulls":0}

print(cislo) # počítač vybere náhodné číslo ze souboru (při hraní hry jen nutné skrýt)
nahodny_seznam = list(cislo)   # z náhodně vybraného čísla ze souboru se udělá seznam číslic

zadane_cislo = input("Enter a number:") # hráč zadá svůj 1. tip
print (cara)
seznam_cisel = list(zadane_cislo) # ze zadaného čísla udělá seznam číslic

if kontrola_cisla (zadane_cislo) is True:
    pocet_pokusu += 1
    zpusob_tisku(existence_cislice(zadane_cislo))
    while opakovani(existence_cislice(zadane_cislo)) is True:
          zadane_cislo = input("Enter a number:") # hráč zadá svůj další tip
          print (cara)
          seznam_cisel = list(zadane_cislo)
          if kontrola_cisla (zadane_cislo) is True:
            pocet_pokusu += 1
            zpusob_tisku(existence_cislice(zadane_cislo))
            opakovani(existence_cislice(zadane_cislo))
          else:
            quit
    else:
        quit
quit
