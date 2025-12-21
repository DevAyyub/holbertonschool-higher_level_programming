#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.
"""
import sys


def is_safe(placed_queens, row, col):
    """
    Checks if a queen placed at (row, col) is safe from attacks
    by previously placed queens.
    
    Args:
        placed_queens (list): List of [r, c] pairs for existing queens.
        row (int): The current row.
        col (int): The current column.
    """
    for r, c in placed_queens:
        # Check column conflict
        if c == col:
            return False
        # Check diagonal conflict (absolute difference of rows == absolute difference of cols)
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, placed_queens):
    """
    Recursive backtracking function to find all solutions.
    
    Args:
        n (int): The size of the board (N).
        row (int): The current row we are trying to fill.
        placed_queens (list): List of queens placed so far [[r, c], ...].
    """
    # Base Case: If we have placed queens in all N rows, we found a solution
    if row == n:
        print(placed_queens)
        return

    # Try placing a queen in every column of the current row
    for col in range(n):
        if is_safe(placed_queens, row, col):
            # Place the queen
            placed_queens.append([row, col])
            # Move to the next row
            solve_nqueens(n, row + 1, placed_queens)
            # Backtrack: Remove the queen and try the next column
            placed_queens.pop()


if __name__ == "__main__":
    # Check argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
# 1. Navigate to the project directory
cd ~/holbertonschool-higher_level_programming/python-more_classes

# 2. Create the solution file '101-nqueens.py'
cat << 'EOF' > 101-nqueens.py
#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.
"""
import sys


def is_safe(placed_queens, row, col):
    """
    Checks if a queen placed at (row, col) is safe from attacks
    by previously placed queens.
    
    Args:
        placed_queens (list): List of [r, c] pairs for existing queens.
        row (int): The current row.
        col (int): The current column.
    """
    for r, c in placed_queens:
        # Check column conflict
        if c == col:
            return False
        # Check diagonal conflict (absolute difference of rows == absolute difference of cols)
        if abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row, placed_queens):
    """
    Recursive backtracking function to find all solutions.
    
    Args:
        n (int): The size of the board (N).
        row (int): The current row we are trying to fill.
        placed_queens (list): List of queens placed so far [[r, c], ...].
    """
    # Base Case: If we have placed queens in all N rows, we found a solution
    if row == n:
        print(placed_queens)
        return

    # Try placing a queen in every column of the current row
    for col in range(n):
        if is_safe(placed_queens, row, col):
            # Place the queen
            placed_queens.append([row, col])
            # Move to the next row
            solve_nqueens(n, row + 1, placed_queens)
            # Backtrack: Remove the queen and try the next column
            placed_queens.pop()


if __name__ == "__main__":
    # Check argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Start the solver from row 0 with an empty board
    solve_nqueens(n, 0, [])
