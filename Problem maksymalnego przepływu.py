from collections import deque

class Vertex():
    def __init__(self, key, source = False, sink = False):
        self.key = key
        self.source = source
        self.sink = sink

    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self):
        return self.key
    
class Edge():
    def __init__(self, capacity, flag):
        self.capacity = capacity
        self.actual_flow = 0
        
        self.flag = flag
        if flag == False:
            self.capacity_rest = capacity
        elif flag == True:
            self.capacity_rest = 0
    
    def __repr__(self):
        result_string = str(self.capacity) +  " " + str(self.actual_flow) + " " + str(self.capacity_rest) + " " + str(self.flag)
        return result_string



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

    def insert_edge(self, vertex1 : Vertex, vertex2 : Vertex, edge_value = None):
        self.graph[vertex1][vertex2] = Edge(edge_value, False)
        self.graph[vertex2][vertex1] = Edge(0, True)


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
    
    def get_vertex(self, vertex_id):
        for vertex in self.graph:
            if vertex.key == vertex_id:
                return vertex
        return None


    def get_edge(self, vertex1_id, vertex2_id):
        return self.graph[vertex1_id][vertex2_id]
    
def algorytm_bfs(graph: AdjacencyList, vertex_start: Vertex, vertex_end: Vertex, parent: dict):
    visited = set()
    queue = deque()


    queue.append(vertex_start)
    visited.add(vertex_start)

    while queue:
        current_vertex = queue.popleft()

        if current_vertex == vertex_end:
            return parent

        for neig in graph.graph[current_vertex]:
            krawedz = graph.get_edge(current_vertex, neig)
            if neig not in visited and krawedz.capacity_rest > 0:
                queue.append(neig)
                visited.add(neig)
                parent[neig] = current_vertex

                
    return None

def analiza_sciezki(graph : AdjacencyList, vertex_start : Vertex, vertex_end : Vertex, parent : dict):
    if vertex_end not in parent:
        return None
    
    smallest_capacity = float('inf')

    current_vertex = vertex_end


    sciezka = []

    while current_vertex != vertex_start:
        sciezka.append(current_vertex)
        aktualna_krawedz = graph.get_edge(parent[current_vertex], current_vertex)
        wartosc_krawedzi = aktualna_krawedz.capacity_rest
        if wartosc_krawedzi < smallest_capacity:
            smallest_capacity = wartosc_krawedzi
        current_vertex = parent[current_vertex]


    sciezka.append(vertex_start)
    sciezka.reverse()
    return smallest_capacity


def augmentacja_sciezki(graph : AdjacencyList, vertex_start : Vertex, vertex_end : Vertex, parent : dict, smallest_capacity : float):
    if vertex_end not in parent:
        return None

    current_vertex = vertex_end
    while current_vertex != vertex_start:
        ex_vertex = parent[current_vertex]
        next_edge = graph.get_edge(ex_vertex, current_vertex)
        ex_edge = graph.get_edge(current_vertex, ex_vertex)

        next_edge.capacity_rest -= smallest_capacity
        ex_edge.capacity_rest += smallest_capacity

        if not next_edge.flag:
            next_edge.actual_flow += smallest_capacity
        else:
            ex_edge.actual_flow -= smallest_capacity

        current_vertex = ex_vertex

    return graph



def algorytm_forda_fulkersona(graph : AdjacencyList, vertex_start : Vertex, vertex_end = Vertex):
    parent = {}
    przeplyw_calkowity = 0

    while algorytm_bfs(graph, vertex_start, vertex_end, parent):
        smallest_capacity = float("inf")
        current_vertex = vertex_end

        while current_vertex != vertex_start:
            krawedz = graph.get_edge(parent[current_vertex], current_vertex)
            smallest_capacity = min(krawedz.capacity_rest, smallest_capacity)
            current_vertex = parent[current_vertex]
        

        augmentacja_sciezki(graph, vertex_start, vertex_end, parent, smallest_capacity)
        przeplyw_calkowity += smallest_capacity

    return przeplyw_calkowity


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]



def create_graph(graph, vertex_to_start_key): 
    test = AdjacencyList()

    for ver1, ver2, value in graph:
        if Vertex(ver1) not in test.graph:
            test.insert_vertex(Vertex(ver1))
        if Vertex(ver2) not in test.graph:
            test.insert_vertex(Vertex(ver2))

    for ver1, ver2, value in graph:
        test.insert_edge(test.get_vertex(ver1), test.get_vertex(ver2), value)

    max_flow = algorytm_forda_fulkersona(test, test.get_vertex('s'), test.get_vertex('t'))

    rzeczywisty_przeplyw = 0
    vertex_to_start = test.get_vertex(vertex_to_start_key)

    for neighbour, edge in test.neighbours(vertex_to_start):
        if edge.flag == False:
            rzeczywisty_przeplyw += edge.actual_flow

    print(max_flow)
    printGraph(test)
    print(rzeczywisty_przeplyw)

create_graph(graf_0, 'u')
create_graph(graf_1, 'a')
create_graph(graf_2, 'a')
create_graph(graf_3, 'a')






