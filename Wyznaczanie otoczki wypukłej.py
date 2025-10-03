class Point():
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
       return isinstance(other, Point) and self.x == other.x and self.y == other.y


def left_right(p: Point, q: Point, r: Point):
    value = (q.x - p.x)*(r.y - p.y) - (q.y - p.y)*(r.x - p.x)
    if value > 0:
        return 'left'
    elif value < 0:
        return 'right'
    else:
        return 'line'

def pierwszy_punkt(data):
    minimalny_punkt = data[0]
    for elem in data:
        if elem.x < minimalny_punkt.x or (elem.x == minimalny_punkt.x and elem.y < minimalny_punkt.y):
            minimalny_punkt = elem
    return minimalny_punkt

def kwadrat_odleglsci(point_1: Point, point_2: Point):
    return (point_1.x - point_2.x)**2 + (point_1.y - point_2.y)**2

def jarvis_algorithm_v1(data):
    first_point = pierwszy_punkt(data)

    ciag_punktow = []
    ciag_punktow.append(first_point)

    p = first_point
    while True:
        it = iter(data)
        _ = next(it)
        q = next(it)

        if q == p:
            q = next(it)

        for r in data:
            if r == p:
                continue
            if left_right(p, q, r) == 'right':
                q = r

        if q == first_point:
            break
        ciag_punktow.append(q)
        p = q

    return ciag_punktow

def jarvis_algorithm_v2(data):
    first_point = pierwszy_punkt(data)

    ciag_punktow = []
    ciag_punktow.append(first_point)

    p = first_point
    while True:
        it = iter(data)
        _ = next(it)
        q = next(it)

        if q == p:
            q = next(it)

        for r in data:
            if r == p:
                continue

            kierunek = left_right(p, q, r)

            if kierunek == 'right':
                q = r
            elif kierunek == 'line' and kwadrat_odleglsci(p, r) > kwadrat_odleglsci(p, q):
                q = r

        if q == first_point:
            break
        ciag_punktow.append(q)
        p = q

    return ciag_punktow

data_set = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
list_points = []
for elem in data_set:
    list_points.append(Point(elem[0], elem[1]))



print(jarvis_algorithm_v1(list_points))
print(jarvis_algorithm_v2(list_points))

