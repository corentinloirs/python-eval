from colorama import Fore, Style
from ruler import Ruler, red_text
import sys
import numpy as np

import argparse

parser = argparse.ArgumentParser() #on récupère le fichier, cf primer

parser.add_argument("dataset", help="Couples de fragments", type=str)

args = parser.parse_args()

texte = args.dataset

with open(texte, 'r') as fichier:
    liste = []
    swap = []
    for ligne in fichier:
        if len(ligne) != 0:
            if len(swap) == 0:
                swap.append(ligne)
            else:
                liste.append((swap[0], ligne))
                swap = []

for k in range(len(liste)):
    ruler = Ruler(*liste[k])
    ruler.compute()
    d = ruler.distance
    top, bottom = ruler.report()
    print(f"====== example # {k} - distance = {d}")
    print(top)
    print(bottom)