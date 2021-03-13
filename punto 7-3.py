'''
Edit Distance Problem: Find the edit distance between two strings.

'''
def distaciaString(s1, s2):
	s = [[0] * (m + 1) for _ in range(n + 1)]

	for i in range(1, n + 1):
		s[i][0] = s[i - 1][0] + 1

	for j in range(1, m + 1):
		s[0][j] = s[0][j - 1] + 1

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			s[i][j] = min(
				s[i - 1][j] + 1,
				s[i][j - 1] + 1,
				s[i - 1][j - 1] if s1[i - 2] == s2[j - 2] else s[i - 1][j - 1] + 1
			)

	edit_distance = s[n][m]
	return edit_distance

if __name__ == "__main__":
	s1 = input()
	s2 = input()
	n, m = len(s1), len(s2)
	print (distaciaString(s1, s2))