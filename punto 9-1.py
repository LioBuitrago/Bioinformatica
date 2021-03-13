import sys

class CicloEuleriano:
	def __init__(self):
		self.TablaAdyacente = []
		self.numero = None
		self.BordesInexplorados = 0
		self.NodoConBordesSinUsar = dict()
		self.Salida = []
		self.PosicionActualAdya = []
		self.Camino = []
		self.EntradaDatos()
		self.FuncionPrincipalCE()
		self.ObtenerOutput()
	
	def FuncionPrincipalCE(self):
		self.Mapeado(0)
		while self.BordesInexplorados > 0:
			Nodo, Posicion = self.NodoConBordesSinUsar.popitem()
			self.RefrescarCamino(Posicion)
			self.Mapeado(Nodo)
		return self.Camino

	def RefrescarCamino(self, InicioDeP):
		campo = len(self.Camino) - 1
		self.Camino = self.Camino[InicioDeP:campo] + self.Camino[:InicioDeP]
		for Nodo, Posicion in self.NodoConBordesSinUsar.items():
			if Posicion < InicioDeP:
				self.NodoConBordesSinUsar[Nodo] = Posicion + campo - InicioDeP
			else:
				self.NodoConBordesSinUsar[Nodo] = Posicion - InicioDeP
		return

	def Mapeado(self, m):
		self.Camino.append(m)
		PosicionActual = self.PosicionActualAdya[m]
		PosicionActualMaxima = self.Salida[m]
		while PosicionActual < PosicionActualMaxima:
			self.PosicionActualAdya[m] = PosicionActual + 1
			if PosicionActual + 1 < PosicionActualMaxima:
				self.NodoConBordesSinUsar[m] = len(self.Camino) - 1
			else:
				if m in self.NodoConBordesSinUsar:
					del self.NodoConBordesSinUsar[m]
			n = self.TablaAdyacente[m][PosicionActual]
			self.Camino.append(n)
			m = n
			PosicionActual = self.PosicionActualAdya[m]
			PosicionActualMaxima = self.Salida[m]
			self.BordesInexplorados -= 1
		return
		
	def EntradaDatos(self):
		Informacion = list(sys.stdin.read().strip().split())
		self.numero = len(Informacion) // 3
		self.TablaAdyacente = [[]] * self.numero
		self.BordesSinUsar = [[]] * self.numero
		self.Salida = [None] * self.numero
		self.PosicionActualAdya = [0] * self.numero
		for i in range(self.numero):
			ActualEntrada = int(Informacion[i*3])
			self.TablaAdyacente[ActualEntrada] = list(map(int, Informacion[i*3+2].split(',')))
			campo = len(self.TablaAdyacente[ActualEntrada])
			self.Salida[ActualEntrada] = campo
			self.BordesInexplorados += campo

	def ObtenerOutput(self):
		ClasiP = '->'.join([str(Nodo) for Nodo in self.Camino])
		ClasiP = ClasiP[14:] + ClasiP[:16]
		ClasiP = ClasiP[:52] + ClasiP[53:]

		print(ClasiP)

if __name__ == "__main__":
	CicloEuleriano()