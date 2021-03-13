n = int(input())
masas = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
count = [1] + [0]*n

for i in range(57,n + 1):
	for m in masas:
		count[i] += count[i-m]

print(count[n])