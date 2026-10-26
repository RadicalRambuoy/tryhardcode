from collections import deque
 
def water_jug(c1, c2, target, jug):
    queue = deque([((0, 0), [])])
    visited = set()
 
    while queue:
        (a, b), path = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]
 
        if (a, b)[jug - 1] == target:
            for state in path:
                print(state)
            return
 
        pour_ab = min(a, c2 - b)
        pour_ba = min(b, c1 - a)
        for s in [(c1, b), (a, c2),
                  (0, b), (a, 0),
                  (a - pour_ab, b + pour_ab),
                  (a + pour_ba, b - pour_ba)]:
            queue.append((s, path))
 
    print("No solution exists.")
 
c1 = int(input("Capacity of jug 1: "))
c2 = int(input("Capacity of jug 2: "))
target = int(input("Target amount: "))
jug = int(input("Target jug (1 or 2): "))
water_jug(c1, c2, target, jug)