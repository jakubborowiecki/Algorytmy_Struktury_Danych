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
    def __init__(self):
        self.tab = []
        self.kopiec_size = 0
        
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

        self.__upheap(self.kopiec_size )
        
  

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
            



test = Kolejka()

prioritets = [7, 5, 1, 2, 5, 3, 4, 8, 9]
string = "GRYMOTYLA"

for i in range(len(prioritets)):
    test.enqueue(Element(string[i], prioritets[i]))


test.print_tree(0, 0)
test.print_tab()
odczyt = test.dequeue()

print(test.peek())
test.print_tab()
print(odczyt)

while test.is_empty() is not True:
    print(test.dequeue())

test.print_tab()