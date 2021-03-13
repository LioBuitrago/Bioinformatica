'''
Problema de cambio. Dada una cantidad limite, la idea es calcular cual es la convinacion menor para
poder obtener el monto final.
'''
import numpy as np

def minimoMon(cant, monedas):
    lista = [0]*(cant+1)
    lista[0] = 0
    for k in range(1, cant+1):
        constMin = np.inf 
        '''Constante'''
        for i in monedas:
            if k >= i:
                constMin = min(constMin, lista[k-i])
        lista[k] = constMin + 1
    print (lista[-1])
    return lista[-1]
n = int(input().strip())
monedas = [int(x) for x in input().split(',')]

if __name__ == '__main__':
    minimoMon(n, monedas)
