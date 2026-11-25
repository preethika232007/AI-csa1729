
from collections import deque

start = tuple(map(int, input("Enter 9 numbers (use 0 for blank): ").split()))

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = deque([start])
visited = {start}
parent = {start: None}

while queue:
    state = queue.popleft()

    if state == goal:
        print("Solution found!")
        break

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = []
    if row > 0:
        moves.append(zero - 3)
    if row < 2:
        moves.append(zero + 3)
    if col > 0:
        moves.append(zero - 1)
    if col < 2:
        moves.append(zero + 1)

    for pos in moves:
        new_state = list(state)
        new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
        new_state = tuple(new_state)

        if new_state not in visited:
            visited.add(new_state)
            parent[new_state] = state
            queue.append(new_state)
else:
    print("No solution found!")
    exit()

path = []
while state is not None:
    path.append(state)
    state = parent[state]

path.reverse()

print("Steps to solve:")
for state in path:
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
