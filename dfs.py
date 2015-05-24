def dfs(graph, start):
	visited = set()
	stack = [start]

	while stack:
		vertex = stack.pop()
		if (vertex not in visited):
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

def dfsRecursion(graph,start,visited=None):
	if visited == None:
		visited = set()

	visited.add(start)

	for next in graph[start] - visited:
		dfsRecursion(graph,next,visited)

	return visited

def main():
	graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

	print (dfs(graph,'A'))
	print (dfsRecursion(graph,'A'))

main()
