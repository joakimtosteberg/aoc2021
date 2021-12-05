import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def create(data):
        point = data.split(',')
        return Point(int(point[0]),
                     int(point[1]))

    def __str__(self):
        return f"({self.x},{self.y})"

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    @staticmethod
    def create(data):
        points = data.split(' -> ')
        return Line(Point.create(points[0]),
                    Point.create(points[1]))


    def __str__(self):
        return f"{self.start}:{self.end}"

class Map:
    def __init__(self):
        self.lines = []
        self.max_x = 0
        self.max_y = 0
        self.map = {}

    def add_line(self, data):
        line = Line.create(data)
        self.max_x = max(line.start.x,
                         line.end.x,
                         self.max_x)
        self.max_y = max(line.start.y,
                         line.end.y,
                         self.max_y)
        self.lines.append(line)


    def print_lines(self):
        for line in self.lines:
            print(line)


    def generate_map(self, handle_diagonals):
        for x in range(0,self.max_x+1):
            for y in range(0, self.max_y+1):
                self.map[(x,y)] = 0

        for line in self.lines:
            self._add_line_to_map(line, handle_diagonals)

    def _add_line_to_map(self, line, handle_diagonals):
        x_steps = line.end.x - line.start.x
        y_steps = line.end.y - line.start.y
        steps = max(abs(x_steps),abs(y_steps))
        delta_x = int(x_steps/steps)
        delta_y = int(y_steps/steps)
        if delta_x and delta_y and not handle_diagonals:
            return
        for i in range(0,steps+1):
            x = line.start.x + delta_x*i
            y = line.start.y + delta_y*i
            self.map[(x,y)] = self.map[(x,y)] + 1

    def print_map(self):
        for y in range(0,self.max_y+1):
            for x in range(0, self.max_x+1):
                val = self.map[(x,y)] if self.map[(x,y)] else '.'
                print(val, end='')
            print()

    def evaluate(self):
        score = 0
        for y in range(0,self.max_y+1):
            for x in range(0, self.max_x+1):
                if self.map[(x,y)] >= 2:
                    score = score + 1
        return score
        

map = Map()

with open(sys.argv[1]) as f:
    for line in f:
        map.add_line(line.strip())

#map.print_lines()
map.generate_map(handle_diagonals=False)
print(map.evaluate())
#map.print_map()

map.generate_map(handle_diagonals=True)
print(map.evaluate())
