from typing import Union 

class Table():
    def __init__(self, size: int, c1 = 1, c2 = 0):
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2


    def mix(self, data : Union[int, str]): #dajesz klucz, a klucz zamienia na index tablicy i wstawia element
        pass
        #obliczającą modulo rozmiaru tablicy

    def solve_colision(self): #metoda adresowania otwartego
        pass

    def search(self):
        pass

    def insert(self, data):
        try:
            pass
        except ValueError:
            print("Brak miejsca")


    def remove(self, key):
        try:
            pass

        except ValueError:
            print("Brak danej")


    def __str__(self):
        pass

    

#Elementy tablicy również powinny być zaimplementowane jako klasa z dwoma atrybutami przechowującymi: klucz oraz  wartość (jakąś daną).
#Ponadto napisz metodę __str__(self) zwracającą napis przedstawiający  element w postaci klucz:wartość

class element_Table():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        string = str(self.key) + ":" + str(self.value)
        return string





ok = element_Table(2, 5)
print(ok)