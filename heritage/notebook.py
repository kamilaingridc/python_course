from paper import *
# importa todos os métodos e atributos de papel

class Notebook(Paper):
    def __init__(self, pages):
        self._size *= pages

A = Notebook(10)
print(A._size)

A.write('aaa')
print(A.read())
