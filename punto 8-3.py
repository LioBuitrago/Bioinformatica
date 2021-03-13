patterns = []
try:
	while True:
		patterns.append(input())
except EOFError:
	overlap_graph = { x: [] for x in patterns }
	for vertex in overlap_graph.keys():
		for read in patterns:
			if read[:-1] == vertex[1:]:
				overlap_graph[vertex].append(read)
				
for vertex in overlap_graph.keys():
	if len(overlap_graph[vertex]) == 0:
		continue
	elif len(overlap_graph[vertex]) == 1:
		print(vertex + " -> " + overlap_graph[vertex][0])
	else:
		print(vertex + " -> " + overlap_graph[vertex][0], end='')
		for adj_vertex in overlap_graph[vertex][1:]:
			print("," + adj_vertex, end='')
		print("")
