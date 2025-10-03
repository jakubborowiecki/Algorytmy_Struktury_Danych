import polska

class Vertex():
    def __init__(self, key):
        self.key = key
    
    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return self.key
    
    

class AdjacencyMatrix():
    def __init__(self, parametr = 0):
        self.matrix = []
        self.wierzcholki = []
        self.parametr = parametr

    def is_empty(self):
        return len(self.matrix) == 0

    def insert_vertex(self, vertex : Vertex):
        self.wierzcholki.append(vertex)

        if self.is_empty():
            self.matrix.append([self.parametr])
        else:
            for row in self.matrix:
                row.append(self.parametr)
            self.matrix.append([self.parametr for _ in range(len(self.matrix[0]))])




    def insert_edge(self, vertex1 : Vertex, vertex2 : Vertex, edge = 1):
        wierzcholek_id_1 = self.wierzcholki.index(vertex1)
        wierzcholek_id_2 = self.wierzcholki.index(vertex2)

        self.matrix[wierzcholek_id_1][wierzcholek_id_2] = edge
        self.matrix[wierzcholek_id_2][wierzcholek_id_1] = edge

    def delete_vertex(self, vertex : Vertex):
        wierzcholek_id = self.wierzcholki.index(vertex)

        del self.wierzcholki[wierzcholek_id]

        del self.matrix[wierzcholek_id]

        for row in self.matrix:
            del row[wierzcholek_id]



    def delete_edge(self, vertex1 : Vertex, vertex2 : Vertex):
        wierzcholek_id_1 = self.wierzcholki.index(vertex1)
        wierzcholek_id_2 = self.wierzcholki.index(vertex2)

        self.matrix[wierzcholek_id_1][wierzcholek_id_2] = self.parametr
        self.matrix[wierzcholek_id_2][wierzcholek_id_1] = self.parametr


    def neighbours(self, vertex_id):
        for i, edge in enumerate(self.matrix[vertex_id]):
            if edge != self.parametr:
                yield(i, edge)

    
    def vertices(self):
        for i in range(0, len(self.wierzcholki)):
            yield i
    
    def get_vertex(self, vertex_id):
        return self.wierzcholki[vertex_id]
    


class AdjacencyList():
    def __init__(self):
        self.graph = {}
    
    def is_empty(self):
        if len(self.graph) == 0:
            return True
        else:
            return False
        


    def insert_vertex(self, vertex : Vertex):
        self.graph[vertex] = {}

    def insert_edge(self, vertex1 : Vertex, vertex2 : Vertex, edge = None):
        self.graph[vertex1][vertex2] = edge


    def delete_vertex(self, vertex : Vertex):

        for v in self.graph.keys():
            if vertex in self.graph[v]:
                del self.graph[v][vertex]

        del self.graph[vertex]

    def delete_edge(self, vertex1 : Vertex, vertex2 : Vertex):
        del self.graph[vertex1][vertex2]


    def neighbours(self, vertex_id):
        return self.graph[vertex_id].items()
    
    def vertices(self):
        return self.graph.keys()
    
    def get_vertex(self, vertex_id : Vertex):
        return vertex_id

        





test1 = AdjacencyList()
test2 = AdjacencyMatrix()

graf =[('Z','G'), ('Z', 'P'), ('Z', 'F'),
       ('G','Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
       ('N','G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
       ('B','N'), ('B', 'W'), ('B', 'L'), 
       ('F','Z'), ('F', 'P'), ('F', 'D'), 
       ('P','F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P','E'), ('P', 'O'), ('P', 'D'),        
       ('C','P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C','E'),        
       ('E','P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E','S'), ('E', 'O'),        
       ('W','C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W','T'), ('W', 'E'),        
       ('L','W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
       ('D','F'), ('D', 'P'), ('D', 'O'), 
       ('O','D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
       ('S','O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
       ('T','S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T','R'), ('T', 'K'),        
       ('K','S'), ('K', 'T'), ('K', 'R'), 
       ('R','K'), ('R', 'T'), ('R', 'L')]

vertex_list = ['Z', 'G', 'N', 'B', 'F', 'P', 'C', 'E', 'W', 'L', 'D', 'O', 'S', 'T', 'K', 'R']
wierzcholki = [Vertex(key) for key in vertex_list]

vertex_map = {v.key: v for v in wierzcholki}




for v in wierzcholki:
    test1.insert_vertex(v)


for v1, v2 in graf:
    test1.insert_edge(vertex_map[v1], vertex_map[v2])

test1.delete_vertex(vertex_map['K'])

test1.delete_edge(vertex_map['W'], vertex_map['E'])
test1.delete_edge(vertex_map['E'], vertex_map['W'])

polska.draw_map(test1)



# for v in wierzcholki:
#     test2.insert_vertex(v)


# for v1, v2 in graf:
#     test2.insert_edge(vertex_map[v1], vertex_map[v2])

# test2.delete_vertex(vertex_map['K'])

# test2.delete_edge(vertex_map['W'], vertex_map['E'])
# test2.delete_edge(vertex_map['E'], vertex_map['W'])

# polska.draw_map(test2)