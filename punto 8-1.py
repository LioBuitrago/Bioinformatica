'''
Resolver la composicion en string del problema planteado
'''
k = int(input().strip())
texto = input().strip()

composicion = sorted([texto[i:i+k] for i in range(len(texto)-k+1)])

print('\n'. join(composicion))