import heapq

def heuristic(state):
    goal_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 0: (2, 2)}
    distance = 0
    for idx in range(9):
        num = state[idx]
        if num == 0:
            continue
        x, y = idx // 3, idx % 3
        goal_x, goal_y = goal_pos[num]
        distance += abs(x - goal_x) + abs(y - goal_y)
    return distance

def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    row, col = i // 3, i % 3

    # 上移
    if row > 0:
        new_i = i - 3
        new_state = list(state)
        new_state[i], new_state[new_i] = new_state[new_i], new_state[i]
        neighbors.append(tuple(new_state))
    
    # 下移
    if row < 2:
        new_i = i + 3
        new_state = list(state)
        new_state[i], new_state[new_i] = new_state[new_i], new_state[i]
        neighbors.append(tuple(new_state))
    
    # 左移
    if col > 0:
        new_i = i - 1
        new_state = list(state)
        new_state[i], new_state[new_i] = new_state[new_i], new_state[i]
        neighbors.append(tuple(new_state))
    
    # 右移
    if col < 2:
        new_i = i + 1
        new_state = list(state)
        new_state[i], new_state[new_i] = new_state[new_i], new_state[i]
        neighbors.append(tuple(new_state))
    
    return neighbors

def astar(start, goal):
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start), 0, start))
    came_from = {}
    g_score = {start: 0}
    closed = set()

    while open_heap:
        current_f, current_g, current_state = heapq.heappop(open_heap)

        if current_state == goal:
            # 重构路径
            path = []
            while current_state in came_from:
                path.append(current_state)
                current_state = came_from[current_state]
            path.append(start)
            return path[::-1]  # 反转得到从起点到目标的路径

        if current_state in closed:
            continue
        closed.add(current_state)

        for neighbor in get_neighbors(current_state):
            tentative_g = current_g + 1
            if neighbor not in g_score or tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current_state
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor)
                heapq.heappush(open_heap, (f, tentative_g, neighbor))

    return None  # 无解

if __name__ == "__main__":
    # 示例初始状态和目标状态
    start_state = (2, 8, 3, 1, 6, 4, 0, 7, 5)
    goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)

    path = astar(start_state, goal_state)

    if path:
        print(f"找到解，路径长度：{len(path)-1}")
        print("路径步骤：")
        for idx, state in enumerate(path):
            print(f"步骤 {idx}:")
            for i in range(3):
                print(state[i*3 : (i+1)*3])
            print()
    else:
        print("无解")