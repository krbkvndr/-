
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length(self) -> float:
        # длинна вектора
        return ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)**0.5

    def __add__(self, other):
        # сложение векторов
        new_end_x = self.end.x + (other.end.x - other.start.x)
        new_end_y = self.end.y + (other.end.y - other.start.y)
        return Vector(self.start, Point(new_end_x, new_end_y))



points = []
for i in range(1, 5):
    x = float(input(f"Точка {i} x: "))
    y = float(input(f"Точка {i} y: "))
    points.append(Point(x, y))


vector1 = Vector(points[0], points[1])
vector2 = Vector(points[2], points[3])


print(f"длинна вектора 1: {vector1.length()}")  # Выводим длину первого вектора


print(f"длинна векиора 2: {vector2.length()}")  # Выводим длину второго вектора

vector3 = vector1 + vector2

print(f"длинна вектора 3: {vector3.length()}")

