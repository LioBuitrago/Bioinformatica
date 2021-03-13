'''
Motif enumeration problem.
Wich DNA patrones play the role of molecular clocks?

'''

from functools import reduce

def motif_enumeration(k, d, DNA):
    patrones = []
    for DNA_string in DNA:
        for i in range(len(DNA[0]) - k + 1):
            pattern_curr = DNA_string[i:i + k]
            mutations_list = mutations(pattern_curr)
            for mutation in mutations_list:
                if error_en_adn(mutation, DNA, d):
                    patrones.append(mutation)
    return " ".join(list(set(patrones)))


def distancia_hamming(patron, motif):
    return sum([1 for i in range(len(motif)) if patron[i] != motif[i]])


def error_en_string(patron, dna_string, d):
    k = len(patron)
    return reduce(lambda x, y: x | y,
                  [distancia_hamming(patron, dna_string[i:i + k]) <= d for i in range(len(dna_string) - k + 1)])


def error_en_adn(patron, DNA, d):
    return reduce(lambda x, y: x & y,
                  [error_en_string(patron, DNA[i], d) for i in range(len(DNA))])


def mutations(patron):
    k = len(patron)
    return list({patron[:i] + j + patron[i + 1:k] for i in range(0, k) for j in ["A", "C", "G", "T"]})


if __name__ == "__main__":
    k, d = tuple(map(int, input().split(" ")))
    DNA = [input() for i in range(4)]
    print(motif_enumeration(k, d, DNA))