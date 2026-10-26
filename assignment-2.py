def cost(path, graph):
    total = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
    return total + graph[path[-1]][path[0]]
 
def hill_climbing(graph, start):
    n = len(graph)
    path = [start] + [c for c in range(n) if c != start]
    best = cost(path, graph)
 
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                new = path[:]
                new[i], new[j] = new[j], new[i]
                new_cost = cost(new, graph)
                if new_cost < best:
                    path, best = new, new_cost
                    improved = True
 
    print("Best tour:", " -> ".join(map(str, path)), "->", path[0])
    print("Cost =", best)
 
n = int(input("Number of cities: "))
print("Enter the distance matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]
start = int(input(f"Starting city (0 to {n - 1}): "))
hill_climbing(graph, start)