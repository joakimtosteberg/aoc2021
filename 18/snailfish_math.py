import math
import sys
import copy

snailfish_numbers = []

class Number:
    def __init__(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

class LiteralNumber(Number):
    def __init__(self, value, parent):
        super().__init__(parent)
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def get_first(self):
        return self

    def reduce(self):
        pass

    def get_last_literal(self):
        return self

    def get_first_literal(self):
        return self

    def explode(self, depth):
        return False

    def split(self):
        if self.value < 10:
            return False

        self.parent.replace(self, CompositeNumber(math.floor(self.value/2), math.ceil(self.value/2), self.parent))
        return True

    def magnitude(self):
        return self.value

class CompositeNumber(Number):
    def __init__(self, lhs, rhs, parent):
        super().__init__(parent)

        if type(lhs) is list:
            self.lhs = CompositeNumber(lhs[0], lhs[1], self)
        elif issubclass(type(lhs), Number):
            self.lhs = lhs
        else:
            self.lhs = LiteralNumber(lhs, self)

        if type(rhs) is list:
            self.rhs = CompositeNumber(rhs[0], rhs[1], self)
        elif issubclass(type(rhs), Number):
            self.rhs = rhs
        else:
            self.rhs = LiteralNumber(rhs, self)

    def get_first(self):
        return self.lhs.get_first()

    def __str__(self):
        return f"[{self.lhs},{self.rhs}]"

    def explode(self, depth):
        if depth == 4:
            prev_literal = self.parent.get_prev_literal(self)
            if prev_literal:
                prev_literal.value += self.lhs.value
            next_literal = self.parent.get_next_literal(self)
            if next_literal:
                next_literal.value += self.rhs.value
            self.parent.replace(self, LiteralNumber(0, self.parent))
            return True
        else:
            return (self.lhs.explode(depth+1) or
                    self.rhs.explode(depth+1))

    def replace(self, number, new_number):
        if self.lhs == number:
            self.lhs = new_number
        elif self.rhs == number:
            self.rhs = new_number
        else:
            print("BADDY1")

    def get_prev_literal(self, child):
        if self.rhs == child:
            return self.lhs.get_last_literal()
        elif self.lhs == child:
            if not self.parent:
                return None
            else:
                return self.parent.get_prev_literal(self)
        else:
            print("BADDY2")

    def get_next_literal(self, child):
        if self.lhs == child:
            return self.rhs.get_first_literal()
        elif self.rhs == child:
            if not self.parent:
                return None
            else:
                return self.parent.get_next_literal(self)
        else:
            print("BADDY3")

    def get_last_literal(self):
        return self.rhs.get_last_literal()

    def get_first_literal(self):
        return self.lhs.get_first_literal()

    def split(self):
        return (self.lhs.split() or self.rhs.split())

    def reduce(self):
        return (self.lhs.explode(1) or
                self.rhs.explode(1) or
                self.lhs.split() or
                self.rhs.split())

    def magnitude(self):
        return self.lhs.magnitude()*3 + self.rhs.magnitude()*2

numbers = []
with open(sys.argv[1]) as f:
    for line in f:
        number = eval(line.strip())
        numbers.append(CompositeNumber(number[0], number[1], None))

def add_numbers(lhs, rhs):
   number = CompositeNumber(lhs, rhs, None)
   lhs.parent = number
   rhs.parent = number
   while number.reduce():
       pass
   return number

def sum_numbers(numbers):
    number = copy.deepcopy(numbers[0])
    for i in range(1,len(numbers)):
        number = add_numbers(number, copy.deepcopy(numbers[i]))
    return number

def find_max_magnitude(numbers):
    max_magnitude = 0
    for i in range(0,len(numbers)):
        for j in range(0, len(numbers)):
            if i==j:
                continue
            number = add_numbers(copy.deepcopy(numbers[i]), copy.deepcopy(numbers[j]))
            max_magnitude = max(max_magnitude, number.magnitude())
    return max_magnitude

print(f"magnitude of sum {sum_numbers(numbers).magnitude()}")
print(f"maximum magnitude of a pair: {find_max_magnitude(numbers)}")
