'''
Reverse complement problem. Dado un patron secuencial de ADN en tipo string, 
es necesario obtener el complemento inverso.
'''
secuenciaADN = input()


def ComplementoInverso(secuencia):

    #establecimiento explicito de complementos ADN
    complementos = {'A':'T','C':'G','G':'C','T':'A'}

    #poner a la inversa la secuencia para los datos de salida y luego reemplazar
    #los nucleos con sus respectivos complementos.
    invCompSeq = secuencia[::-1]
    for nut,comp in complementos.items():
        invCompSeq = invCompSeq.replace(nut,comp)

    return invCompSeq.upper()

invCompSeq = ComplementoInverso(secuenciaADN)

print(''.join(invCompSeq))