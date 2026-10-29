from collections import deque

M = int(input("Enter number of missionaries: "))
C = int(input("Enter number of cannibals: "))
capacity = int(input("Enter boat capacity: "))

start = (M, C, 0)
goal = (0, 0, 1)

def safe(m, c):
    return (m == 0 or m >= c) and (M-m == 0 or M-m >= C-c)

queue = deque([start])
parent = {start: None}
action = {}

while queue:
    state = queue.popleft()
    m, c, boat = state

    if state == goal:
        break

    for x in range(capacity + 1):
        for y in range(capacity + 1):
            if 1 <= x + y <= capacity:
                if boat == 0:
                    new = (m-x, c-y, 1)
                    move = f"{x} M and {y} C cross left to right"
                else:
                    new = (m+x, c+y, 0)
                    move = f"{x} M and {y} C cross right to left"

                if x <= (m if boat == 0 else M-m) and \
                   y <= (c if boat == 0 else C-c):

                    if (0 <= new[0] <= M and
                        0 <= new[1] <= C and
                        safe(new[0], new[1]) and
                        new not in parent):

                        parent[new] = state
                        action[new] = move
                        queue.append(new)

if goal in parent:
    path = []
    state = goal

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for i, state in enumerate(path):
        m, c, boat = state
        print(f"\nStep {i}")
        print(f"Left Bank: {m} M, {c} C")
        print(f"Right Bank: {M-m} M, {C-c} C")
        print("Boat:", "Left" if boat == 0 else "Right")

        if i > 0:
            print("Action:", action[state])
else:
    print("No solution exists.")