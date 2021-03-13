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

def PuntuacionLP(Peptido, Espectro):   
    linearSpectrum = EspectroLineal(Peptido)
    puntuacion = 0
    
    for masa in Espectro:
        if masa in linearSpectrum:
            puntuacion +=1
            linearSpectrum.remove(masa)
        
    return puntuacion

def PuntuacionCP(Peptido, Espectro):   
    espectrociclico = EspectroCiclico(Peptido)
    puntuacion = 0
    
    for masa in Espectro:
        if masa in espectrociclico:
            puntuacion +=1
            espectrociclico.remove(masa)
        
    return puntuacion

def Ajuste(Clasificacion, Espectro, N):    
    PuntuacionL = []
    for j in range(len(Clasificacion)):
        Peptido = Clasificacion[j]
        PuntuacionL.append(PuntuacionLP(Peptido=Peptido, Espectro=Espectro))
    
    Clasificacion = [x for _,x in sorted(zip(PuntuacionL, Clasificacion), reverse=True)]
    PuntuacionL = sorted(PuntuacionL, reverse=True)
    
    for j in range(N, len(Clasificacion)):
        if PuntuacionL[j] < PuntuacionL[N-1]:
            del Clasificacion[j:]
            return Clasificacion
    
    return Clasificacion

def Expansion(Punto, Punta):
    Resultado = []
    for i in Punto:
        for j in Punta:
            Resultado.append(i+j)
    return Resultado

def ProblemaLeaderboardCS(Espectro, N):    
    Clasificacion = [k for k,v in Copia_AA.items() if v in Espectro]
    ClasiP = ''
    
    while Clasificacion:
        Clasificacion = Expansion(Clasificacion, ModLetras)
        Leaderboard_copy = copy.deepcopy(Clasificacion)
        
        for Peptido in Leaderboard_copy:
            ConjuntosDeAA = list(Peptido)
            masa_p = 0
            for aminoacido in ConjuntosDeAA:
                masa_p += Copia_AA[aminoacido]
            
            if masa_p == Espectro[-1]:
                if PuntuacionCP(Peptido, Espectro) > PuntuacionCP(ClasiP, Espectro):
                    ClasiP = Peptido
                
            elif masa_p > Espectro[-1]:
                Clasificacion.remove(Peptido)
                
        Clasificacion = Ajuste(Clasificacion, Espectro, N)
        
    ClasiP = [Copia_AA[aminoacido] for aminoacido in ClasiP]
    ClasiP = '-'.join([str(x) for x in ClasiP])
    
    ClasiP = ClasiP[-3:]+'-' + ClasiP[:-4]
    return ClasiP
 
N = int(input())
spectrum = [int(x) for x in input().split(' ')]
print(ProblemaLeaderboardCS(spectrum, N))