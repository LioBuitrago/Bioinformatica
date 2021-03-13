import sys
import math
import random
import numpy as np

def DistanciaDeHamming(p, q):
    assert len(p)==len(q)
    k = len(p)
    NumeroMismatches = 0
    for i in range(k):
        if p[i] != q[i]:
            NumeroMismatches +=1
        else:
            continue
    DDH = NumeroMismatches
    
    return DDH

def PerfilPseudoconteo(motif_env, k):
	matrix = []
	for i in range(4):
		matrix.append([0.0] * k)
		
	Conteo_Total = len(motif_env) + 4
	for i in range(k):
		ContadaM = {"A" : 1, "C" : 1, "G" : 1, "T" : 1}
		for motif in motif_env:
			ContadaM["A"] += motif[i].count("A")
			ContadaM["C"] += motif[i].count("C")
			ContadaM["G"] += motif[i].count("G")
			ContadaM["T"] += motif[i].count("T")
		matrix[0][i] = ContadaM["A"] / Conteo_Total
		matrix[1][i] = ContadaM["C"] / Conteo_Total
		matrix[2][i] = ContadaM["G"] / Conteo_Total
		matrix[3][i] = ContadaM["T"] / Conteo_Total
		
	return matrix

def Puntaje(motifs): 
	k = len(motifs[0])
	Consenso = []
	for i in range(k):
		Frecuencia = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
		for motif in motifs:
			Frecuencia["A"] += motif[i].count("A")
			Frecuencia["C"] += motif[i].count("C")
			Frecuencia["G"] += motif[i].count("G")
			Frecuencia["T"] += motif[i].count("T")
		FrecuenciaMa = max(Frecuencia.values())
		for nt, count in Frecuencia.items():
			if count == FrecuenciaMa:
				Consenso.append(nt)
				break
	Consenso = "".join(Consenso)
	PuntajePorCadaMotif = []
	for motif in motifs:
		PuntajePorUnMotif = DistanciaDeHamming(Consenso, motif)
		PuntajePorCadaMotif.append(PuntajePorUnMotif)	
	puntaje = sum(PuntajePorCadaMotif)
	
	return puntaje

def K_MasProbables(Apunte, k, MatrixPer):  
	K_P = {}	
	for i in range(len(Apunte)-k+1):
		kmer = Apunte[i : i+k]
		FilaA, FilaC, FilaG, FilaT = MatrixPer[0], MatrixPer[1], MatrixPer[2], MatrixPer[3]
		ProbabilidadK = []
		for j in range(len(kmer)):
			if kmer[j] == 'A':
				ProbabilidadK.append(FilaA[j])
			elif kmer[j] == 'C':
				ProbabilidadK.append(FilaC[j])
			elif kmer[j] == 'G':
				ProbabilidadK.append(FilaG[j])
			elif kmer[j] == 'T':
				ProbabilidadK.append(FilaT[j])
		ProbabilidadK = np.prod(np.array(ProbabilidadK))
		K_P[kmer] = ProbabilidadK
		
	ProbabilidadMa = max([prob for prob in K_P.values()])
	k_MP = [kmer for kmer, prob in K_P.items() if prob==ProbabilidadMa]
	
	return ''.join(k_MP[0])

def ProblemaGreedyMotifSearchWithPseudoCount(k, t, adn):
	Mejores_Motif = []
	for seq in adn:
		first = seq[:k]
		Mejores_Motif.append(first)
	
	PrimeraSecuencia = adn[0]
	for inicio in range(len(PrimeraSecuencia) - k + 1):
		kmer = PrimeraSecuencia[inicio : inicio + k]
		motif = [kmer]
		for i in range(1, t):
			matrix = PerfilPseudoconteo(motif, k)
			most_probable = K_MasProbables(adn[i], k, matrix)
			motif.append(most_probable)	
		if Puntaje(motif) < Puntaje(Mejores_Motif):
			Mejores_Motif = motif
			
	return Mejores_Motif

k, t = tuple(map(int, input().split(" ")))
a_d_n = sys.stdin.read().split('\n')
print("\n".join(ProblemaGreedyMotifSearchWithPseudoCount(k, t, a_d_n)))