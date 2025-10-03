from copy import deepcopy


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
    
    def get_vertex_by_key(self, key):
        for v in self.wierzcholki:
            if v.key == key:
                return v
        return None

    def size(self):
        row = len(self.matrix)
        col = len(self.matrix[0]) if self.matrix else 0

        return row, col
    

    def __eq__(self, other):
        if self.size() == other.size():
            row = self.size()[0]
            col = self.size()[1]

            for i in range (row):
                for j in range (col):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            
            return True
        else:
            return False
        
    def __str__(self):
        result = ""
        for i in range(self.size()[0]):
            result += "| " + " ".join(map(str, self.matrix[i])) + " |\n"
        return result.strip()
    
    def __getitem__(self, index):
        return self.matrix[index]

    def __add__(self, other):

        if self.size() == other.size():

            result = []
            for i in range(self.size()[0]):
                row = []
                for j in range(self.size()[1]):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)

            new_adj_matrix = AdjacencyMatrix(self.parametr)
            new_adj_matrix.matrix = result
            new_adj_matrix.wierzcholki = self.wierzcholki.copy()

            return new_adj_matrix
        else:
            return "Wymiary macierzy nie są poprawne"

    
    def __mul__(self, other):
        
        if self.size()[1] == other.size()[0]:
            result = []
            for i in range(self.size()[0]):
                row = []
                for j in range(other.size()[1]):
                    suma_komorki = 0
                    for k in range (self.size()[1]):
                        suma_komorki += self[i][k] * other[k][j]

                    row.append(suma_komorki)
                result.append(row)

            new_adj_matrix = AdjacencyMatrix(self.parametr)
            new_adj_matrix.matrix = result
            new_adj_matrix.wierzcholki = self.wierzcholki.copy()

            return new_adj_matrix
        else:
            return "Wymiary macierzy nie są poprawne"
        
    def transponse_matrix(self):
        row = self.size()[0]
        col = self.size()[1]
        result = []

        for i in range (col):
            new_row  = []
            for j in range(row):
                new_row.append(self.matrix[j][i])
            result.append(new_row)

        new_adj_matrix = AdjacencyMatrix(self.parametr)
        new_adj_matrix.matrix = result
        new_adj_matrix.wierzcholki = self.wierzcholki.copy()
        
        return new_adj_matrix
    
graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

def build_graph(graph):
    graf = AdjacencyMatrix()

    for x,y,z in graph:
        if graf.get_vertex_by_key(x) is None:
            graf.insert_vertex(Vertex(x))
        if graf.get_vertex_by_key(y) is None:
            graf.insert_vertex(Vertex(y))


    for x,y,z in graph:
        graf.insert_edge(graf.get_vertex_by_key(x), graf.get_vertex_by_key(y), z)


    return graf

def build_matrix_m0(graf_p : AdjacencyMatrix, graf_g :AdjacencyMatrix):
    matrix_m0 = AdjacencyMatrix()

    for i in range(graf_p.size()[0]):
        row = []
        liczba_sasiadow_p = sum(graf_p[i])

        for j in range(graf_g.size()[0]):  
            liczba_sasiadow_g = sum(graf_g[j])

            if liczba_sasiadow_p <= liczba_sasiadow_g:
                row.append(1)
            else:
                row.append(0)

  
        matrix_m0.matrix.append(row)
    return matrix_m0


def prune(matrix_m0 : AdjacencyMatrix, graf_p : AdjacencyMatrix, graf_g : AdjacencyMatrix):
    zmiana = True

    while zmiana:
        zmiana = False
        for i in range(matrix_m0.size()[0]):
            for j in range(matrix_m0.size()[1]):
                if matrix_m0.matrix[i][j] == 1:
                    for x, _ in graf_p.neighbours(i):
                        found = False

                        for y, _ in graf_g.neighbours(j):
                            if matrix_m0.matrix[x][y] == 1:
                                found = True
                                break
                                
                        if found == False:
                            matrix_m0.matrix[i][j] = 0
                            zmiana = True
                            break




def algorytm_ullmana_version_1(matrix_M: AdjacencyMatrix, graf_p: AdjacencyMatrix, graf_g: AdjacencyMatrix, used: list, current_row: int, counter: int, founded_isomorphism: list):
    counter += 1
    if current_row == matrix_M.size()[0]:
        result_matrix = matrix_M * graf_g * matrix_M.transponse_matrix()
        if result_matrix == graf_p:
            founded_isomorphism.append(deepcopy(matrix_M))
        return len(founded_isomorphism), counter

    for column in range(matrix_M.size()[1]):
        if not used[column]:
            used[column] = True

            for i in range(matrix_M.size()[1]):
                matrix_M[current_row][i] = 0

            matrix_M[current_row][column] = 1


            _, counter = algorytm_ullmana_version_1(matrix_M, graf_p, graf_g, used, current_row + 1, counter, founded_isomorphism)

            used[column] = False

    return len(founded_isomorphism), counter



def algorytm_ullmana_version_2(matrix_M: AdjacencyMatrix, graf_p: AdjacencyMatrix, graf_g: AdjacencyMatrix, used: list, current_row: int, counter: int, founded_isomorphism: list):
    counter += 1
    if current_row == matrix_M.size()[0]:
        result_matrix = matrix_M * graf_g * matrix_M.transponse_matrix()

        if result_matrix == graf_p:
            founded_isomorphism.append(deepcopy(matrix_M))
        return len(founded_isomorphism), counter

    for column in range(matrix_M.size()[1]):
        if not used[column] and matrix_M[current_row][column] == 1:
            used[column] = True

            kopia_matrix_m = deepcopy(matrix_M)

            for i in range(kopia_matrix_m.size()[1]):
                kopia_matrix_m[current_row][i] = 0

            kopia_matrix_m[current_row][column] = 1


            _, counter = algorytm_ullmana_version_2(
                kopia_matrix_m, graf_p, graf_g, used, current_row + 1, counter, founded_isomorphism)
            used[column] = False

    return len(founded_isomorphism), counter



def algorytm_ullmana_version_3(matrix_M: AdjacencyMatrix, graf_p: AdjacencyMatrix, graf_g: AdjacencyMatrix, used: list, current_row: int, counter: int, founded_isomorphism: list):
    counter += 1
    if current_row == matrix_M.size()[0]:
        result_matrix = matrix_M * graf_g * matrix_M.transponse_matrix()
        if result_matrix == graf_p:
            founded_isomorphism.append(deepcopy(matrix_M))
        return len(founded_isomorphism), counter

    for column in range(matrix_M.size()[1]):
        if not used[column] and matrix_M[current_row][column] == 1:
            nowe_used = used.copy()
            nowe_used[column] = True

            kopia_matrix_m = deepcopy(matrix_M)

            for i in range(kopia_matrix_m.size()[1]):
                kopia_matrix_m[current_row][i] = 0
            kopia_matrix_m[current_row][column] = 1

            prune(kopia_matrix_m, graf_p, graf_g)

            _, returned_counter = algorytm_ullmana_version_3(
                kopia_matrix_m, graf_p, graf_g, nowe_used, current_row + 1, 0, founded_isomorphism)
            counter += returned_counter

    return len(founded_isomorphism), counter

graf_p_ = build_graph(graph_P)
graf_g_ = build_graph(graph_G)

def create_empty_M(rows, cols):
    M = AdjacencyMatrix(0)
    M.wierzcholki = [Vertex(str(i)) for i in range(rows)]
    M.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    return M




graf_m_v1 = build_matrix_m0(graf_p_, graf_g_)
used_v1 = [False] * graf_m_v1.size()[1]
founded_isomorphism_v1 = []
counter_v1 = 0
print(algorytm_ullmana_version_1(graf_m_v1, graf_p_, graf_g_, used_v1, 0, counter_v1, founded_isomorphism_v1))



graf_m0_v2 = build_matrix_m0(graf_p_, graf_g_)
used_v2 = [False] * graf_m0_v2.size()[1]
founded_isomorphism_v2 = []
counter_v2 = 0
print(algorytm_ullmana_version_2(graf_m0_v2, graf_p_, graf_g_, used_v2, 0, counter_v2, founded_isomorphism_v2))




graf_m0_v3 = build_matrix_m0(graf_p_, graf_g_)
used_v3 = [False] * graf_m0_v3.size()[1]
founded_isomorphism_v3 = []
counter_v3 = 0
print(algorytm_ullmana_version_3(graf_m0_v3, graf_p_, graf_g_, used_v3, 0, counter_v3, founded_isomorphism_v3))