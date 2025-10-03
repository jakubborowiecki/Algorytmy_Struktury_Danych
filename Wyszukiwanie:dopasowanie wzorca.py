import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()

def metoda_naiwna(text : str, wzorzec : str):
    dlugosc_text = len(text)
    dlugosc_wzorzec = len(wzorzec)

    m = 0

    wzorzec_counter = 0
    liczba_opracji_counter = 0

    while m <= dlugosc_text - dlugosc_wzorzec:
        i = 0
        while i < dlugosc_wzorzec:
            liczba_opracji_counter += 1
            if text[m+i] == wzorzec[i]:
                i += 1
            else:
                break
        
        if i == dlugosc_wzorzec:
            wzorzec_counter += 1

        m += 1                 
 
    return wzorzec_counter, liczba_opracji_counter

def hash(word):
    d = 256
    q = 101
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw


def rabin_karp_normal_hash(string, wzorzec):

    dlugosc_text = len(string)
    dlugosc_wzorzec = len(wzorzec)

    wzorzec_counter = 0
    porownanie_wzorzec = 0



    h_wzorca = hash(wzorzec)

    kolizja = 0 

    m = 0
    while m <= dlugosc_text-dlugosc_wzorzec:
        h_stringu = hash(string[m: m+dlugosc_wzorzec])
        porownanie_wzorzec += 1

        if h_stringu == h_wzorca:
            if string[m : m + dlugosc_wzorzec] == wzorzec:
                wzorzec_counter += 1
            else:
                kolizja += 1


        m += 1
    return wzorzec_counter, porownanie_wzorzec, kolizja

def rabin_karp_rolling_hash(string, wzorzec):

    dlugosc_text = len(string)
    dlugosc_wzorzec = len(wzorzec)

    wzorzec_counter = 0
    porownanie_wzorzec = 0



    h_wzorca = hash(wzorzec)

    
    d = 256
    q = 101
    m = 0
    h = 1

    h = 1
    for i in range(dlugosc_wzorzec - 1):
        h = (h * d) % q


        
    kolizja = 0 
    h_stringu = hash(string[m: m+dlugosc_wzorzec])


    while m <= dlugosc_text-dlugosc_wzorzec:

        porownanie_wzorzec += 1

        if h_stringu == h_wzorca:
            if string[m : m + dlugosc_wzorzec] == wzorzec:
                wzorzec_counter += 1
            else:
                kolizja += 1
    
        if m + dlugosc_wzorzec < dlugosc_text:
            h_stringu = (d * (h_stringu - ord(string[m]) * h) + ord(string[m + dlugosc_wzorzec])) % q

        if h_stringu < 0:
            h_stringu += q

        m += 1
    return wzorzec_counter, porownanie_wzorzec, kolizja


def algorithm_kmp_table(wzorzec):

    pos = 1
    cnd = 0

    dlugosc_wzorzec = len(wzorzec)

    T = dlugosc_wzorzec * [-1]

    while pos < dlugosc_wzorzec:
        if wzorzec[pos] == wzorzec[cnd]:
            T[pos] = cnd
            pos += 1
            cnd += 1
        else:
            while cnd > 0 and wzorzec[pos] != wzorzec[cnd]:
                cnd = T[cnd - 1]
            if wzorzec[pos] == wzorzec[cnd]:
                T[pos] = cnd
                pos += 1
                cnd += 1
            else:
                T[pos] = 0
                pos += 1
    return T

def kmp_search_algorithm(string, wzorzec):
    m = 0
    i = 0
    T = algorithm_kmp_table(wzorzec)
    nP = 0
    P = []

    liczba_porownan = 0

    while m < len(string):
        liczba_porownan += 1

        if wzorzec[i] == string[m]:
            m += 1
            i += 1


            if i == len(wzorzec):
                P.append(m - i)
                nP += 1
                i = T[i - 1]
        else:
            i = T[i]
            if i <0:
                m = m + 1
                i = i + 1
    P = len(P)
    return P, liczba_porownan


t_start_1 = time.perf_counter()
liczba_powt_1, liczba_porownan_1 = metoda_naiwna(S, 'time.')
t_stop_1 = time.perf_counter()
t_total_1 = t_stop_1 - t_start_1
print(f"{liczba_powt_1}; {liczba_porownan_1}; {t_total_1}")


t_start_2 = time.perf_counter()
liczba_powt_2, liczba_porownan_2, liczba_kolizji_2 = rabin_karp_normal_hash(S, 'time.')
t_stop_2 = time.perf_counter()
t_total_2 = t_stop_2 - t_start_2

print(f"{liczba_powt_2}; {liczba_porownan_2}; {liczba_kolizji_2}; {t_total_2}")

t_start_3 = time.perf_counter()
liczba_powt_3, liczba_porownan_3, liczba_kolizji_3 = rabin_karp_rolling_hash(S, 'time.')
t_stop_3 = time.perf_counter()
t_total_3 = t_stop_3 - t_start_3

print(f"{liczba_powt_3}; {liczba_porownan_3}; {liczba_kolizji_3}; {t_total_3}")

t_start_4 = time.perf_counter()
liczba_powt_4, liczba_porownan_4 = kmp_search_algorithm(S, 'time.')
t_stop_4 = time.perf_counter()
t_total_4 = t_stop_4 - t_start_4
print(f"{liczba_powt_4}; {liczba_porownan_4}; {t_total_4}")
