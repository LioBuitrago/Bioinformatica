'''
Generating theoretical spectrum problem. Dada una cadena de aminoacidos peptidos,
buscamos obtener Cyclospectrum(Peptide)
The theoretical spectrum of a cyclic peptide Peptide is the collection of all of
the masses of its subpeptides, in addition to the mass 0 and the mass of the entire 
peptide, with masses ordered from smallest to largest.
'''


def CalculoDeMasa(frag):
    tabla_de_masas = { 'G':57, 'A':71, 'S':87, 'P':97, 'V':99,
                   'T':101, 'C':103, 'I':113, 'L':113, 'N':114,
                   'D':115, 'K':128, 'Q':128, 'E':129, 'M':131,
                   'H':137, 'F':147, 'R':156, 'Y':163, 'W':186 }
    
    masa = 0
    for ff in frag: masa += tabla_de_masas[ff]
    spectrum.append(masa)

peptido = input()
spectrum = [0]

for i in range(1, len(peptido)): # Longitud del fragmento.
    
    for j in range(len(peptido)): # Posicion de inicio.
        frag = peptido[j:j+i]
        
        if len(frag) < i:
            frag = peptido[j:j+len(frag)] + peptido[:i-len(frag)]

        CalculoDeMasa(frag)

CalculoDeMasa(peptido) 
spectrum = sorted(spectrum, key=int) 

print(' '.join(str(x) for x in spectrum))