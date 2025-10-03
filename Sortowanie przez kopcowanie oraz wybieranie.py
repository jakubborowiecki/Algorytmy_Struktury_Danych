import random
import time

class Element():
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet
        
    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __repr__(self):
        return f"{self.__priorytet}:{self.__dane}"
    

class Kolejka():
    def __init__(self, table_to_sort = None):

        if table_to_sort == None:
            self.tab = []
            self.kopiec_size = 0
        else:
            self.tab = table_to_sort
            self.kopiec_size = len(table_to_sort)
            for i in range(self.kopiec_size//2 - 1, -1, -1):
                self.__downheap(i)
        
    def list_size(self):
        return len(self.tab)

    def is_empty(self):
        return self.kopiec_size == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]
        

    def left_child(self, index : int):
        return index*2+1
    

    def right_child(self, index : int):
        return (index*2) + 2
    

    def parent(self, index : int):
        return (index-1)//2


    def enqueue(self, obiekt : Element):
        if self.list_size() == self.kopiec_size:
            self.tab.append(obiekt)
        else:
            self.tab[self.kopiec_size] = obiekt

        self.kopiec_size += 1

        self.__upheap(self.kopiec_size)
        
  

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            zwrot = self.tab[0]
            self.tab[0], self.tab[self.kopiec_size - 1] = self.tab[self.kopiec_size - 1], self.tab[0]
            
            self.kopiec_size -= 1
            self.__downheap(0)
            return zwrot
            


    def __upheap(self, index : int):
        index = index - 1
        value = self.tab[index]
        parent_index = self.parent(index)

        while (parent_index >= 0 and self.tab[parent_index] < value):
            
            self.tab[index], self.tab[parent_index] = self.tab[parent_index], self.tab[index]


            index = parent_index
            parent_index = self.parent(index)

    def __downheap(self, index: int):
        while True:
            left_child = self.left_child(index)
            right_child = self.right_child(index)
            
            bigger_child = index
            
            if left_child < self.kopiec_size and self.tab[left_child] > self.tab[bigger_child]:
                bigger_child = left_child
            
            if right_child < self.kopiec_size and self.tab[right_child] > self.tab[bigger_child]:
                bigger_child = right_child
            
            if bigger_child != index:
                self.tab[index], self.tab[bigger_child] = self.tab[bigger_child], self.tab[index]
                index = bigger_child
            else:
                break



    def print_tab(self):
        print('{', end='')
        print(*self.tab[:self.kopiec_size], sep=',', end='')
        print('}')

    def print_tree(self, index, level):
        if index < self.kopiec_size:
            self.print_tree(self.right_child(index), level + 1)
            print(2 * level * '  ', self.tab[index] if self.tab[index] else None)
            self.print_tree(self.left_child(index), level + 1)
            
    def sort_kopcowanie(self):
        for i in range(self.kopiec_size):
            index = i

            for j in range(i + 1, self.kopiec_size):
                if self.tab[j] > self.tab[index]:
                    index = j

            self.tab[i], self.tab[index] = self.tab[index], self.tab[i]



        
    def sort_swap(self):
        for i in range(1, len(self.tab)):
            key = self.tab[i]
            j = i -1

            while j >= 0 and self.tab[j] > key:
                self.tab[j+1] = self.tab[j]
                j -= 1
            self.tab[j + 1] = key

    def sort_shift(self):
        for i in range(1, len(self.tab)):
            key = self.tab.pop(i)

            j = i - 1
            while j >= 0 and self.tab[j] > key:
                j -= 1
            self.tab.insert(j+1, key)
        

def sort_swap_function(tab):
    for i in range(1, len(tab)):
        key = tab[i]
        j = i -1

        while j >= 0 and tab[j] > key:
            tab[j+1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab

def sort_shift_function(tab):
    for i in range(1, len(tab)):
        key = tab.pop(i)

        j = i - 1
        while j >= 0 and tab[j] > key:
            j -= 1
        tab.insert(j+1, key)
    return tab







def test_1():
    tablica_elemow1 = [Element(value, key) for key, value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    test_1 = Kolejka(tablica_elemow1)

    test_1.print_tab()
    test_1.print_tree(0, 0)

    test_1.sort_kopcowanie()
    test_1.print_tab()

    print("NIESTABILNY")

    tablica_elemow2 = [Element(value, key) for key, value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    test_2 = Kolejka(tablica_elemow2)

    test_2.print_tab()
    test_2.sort_swap()
    test_2.print_tab()
    print("STABILNY")

    tablica_elemow3 = [Element(value, key) for key, value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    test_3 = Kolejka(tablica_elemow3)

    test_3.print_tab()
    test_3.sort_shift()
    test_3.print_tab()
    print("STABILNY")




def test_2():
    t_start = time.perf_counter()
    
    tab = []
    for _ in range(10000):
        tab.append(int(random.random() * 100))

    tab_kopia_1 = list(tab)
    tab_kopia_2 = list(tab)
    kopiec = Kolejka(tab)
    kopiec.sort_kopcowanie()
    t_stop = time.perf_counter()
    total_time = t_stop - t_start

    print(total_time)






    t_start = time.perf_counter()

    sort_swap_function(tab_kopia_1)
    t_stop = time.perf_counter()
    total_time = t_stop - t_start

    print(total_time)



    t_start = time.perf_counter()
    
    sort_shift_function(tab_kopia_2)
    t_stop = time.perf_counter()
    total_time = t_stop - t_start

    print(total_time)
    


number = int(input("Podaj liczbe: "))

if number == 1:
    test_1()
elif number == 2:
    test_2()