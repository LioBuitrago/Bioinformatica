'''
Peptide encoding problem. Se deben hallar los substrings de una cadenada dada de ADN
decodificando dichos conjuntos, teniendo en cuenta la version inversa y la version 
cuando se cambia de ADN a ARN, todo bajo la base de GeneticCode.
'''

secuencia = input()
patron = input()

CombinacionesTipoCodon = {
    'AAA': 'K',
    'AAC': 'N',
    'AAG': 'K',
    'AAU': 'N',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACU': 'T',
    'AGA': 'R',
    'AGC': 'S',
    'AGG': 'R',
    'AGU': 'S',
    'AUA': 'I',
    'AUC': 'I',
    'AUG': 'M',
    'AUU': 'I',
    'CAA': 'Q',
    'CAC': 'H',
    'CAG': 'Q',
    'CAU': 'H',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCU': 'P',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGU': 'R',
    'CUA': 'L',
    'CUC': 'L',
    'CUG': 'L',
    'CUU': 'L',
    'GAA': 'E',
    'GAC': 'D',
    'GAG': 'E',
    'GAU': 'D',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCU': 'A',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGU': 'G',
    'GUA': 'V',
    'GUC': 'V',
    'GUG': 'V',
    'GUU': 'V',
    'UAA': 'alto',
    'UAC': 'Y',
    'UAG': 'alto',
    'UAU': 'Y',
    'UCA': 'S',
    'UCC': 'S',
    'UCG': 'S',
    'UCU': 'S',
    'UGA': 'alto',
    'UGC': 'C',
    'UGG': 'W',
    'UGU': 'C',
    'UUA': 'L',
    'UUC': 'F',
    'UUG': 'L',
    'UUU': 'F',
}


complementos = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def amino_acid_string_Peptide(mrna):
    
    solucion=''


    for i in range(0, len(mrna), 3):
        triforce=CombinacionesTipoCodon[mrna[i:i+3]]
        if triforce=='alto':
            break
        solucion+=triforce

    return solucion

def conversion_ARN(kmer):
    return kmer.replace('T', 'U') 

def complemento_inverso(kmer):
	reverso = ''
	for base in kmer:
		reverso = complementos[base] + reverso
	return reverso

k = len(patron) * 3

resultado = ''

for ext in range(len(secuencia) - k + 1):
	kmer = secuencia[ext:ext+k]
	if amino_acid_string_Peptide(conversion_ARN(kmer)) == patron:
		resultado = resultado + kmer + '\n'
for ext in range(len(secuencia) - k + 1):
    kmer = secuencia[ext:ext+k]
    if amino_acid_string_Peptide(conversion_ARN(complemento_inverso(kmer))) == patron:
        resultado = resultado + kmer + '\n'

print(resultado)

