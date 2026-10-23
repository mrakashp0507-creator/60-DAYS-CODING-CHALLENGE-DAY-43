
from collections import deque


# All 8 possible movement directions.
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]


def shortest_path_binary_matrix(grid, show_trace=False):
    """
    Return (shortest_path_length, path).

    0 = walkable cell
    1 = blocked cell

    Path length counts the starting cell.
    Returns (-1, []) when no path exists.
    """
    if not grid or not grid[0]:
        return -1, []

    rows = len(grid)
    cols = len(grid[0])

    # The start and destination must be open.
    if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
        return -1, []

    start = (0, 0)
    destination = (rows - 1, cols - 1)

    # Queue entries contain (row, column, distance).
    queue = deque([(0, 0, 1)])

    # Mark visited when enqueuing, not when dequeuing.
    visited = {start}

    # Store each cell's predecessor to reconstruct the path.
    parent = {start: None}

    while queue:
        level_size = len(queue)

        if show_trace:
            print(f"\nBFS level: {queue[0][2]}")
            print("Cells waiting:", [(r, c) for r, c, _ in queue])

        # Process the current BFS level.
        for _ in range(level_size):
            r, c, distance = queue.popleft()

            if show_trace:
                print(f"  Explore ({r}, {c}), distance={distance}")

            if (r, c) == destination:
                path = []
                current = destination

                while current is not None:
                    path.append(current)
                    current = parent[current]

                path.reverse()
                return distance, path

            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc
                neighbor = (nr, nc)

                # Ignore out-of-bounds cells.
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                # Ignore blocked or previously visited cells.
                if grid[nr][nc] != 0 or neighbor in visited:
                    continue

                # Mark visited immediately to prevent duplicates.
                visited.add(neighbor)
                parent[neighbor] = (r, c)
                queue.append((nr, nc, distance + 1))

    return -1, []


def print_grid(grid, path=None):
    """Display the grid and optionally mark the chosen route."""
    path_cells = set(path or [])

    for r, row in enumerate(grid):
        symbols = []

        for c, cell in enumerate(row):
            if (r, c) == (0, 0):
                symbols.append("S")
            elif (r, c) == (len(grid) - 1, len(row) - 1):
                symbols.append("E")
            elif cell == 1:
                symbols.append("#")
            elif (r, c) in path_cells:
                symbols.append("*")
            else:
                symbols.append(".")

        print(" ".join(symbols))


def run_tests():
    """Test reachable, blocked, and unreachable scenarios."""
    tests = [
        (
            "Diagonal escape",
            [[0, 1], [1, 0]],
            2,
        ),
        (
            "Open 3x3 city",
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            3,
        ),
        (
            "Blocked start",
            [[1, 0], [0, 0]],
            -1,
        ),
        (
            "Blocked destination",
            [[0, 0], [0, 1]],
            -1,
        ),
        (
            "No possible route",
            [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
            -1,
        ),
        (
            "Single open cell",
            [[0]],
            1,
        ),
        (
            "Single blocked cell",
            [[1]],
            -1,
        ),
        (
            "Empty grid",
            [],
            -1,
        ),
    ]

    print("\n=== TEST RESULTS ===")
    all_passed = True

    for name, grid, expected in tests:
        distance, path = shortest_path_binary_matrix(grid)
        passed = distance == expected
        all_passed = all_passed and passed

        print(
            f"{name}: distance={distance}, expected={expected} "
            f"-> {'PASS' if passed else 'FAIL'}"
        )

        # Verify that the reconstructed route has the correct length.
        if distance != -1 and len(path) != distance:
            all_passed = False
            print("  FAIL: path length does not match distance")

    print(
        "\nOverall:",
        "ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED",
    )


def main():
    grid = [
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
    ]

    print("=" * 50)
    print("       ZOMBIE CITY ESCAPE PLANNER")
    print("=" * 50)

    print("\n=== CITY MAP ===")
    print_grid(grid)

    distance, path = shortest_path_binary_matrix(
        grid, show_trace=True
    )

    print("\n=== ESCAPE RESULT ===")

    if distance == -1:
        print("No safe escape route exists.")
    else:
        print("Shortest path length:", distance)
        print("Route:", " -> ".join(map(str, path)))
        print("\n=== ROUTE VISUALIZATION ===")
        print_grid(grid, path)

    print("\n=== COMPLEXITY ===")
    print("Time: O(R * C)")
    print("Space: O(R * C)")

    run_tests()


if __name__ == "__main__":
    main()
