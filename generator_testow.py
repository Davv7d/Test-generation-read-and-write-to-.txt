from random import shuffle
from random import randrange

testy = './testy/'
odp = './odpowiedzi/'

odp_abcd = {0:'A)',1:'B)',2:'C)',3:'D)'}


def dodaj_odp(pytania,poprawna,poprawna_nr):
        odpl =[]
        while(len(odpl)<=4):
                odpw = pytania[randrange(len(pytania))][1]
                if not (odpw in odpl) or (poprawna == odpw):
                        odpl.append(odpw)
        odpl[poprawna_nr] = poprawna
        return odpl                

def ile_pytan():
        print("Ile pytan chcesz wygenerować")
        ile_pytan = input()
        return int(ile_pytan)

def wczytaj_pytania():
        pytania = []
        dane_test = open('stolice.txt')
        for linia in dane_test:
                pytania.append(linia.split(","))
        dane_test.close()
        return pytania

def wybierz_losowe_pytania(pytnia):
        lista_pytan = []
        for i in range(len(pytania)):
            lista_pytan.append(i)
        shuffle(lista_pytan)
        return lista_pytan

def wczytaj_wylosowane_pytania(ile,losuj,pytania):
        wylosowane =[]
        for i in range(ile):
                py=losuj[i]
                nr=i+1
                wylosowane.append([nr,pytania[py][0],pytania[py][1],randrange(3)]) 
        return wylosowane

def zapisz_odp(nr_tematu,ile,losowe_pytania):
        odpowiedzi = open(odp+'odp'+nr_tematu+'.txt', 'w')

        for i in range(ile):
            odpowiedzi.write(str(i+1)+'.'+odp_abcd[losowe_pytania[i][3]]+'\n')
        odpowiedzi.close()

def zapisz_test(ile,nr_testu,pytania,losowe_pytania):
        test = open(testy+'test'+nr_testu+'.txt', 'w')
        test.write(' Imie Nazwisko: \n\n')
        test.write(' Data: \n\n')
        test.write(' Semestr: \n\n')
        test.write('\t\t Stolice - sprawdzian (Formularz '+str(nr_testu)+' )\n\n\n')
        for i in range(ile):
                nr=str(i+1)
                test.write(nr+'.Jaka jest stolice ma panstwo '+losowe_pytania[i][1]+'?\n')
                odpw=dodaj_odp(pytania,losowe_pytania[i][2],losowe_pytania[i][3])
                test.write(odp_abcd[0]+odpw[0])
                test.write(odp_abcd[1]+odpw[1])
                test.write(odp_abcd[2]+odpw[2])
                test.write(odp_abcd[3]+odpw[3]+"\n")
        test.close()
        
 
        
print("Podaj numer testu:")
nr_testu = input()

ile = ile_pytan()
wszystkie_pytania = wczytaj_pytania()
if not (ile <=len(wszystkie_pytania)):
        print('Podales za duza ilosc pytan, podaj jeszcze raz. Max: ',len(wszystkie_pytania),'\n')
        ile = ile_pytan()


#Generowanie testu
        

pytania = wczytaj_pytania()
losuj =wybierz_losowe_pytania(pytania)
losowe_pytania = wczytaj_wylosowane_pytania(ile,losuj,pytania)

zapisz_odp(nr_testu,ile,losowe_pytania)
zapisz_test(ile,nr_testu,pytania,losowe_pytania)

print("Test wraz z odpowiedziami Został wygenerowany. \nPliki z testem i odpowiedziami znajdują się w odpowiednio katalogach:\n Testy i Odpowiedzi.") 
