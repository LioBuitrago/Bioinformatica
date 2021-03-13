'''
Pattern count problem. Se realiza el metodo mediante un
conteo realizado con strings dependiendo de cierto patron
dentro de una cadena de nucleotidos.
'''

genoma = input()
patron = input()

results = 0
sub_len = len(patron)
for i in range(len(genoma)):
    if genoma[i:i+sub_len] == patron:
        results += 1
print (results)