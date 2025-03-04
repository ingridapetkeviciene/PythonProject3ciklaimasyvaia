import random

print("H")
numbers = [4, 2, 4, 10]
print(numbers)

empty_list = []
print(empty_list)

empty_list.append(20) # prideda reiksme
print(empty_list)

empty_list.extend([1, 5, 6])# butina naudoti lauztinius skliaustus, yterpia daugiau negu viena reiksme
print(empty_list)

print(empty_list.count(20)) # pereina per visas funkcijas ir suskaiciuoja kiek yra

# empty_list.remove(4) # panaikina ieskoma pirmaja reiksme
# print(empty_list)

popped_element = empty_list.pop() # panaikina paskutine reiksme sarase
print(empty_list)

print(popped_element)

student = [' linas', 'petras', 'agne']

print(student)

student.sort() #rusiuooja
print(student)

student.sort(reverse=True) # rusiuoja atvirksciai
print(student)
# TEVE MUSU
my_numer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # indeksai prasideda nuo 0 ir eina didejancia tvarka

print(my_numer[6]) # turetu atspausdinti 7

print(my_numer [0:4]) # leidzia paimti intervala
print(my_numer[0:4]) # nuo pradzios iki nurodytos pozicijos
print(my_numer[-2]) # 2 nuo galo
print(my_numer[-5:]) # nuo 5 pozicijos iki galo
print(my_numer[:-5]) # nuo pradzios iki 5 pozicijos nuo galo
print(my_numer[2:-5]) #nuo 2 pozicijos iki 5 nuo galo
print(my_numer[-6:-2]) # imame nuo 6 nuo gali iki 2 nuo galo
print(my_numer[:])# paima viska nuo pradzios iki galo, lygiai taip pat kaip nk neyrasius

print(my_numer[::2])# paima kas 2 elementa
print(my_numer[1::2]) # viskas nuo pirmo indekso kas antras elementas ( elementai prasideda nuo 0 )
print(my_numer[3:7:2]) # nuo 3 iki 7 kas antras
print(my_numer[2:-2:2]) # paimu viska be pirmu 2 ir paskutiniu dvieju kas antra
print(my_numer[::-1]) # visi elementai nuo galo
print(my_numer[::-2]) # visa imtis kas 2 bet nuo galo


for student_vardas in student :
    print("studento vardas yra")
    print(student_vardas)

    # ciklas , nurodoma pro kokius elementus nori praeiti , kiekviena varda priskiria naujam kintamajam , kas pastumta per viena
    # tab y desine yra ciklo kunas

print("po ciklo")

# print(range(0,10)):
# ciklo prasisukimas n kartu kazkiek

for number in range(0,4): # grazina reiksmes range
    print(number)

# i tai kas tyliai vyksta procesas

# loop
#while- naudojam tada kada nezinom kuris bus reikiamas ats, kol patenkina salyga  ; for- zino kiek kartu suksis

# print(10/2)
# print(10 %2)
# print(12%5)
# print(10%2 ==0)

for y in range(1,11):
    print(y)


# Ciklai
########################################## Uzduotys####################################################################

# 1.Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

for i in range(10):
 print("Labas")
# for i in range(0,10): nereikia 0 norint aspausdint 10x

# 2.Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.


for i in range(10) :
    print(i)

# 3.Sukurkite masyvą iš dešimties augalų pavadinimų.

plants = ["roze", "kaktusas", "liepa", "nendre", "kastonas", "zole", "lugne", "trauklapis", "berzas", "zalcialunkis"]
print(plants)

# 4.Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

for plant in plants :
    print(plant)

 # 5.Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo
 # paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).

print(plants[::-1])  # visi elementai nuo galo

# 6.Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

number =[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print(number[::2])     # paima kas 2 elementa

for i in range (10, 51, 2):
 print(i)

# 7.Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei
# skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite
# continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie
# dalinasi iš 10 be liekanos)

# pvz
# print("break")
# for i in range(1,20):
#     if i % 5 == 0:#ar dalinasi is 3 be liekanos
#         break
#     print(i)


for i in range (10, 51, 2): # su liekana
    if i % 10 == 0 :
        continue
    print(i)

# 8.Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek
# kartų kintamasis i turėjo porinę reikšmę;


count = 0
for i in range (0, 21):
    if i % 2 == 0 :
      count += 1
print("Kiekis", count)


# 9.Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių
# nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)

plants = ["roze", "kaktusas", "liepa", "nendre", "kastonas", "zole", "lugne", "trauklapis", "berzas", "zalcialunkis"]



#print(plants.count('roze')) # pereina per visas funkcijas ir suskaiciuoja zodzius , bet ne simbolius , reikia simboliu

trumpesni = sum(1 for word in plants if len(word) < 5)
print(trumpesni)
ilgesni = sum(1 for word in plants if len(word) > 7)
print(ilgesni)



#10.Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai.
# (tarp 5 ir 10 simbolių ilgio)

plants = ["roze", "kaktusas", "liepa", "nendre", "kastonas", "zole", "lugne", "trauklapis", "berzas", "zalcialunkis"]

count = sum(1 for word in plants if len(word) in range(5, 10))
print("Zodziu skaicius:", count)

################################## Sunkesni ############################################################################


#1#Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek
# tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

import random

atsisitkiniai_skaiciai = [random.randint(0, 300) for _ in range(300)] # sugeneruoti atsitiktiniai skaiciai ir prasukti

print(" ".join(map(str, atsisitkiniai_skaiciai))) # tarpai

formatavimas = [ f"[{num}]" if num > 275 else str(num) for num in atsisitkiniai_skaiciai]
print(" ".join(formatavimas))

didesni_150 = sum(1 for num in atsisitkiniai_skaiciai if num > 150)
print("Didesni nei 150:", didesni_150)





#2#Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite
# kableliais. Po paskutinio skaičiaus kablelio neturi būti.

print(", ".join(str(i) for i in range(1, 3001) if i % 77 == 0))



#3#Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”

krastiniu_suma = 25 # susikuriame kintamajy, kurio reiksmei pasikeitus (t.y. 25 ) kodas vistiek veiktu

for i in range(0, krastiniu_suma): # nusirodome intervala, isorinis ciklas kuris suksis x kartu
    row = "" # sukuriama tuscia eilute kurioje bus saugoma *
    for i in range (0, krastiniu_suma): # sis ciklas sukuria viena eilute is 25 zvaigzduciu
        row += "*" # prideda viena zvaigzdute
    print(row) # spausdinam rezultata



#5#Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;


monetos_kritimo_rezultatas = random.randint(0,1)


while True:  # Teisingas while ciklas
    monetos_kritimo_rezultatas = random.randint(0, 1)  #  generuojame naują reikšmę

    if monetos_kritimo_rezultatas == 1: # monetos kritimo rezultatas prilyginamas 1, nes 1= skaicius
        print(f"S {monetos_kritimo_rezultatas}")# spausdinam, f funkcija palaiko {}
    else: # kitu atveju
        print("H")
        break  # Stabdom kai iskrenta herbas

# Tris kartus iškritus herbui;

h = 0 # skaitiklis kuris skaiciuos kiek x iskrito herbas

while h < 3 : # programa metys  kol 3 x iskris herbas
    monetos_kritimo_rezultatas = random.randint(0, 1) # atsitiktines reiksmes
    if monetos_kritimo_rezultatas == 0: # kritimo rezultaras prilyginamas 0
        print("H")
        h += 1 # prie pries tai buvusios reiksmes pridedam 1?
    else :
        print ("S") # stabdyti nereikia nes aiskus salygos apibrezimas?

# Tris kartus iš eilės iškritus herbui;

h = 0 # kintamasis kuris seks kiek kartu iskris Herbas

while h < 3 : # programa metys  kol 3 x iskris herbas
    monetos_kritimo_rezultatas = random.randint(0, 1) # atsitiktines reiksmes
    if monetos_kritimo_rezultatas == 0: # kritimo rezultaras prilyginamas 0
        print("H")
        h += 1 # prie pries tai buvusios reiksmes pridedam 1?
    else :
        print ("S") # stabdyti nereikia nes aiskus salygos apibrezimas?
        h = 0 # anuliuojamas herbas


#6# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: laimėtojo vardas”.
# Taškų kiekį generuokite funkcija random.randint(x,x). Žaidimą laimi tas, kas greičiau surenka 222 taškus.
# Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.


petras = 0
kazys = 0 # sukuriam tasku skaiciavimui

petro_taskai= random.randint(10,20) # atsistiktines reiksmes
kazio_taskai = random.randint(5,25)


print(petro_taskai)# pasitikrinam ar veikia
print(kazio_taskai)

while petras < 222 and kazys < 222 : # filosofuojam , konstruojam metimus is atsitiktiniu reiksmiu
    petro_taskai = random.randint(10, 20)
    kazio_taskai = random.randint(5, 25)

    petras += petro_taskai # pridedam prie pries tai buvusios reiksmes?
    kazys += kazio_taskai
    print(
        f"Kazys: {kazys} (viso: {kazio_taskai}), Petras: {petro_taskai} (viso: {petras})")

    if kazys >= 222 or petras >= 222 : # nustatom laimetoja
        laimetojas = "Kazys" if kazys >= 222 else "Petras"
        print(f"Partiją laimėjo: {laimetojas}")
        break


# #8# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis
# # 8.5cm (pilnai sulenda į lentą).
# # “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm.
# # Suskaičiuokite kiek reikia smūgių.
# # “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė
# # (pasinaudokite random.randint(x,x)


    vinies_ilgis = 85
    visos_vinys = 5
    gylis = 0
    smugiai = 0  # susikuriame skaiciavimui


import random



for i in range(1, visos_vinys + 1):


    while gylis < vinies_ilgis: # kol vinis neykalta, kalam
        smugiai += 1
        if random.randint(0, 1) == 1:  # 50% tikimybė mažam arba dideliam smūgiui
            ikalimas = random.randint(20, 30)
        else:
            ikalimas = random.randint(5, 20)

        gylis += ikalimas

    print(f"Vinies {i} įkalimui prireikė {smugiai} smūgių.")


#######################################################################################################################
# PRISIMINIMUI###

#for fiksuota kieky operaciju , break sustabdo cikla ties reikiama vieta, continue nepabaigia setaracijos , soka i
#sekancia

#while, naudojama kai nezinome kada baigsis operacija. While true (suksis begalybe x)
#listai- masyvai (sarasai) vienas kintamasis su daug reiksmiu
# masyvuose gali buti skaiciai, tekstai, objektai
#objektai kai kuri savo , grieztos strukturos
#dvimatis masyvas = masyvas masyve

# P.S. figuriniai sklaustai {} naudojami su f
########################################################################################################################







