class Vector:

    def __init__(self, v):
        self.vector = v

    def __add__(self,v):
        [self.vector[i] + v[i] for i in range(leng(self.v))] if len(self.vector) == len(v) else []

    def __sub__(self,v):
        [self.vector[i] - v[i] for i in range(leng(self.v))] if len(self.vector) == len(v) else []
