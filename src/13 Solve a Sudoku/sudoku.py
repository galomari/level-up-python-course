
def is_valid(puzzle, num, position):
    # Check if the number is not already in the given row
    for i in range(len(puzzle[0])):  # Ensure column index is within the puzzle's width
        if puzzle[position[0]][i] == num and i != position[1]:  # Corrected condition
            return False

    # Check if the number is not already in the given column
    for i in range(len(puzzle)):  # Ensure row index is within the puzzle's height
        if puzzle[i][position[1]] == num and i != position[0]:  # Corrected condition
            return False

    # Check the 3x3 box
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == num and (i, j) != position:  # Ensure i and j are within range
                return False

    return True


def solve_sudoku(puzzle):
    # Find the first empty spot
    empty = None
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                empty = (i, j)
                break
        if empty is not None:
            break

    if not empty:
        return True  # Puzzle solved
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(puzzle, num, (row, col)):
            puzzle[row][col] = num

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = 0  # backtrack

    return False  # trigger backtracking if no number is valid


def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(num) for num in row))


# Example Sudoku grid
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


if solve_sudoku(puzzle):
    print("Sudoku solved:")
    print(len(puzzle))
    print_puzzle(puzzle)
else:
    print("No solution exists")
