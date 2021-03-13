'''
Frecuent words problem. Dada una cadena ADN en tipo texto string con un dato int k
se debe hallar los mas frecuentes k-mers en el texto.
'''
text = input()
k = int(input())

def Frecuencia(text,k):

    #generar una lista de todos los kmer.
    kmerList = []
    for i in range(len(text)-k+1):
        kmerList.append(text[i:i+k])

    #obtener el conteo de k.
    kmerCounts = {}
    for kmer in kmerList:
        kmerCounts[kmer] = kmerCounts.get(kmer,0) + 1

    #identificar las kmer mas frecuentes.
    maxCount = max(kmerCounts.values())
    mostFreqKmers = [kmer for kmer,val in kmerCounts.items() if val == maxCount]

    return mostFreqKmers

mostFreqKmers = Frecuencia(text,k)

print(' '.join(mostFreqKmers))