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

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)
                return
        self.tabla[indice].append((clave, valor))

    def modificar(self, clave, nuevo_valor):
        indice = self._hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, nuevo_valor)
                return
        if self.tabla_padre:
            self.tabla_padre.modificar(clave, nuevo_valor)
        else:
            raise KeyError(f"La clave '{clave}' no existe en la tabla de símbolos.")
