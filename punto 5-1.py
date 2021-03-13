'''
Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
'''
from functools import reduce

def pr(patron, perfil):
    return reduce(lambda x, y: x * y, [perfil[patron[i]][i] for i in range(len(patron))])

def most_probable_k_mer(dna, k, perfil):
    k_mers = {pr(dna[i:i + k], perfil): dna[i:i + k] for i in range(len(dna) - k + 1)}
    return k_mers[max(k_mers.keys())]

if __name__ == "__main__":
    dna = input()
    k = int(input())
    perfil = {i: list(map(float, input().split(" "))) for i in ["A", "C", "G", "T"]}
    print(most_probable_k_mer(dna, k, perfil))
