def PAM_250() -> dict:
    return [
        [ 2, -2,  0,  0, -3,  1, -1, -1, -1, -2, -1,  0,  1,  0, -2,  1,  1,  0, -6, -3],
        [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4,  0, -2, -2, -8,  0],
        [ 0, -5,  4,  3, -6,  1,  1, -2,  0, -4, -3,  2, -1,  2, -1,  0,  0, -2, -7, -4],
        [ 0, -5,  3,  4, -5,  0,  1, -2,  0, -3, -2,  1, -1,  2, -1,  0,  0, -2, -7, -4],
        [-3, -4, -6, -5,  9, -5, -2,  1, -5,  2,  0, -3, -5, -5, -4, -3, -3, -1,  0,  7],
        [ 1, -3,  1,  0, -5,  5, -2, -3, -2, -4, -3,  0,  0, -1, -3,  1,  0, -1, -7, -5],
        [-1, -3,  1,  1, -2, -2,  6, -2,  0, -2, -2,  2,  0,  3,  2, -1, -1, -2, -3,  0],
        [-1, -2, -2, -2,  1, -3, -2,  5, -2,  2,  2, -2, -2, -2, -2, -1,  0,  4, -5, -1],
        [-1, -5,  0,  0, -5, -2,  0, -2,  5, -3,  0,  1, -1,  1,  3,  0,  0, -2, -3, -4],
        [-2, -6, -4, -3,  2, -4, -2,  2, -3,  6,  4, -3, -3, -2, -3, -3, -2,  2, -2, -1],
        [-1, -5, -3, -2,  0, -3, -2,  2,  0,  4,  6, -2, -2, -1,  0, -2, -1,  2, -4, -2],
        [ 0, -4,  2,  1, -3,  0,  2, -2,  1, -3, -2,  2,  0,  1,  0,  1,  0, -2, -4, -2],
        [ 1, -3, -1, -1, -5,  0,  0, -2, -1, -3, -2,  0,  6,  0,  0,  1,  0, -1, -6, -5],
        [ 0, -5,  2,  2, -5, -1,  3, -2,  1, -2, -1,  1,  0,  4,  1, -1, -1, -2, -5, -4],
        [-2, -4, -1, -1, -4, -3,  2, -2,  3, -3,  0,  0,  0,  1,  6,  0, -1, -2,  2, -4],
        [ 1,  0,  0,  0, -3,  1, -1, -1,  0, -3, -2,  1,  1, -1,  0,  2,  1, -1, -2, -3],
        [ 1, -2,  0,  0, -3,  0, -1,  0,  0, -2, -1,  0,  0, -1, -1,  1,  3,  0, -5, -3],
        [ 0, -2, -2, -2, -1, -1, -2,  4, -2,  2,  2, -2, -1, -2, -2, -1,  0,  4, -6, -2],
        [-6, -8, -7, -7,  0, -7, -3, -5, -3, -2, -4, -4, -6, -5,  2, -2, -5, -6, 17,  0],
        [-3,  0, -4, -4,  7, -5,  0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2,  0, 10]
    ]


def idx(c) -> int:
    indexes = {
        '-':  0, 'A':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6, 
        'H':  7, 'I':  8, 'K':  9, 'L': 10, 'M': 11, 'N': 12, 'P': 13, 
        'Q': 14, 'R': 15, 'S': 16, 'T': 17, 'V': 18, 'W': 19, 'Y': 20 
    }
    return indexes[c]


def local_alignment_backtrack(v, w, sigma, score) -> dict:
    idx_row_max_score = idx_column_max_score = 0
    max_score = 0
    n, m = len(v), len(w)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[2] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(
                0,
                s[i - 1][j] - sigma,
                s[i][j - 1] - sigma,
                s[i - 1][j - 1] + score[idx(v[i - 1]) - 1][idx(w[j - 1]) - 1]
            )
            if (max_score <= s[i][j]):
                max_score = s[i][j]
                idx_row_max_score = i
                idx_column_max_score = j
            if s[i][j] == 0:
                backtrack[i][j] = 2
            elif s[i][j] == s[i - 1][j] - sigma:
                backtrack[i][j] = 1
            elif s[i][j] == s[i][j - 1] - sigma:
                backtrack[i][j] = 0
            else:
                backtrack[i][j] = -1
    return backtrack, max_score, (idx_row_max_score, idx_column_max_score)


def local_alignment(backtrack, s, t, result, i, j):
    if i == 0 or j == 0 or backtrack[i][j] == 2:
        return result
    elif backtrack[i][j] == 1:
        result[0] += s[i - 1]
        result[1] += '-'
        local_alignment(backtrack, s, t, result, i - 1, j)
    elif backtrack[i][j] == 0:
        result[0] += '-'
        result[1] += t[j - 1]
        local_alignment(backtrack, s, t, result, i, j - 1)
    else:
        result[0] += s[i - 1]
        result[1] += t[j - 1]
        local_alignment(backtrack, s, t, result, i - 1, j - 1)
    return result


if __name__ == "__main__":
    s = input()
    t = input()
    sigma = 5
    backtrack, max_score, indexes = local_alignment_backtrack(s, t, sigma, PAM_250())
    result = local_alignment(backtrack, s, t, ["", ""], indexes[0], indexes[1])
    print(max_score)
    print(result[0][::-1])
    print(result[1][::-1])