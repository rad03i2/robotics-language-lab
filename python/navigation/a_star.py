"""A* path planning on a small grid map."""

from heapq import heappop, heappush

GridPoint = tuple[int, int]


def neighbors(point: GridPoint, width: int, height: int) -> list[GridPoint]:
    x, y = point
    result: list[GridPoint] = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            result.append((nx, ny))
    return result


def heuristic(a: GridPoint, b: GridPoint) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(width: int, height: int, start: GridPoint, goal: GridPoint, walls: set[GridPoint]) -> list[GridPoint]:
    frontier: list[tuple[int, GridPoint]] = []
    heappush(frontier, (0, start))
    came_from: dict[GridPoint, GridPoint | None] = {start: None}
    cost_so_far: dict[GridPoint, int] = {start: 0}

    while frontier:
        _, current = heappop(frontier)
        if current == goal:
            break

        for next_point in neighbors(current, width, height):
            if next_point in walls:
                continue
            new_cost = cost_so_far[current] + 1
            if next_point not in cost_so_far or new_cost < cost_so_far[next_point]:
                cost_so_far[next_point] = new_cost
                priority = new_cost + heuristic(goal, next_point)
                heappush(frontier, (priority, next_point))
                came_from[next_point] = current

    if goal not in came_from:
        return []

    path: list[GridPoint] = []
    current: GridPoint | None = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    return list(reversed(path))


if __name__ == "__main__":
    wall_cells = {(2, 1), (2, 2), (2, 3)}
    print(a_star(6, 5, (0, 0), (5, 4), wall_cells))
