from collections import deque

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount of water: "))

def water_jug(a, b, target):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            print("\nSolution found:")
            for i, (p, q) in enumerate(path):
                print(f"Step {i}: Jug 1 = {p}L, Jug 2 = {q}L")
            return

        next_states = [
            (a, y),                 # Fill Jug 1
            (x, b),                 # Fill Jug 2
            (0, y),                 # Empty Jug 1
            (x, 0),                 # Empty Jug 2
            (x - min(x, b-y), y + min(x, b-y)),  # Pour Jug 1 to Jug 2
            (x + min(y, a-x), y - min(y, a-x))   # Pour Jug 2 to Jug 1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("Target cannot be reached.")

water_jug(jug1, jug2, target)