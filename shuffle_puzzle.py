import random

def display_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(row))

def find_empty(puzzle):
    for i, row in enumerate(puzzle):
        for j, cell in enumerate(row):
            if cell == "_":
                return i, j
    return None

def swap(puzzle, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    puzzle[x1][y1], puzzle[x2][y2] = puzzle[x2][y2], puzzle[x1][y1]

def shuffle_puzzle(puzzle):
    for _ in range(100):
        empty_pos = find_empty(puzzle)
        x, y = empty_pos
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        valid_moves = [(i, j) for i, j in moves if 0 <= i < 3 and 0 <= j < 3]
        swap(puzzle, empty_pos, random.choice(valid_moves))

def is_solved(puzzle):
    goal = [list("123"), list("456"), list("78_")]
    return puzzle == goal

def puzzle_game():
    puzzle = [list("123"), list("456"), list("78_")]
    shuffle_puzzle(puzzle)

    print("Welcome to the Sliding Puzzle Game!")
    print("Arrange the tiles in order from 1 to 8, with the blank space (_) at the bottom-right.")

    while not is_solved(puzzle):
        display_puzzle(puzzle)
        move = input("Enter your move (w/a/s/d for up/left/down/right): ").strip().lower()
        empty_pos = find_empty(puzzle)
        x, y = empty_pos

        if move == "w" and x > 0:
            swap(puzzle, (x, y), (x-1, y))
        elif move == "a" and y > 0:
            swap(puzzle, (x, y), (x, y-1))
        elif move == "s" and x < 2:
            swap(puzzle, (x, y), (x+1, y))
        elif move == "d" and y < 2:
            swap(puzzle, (x, y), (x, y+1))
        else:
            print("Invalid move! Try again.")

    print("Congratulations! You solved the puzzle!")

if __name__ == "__main__":
    puzzle_game()
