# -*- coding: utf-8 -*-
import Tkinter					
import sys						
from math import *      		
import matplotlib.pyplot as plt 
import numpy as np      		
import linecache        		

##########
##########    Autorzy: Łukasz Pijawski
##########


##########
##########    ŁADOWANIE
########## 

#t - czas
#C - pojemność kondensatora
#R - opór
#E - siła elektromotoryczna

###########
###########

def ladowanie(C, R, E, czas): 
    q = []                                          #przypisanie do q pustej listy
    for t in czas:                                  #exp(x) - potega liczby eulera z biblioteki math
        q.append(C * E * (1 - exp(-t / (R * C))))   #przypisanie do listy q kolejnych wartosci wyrazenia
    return q
    
############

def ladunek_koncowy_ladowania(t, C, R, E):
    q = C * E * (1 - exp(-t / (R * C)))
    return q

############

def natezenie_ladowania(C, R, E, czas):
    I = []
    for t in czas:
        I.append((E / R) * exp(-t / (R * C)))
    return I

############

def napiecie_ladowania(C, R, E, czas):
    U = []
    for t in czas:
        U.append(E * (1 - exp(-t / (R * C))))
    return U

############
############    ROZŁADOWANIE
############

#t - czas
#C - pojemność kondensatora
#R - opór
#q0 - ladunek początkowy

###########
###########

def rozladowanie(C, R, q0, czas):
    q = []
    for t in czas:             
        q.append(q0 * exp(-t / (R * C)))
    return q
    
############

def ladunek_koncowy_rozladowania(t, C, R, q0):
    q = q0 * exp(-t / (R * C))
    return q

############

def natezenie_rozladowania(C, R, q0, czas):
    I = []
    for t in czas:
        I.append((-q0 / (R * C)) * exp(-t / (R * C)))
    return I

############

def napiecie_rozladowania(C, R, q0, czas):
    U = []
    for t in czas:
        U.append((q0 / C) * exp(-t / (R * C)))
    return U

############
############    INNE
############

############
############

def czas_do_naladowania(R, C):
    a = 5 * R * C
    return a

############
############

def limit_ladunku(C, E, czas):
    y = []
    for t in czas:
        y.append(C * E)
    return y
    
############
############

def limit_napiecia(E, czas):
    y = []
    for t in czas:
        y.append(E)
    return y
    
############
############

def limit_natezenia(R, E, czas):
    y = []
    for t in czas:
        y.append(E / R)
    return y
    
############
############	Sprawdza czy wprowadzony tekst jest liczbą

def czy_liczba(tekst):
    if tekst == "":		#sprawdzenie czy lancuch jest pusty
	return 'x'
    tekst = tekst.replace(',', '.')     #zamiana przecinkow na kropki
    if tekst.count('.') > 1:            #sprawdzenie czy jest wiecej niz jedna kropka
        return 'x'
    pom1 = tekst[0]				#przypisanie pierwszego znaku
    pom2 = tekst[-1]			#przypisanie ostatniego znaku
    pom3 = ''
    if pom1 == '.':             #sprawdzenie czy lancuch nie zaczyna sie kropka
        if len(tekst) == 1:     #sprawdzenie czy lancuch nie sklada sie tylko z kropki
            return 'x'
        tekst = '0' + tekst     #jesli uzytkownik zapomni dopisac zera na poczatku to program odczyta liczbe jako ulamek
    if pom2 == '.':		#sprawdzenie czy lancuch nie konczy sie kropka
        tekst = tekst + '0'     #jesli uzytkownik doda sama kropke na koniec to liczba i tak bedzie odczytana
    if pom1 == '-':			#sprawdzenie czy lancuch nie zaczyna sie od minusa
        if len(tekst) == 1:
            return 'x'
        pom3 = '-'
	tekst = tekst[1:]      #sprawdzenie czy tekst jest liczba nie liczac minusa
    for i in tekst:
        if i.isdigit() == False:
            if i != '.':
                return 'x'
    tekst = pom3 + tekst
    return tekst

############
############	Sprawdza, czy wprowadzony tekst jest poprawny

def wczytywanie(zrodlo, opis, blad):
    dana = zrodlo.strip()      			#usuwanie bialych znakow z poczatku i konca przy wczytywaniu
    dana = czy_liczba(dana)             #sprawdzenie czy wprowadzony tekst jest liczba
    if dana == 'x':
		tekst = blad.cget("text") + u'Błąd: ' + opis + u' musi być liczbą.\n'		#dołączanie tekstu do etykiety wyświetlającej błędy
		blad.config(text = tekst)
		return 'ponownie'
    dana = float(dana)                  #zamiana tekstu na liczbe typu float
    if dana <= 0:                       #sprawdzenie czy liczba jest dodatnia
		tekst = blad.cget("text") + u'Błąd: ' + opis + u' musi być dodatnia.\n'		#u przed ciągiem oznacza, że tekst ma być odczytany jako Unicode 
		blad.config(text = tekst)													#(umożliwia użycie polskich znaków wyswietlanych w programie (niestety nie w przypadku plików i wykresów)
		return 'ponownie'
    return dana

############
def ostatnia_konfiguracja(nazwa_pliku): #odczytywanie z pliku ostatniej konfiguracji
    try:
        f = open(nazwa_pliku, 'rU')         #otwarcie pliku do czytania i z ujednoliconym rozpoznawaniem znaku konca linii niezaleznie od systemu operacyjnego
    except IOError:                     #sprawdzenie czy plik istnieje
        return ''
    ile = len(f.readlines())            #policzenie linii
    konfiguracja = ''
    for i in range(6, 1, -1):
        konfiguracja += linecache.getline(nazwa_pliku , ile - i)
    linecache.clearcache()              #czyszczenie bufora z zapisanymi liniami
    f.close()
    return konfiguracja

############
############

def zamknij():
	sys.exit()

############
############	Wyświetlanie jednego lub dwoch kondensatorow
	
def wyswietlJeden():
	
	Kondensatory.pack_forget()		#"zapominanie" starej ramki
	Kondensatory.pack()				#definiowanie ramki na nowo
	kondensator1.pack_forget()
	kondensator2.pack_forget()		#ukrycie ramki dla drugiego kondensatora
	kondensator1.pack(side = "top")	#side - umiejscowienie elementu w ramce nadrzędnej
	
	opis.pack()
	
	pojemnosc.pack()
	pojemnoscPobranie.pack()
	
	opor.pack()
	oporPobranie.pack()
	
	SEM.pack()
	SEMPobranie.pack()
	
	ladunek.pack()
	ladunekPobranie.pack()
	
	Bledy.pack_forget()
	Bledy.pack()
	bledy2.pack_forget()
	bledy.pack(side = "top")
	
	badajLadowanie.pack(side = "top")
	badajRozladowanie.pack(side = "top")
	badajLadowanie2.pack_forget()
	badajRozladowanie2.pack_forget()

	
def wyswietlDwa():
	Kondensatory.pack_forget()
	Kondensatory.pack()
	kondensator1.pack(side = "left")
	kondensator2.pack(side = "right")
	
	opis.pack()
	
	pojemnosc.pack()
	pojemnoscPobranie.pack()
	
	opor.pack()
	oporPobranie.pack()
	
	SEM.pack()
	SEMPobranie.pack()
	
	ladunek.pack()
	ladunekPobranie.pack()
	
	opis2.pack()
	
	pojemnosc2.pack()
	pojemnoscPobranie2.pack()
	
	opor2.pack()
	oporPobranie2.pack()
	
	SEM2.pack()
	SEMPobranie2.pack()
	
	ladunek2.pack()
	ladunekPobranie2.pack()
	
	Bledy.pack_forget()
	Bledy.pack()
	bledy.pack(side = "left")
	bledy2.pack(side = "right")
	
	badajLadowanie.pack_forget()
	badajRozladowanie.pack_forget()
	badajLadowanie2.pack(side = "top")
	badajRozladowanie2.pack(side = "top")



############
############

def proces_ladowania():
	########    wczytywanie danych ze sprawdzeniem ich poprawnosci
	
	blad = 0			#zmienna pokazujaca ze wystapil błąd podczas wczytywania
	
	bledy.config(text = "")	#zerowanie etykiety zawierającej opisy błędów
	
	C = wczytywanie(pojemnoscPobranie.get(), u"Pojemność kondensatora", bledy)
	if C == 'ponownie':
		blad = 1
		
	R = wczytywanie(oporPobranie.get(), u'Wartość oporu', bledy)
	if R == 'ponownie':
		blad = 1
		
	E = wczytywanie(SEMPobranie.get(), u'Wartość SEM', bledy)
	if E == 'ponownie':
		blad = 1
		
	if blad > 0:
		return 0		#jeśli wystąpił błąd to przerywamy funkcję, ale mamy pełen zapis błędów
		
	
	
	########    tworzenie tablic z wartosciami by uzyc ich w wykresach
	t = czas_do_naladowania(R, C)
	krok = t / 100.0
	czas = np.arange(0, t, krok)             #przypisanie do zmiennej czas listy wartosci od 0 do t z krokiem
	q = ladowanie(C, R, E, czas)
	Q = limit_ladunku(C, E, czas)

	U = napiecie_ladowania(C, R, E, czas)
	u = limit_napiecia(E, czas)

	I = natezenie_ladowania(C, R, E, czas)
	i = limit_natezenia(R, E, czas)	

	########	liczenie stopnia naladowania kondensatora

	pom1 = ladunek_koncowy_ladowania(t, C, R, E)

	info1.config(text = u"Na kondensatorze zgromadziło się " + str(pom1) + u" [C] ładunku.\n")
	info2.config(text = u"Potrzeba " + str(t) + u" sekund, żeby naładować kondensator o podanych parametrach \n(zgromadzenie >99 % maks. ładunku).\n")
	
	########	zapis danych do pliku

	plik = open('daneLadowania.txt', 'a')
	plik.write("Pojemnosc:  \t\t" + str(C) + " [F]\n")
	plik.write("Opor:       \t\t" + str(R) + " [om]\n")
	plik.write("Sila elektromotoryczna: \t" + str(E) + " [V]\n")
	plik.write("Czas ladowania: \t\t" + str(t) + " [s]\n")
	plik.write("Zgromadzony ladunek: \t" + str(pom1) + " [C]\n")
	plik.write("############################################################################################\n\n")
	plik.close()
	
	lad_konf = ostatnia_konfiguracja('daneLadowania.txt')
	ladKonf.config(text = u"Ostatnia konfiguracja parametrów ładowania: \n" + lad_konf)

	########    pierwszy wykres

	fig = plt.figure(1)					#numer wykresu i przypisanie wykresu do zmiennej
	fig.canvas.set_window_title('Ladunek')		#ustawienie tytulu okna
	plt.title('Ladowanie kondensatora - ilosc ladunku') #tytul wykresu
	plt.xlabel('Czas [s]')                              #opis osi X
	plt.ylabel('Zgromadzony ladunek [C]')               #opis osi Y

	#generowanie wykresow funkcji, label - etykieta do funkcji w legendzie

	plt.plot(czas, q, label = 'q - ilosc ladunku (parametry: ' + str(C) + ' [F] ' + str(R) + ' [om] ' + str(E) + ' [V])')
	plt.plot(czas, Q, '--', label = 'CE - do tej wartosci dazy ilosc \nzgromadzonego ladunku')
	plt.legend(loc = 'best')        #wyswietlenie legendy z 'najlepsza' lokalizacja - by wykres nie zaslanial
	plt.axis([0, t, 0, C * E * 1.3])    #ustawienie jakie przedziały argumentów i wartosci maja byc wyswietlane

	########    drugi wykres

	fig = plt.figure(2)	            #numer wykresu
	fig.canvas.set_window_title('Napiecie')
	plt.title('Ladowanie kondensatora - wartosc napiecia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napiecie na kondensatorze [V]')

	plt.plot(czas, U, label = 'U - wartosc napiecia na kondensatorze (parametry: ' + str(C) + ' [F] ' + str(R) + ' [om] ' + str(E) + ' [V])')
	plt.plot(czas, u, '--', label = 'E - napiecie na kondensatorze dazy \ndo zrownania sie z sila elektromotoryczna')
	plt.legend(loc = 'best')
	plt.axis([0, t, 0, E * 1.3])

	########    trzeci wykres

	fig = plt.figure(3)	            #numer wykresu
	fig.canvas.set_window_title('Natezenie')
	plt.title('Ladowanie kondensatora - wartosc natezenia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Natezenie pradu w obwodzie [A]')

	plt.plot(czas, I, label = 'I - wartosc natezenia (parametry: ' + str(C) + ' [F] ' + str(R) + ' [om] ' + str(E) + ' [V])')
	plt.plot(czas, i, '--', label = 'E / R - najwieksza wartosc natezenia\nna poczatku ladowania')
	plt.legend(loc = 'best')
	plt.axis([0, t, 0, (E / R) * 1.3])

	plt.show()  #wyswietlenie wykresow

	return 0

############
############

def proces_ladowania2():
	########    wczytywanie danych ze sprawdzeniem ich poprawnosci

	blad = 0
	
	bledy.config(text = "")
	
	bledy2.config(text = "")

	########    parametry pierwszego kondensatora
	

	C1 = wczytywanie(pojemnoscPobranie.get(), u"Pojemność kondensatora", bledy)
	if C1 == 'ponownie':
		blad = 1
		
	R1 = wczytywanie(oporPobranie.get(), u'Wartość oporu', bledy)
	if R1 == 'ponownie':
		blad = 1
		
	E1 = wczytywanie(SEMPobranie.get(), u'Wartość SEM', bledy)
	if E1 == 'ponownie':
		blad = 1


	########    parametry drugiego kondensatora

	C2 = wczytywanie(pojemnoscPobranie2.get(), u"Pojemność kondensatora", bledy2)
	if C2 == 'ponownie':
		blad = 1
		
	R2 = wczytywanie(oporPobranie2.get(), u'Wartość oporu', bledy2)
	if R2 == 'ponownie':
		blad = 1
		
	E2 = wczytywanie(SEMPobranie2.get(), u'Wartość SEM', bledy2)
	if E2 == 'ponownie':
		blad = 1
		
	if blad > 0:
		return 0     

	########    tworzenie tablic z wartosciami by uzyc ich w wykresach
	t1 = czas_do_naladowania(R1, C1)
	t2 = czas_do_naladowania(R2, C2)

	krok = max(t1, t2) / 100.0
	czas = np.arange(0, max(t1, t2), krok)             #przypisanie do zmiennej czas listy wartosci od 0 do t z krokiem

	q1 = ladowanie(C1, R1, E1, czas)
	q2 = ladowanie(C2, R2, E2, czas)
	Q1 = limit_ladunku(C1, E1, czas)
	Q2 = limit_ladunku(C2, E2, czas)

	U1 = napiecie_ladowania(C1, R1, E1, czas)
	U2 = napiecie_ladowania(C2, R2, E2, czas)
	u1 = limit_napiecia(E1, czas)
	u2 = limit_napiecia(E2, czas)

	I1 = natezenie_ladowania(C1, R1, E1, czas)
	I2 = natezenie_ladowania(C2, R2, E2, czas)
	i1 = limit_natezenia(R1, E1, czas)	
	i2 = limit_natezenia(R2, E2, czas)	
		
	########	liczenie stopnia naladowania kondensatora


	pom1 = ladunek_koncowy_ladowania(t1, C1, R1, E1)
	pom2 = ladunek_koncowy_ladowania(t2, C2, R2, E2)	

	info1.config(text = u"Na pierwszym kondensatorze zgromadziło się " + str(pom1) + " [C], a na drugim " + str(pom2) + u" [C] ładunku.\n")
	info2.config(text = "Potrzeba " + str(t1) + u" sekund, żeby naładowac pierwszy kondensator, a " + str(t2) + u" sekund, żeby naładować drugi\n(zgromadzenie >99 % maks. ładunku).\n")

	########	zapis danych do pliku
	
	plik = open('daneLadowania2.txt', 'a')
	plik.write("Parametry porownywanych kondensatorow:\n--------------------------------------\n")
	plik.write("Pojemnosci:\t\t\t" + '%-30s' % (str(C1) + " [F]") + '\t' + str(C2) + " [F]\n")
	plik.write("Opory:\t\t\t\t" + '%-30s' % (str(R1) + " [om]") + '\t' + str(R2) + " [om]\n")
	plik.write("Sily elektromotoryczne:\t\t" + '%-30s' %  (str(E1) + " [V]") + '\t' + str(E2) + " [V]\n")
	plik.write("Czasy ladowania:\t\t\t" + '%-30s' %  (str(t1) + " [s]") + '\t' + str(t2) + " [s]\n")
	plik.write("Zgromadzone ladunki:\t\t" + '%-30s' %  (str(pom1) + " [C]") + '\t' + str(pom2) + " [C]\n")
	plik.write("############################################################################################\n\n")
	plik.close()
	
	lad_konf = ostatnia_konfiguracja('daneLadowania2.txt')
	ladKonf.config(text = u"Ostatnia konfiguracja parametrów ładowania: \n" + lad_konf)

	########    pierwszy wykres

	fig = plt.figure(1)					#numer wykresu i przypisanie wykresu do zmiennej
	fig.canvas.set_window_title('Ladunek')		#ustawienie tytulu okna
	plt.title('Ladowanie kondensatora - ilosc ladunku') #tytul wykresu
	plt.xlabel('Czas [s]')                              #opis osi X
	plt.ylabel('Zgromadzony ladunek [C]')               #opis osi Y

	#generowanie wykresow funkcji, label - etykieta do funkcji w legendzie

	plt.plot(czas, q1, label = 'q1 - ilosc ladunku na pierwszym kondensatorze (' + str(C1) + ' [F] ' + str(R1) + ' [om] ' + str(E1) + ' [V])')
	plt.plot(czas, q2, label = 'q2 - ilosc ladunku na drugim kondensatorze (' + str(C2) + ' [F] ' + str(R2) + ' [om] ' + str(E2) + ' [V])') 
	plt.plot(czas, Q1, '--', label = 'CE1 - do tej wartosci dazy ilosc \nzgromadzonego ladunku na pierwszym kondensatorze')
	plt.plot(czas, Q2, '--', label = 'CE2 - do tej wartosci dazy ilosc \nzgromadzonego ladunku na drugim kondensatorze')
	plt.legend(loc = 'best')        #wyswietlenie legendy z 'najlepsza' lokalizacja - by wykres nie zaslanial
	plt.axis([0, max(t1, t2), 0, max(C1, C2) * max(E1, E2) * 1.3])    #ustawienie jakie przedziały argumentów i wartosci maja byc wyswietlane

	########    drugi wykres

	fig = plt.figure(2)	            #numer wykresu
	fig.canvas.set_window_title('Napiecie')
	plt.title('Ladowanie kondensatora - wartosc napiecia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napiecie na kondensatorze [V]')

	plt.plot(czas, U1, label = 'U1 - wartosc napiecia na pierwszym kondensatorze (' + str(C1) + ' [F] ' + str(R1) + ' [om] ' + str(E1) + ' [V])')
	plt.plot(czas, U2, label = 'U2 - wartosc napiecia na drugim kondensatorze (' + str(C2) + ' [F] ' + str(R2) + ' [om] ' + str(E2) + ' [V])')
	plt.plot(czas, u1, '--', label = 'E1 - napiecie na pierwszym kondensatorze dazy \ndo zrownanie sie z sila elektromotoryczna')
	plt.plot(czas, u2, '--', label = 'E2 - napiecie na drugim kondensatorze dazy \ndo zrownanie sie z sila elektromotoryczna')
	plt.legend(loc = 'best')
	plt.axis([0, max(t1, t2), 0, max(E1, E2) * 1.3])

	########    trzeci wykres

	fig = plt.figure(3)	            #numer wykresu
	fig.canvas.set_window_title('Natezenie')
	plt.title('Ladowanie kondensatora - wartosc natezenia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Natezenie pradu w obwodzie [A]')

	plt.plot(czas, I1, label = 'I1 - wartosc natezenia w pierwszym kondensatorze (' + str(C1) + ' [F] ' + str(R1) + ' [om] ' + str(E1) + ' [V])')
	plt.plot(czas, I2, label = 'I2 - wartosc natezenia w drugim kondensatorze (' + str(C2) + ' [F] ' + str(R2) + ' [om] ' + str(E2) + ' [V])')
	plt.plot(czas, i1, '--', label = 'E1 / R1 - najwieksza wartosc natezenia w pierwszym kondensatorze\nna poczatku ladowania')
	plt.plot(czas, i2, '--', label = 'E2 / R2 - najwieksza wartosc natezenia w drugim kondensatorze\nna poczatku ladowania')
	plt.legend(loc = 1)
	plt.axis([0, max(t1, t2), 0, max((E1 / R1), (E2 / R2)) * 1.3])

	plt.show()  #wyswietlenie wykresow

	return 0

############
############

############
###########

def proces_rozladowania():
    ########    wczytywanie danych ze sprawdzeniem ich poprawnosci
	
	blad = 0
	
	bledy.config(text = "")
			
	C = wczytywanie(pojemnoscPobranie.get(), u"Pojemność kondensatora", bledy)
	if C == 'ponownie':
		blad = 1
		
	R = wczytywanie(oporPobranie.get(), u'Wartość oporu', bledy)
	if R == 'ponownie':
		blad = 1

	q0 = wczytywanie(ladunekPobranie.get(), u"Wartość ładunku początkowego", bledy)
	if q0 == 'ponownie':
		blad = 1
		
	if blad > 0:
		return 0

	########    tworzenie tablic z wartosciami by uzyc ich w wykresach
	t = czas_do_naladowania(R, C)
	krok = t / 100.0
	czas = np.arange(0, t, krok)
	q = rozladowanie(C, R, q0, czas)
	Q = limit_ladunku(q0, 1, czas)

	U = napiecie_rozladowania(C, R, q0, czas)
	u = limit_napiecia(q0 / C, czas)

	I = natezenie_rozladowania(C, R, q0, czas)

	########	liczenie stopnia rozladowania

	pom1 = ladunek_koncowy_rozladowania(t, C, R, q0)

	info1.config(text = u"Na kondensatorze pozostało " + str(pom1) + u" [C] ładunku.\n")
	info2.config(text = "Potrzeba " + str(t) + u" sekund, żeby rozładować kondensator o podanych parametrach \n(pozostanie <1 % ładunku).\n")

	########	zapis danych do pliku

	plik = open('daneRozladowania.txt', 'a')
	plik.write("Pojemnosc:  \t\t" + str(C) + " [F]\n")
	plik.write("Opor:       \t\t" + str(R) + " [om]\n")
	plik.write("Ladunek poczatkowy: \t" + str(q0) + " [C]\n")
	plik.write("Czas rozladowania:  \t" + str(t) + " [s]\n")
	plik.write("Pozostaly ladunek:  \t" + str(pom1) + " [C]\n")
	plik.write("############################################################################################\n\n")
	plik.close()
	
	roz_konf = ostatnia_konfiguracja('daneRozladowania.txt')
	rozKonf.config(text = u"Ostatnia konfiguracja parametrów rozładowania: \n" + roz_konf)

	########    pierwszy wykres

	fig = plt.figure(1)
	fig.canvas.set_window_title('Ladunek')
	plt.title('Rozladowanie kondensatora - ilosc ladunku') #tytul wykresu
	plt.xlabel('Czas [s]')                              #opis osi X
	plt.ylabel('Zgromadzony ladunek [C]')               #opis osi Y

	#generowanie wykresow funkcji, label - etykieta do funkcji w legendzie

	plt.plot(czas, q, label = 'q - ilosc ladunku (parametry: ' + str(C) + ' [F] ' + str(R) + ' [om] ' + str(q0) + ' [C])')
	plt.plot(czas, Q, '--', label = 'q0 - poczatkowa ilosc\nzgromadzonego ladunku')
	plt.legend(loc = 'best')                #wyswietlenie legendy z 'najlepsza' lokalizacja - by wykres nie zaslanial
	plt.axis([0, t, 0, q0 * 1.3])           #ustawienie jakie przedziały argumentów i wartosci maja byc wyswietlane

	########    drugi wykres

	fig = plt.figure(2)
	fig.canvas.set_window_title('Napiecie')
	plt.title('Rozladowanie kondensatora - wartosc napiecia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napiecie na kondensatorze [V]')

	plt.plot(czas, U, label = 'U - wartosc napiecia na kondensatorze (parametry: ' + str(C) + ' [F] ' + str(R) + ' [om] ' + str(q0) + ' [C])')
	plt.plot(czas, u, '--', label = 'U0 - poczatkowe napiecie na kondensatorze')
	plt.legend(loc = 'best')
	plt.axis([0, t, 0, (q0 / C) * 1.3])

	########    trzeci wykres

	fig = plt.figure(3)
	fig.canvas.set_window_title('Natezenie')
	plt.title('Rozladowanie kondensatora - wartosc natezenia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Natezenie pradu w obwodzie [A]')

	plt.plot(czas, I, label = 'I - wartosc natezenia (parametry: ' + str(C) + ' [F] ' + str(R) + ' [om] ' + str(q0) + ' [C])')
	plt.legend(loc = 'best')
	plt.axis([0, t, -q0 / (R * C), 0])


	plt.show()  #wyswietlenie wykresow

	return 0
	
############
############

def proces_rozladowania2():
	########    wczytywanie danych ze sprawdzeniem ich poprawnosci

	blad = 0
	
	bledy.config(text = "")
	
	bledy2.config(text = "")

	########    parametry pierwszego kondensatora


	C1 = wczytywanie(pojemnoscPobranie.get(), u"Pojemność kondensatora", bledy)
	if C1 == 'ponownie':
		blad = 1
		
	R1 = wczytywanie(oporPobranie.get(), u'Wartość oporu', bledy)
	if R1 == 'ponownie':
		blad = 1
		
	q01 = wczytywanie(ladunekPobranie.get(), u'Wartość ładunku początkowego', bledy)
	if q01 == 'ponownie':
		blad = 1

	########    parametry drugiego kondensatora

	C2 = wczytywanie(pojemnoscPobranie2.get(), u"Pojemność kondensatora", bledy2)
	if C2 == 'ponownie':
		blad = 1
		
	R2 = wczytywanie(oporPobranie2.get(), u'Wartość oporu', bledy2)
	if R2 == 'ponownie':
		blad = 1
		
	q02 = wczytywanie(ladunekPobranie2.get(), u'Wartość ładunku początkowego', bledy2)
	if q02 == 'ponownie':
		blad = 1     
	
	if blad > 0:
		return 0
		   
	########    tworzenie tablic z wartosciami by uzyc ich w wykresach
	t1 = czas_do_naladowania(R1, C1)
	t2 = czas_do_naladowania(R2, C2)
	krok = max(t1, t2) / 100.0
	czas = np.arange(0, max(t1, t2), krok)
	q1 = rozladowanie(C1, R1, q01, czas)
	q2 = rozladowanie(C2, R2, q02, czas)
	Q1 = limit_ladunku(q01, 1, czas)
	Q2 = limit_ladunku(q02, 1, czas)

	U1 = napiecie_rozladowania(C1, R1, q01, czas)
	U2 = napiecie_rozladowania(C2, R2, q02, czas)
	u1 = limit_napiecia(q01 / C1, czas)
	u2 = limit_napiecia(q02 / C2, czas)

	I1 = natezenie_rozladowania(C1, R1, q01, czas)
	I2 = natezenie_rozladowania(C2, R2, q02, czas)

	########	liczenie stopnia rozladowania

	pom1 = ladunek_koncowy_rozladowania(t1, C1, R1, q01)
	pom2 = ladunek_koncowy_rozladowania(t2, C2, R2, q02)

	info1.config(text = u"Na pierwszym kondensatorze pozostało " + str(pom1) + u" [C], a na drugim " + str(pom2) + u" [C] ładunku.\n")
	info2.config(text = "Potrzeba " + str(t1) + u" sekund, żeby rozładować pierwszy kondensator, a " + str(t2) + u" sekund, żeby rozładować drugi\n(pozostanie <1 % ładunku).\n")
	
	########	zapis danych do pliku

	plik = open('daneRozladowania2.txt', 'a')
	plik.write("Parametry porownywanych kondensatorow:\n--------------------------------------\n")
	plik.write("Pojemnosci:\t\t\t" + '%-30s' % (str(C1) + " [F]") + '\t\t' + str(C2) + " [F]\n")
	plik.write("Opory:\t\t\t\t" + '%-30s' % (str(R1) + " [om]") + '\t\t' + str(R2) + " [om]\n")
	plik.write("Ladunki poczatkowe:\t\t" + '%-30s' % (str(q01) + " [C]") + '\t\t' + str(q02) + " [C]\n")
	plik.write("Czasy rozladowania:\t\t" + '%-30s' % (str(t1) + " [s]") + '\t\t' + str(t2) + " [s]\n")
	plik.write("Pozostale ladunki:\t\t\t" + '%-30s' % (str(pom1) + " [C]") + '\t' + str(pom2) + " [C]\n")
	plik.write("############################################################################################\n\n")
	plik.close()
	
	roz_konf = ostatnia_konfiguracja('daneRozladowania2.txt')
	rozKonf.config(text = u"Ostatnia konfiguracja parametrów rozładowania: \n" + roz_konf)

	########    pierwszy wykres

	fig = plt.figure(1)
	fig.canvas.set_window_title('Ladunek')
	plt.title('Rozladowanie kondensatora - ilosc ladunku') #tytul wykresu
	plt.xlabel('Czas [s]')                              #opis osi X
	plt.ylabel('Zgromadzony ladunek [C]')               #opis osi Y

	#generowanie wykresow funkcji, label - etykieta do funkcji w legendzie

	plt.plot(czas, q1, label = 'q1 - ilosc ladunku na pierwszym kondensatorze (' + str(C1) + ' [F] ' + str(R1) + ' [om] ' + str(q01) + ' [V])')
	plt.plot(czas, q2, label = 'q2 - ilosc ladunku na drugim kondensatorze (' + str(C2) + ' [F] ' + str(R2) + ' [om] ' + str(q02) + ' [V])')
	plt.plot(czas, Q1, '--', label = 'q01 - poczatkowa ilosc zgromadzonego ladunku\nna pierwszym kondensatorze')
	plt.plot(czas, Q2, '--', label = 'q02 - poczatkowa ilosc zgromadzonego ladunku\nna drugim kondensatorze')
	plt.legend(loc = 'best')                #wyswietlenie legendy z 'najlepsza' lokalizacja - by wykres nie zaslanial
	plt.axis([0, max(t1, t2), 0, max(q01, q02) * 1.3])           #ustawienie jakie przedziały argumentów i wartosci maja byc wyswietlane

	########    drugi wykres

	fig = plt.figure(2)
	fig.canvas.set_window_title('Napiecie')
	plt.title('Rozladowanie kondensatora - wartosc napiecia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Napiecie na kondensatorze [V]')

	plt.plot(czas, U1, label = 'U1 - wartosc napiecia na pierwszym kondensatorze (' + str(C1) + ' [F] ' + str(R1) + ' [om] ' + str(q01) + ' [V])')
	plt.plot(czas, U2, label = 'U2 - wartosc napiecia na drugim kondensatorze (' + str(C2) + ' [F] ' + str(R2) + ' [om] ' + str(q02) + ' [V])')
	plt.plot(czas, u1, '--', label = 'U01 - poczatkowe napiecie na pierwszym kondensatorze')
	plt.plot(czas, u2, '--', label = 'U02 - poczatkowe napiecie na drugim kondensatorze')
	plt.legend(loc = 'best')
	plt.axis([0, max(t1, t2), 0, (max(q01, q02) / max(C1, C2)) * 1.3])

	########    trzeci wykres

	fig = plt.figure(3)
	fig.canvas.set_window_title('Natezenie')
	plt.title('Rozladowanie kondensatora - wartosc natezenia')
	plt.xlabel('Czas [s]')
	plt.ylabel('Natezenie pradu w obwodzie [A]')

	plt.plot(czas, I1, label = 'I1 - wartosc natezenia na pierwszym kondensatorze (' + str(C1) + ' [F] ' + str(R1) + ' [om] ' + str(q01) + ' [V])')
	plt.plot(czas, I2, label = 'I2 - wartosc natezenia na drugim kondensatorze (' + str(C2) + ' [F] ' + str(R2) + ' [om] ' + str(q02) + ' [V])')
	plt.legend(loc = 'best')
	plt.axis([0, max(t1, t2), -max(q01, q02) / (max(R1, R2) * max(C1, C2)), 0])


	plt.show()  #wyswietlenie wykresow

	return 0	

    
############
############    Program głowny
############

main = Tkinter.Tk()		#okno główne

############	Deklarowanie ramek

Konfiguracja = Tkinter.Frame(main)
Konfiguracja.pack(side = "top")

Kondensatory = Tkinter.Frame(main)

kondensator1 = Tkinter.Frame(Kondensatory)

kondensator2 = Tkinter.Frame(Kondensatory)

Bledy = Tkinter.Frame(main)
bledy = Tkinter.Label(Bledy, text = "")
bledy2 = Tkinter.Label(Bledy, text = "")

Przyciski = Tkinter.Frame(main)
Przyciski.pack(side = "bottom")

#######################

tytul = Tkinter.Label(Konfiguracja, text = u"ŁADOWANIE I ROZŁADOWANIE KONDENSATORÓW\n")	#etykieta tytułowa

ladKonf = Tkinter.Label(Konfiguracja, justify = "left")
rozKonf = Tkinter.Label(Konfiguracja, justify = "left")

lad_konf = ostatnia_konfiguracja('daneLadowania2.txt')       #odczytywanie z pliku ostatniej konfiguracji
roz_konf = ostatnia_konfiguracja('daneRozladowania2.txt')

if lad_konf == '':
	lad_konf = ostatnia_konfiguracja('daneLadowania.txt')
	
if roz_konf == '':
	roz_konf = ostatnia_konfiguracja('daneRozladowania.txt')

if lad_konf != '':
	ladKonf.config(text = u"Ostatnia konfiguracja parametrów ładowania:\n" + lad_konf)
else:
	ladKonf.config(text = u"Brak zapisanych konfiguracji ładowania\n")
        
if roz_konf != '':
	rozKonf.config(text = u"Ostatnia konfiguracja parametrów rozładowania:\n" + roz_konf)
else:
	rozKonf.config(text = u"Brak zapisanych konfiguracji rozładowania\n")
	
var = Tkinter.IntVar()		#zmienna łącząca przyciski typu 'radio' przyjmująca wartości liczbowe

dwaKondensatory = Tkinter.Radiobutton(Konfiguracja, text = u"Chcę porównać dwa kondensatory", variable = var, value = 2, command = wyswietlDwa)
dwaKondensatory.pack(side = "bottom", anchor = 'w')	#anchor - punkt zaczepienia, w - 'zachód', przycisk jest z lewej strony

jedenKondensator = Tkinter.Radiobutton(Konfiguracja, text = "Chcę przeanalizować jeden kondensator", variable = var, value = 1, command = wyswietlJeden)
jedenKondensator.pack(side = "bottom", anchor = 'w')
	
################
################	Odczytywanie parametrow pierwszego kondensatora

opis = Tkinter.Label(kondensator1, text = "Parametry pierwszego kondensatora\n")		#etykieta pierwszego kondensatora

pojemnosc = Tkinter.Label(kondensator1, text = u"Pojemność [F]", justify = "left")		#etykieta pola
pojemnoscPobranie = Tkinter.Entry(kondensator1)											#pole do wprowadzania danych

opor = Tkinter.Label(kondensator1, text = u"Opór [om]")	
oporPobranie = Tkinter.Entry(kondensator1)

SEM = Tkinter.Label(kondensator1, text = u"Siła elektromotoryczna [V]")	
SEMPobranie = Tkinter.Entry(kondensator1)

ladunek = Tkinter.Label(kondensator1, text = u"Ładunek początkowy [C]")	
ladunekPobranie = Tkinter.Entry(kondensator1)

################
################	Odczytywanie parametrow drugiego kondensatora

opis2 = Tkinter.Label(kondensator2, text = "Parametry drugiego kondensatora\n")

pojemnosc2 = Tkinter.Label(kondensator2, text = u"Pojemność [F]", justify = "left")	
pojemnoscPobranie2 = Tkinter.Entry(kondensator2)

opor2 = Tkinter.Label(kondensator2, text = u"Opór [om]")	
oporPobranie2 = Tkinter.Entry(kondensator2)

SEM2 = Tkinter.Label(kondensator2, text = u"Siła elektromotoryczna [V]")	
SEMPobranie2 = Tkinter.Entry(kondensator2)

ladunek2 = Tkinter.Label(kondensator2, text = u"Ładunek początkowy [C]")	
ladunekPobranie2 = Tkinter.Entry(kondensator2)

################
################	Przyciski

badajLadowanie = Tkinter.Button(Przyciski, text = u"Badaj ładowanie", command = proces_ladowania)			#uruchomienie ładowania
badajRozladowanie = Tkinter.Button(Przyciski, text = u"Badaj rozładowanie", command = proces_rozladowania)	#uruchomienie rozładowania

badajLadowanie2 = Tkinter.Button(Przyciski, text = u"Badaj ładowanie", command = proces_ladowania2)			#ładowanie i rozładowanie dla dwóch kondensatorów
badajRozladowanie2 = Tkinter.Button(Przyciski, text = u"Badaj rozładowanie", command = proces_rozladowania2)

info1 = Tkinter.Label(Przyciski, text = "")		#etykiety pokazujące wyniki
info2 = Tkinter.Label(Przyciski, text = "")

zamknij = Tkinter.Button(Przyciski, text = u"Zakończ program", command = zamknij)	#przycisk kończący program

tytul.pack()
ladKonf.pack(side = "left")
rozKonf.pack(side = "right")

info1.pack()
info2.pack()

zamknij.pack(side = "bottom")

main.mainloop()
