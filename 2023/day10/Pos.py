class Pos:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __eq__(self, other):
        return (self.r, self.c) == (other.r, other.c)

    def __add__(self, other):
        return Pos(self.r + other.r, self.c + other.c)

    def __hash__(self):
        return hash((self.r, self.c))

    def __repr__(self):
        return f'({self.r}, {self.c})'
