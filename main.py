import sys

#print(sys.version)

#Zaznacz i CTRL + SLASH  - KOMENTARZ BLOKOWY


"""
a = 56
print(a)
print(type(a))  #Wypisuje typ zmiennej
b = 5.5
print(type(b))
zmienna_tekstowa = 'wizualizacja danych'
print(zmienna_tekstowa)
print(type(zmienna_tekstowa))
"""


""" ##DZIALANIA
a = 6
b = 3

c = a + b
print(c)
d = a - b
print(d)

e = 4
f = a // b #dzielenie calkowite
print(f)
f = a // b
print(f)

g = a ** 2 #potegowanie, lepiej uzywac dla liczb ktore nie sa ulamkami
print(g)

h = pow(a, 2) #potegowanie a podstawa, 2 wykladnik, pow funkcja do potegowania
print(h)

i = 6 ** 1/2  #Błędnie, poneiwaz operator dziala do 1 znaku ktory jest za ** cyzli w tym przypadku 1, wynik bedzie sie roznil, chyba ze 1/2 damy w nawias
print(i)
i = 6 ** (1/2)
print(i)

j = pow(6, (1/2))
print(j)
"""



""" LACZENIE SLOW
k = 'wizualizacja danych'
l = ' grupa '
m = 2
print(k + l + str(m))
"""



"""
a = 6
b = 5
print('liczba a jest rowna {:d}'.format(a))     #w klamrze jesli wpiszemy :d to liczba bedzie wyswietlona w formacie dziesietnym
print('liczba a jest rowna {}'.format(a, b))       #w klamrze jesli nie wpiszemy nic to liczba wyswietli sie w aktualnym formacie

z = 6.342342
print('liczba z jest rowna {:.2f}'.format(z))   # :f typ float, :.2f - dwa miejsca po przecinku (maksymalnie 6 przy float)
"""


"""
a = input('Wprowadz liczbe: ') #Zawsze wprowadzmy stringa, potem trzeba zmienic na zmienna liczbowa jesli jest tak potrzeba
print(a + ' to wartosc liczby a')
print(type(a))
a = int(a)                     #Zmiana typu
print(a*5)

sys.stdout.write('Wprowadz liczbe: ')   #potrzebny import sys
b = sys.stdin.readline()
print(b + ' to wartosc liczby b')
print(type(b))
#SPOJRZ NA ROZNICE WYSWIETLANIA W LINII przy input oraz readline
"""

""" LISTA
lista = [5, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']     # [a, b, c] jeden element
print(lista)

lista.append(67)  #dodanie nowego elementu, bedzie umieszczony na samym koncu tej listy
print(lista)

lista.insert(2, 'DHSFGJSDGFJSGF')    # (index, 'cos co chcemy wstawic')  wybieramy w ktore miesjce chcemy wstawic nowy element
print(lista)

lista.extend([20, 21, 22, 23])    #dodanie elementow na sam koniec listy
print(lista)

lista.pop(2)    #usuwa element z indexem = 2
print(lista)

lista.remove([2, 3, 4]) #usuwa wybrane, wypisane
print(lista)

del lista[1]    #mozna sie odniesc do elementu listy
print(lista)

lista.reverse() #odwrocenie listy
print(lista)

#lista.sort()   #Przy sortowaniu wartosci wszystkie elementy musza byc podobne czyli nie moze byc 1, ab bo ab to litery, nie da sie tego porownac
#print(lista)
"""

""" SLOWNIK KLUCZ - WARTOSC 
slownik = {'klucz': 'wartosc', 1: 2, 'a': 3, 4: 'b'}    #elementy sa w parach klucz - wartosc, klucz musi byc unikalny
print(slownik)
print(slownik[4])     #aby wypisac wybrany element w [nazw klucza]
print(slownik['klucz'])     #aby wypisac wybrany element w [nazw klucza]

slownik[6] = 45     #dodanie elementu po kluczu [6] - klucz, 45 - wartosc
print(slownik)

slownik.pop(1)  #usunie pierwsza pare
print(slownik)

print(slownik.keys())       #wyswietli klucze
print(slownik.values())     #wysweitli wartosci

del slownik[6] #usuniecie pary poprzez podanie klucza, ktory chce usunac
print(slownik)
"""


#Instrukcje warunkowe, pamietac o tabulacjach (nie ma klamer)
"""
a = 8
b = 8

if a > b:
    print("a is greater than b")
elif a < b:                                       #to samo co else if
    print("a is less than b")
else:
    print("a is equal to b")
"""

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a > b) & (c > d):       # & - AND
    print(a, c)
else:
    print(b, d)

if (a > b) | (c > d):       # | - OR
    print(a, c)
else:
    print(b, d)
"""



"""
for i in range(8):   #range(8) - warunek zakonczenia sekwencji czyli wartosc 8, i = 0
    print(i)
else:
    print('koniec petli')

for i in range(2, 8, 1):  # range(2, 8, 1) od 2 do 8, skok o 1,
    print(i)
else:
    print('koniec petli')
"""


"""
NIE DZIALA!!!!!!!!!!!!!
lista = [5, 6, 7, 8, 9, 10, 11]
print(lista)

for i int lista:
print(i)

for i in range(0, 5):
    for j in range(0, 5):
        result = i+j
        print(result)
      print('koniec petli')
"""



"""      
for i in range(0, 5):
    for j in range(0, 5):
        result = i+j
        print(result)
    print('')
"""



"""
lista = [5, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']

licznik = 0
while licznik < len(lista):
    print(lista[licznik])
    licznik += 1    #badz licznik = licznik + 1
else:
    print('koniec petli')
"""



"""
licznik = 0
while licznik != 10:
    if licznik == 7:
        print(licznik)
        break
    else:
        licznik += 1
else:
    print('licznik')
"""


#ZADANIE
#lista jesli podana wartosc po odjeciu elementu z listy da 0 to zakoncz petle, jesli nie to daj komunikat

licznik = 0
lista = [5, 56, 12, 23, 3, 4, 1, 6, 8 ,9 ,10]

a = int(input('Wporwadz liczbe: '))

while licznik < len(lista):
    if(a - lista[licznik]) == 0:
        break
    licznik += 1
else:
    print('licznik')