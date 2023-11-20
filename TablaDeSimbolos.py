class TablaDeSimbolos:

    def __init__(self, tamaño=100, tabla_padre=None):
        self.tamaño = tamaño
        self.tabla_padre = tabla_padre
        self.tabla = [[] for _ in range(tamaño)]

    def _hash(self, clave):
        return hash(clave) % self.tamaño

    def buscar(self, clave):
        indice = self._hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return True
        if self.tabla_padre:
            return self.tabla_padre.buscar(clave)
        return False