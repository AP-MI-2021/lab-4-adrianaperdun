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
        elif op == 'x':
            break
        else:
            print("Eroare. Incercati sa indroduceti alta valoare")

main()