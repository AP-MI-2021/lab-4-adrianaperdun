def citire():
    '''
    Citim lista
    :return: elementele listei
    '''
    l = []
    n = int(input("Dati elemente: "))
    for i in range(n):
        l.append(int(input(f"l[{i}]= ")))
    return l

def numarprim(n):
    '''
    Verificam daca un numar dat este prim.
    :param n: numarul de intrare
    :return: Daca e prim va returna True, respectiv False in caz contrar.
    '''
    ok = False
    if n > 1:
        for i in range(2, n//2+1):
            if n % i == 0:
                ok = True
    return ok

def eliminareprime(l):
    '''
    Eliminarea numerelor prime din lista
    :param l: lista initiala
    :return: lista fara elemente prime
    '''
    r = []
    for i in l:
        if numarprim(i):
            r.append(i)
    return r


def mediaartimetica(l):
    '''
    Calculam media aritmetica a listei initiale.
    :param l: lista
    :return: media aritmetica
    '''
    ave = sum(l) / len(l)
    return ave

def maimaredecat(n):
    '''
    Verifica daca un numar dat este mai mic decat media aritmetica a elementelor
    :param n: numarul dat
    :return: True daca este mai mic, False in caz contra
    '''
    ok = False
    if mediaartimetica(l) > n:
        ok = True
    return ok

def divizoriproprii(n):
    '''
    Calculam divizorii proprii ai unui numar
    :param n: numarul
    :return: diviorii proprii
    '''
    t = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            t=t+1
    return t

def listacudivivori(l):
    x = 0
    li = []
    for i in l:
        if numarprim(i) == 0:
            li.append(i)
        else:
            x =divizoriproprii(i)
            li.append(x)

    return li


def test_mediaaritmetica():
    assert mediaartimetica([7,2,4,18]) == 7
    assert mediaartimetica([1,1,1,1,1,1,1]) == 1

def test_numarprim():
    assert numarprim(7) is True
    assert numarprim(8) is False
    assert numarprim(5) is True


def main():
    l = []
    while True:
        print("1. Citirea listei.")
        print("2. Afisarea listei dupa eliminarea numerelor prime.")
        print("3. Verifica daca media aritmetica a numerelor este mai mare decat un numar dat.")
        print("4. Afisarea listei obtinute prin adaugarea dupa fiecare element numarul de divizori proprii ai elementului .")
        print("5. Lista unde numerele sunt inlocuite cu un tuplu unde pe prima pozitie este numarul, pe a doua va fi indexul, iar pe a treia numarul de aparitii.")
        print("x. Iesire")
        op = input("Dati optiunea: ")
        if op == '1':
            l = citire()
        elif op == '2':
            print(eliminareprime(l))
        elif op == '3':
            n = int(input("Dati un numar: "))
            print(maimaredecat(n))
        elif op == '4':
            print(listacudivivori(l))
        elif op == 'a':
            print(mediaartimetica(l))
        elif op == 'x':
            break
        else:
            print("Eroare. Incercati sa indroduceti alta valoare")

main()
