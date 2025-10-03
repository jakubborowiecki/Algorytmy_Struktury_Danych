def dopasowanie_rekurencyjnie(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    if P[i - 1] == T[j - 1]:
        return dopasowanie_rekurencyjnie(P, T, i - 1, j - 1)

    koszt_wymiany = dopasowanie_rekurencyjnie(P, T, i - 1, j - 1) + 1
    koszt_usunięcia = dopasowanie_rekurencyjnie(P, T, i - 1, j) + 1
    koszt_wstawienia = dopasowanie_rekurencyjnie(P, T, i, j - 1) + 1

    return min(koszt_wymiany, koszt_wstawienia, koszt_usunięcia)


def dopasowanie_PD(P, T):
    dlugosc_P = len(P)
    dlugosc_T = len(T)

    dystans = []
    for i in range(dlugosc_P + 1):
        dystans.append([0] * (dlugosc_T + 1))

    rodzice = []
    for i in range(dlugosc_P + 1):
        rodzice.append(['X'] * (dlugosc_T + 1))

    for i in range(dlugosc_P + 1):
        dystans[i][0] = i
    for j in range(dlugosc_T + 1):
        dystans[0][j] = j

    for i in range(1, dlugosc_P + 1):
        for j in range(1, dlugosc_T + 1):

            if P[i - 1] != T[j - 1]:
                koszt_wymiany = dystans[i - 1][j - 1] + 1
            else:
                koszt_wymiany = dystans[i - 1][j - 1]

            koszt_usunięcia = dystans[i - 1][j] + 1
            koszt_wstawienia = dystans[i][j - 1] + 1

            dystans[i][j] = min(koszt_wymiany, koszt_usunięcia, koszt_wstawienia)


            if dystans[i][j] == koszt_wymiany:
                if P[i - 1] != T[j - 1]:
                    rodzice[i][j] = 'S'
                else:
                    rodzice[i][j] = 'M'
            elif dystans[i][j] == koszt_usunięcia:
                rodzice[i][j] = 'D'
            elif dystans[i][j] == koszt_wstawienia:
                rodzice[i][j] = 'I'

    return dystans, rodzice


def odtwarzanie_sciezki(P, T, parent):
    i = len(P)
    j = len(T)
    sciezka = []

    while i > 0 or j > 0:
        if i == 0:
            sciezka.append('I')
            j -= 1
        elif j == 0:
            sciezka.append('D')
            i -= 1
        else:
            operacja = parent[i][j]
            if operacja in ['M', 'S']:
                sciezka.append(operacja)
                i -= 1
                j -= 1
            elif operacja == 'I':
                sciezka.append(operacja)
                j -= 1
            elif operacja == 'D':
                sciezka.append(operacja)
                i -= 1

    return ''.join(sciezka[::-1])


def odtwarzanie_sciezki_to_najdluzsza(P, T, parent):
    i = len(P)
    j = len(T)
    sciezka = []

    while i > 0 or j > 0:
        if i == 0:
            sciezka.append('I')
            j -= 1
        elif j == 0:
            sciezka.append('D')
            i -= 1
        else:
            operacja = parent[i][j]
            if operacja == 'M':
                sciezka.append(P[i - 1]) 
                i -= 1
                j -= 1
            elif operacja == 'D':
                i -= 1
            elif operacja == 'I':
                j -= 1

    return ''.join(sciezka[::-1])


def wyszukaj_podciag(P, T):
    dlugosc_P = len(P)
    dlugosc_T = len(T)
    
    dystans, rodzice = dopasowanie_PD(P, T)
    
    minimalny_koszt = float('inf')
    for j in range(dlugosc_T + 1):
        minimalny_koszt = min(minimalny_koszt, dystans[dlugosc_P][j])

    minimalny_indeks = dystans[dlugosc_P].index(minimalny_koszt)

    sciezka = odtwarzanie_sciezki(P, T, rodzice)

    return minimalny_koszt, minimalny_indeks, sciezka


def najdluzsza_wspolna_sekwencja(P, T):
    dlugosc_P = len(P)
    dlugosc_T = len(T)

    dystans = [[0] * (dlugosc_T + 1) for _ in range(dlugosc_P + 1)]
    rodzice = [['X'] * (dlugosc_T + 1) for _ in range(dlugosc_P + 1)]

    
    for i in range(1, dlugosc_P + 1):
        for j in range(1, dlugosc_T + 1):
            if P[i - 1] == T[j - 1]:
                dystans[i][j] = dystans[i - 1][j - 1] + 1
                rodzice[i][j] = 'M'
            else:
                dystans[i][j] = max(dystans[i - 1][j], dystans[i][j - 1])
                if dystans[i][j] == dystans[i - 1][j]:
                    rodzice[i][j] = 'D'
                elif dystans[i][j] == dystans[i][j - 1]:
                    rodzice[i][j] = 'I'

    wspolna_sekwencja = odtwarzanie_sciezki_to_najdluzsza(P, T, rodzice)

    return wspolna_sekwencja




def najdluzsza_podsekwencja_monotoniczna(T):
    P = ''.join(sorted(T))
    return najdluzsza_wspolna_sekwencja(P, T)



P_1 = ' kot'
T_1 = ' pies'
print(dopasowanie_rekurencyjnie(P_1, T_1, len(P_1), len(T_1)))

P_2 = ' biały autobus'
T_2 = ' czarny autokar'
cost_2, _ = dopasowanie_PD(P_2, T_2)
print(cost_2[len(P_2)][len(T_2)])

P_3 = ' thou shalt not'
T_3 = ' you should not'
cost_3, indeks_min, sciezka_3 = wyszukaj_podciag(P_3, T_3)
print(sciezka_3)

P_4 = "ban"
T_4 = "mokeyssbanana"
minimalny_koszt, minimalny_indeks, sciezka = wyszukaj_podciag(P_4, T_4)
print(minimalny_indeks)


P_5 = ' democrat'
T_5 = ' republican'
result = najdluzsza_wspolna_sekwencja(P_5, T_5)
print(result)

T_6 = '243517698'
monotoniczna_sekwencja = najdluzsza_podsekwencja_monotoniczna(T_6)
print(monotoniczna_sekwencja)