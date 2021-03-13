clave = input()
try:
    while True:
        clave += input()[-1]
except EOFError:
    print(clave)