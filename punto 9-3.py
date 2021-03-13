import sys

class CaminoEuleriano:
    def __init__(self, Adyacencia):
        self.Adyacencia = Adyacencia
        self.RefrescarAdyacencia()
    
    def EntradaDatos(self):
        Informacion = list(sys.stdin.read().strip().split())
        ActualMaximo = 0
        for i in range(len(Informacion) // 3):
            ActualMaximo = max(int(Informacion[i*3]), ActualMaximo, max(list(map(int, Informacion[i*3+2].split(',')))))
        self.numero = ActualMaximo + 1
        self.Adyacencia = [[]] * self.numero
        self.unusedEdges = [[]] * self.numero
        self.Entrada = [0] * self.numero
        self.Salida = [0] * self.numero
        self.PosicionActualAdya = [0] * self.numero
        for i in range(len(Informacion) // 3):
            EntradaActual = int(Informacion[i*3])
            self.Adyacencia[EntradaActual] = list(map(int, Informacion[i*3+2].split(',')))
            for n in self.Adyacencia[EntradaActual]:
                self.Entrada[n] += 1
            campo = len(self.Adyacencia[EntradaActual])
            self.Salida[EntradaActual] = campo
            self.BordesInexplorados += campo
    
    def AnadirBorde(self):
        if type(self.Adyacencia) is dict:
            for n in self.Adyacencia.keys():
                if self.Entrada[n] != self.Salida[n]:
                    if self.Entrada[n] < self.Salida[n]:
                        self.NodoDesvalanceado.append(n)
                    else:
                        self.NodoDesvalanceado.insert(0, n)
            if len(self.NodoDesvalanceado) > 0:
                self.Adyacencia[self.NodoDesvalanceado[0]].append(self.NodoDesvalanceado[1])
                self.Salida[self.NodoDesvalanceado[0]] += 1
                self.Entrada[self.NodoDesvalanceado[1]] += 1
            return    
        for n in range(self.numero):
            if self.Entrada[n] != self.Salida[n]:
                if self.Entrada[n] < self.Salida[n]:
                    self.NodoDesvalanceado.append(n)
                else:
                    self.NodoDesvalanceado.insert(0, n)
        if len(self.NodoDesvalanceado) > 0:
            self.Adyacencia[self.NodoDesvalanceado[0]].append(self.NodoDesvalanceado[1])
            self.Salida[self.NodoDesvalanceado[0]] += 1
            self.Entrada[self.NodoDesvalanceado[1]] += 1
        return

    def Mapeado(self, e):
        self.Camino.append(e)
        PosicionActual = self.PosicionActualAdya[e]
        PosicionActualMa = self.Salida[e]
        while PosicionActual < PosicionActualMa:
            self.PosicionActualAdya[e] = PosicionActual + 1
            if PosicionActual + 1 < PosicionActualMa:
                self.NodoConBordesSinUsar[e] = len(self.Camino) - 1
            else:
                if e in self.NodoConBordesSinUsar:
                    del self.NodoConBordesSinUsar[e]
            n = self.Adyacencia[e][PosicionActual]
            self.Camino.append(n)
            e = n
            PosicionActual = self.PosicionActualAdya[e]
            PosicionActualMa = self.Salida[e]
            self.BordesInexplorados -= 1
        return

    def RefrescarAdyacencia(self):
        self.numero = len(self.Adyacencia)
        self.BordesInexplorados = 0
        self.NodoConBordesSinUsar = dict()
        self.Entrada = dict()
        self.Salida = dict()
        self.PosicionActualAdya = dict()
        self.Camino = []
        self.NodoDesvalanceado = []
        for m, ListaN in self.Adyacencia.items():
            self.Entrada[m] = self.Entrada.get(m, 0)
            for n in ListaN:
                self.Entrada[n] = self.Entrada.get(n, 0) + 1
            campo = len(ListaN)
            self.Salida[m] = campo
            self.BordesInexplorados += campo
            self.PosicionActualAdya[m] = 0

    def RefrescarCamino(self, InicioDeP):
        campo = len(self.Camino) - 1
        self.Camino = self.Camino[InicioDeP:campo] + self.Camino[:InicioDeP]
        for nodo, pos in self.NodoConBordesSinUsar.items():
            if pos < InicioDeP:
                self.NodoConBordesSinUsar[nodo] = pos + campo - InicioDeP
            else:
                self.NodoConBordesSinUsar[nodo] = pos - InicioDeP
        return

    def CaminoEu(self):
        self.AnadirBorde()
        self.CicloEu()
        if len(self.NodoDesvalanceado) > 0:
            for i in range(len(self.Camino)-1):
                if self.Camino[i] == self.NodoDesvalanceado[0] and self.Camino[i+1] == self.NodoDesvalanceado[1]:
                    self.RefrescarCamino(i+1)
                    break
        return self.Camino  

    def CicloEu(self):
        if type(self.Adyacencia) is dict:
            m, ListaN = self.Adyacencia.popitem()
            self.Adyacencia[m] = ListaN
            self.Mapeado(m)
        else:
            self.Mapeado(0)
        while self.BordesInexplorados > 0:
            nodo, pos = self.NodoConBordesSinUsar.popitem()
            self.RefrescarCamino(pos)
            self.Mapeado(nodo)
        return self.Camino        

    def ObtenerOutput(self):
        print('->'.join([str(nodo) for nodo in self.Camino]))     

class StringReconstruction:
    def __init__(self):
        self.Adyacencia = self.LeerInformacion()
        self.Camino = CaminoEuleriano(self.Adyacencia).CaminoEu()
        print(self.ReconstruccionCamino(self.Camino))

    def LeerInformacion(self):
        Informacion = list(sys.stdin.read().strip().split())
        Adyacencia = self.DB(int(Informacion[0]), Informacion[1:]) 
        return Adyacencia
    
    def DB(self, k, Patrones):
        BaseAdyacencia = dict()
        for p in Patrones:
            if p[:k-1] in BaseAdyacencia:
                BaseAdyacencia[p[:k-1]].append(p[1:])
            else:
                BaseAdyacencia[p[:k-1]] = []
                BaseAdyacencia[p[:k-1]].append(p[1:])
            if p[1:] not in BaseAdyacencia:
                BaseAdyacencia[p[1:]] = []
        return BaseAdyacencia

    def ReconstruccionCamino(self, Camino):
        return Camino[0] + ''.join(seq[-1] for seq in Camino[1:])

if __name__ == "__main__":
    StringReconstruction()