class ChildNode():
    def __init__(self, key, value, left_side = None, right_side = None):
        self.key = key
        self.value = value
        self.left_side = left_side
        self.right_side = right_side
    


class RootNode():
    def __init__(self, root = None):
        self.root = root


    def height(self, node = None):
        if node == None and self.root != None:
            node = self.root
        if node == None:
            return 0
        
        if node.left_side == None and node.right_side == None:
            return 1
        
        left_height = self.height(node.left_side)
        right_height = self.height(node.right_side)

        if left_height > right_height:
            return 1 + left_height
        else:
            return 1 + right_height



    def __search(self, node: ChildNode, key):
        if node == None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.__search(node.left_side, key)
        elif key > node.key:
            return self.__search(node.right_side, key)
        


    def search(self, key):
        if self.root == None:
            return None
        else:
            return self.__search(self.root, key)



    def __insert(self, node : ChildNode, key, value):
        if key < node.key:
            if node.left_side == None:
                nowa_galaz = ChildNode(key, value)
                node.left_side = nowa_galaz
            else:
                self.__insert(node.left_side, key, value)
        
        elif key > node.key:
            if node.right_side == None:
                nowa_galaz = ChildNode(key, value)
                node.right_side = nowa_galaz
            else:
                self.__insert(node.right_side, key, value)
        else:
            node.value = value


    def insert(self, key, value):
        if self.root == None:
            nowy_korzen = ChildNode(key, value)
            self.root = nowy_korzen
        else:
            self.__insert(self.root, key, value)


    def __delete(self, node: ChildNode, key):
        if node == None:
            return None

        if key == node.key:
            if node.left_side == None and node.right_side == None:
                return None


            elif node.left_side == None and node.right_side != None:
                node = node.right_side
                node.left_side = None
                return node
                
            elif node.left_side != None and node.right_side == None:
                node = node.left_side
                node.right_side = None
                return node

            elif node.left_side != None and node.right_side != None:
                najmniejszy_z_prawego_poddrzewa = self.pierwszy_node_ktory_nie_ma_lewego_dziecka(node.right_side)

                node.key = najmniejszy_z_prawego_poddrzewa.key
                node.value = najmniejszy_z_prawego_poddrzewa.value

                node.right_side = self.__delete(node.right_side, najmniejszy_z_prawego_poddrzewa.key)
                return node

        elif key < node.key:
            node.left_side = self.__delete(node.left_side, key)
        elif key > node.key:
            node.right_side = self.__delete(node.right_side, key)
        
    def pierwszy_node_ktory_nie_ma_lewego_dziecka(self, node : ChildNode):
        if node.left_side == None:
            return node
        else:
            return self.pierwszy_node_ktory_nie_ma_lewego_dziecka(node.left_side)


    def delete(self, key):
        if self.root == None:
            return None
        else:
            self.root = self.__delete(self.root, key)
    

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node : ChildNode, lvl):
        if node!=None:
            self.__print_tree(node.right_side, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left_side, lvl+5)


    def __print_list_elements(self, node : ChildNode):
        if node == None:
            return ''
        string = ''
        if node.left_side != None:
            left = self.__print_list_elements(node.left_side)
        else:
            left = ''

        mid = f"{node.key}:'{node.value}',"
    
        if node.right_side != None:
            right = self.__print_list_elements(node.right_side)
        else:
            right = ''

        string = left + mid + right
        return string
        

    def print_list_elements(self):
        if self.root == None:
            return None
        else:
            return self.__print_list_elements(self.root)

BST = RootNode()

keys = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

for i in range(len(keys)):
    BST.insert(keys[i], values[i])




BST.print_tree()
print(BST.print_list_elements())

print(BST.search(24))
BST.insert(24, 'AA')
BST.insert(6, 'M')
BST.delete(62)
BST.insert(59, 'N')
BST.insert(100, 'P')
BST.delete(8)
BST.delete(15)
BST.insert(55, 'R')
BST.delete(50)
BST.delete(5)
BST.delete(24)
print(BST.height())
print(BST.print_list_elements())
BST.print_tree()