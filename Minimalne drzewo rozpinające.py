
graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]

class Vertex():
    def __init__(self, key, color = None):
        self.key = key
        self.color = color
    
    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return False
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




    def insert_edge(self, vertex1 : Vertex, vertex2 : Vertex, edge):
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


def primo(graph : AdjacencyList):
    graf_mst = AdjacencyList()

    intree = {}
    distance = {}
    parent = {}


    for v in graph.vertices():
        intree[v] = False
        distance[v] = float('inf')
        parent[v] = None


    for v in graph.vertices():
        v_start = v
        break

    distance[v_start] = 0

    while True:
        
        total_distance = 0
        v_potencial = None
        minimal_distance = float('inf')

        for neighbour in graph.vertices():
            if not intree[neighbour] and distance[neighbour] < minimal_distance:
                v_potencial = neighbour
                minimal_distance = distance[neighbour]

        if v_potencial == None:
            break

        v = v_potencial

        intree[v] = True
        graf_mst.insert_vertex(v)

        if parent[v] != None:
            graf_mst.insert_edge(v, parent[v], distance[v])
            graf_mst.insert_edge(parent[v], v, distance[v])
            total_distance += distance[v]

        
        for neighbour, edge in graph.neighbours(v):
            if not intree[neighbour] and edge < distance[neighbour]:
                distance[neighbour] = edge
                parent[neighbour] = v
    
    return graf_mst

graph = AdjacencyList()
vertexes = {}

for v1, v2, edge in graf:
    if v1 not in vertexes:
        vertexes[v1] = Vertex(v1)
        graph.insert_vertex(vertexes[v1])
    
    if v2 not in vertexes:
        vertexes[v2] = Vertex(v2)
        graph.insert_vertex(vertexes[v2])
    
    graph.insert_edge(vertexes[v1], vertexes[v2], edge)
    graph.insert_edge(vertexes[v2], vertexes[v1], edge)

primo_ = primo(graph)


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

printGraph(primo_)
