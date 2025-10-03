class Kolejka():

    def __init__(self):
        self.size = 5
        self.tab = [None for i in range(self.size)] 
        self.index_zapisu = 0
        self.index_odczytu = 0


    def is_empty(self):
        if self.index_odczytu == self.index_zapisu:
            return True
        
        return False
    
    def queue_tab(self):
        return self.tab
    
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.index_odczytu]
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        if self.index_odczytu == self.size-1:
            self.index_odczytu = 0
        
        first_element = self.tab[self.index_odczytu]
        self.tab[self.index_odczytu] = None


        
        self.index_odczytu += 1

        
        return first_element
    
    def enqueue(self, data):
        self.tab[self.index_zapisu] = data
        self.index_zapisu += 1

        if self.index_zapisu == self.size:
            self.index_zapisu = 0


        if self.index_zapisu == self.index_odczytu:
            stary_rozmiar = self.size
            self.size *= 2

            counter = 0

            elementy_do_przeniesienia = self.tab[self.index_odczytu:self.size]

            for i in range(self.index_odczytu, stary_rozmiar):
                self.tab[i] = None

                counter += 1
            
            self.tab[self.size-counter : self.size-1] = elementy_do_przeniesienia
            
            self.index_odczytu = self.size-counter-1


    def __str__(self):
        poczotkowy_index_oczytu = self.index_odczytu
        string = "[ "
        for _ in range(self.size):
            if self.index_odczytu == self.size-1:
                self.index_odczytu = 0
            if self.peek() != None:
                string = string + str(self.peek()) + " "
                self.index_odczytu += 1
        string += "]"
        self.index_odczytu = poczotkowy_index_oczytu
        return string


test = Kolejka()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
test.enqueue(4)

print(test.dequeue())
print(test.peek())


print(test.queue_tab())

print()

test.enqueue(5)
test.enqueue(6)
test.enqueue(7)
test.enqueue(8)

print(test.queue_tab())


for _ in range(test.size):
    ok = test.dequeue()
    if ok is not None:
        print(ok)  

print(test)