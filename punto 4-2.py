'''
Implement MedianString
'''

def median_string(k, DNA):
    patrones = k_mer_patterns(k)
    median = {distancia_patron_adn(patron, DNA): patron for patron in patrones}
    return median[min(median.keys())]

def hamming_distance(patron, motif):
    return sum([1 for i in range(len(motif)) if patron[i] != motif[i]])

def k_mer_patterns(k):
    patrones = ["A", "C", "G", "T"]
    while len(patrones[0]) < k:
        patrones = [patrones[l] + j for j in ["A", "C", "G", "T"] for l in range(0, len(patrones))]
    return patrones

def distancia_minima(patron, text):
    k = len(patron)
    return min([hamming_distance(patron, text[i:i + k]) for i in range(len(text) - k + 1)])

def distancia_patron_adn(patron, DNA):
    return sum([distancia_minima(patron, DNA_string) for DNA_string in DNA])

if __name__ == "__main__":
    k = int(input())
    DNA = [input() for i in range(10)]
    print(median_string(k, DNA))