from collections import Counter
import copy

Letras = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
Masas_AA = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
eliminar = ['I', 'K']
ModLetras = [letras for letras in Letras if letras not in eliminar]
Copia_AA = Masas_AA.copy()
del Copia_AA['I'], Copia_AA['K']

def EspectroCiclico(Peptido):
	Prefijo_M = {}
	Prefijo_M[0] = 0
	
	for i in range(len(Peptido)):
		for letras in Letras:
			if letras==Peptido[i]:
				Prefijo_M[i+1] = Prefijo_M[i] + Masas_AA[letras]
				
	MasaPeptida = Prefijo_M[len(Peptido)]
	Ciclico_Espectro = [0]
	
	for i in range(len(Prefijo_M)):
		for j in range(i+1, len(Prefijo_M)):
			Ciclico_Espectro.append(Prefijo_M[j]-Prefijo_M[i])
			
			if i>0 and j<len(Peptido):
				Ciclico_Espectro.append(MasaPeptida-(Prefijo_M[j]-Prefijo_M[i]))
				
	return sorted(Ciclico_Espectro)

def EspectroLineal(Peptido):    
	Prefijo_M = {}
	Prefijo_M[0] = 0
	
	for i in range(len(Peptido)):
		for letras in Letras:
			if letras==Peptido[i]:
				Prefijo_M[i+1] = Prefijo_M[i] + Masas_AA[letras]
				
	Lineal_Espectro = [0]
				
	for i in range(len(Prefijo_M)):
		for j in range(i+1, len(Prefijo_M)):
			Lineal_Espectro.append(Prefijo_M[j]-Prefijo_M[i])
			
	return sorted(Lineal_Espectro)

def Calculo_CR(list1, list2):
	CR1 = Counter(list1)
	CR2 = Counter(list2)
	for k, n in CR1.items():
		if n > CR2[k]:
			return False
	return True

def Expansion(Punto, Punta):
	Resultado = []
	for i in Punto:
		for j in Punta:
			Resultado.append(i+j)
	return Resultado

def ProblemaSecuenciacionDePeptidos(Espectro):
	Postulantes = [k for k,v in Copia_AA.items() if v in Espectro]
	Solucion_P = []
	
	while Postulantes:
		Postulantes = Expansion(Postulantes, ModLetras)
		DuplicadoPostulantes = copy.deepcopy(Postulantes)
		for Peptido in DuplicadoPostulantes:
			ConjuntosDeAA = list(Peptido)
			masa_p = 0
			for aminoacido in ConjuntosDeAA:
				masa_p += Copia_AA[aminoacido]
			if masa_p == Espectro[-1]:
				if (Calculo_CR(EspectroCiclico(Peptido), Espectro)==True) and Peptido not in Solucion_P:
					Solucion_P.append(Peptido)
				Postulantes.remove(Peptido)  
			elif (Calculo_CR(EspectroLineal(Peptido), Espectro)==False):
				Postulantes.remove(Peptido)

	Resultado = []
	for p in Solucion_P:
		ConjuntosDeAA = list(p)
		MasasConjuntosAA = [Copia_AA[aminoacido] for aminoacido in ConjuntosDeAA]
		MasasUnidas = '-'.join([str(m) for m in MasasConjuntosAA])
		Resultado.append(MasasUnidas)
		
				
	return Resultado

s = [int(x) for x in input().split(' ')]
n = ProblemaSecuenciacionDePeptidos(s)
print(' '.join(n))
