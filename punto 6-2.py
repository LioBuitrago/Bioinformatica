'''
Manhattan tourist problem. Dada la informacion, la idea del problema es recorrer el mayor numero posible
de atracciones durante una visita a dicha ciudad para al final llegar al punto especifico.
'''
def Manhattan(n, m, abajo, derecha):
    score = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        score[i][0] = score[i - 1][0] + abajo[i - 1][0]
    for j in range(1, m + 1):
        score[0][j] = score[0][j - 1] + derecha[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score[i][j] = max(score[i - 1][j] + abajo[i - 1][j], score[i][j - 1] + derecha[i][j - 1])
    print(score[n][m])

if __name__ == '__main__':
    n, m = input().split(' ')
    n, m = int(n), int(m)
    abajo = [[int(x) for x in input().split(' ')] for pxndx in range(n)]
    _ = input()
    derecha = [[int(x) for x in input().split(' ')] for pxndx in range(n + 1)]
    Manhattan(n, m, abajo, derecha)