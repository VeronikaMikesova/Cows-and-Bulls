"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Veronika Mikešová
email: veronikamikesova@gmail.com
discord: Veronika M.#2692
"""

import random

# hlavní funkce - opakuj zadávání čísel, dokud číslo neuhodneš
def uhodni_spravne_cislo(cislo_1, cislo_2) -> bool: 
    hra_bezi = True
    pocet_pokusu = 1
    while hra_bezi:
        while kontrola_cisla(cislo_2) is False:
                cislo_2 = input("Chybně zadané číslo. Zkus zadat znovu:")
                pocet_pokusu = pocet_pokusu + 1
                continue
        # pokud je vygenerované a zadané číslo správné, zjišťuji počet shodných číslic a jejich pozice v samostatné funkci
        vysledek = existence_cislice(cislo_1, cislo_2)
        zpusob_tisku(vysledek)  
    
        if opakovani(vysledek) is False:
            cislo_2 = input("Ještě to není úplně ono. Zkus znovu:")
            pocet_pokusu = pocet_pokusu + 1
            continue
        else:
            hra_bezi = False
            print("Hra ukončena")
            print (f"Hledané číslo je", cislo_1)
            if pocet_pokusu == 1:
                print (f"Číslo bylo nalezeno po {pocet_pokusu} pokusu")
                quit
            else:
                print (f"Číslo bylo nalezeno po {pocet_pokusu} pokusech")
                quit
        
def kontrola_cisla(cislo:str) -> bool:
    seznam = list(cislo)
    mnozina_cisel = set(seznam)
    if cislo.isnumeric() and len(cislo) == 4 and cislo[0] != "0" and len(mnozina_cisel) == len(seznam): # v případě PC čísla první 3 podmínky splněny vždy, ale ne u čísla od hráče
        return True
    else:
        return False
       

def existence_cislice(cislo_1:str, cislo_2:str) -> dict:
    pc_seznam = list(cislo_1)
    muj_seznam = list(cislo_2)
    vysledek = {"cows":0, "bulls":0}
    for cislice in muj_seznam:
        if cislice in pc_seznam:
            vysledek["cows"] = vysledek["cows"] + 1
            if muj_seznam.index(cislice) == pc_seznam.index(cislice):
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

def opakovani(vysledek) -> bool:
    if vysledek["cows"] == 4 and vysledek["bulls"] == 4:
        return True
    else:
        return False


def pc_cislo(cislo:str) -> str: # PC vygeneruje číslo splňující podmínky
    while kontrola_cisla(cislo) is False:
      cislo = str(random.randint(1000, 9999))  
      continue
    else:
        cislo_1 = cislo
    return str(cislo_1)

# HRA ZAČÍNÁ
cislo = str(random.randint(1000, 9999))
cislo_1 = pc_cislo(cislo)
print(cislo_1) # pro účely testování si vytisknu

cislo_2 = input("Vlož číslo:")
uhodni_spravne_cislo(cislo_1, cislo_2)