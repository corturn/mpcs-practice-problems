def num_captures(board: list[list[int]]) -> int:
    """
    Given a board, determine the number of pieces that
    can be captures on the board.

    Args:
        board: Board represented as a list of list of integers,
        where zeroes (0) represent empty squares, and integers
        greater that zero represent a player's piece

    Returns: The number of pieces that can be captured.
    """
    # ignore if 0
    count = 0
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if check_capture(board, (y,x)):
                count += 1
    return count
    
def check_capture(board: list[list[int]], pos: tuple[int, int]):
    l = test_direction(board, pos, (0,-1))
    r = test_direction(board, pos, (0,1))
    n = test_direction(board, pos, (1, 0))
    s = test_direction(board, pos, (-1,0))

    return (l and r) and (l == r) or \
           (n and s) and (n == s)

def test_direction(board: list[list[int]], pos: tuple[int, int], dir: tuple[int, int]):
    y, x = pos
    dy, dx = dir
    val = board[y][x]
    n = len(board)
    while (0 <= y < n and 0 <= x < n):
        piece = board[y][x]
        if piece:
            if piece != val:
                return piece
        y += dy
        x += dx
    return 0

def test_board() -> list[list[int]]:
    """
    Returns the sample board described in the writeup.
    """
    return \
        [[0, 1, 2, 2, 1],
         [0, 2, 3, 0, 0],
         [1, 0, 3, 1, 3],
         [0, 4, 0, 0, 0],
         [0, 1, 2, 0, 0]]
