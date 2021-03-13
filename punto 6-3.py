'''
Subsequence problem. Usando el OUTPUTLCS
'''

def LongSubsecuencia(s, t):
    pxndx = [[0]*(len(t)+1) for _ in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                pxndx[i+1][j+1] = pxndx[i][j]+1
            else:
                pxndx[i+1][j+1] = max(pxndx[i+1][j], pxndx[i][j+1])
    subsecuencia = ''
    i = len(s)
    j = len(t)
    while (i != 0 and j != 0):
        if pxndx[i][j] == pxndx[i-1][j]:
            i -= 1
        elif pxndx[i][j] == pxndx[i][j-1]:
            j -= 1
        else:
            subsecuencia = s[i-1] + subsecuencia
            i -= 1
            j -= 1
    print (subsecuencia)
    return subsecuencia

if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    LongSubsecuencia(s, t)