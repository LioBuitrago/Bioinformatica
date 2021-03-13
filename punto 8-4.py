k = int(input())
text = input()

length = len(text) - k + 1
de_bruijn_graph = { x: [] for x in sorted(text[i:i + k - 1] for i in range(0, length)) }
for i in range(0, length):
	de_bruijn_graph[text[i:i + k - 1]].append(text[i + 1:i + k])
	
for vertex in de_bruijn_graph.keys():
	if len(de_bruijn_graph[vertex]) == 0:
		continue
	elif len(de_bruijn_graph[vertex]) == 1:
		print(vertex + " -> " + de_bruijn_graph[vertex][0])
	else:
		print(vertex + " -> " + de_bruijn_graph[vertex][0], end='')
		for adj_vertex in de_bruijn_graph[vertex][1:]:
			print("," + adj_vertex, end='')
		print("")
