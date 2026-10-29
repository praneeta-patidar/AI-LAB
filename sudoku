def print_grid(grid):
    for row in grid:
        print(*row)


def is_safe(grid, row, col, num):

    # Check the row
    for c in range(9):
        if grid[row][c] == num:
            return False

    # Check the column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True


def solve_sudoku(grid):

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                for num in range(1, 10):

                    if is_safe(grid, row, col, num):
                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        grid[row][col] = 0

                return False

    return True


grid = []

print("Enter Sudoku grid (use 0 for empty cells):")

for i in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

if solve_sudoku(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")