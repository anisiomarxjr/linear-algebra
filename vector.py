def dot_product(a,b):
    sum([a[i] + b[i] for i in range(len(a))]) if len(a) == len(b) else 0

class Vector:

    def __init__(self, v):
        self.vector = v

    def __add__(self,v):
        return [self.vector[i] + v.vector[i] for i in range(len(self.vector))] if len(self.vector) == len(v.vector) else []

    def __sub__(self,v):
        return [self.vector[i] - v.vector[i] for i in range(len(self.vector))] if len(self.vector) == len(v.vector) else []

    def __mul__(self,v):
        return [self.vector[i] * v.vector[i] for i in range(len(self.vector))] if len(self.vector) == len(v.vector) else []
