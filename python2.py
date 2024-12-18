
# import pandas as pd
# import matplotlib.pyplot as plt
# data = pd.read_csv("medier.csv", index_col = 0, skiprows=[0,1], sep=";", na_values=[".", ".."], encoding="latin-1")
# print(data)
# ! PYTHON fungerer ikke, sier SERDAR
#!
#?
#*
#TODO

#! Oppgave 1
tall = int(input("Skriv inn et tall: "))
while tall >= 0:
    print(tall)
    tall -= 1
    
#! Oppgave 2
tall = int(input("Skriv inn et tall: "))
for i in range(1, 11):
    print(f"{tall} x {i} = {tall * i}")

#! Oppgave 3
import random
hemmelig_tall = random.randint(1, 100)
gjett = None

while gjett != hemmelig_tall:
    gjett = int(input("Gjett et tall mellom 1 og 100: "))
    if gjett < hemmelig_tall:
        print("For lavt!")
    elif gjett > hemmelig_tall:
        print("For høyt!")
    else:
        print("Riktig!")

#! Oppgave 4
def er_primtall(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for tall in range(1, 101):
    if er_primtall(tall):
        print(tall, "er et primtall")

#! Oppgave 5 
import math

def sirkel_areal(radius):
    return math.pi * radius**2

while True:
    radius = input("Skriv inn radius (eller 'stopp' for å avslutte): ")
    if radius.lower() == "stopp":
        break
    radius = float(radius)
    print("Arealet av sirkelen er:", sirkel_areal(radius))

#! Oppgave 6
ord_teller = 0

while True:
    tekst = input("Skriv inn tekst (eller 'stopp' for å avslutte): ")
    if tekst.lower() == "stopp":
        break
    ord_teller += len(tekst.split())

print("Totalt antall ord skrevet:", ord_teller)
