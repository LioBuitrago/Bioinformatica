'''
Protein translation problem. Dado un patron RNA string pattern, la
principal meta es convertir el conjunto tipo string en otro tipo 
string pero ya en enfasis a los aminoacidos, haciendo uso de la tabla
general CodonType.

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
'''

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

'''
Called the central dogma of biology. The first step is to go
from the gene to messenger RNA(mRNA) we have here rewritten 
the information now as RNA, and the next step is going from
that messenge RNA to protein(this process is called translation)
into a polypeptide sequences.
'''

def amino_acid_string_Peptide(mrna):
    
    solucion=''
    '''
    The ribosome is made up of proteins + rRNA(ribosomal RNA)
    we often view RNA like DNA as primarily enconding information.
    mRNA it's acting as a transcript for a gene, but it doesn't
    have to only encode information. It can also provide a functional
    structural role, which it does in ribosomal RNA. The ribosome
    it's going to travel along the mRNA from the 5's prime end to the
    three prime end, reading it, and taking that information, and 
    turning it into a sequence of amino acids.
    '''

    for i in range(0, len(mrna), 3):
        triforce=CombinacionesTipoCodon[mrna[i:i+3]]
        if triforce=='alto':
            break
        solucion+=triforce

    return solucion
    '''
    61 codons code amino acids
    3  codons are stop codons
    '''
entrada_de_datos=input()

print(amino_acid_string_Peptide(entrada_de_datos))
