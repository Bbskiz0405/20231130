def calculate_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    # Directions in which to look for adjacent squares (N, E, S, W)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # For each occupied square
                # Check all adjacent squares
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    # If the adjacent square is out of bounds or not occupied, increase perimeter
                    if (rr < 0 or rr >= rows or cc < 0 or cc >= cols or grid[rr][cc] == 0):
                        perimeter += 1

    return perimeter

# Define the grid from the image
grid = [
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1]
]

# Calculate the perimeter
perimeter = calculate_perimeter(grid)
print(perimeter)