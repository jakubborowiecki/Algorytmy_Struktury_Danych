class Element:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    
class List:
    def __init__(self):
        self.head = None


    def destroy(self):
        if self.is_empty():
            print("Lista jest pusta")
        else:
            self.head = None

    def add(self, input):

        temp = self.head
        self.head = Element(input, temp)


    def append(self, input):
        new_elem = Element(input)
        
        if self.head is None:
            self.head = new_elem
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_elem


    def remove(self):
        if self.is_empty():
            print("Nie mozna usunac elementu. Lista jest pusta")
        else:
            self.head = self.head.next
            


    def remove_end(self):
        if self.is_empty():
            print("Nie mozna usunac elementu. Lista jest pusta")
        else:
            temp = self.head
            for _ in range (self.length()-2):
                temp = temp.next
            temp.next = None



    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


    def length(self):
        if self.is_empty():
            return 0
        elif self.head is not None and self.head.next is None:
            return 1
        else:
            counter = 1
            temp = self.head

            while temp.next:
                counter += 1
                temp = temp.next
            return counter

        

    def get(self):
        if self.is_empty():
            return None
        else:
            return  self.head.data

    def print(self):
        if self.is_empty():
            print("Brak listy")
        temp = self.head
        while temp:  
            print("->", temp.data, end=" ")
            temp = temp.next
        print()



dane_uczelnie = [('AGH', 'Kraków', 1919),
             ('UJ', 'Kraków', 1364),
             ('PW', 'Warszawa', 1915),
             ('UW', 'Warszawa', 1915),
             ('UP', 'Poznań', 1919),
             ('PG', 'Gdańsk', 1945)]


uczelnie = List()


for i in range(3):
    uczelnie.append(dane_uczelnie[i])

for i in range(3):
    uczelnie.add(dane_uczelnie[i+3])

uczelnie.print()
print(uczelnie.length())
uczelnie.remove()
print(uczelnie.get())
uczelnie.remove_end()
uczelnie.print()
uczelnie.destroy()
print(uczelnie.is_empty())
uczelnie.remove()
uczelnie.remove_end()
uczelnie.append(dane_uczelnie[0])
uczelnie.remove_end()
print(uczelnie.is_empty())