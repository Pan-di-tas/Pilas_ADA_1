class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if self.items else None

def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco {n} de {origen} a {destino}")
    else:
        torres_de_hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        torres_de_hanoi(n - 1, auxiliar, destino, origen)

def resolver_hanoi():
    n = 3
    torres_de_hanoi(n, "Torre 1", "Torre 2", "Torre 3")

resolver_hanoi()
