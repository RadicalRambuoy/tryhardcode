import heapq
def manhattan(state, goal):
    dist = 0
    for i, tile in enumerate(state):
        if tile != 0:
            j = goal.index(tile)
            dist += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return dist
 
def neighbors(state):
    i = state.index(0)
    r, c = i // 3, i % 3
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[i], s[j] = s[j], s[i]
            result.append(tuple(s))
    return result
 
def astar(start, goal):
    pq = [(manhattan(start, goal), 0, start, [start])]
    visited = set()
 
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            for s in path:
                print(s[0:3], s[3:6], s[6:9], sep="\n")
                print()
            print("Moves:", g)
            return
        if state in visited:
            continue
        visited.add(state)
 
        for n in neighbors(state):
            if n not in visited:
                heapq.heappush(pq, (g + 1 + manhattan(n, goal), g + 1, n, path + [n]))
 
    print("No solution.")
 
start = tuple(map(int, input("Start state (9 numbers, 0 = blank): ").split()))
goal = tuple(map(int, input("Goal state (9 numbers): ").split()))
astar(start, goal)