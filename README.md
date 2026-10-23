
# Day 43 - Shortest Path in Binary Matrix

## Problem Statement
Find the shortest path from the top-left to the
bottom-right cell of a binary matrix.

- 0 = open cell
- 1 = blocked cell
- Movement is allowed in all 8 directions.
- Every move costs one step.
- Path length includes the starting cell.
- Return -1 if no path exists.

## Algorithm: Breadth-First Search (BFS)
1. Validate the grid and start/end cells.
2. Add the starting cell to a queue with distance 1.
3. Process reachable cells level by level.
4. Explore all 8 neighboring positions.
5. Skip blocked, out-of-bounds, and visited cells.
6. Mark visited cells when enqueuing them.
7. Store parent cells to reconstruct the shortest route.
8. Return the destination distance, or -1 if unreachable.

## Features
- BFS shortest-path algorithm
- Eight-direction movement
- Visited-cell tracking
- Path reconstruction
- Level-by-level traversal trace
- Automated edge-case tests

## Complexity
Time: O(R * C)
Space: O(R * C)

R = number of rows
C = number of columns

## Real-World Applications
- GPS and navigation
- Emergency escape planning
- Robotics
- Delivery route planning
- Grid-based games

## Run
python day43_shortest_path_binary_matrix.py
