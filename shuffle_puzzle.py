import random
import time

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

def shuffle_puzzle(puzzle, difficulty):
    shuffle_count = 100 * difficulty
    for _ in range(shuffle_count):
        empty_pos = find_empty(puzzle)
        x, y = empty_pos
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        valid_moves = [(i, j) for i, j in moves if 0 <= i < len(puzzle) and 0 <= j < len(puzzle[0])]
        swap(puzzle, empty_pos, random.choice(valid_moves))

def is_solved(puzzle, goal):
    return puzzle == goal

def puzzle_game():
    print("Welcome to the Sliding Puzzle Game!")
    print("Choose difficulty level:")
    print("1. Easy (3x3)")
    print("2. Medium (4x4)")
    print("3. Hard (5x5)")
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == "1":
        size = 3
        goal = [list("123"), list("456"), list("78_")]
    elif choice == "2":
        size = 4
        goal = [list("1234"), list("5678"), list("9ABC"), list("DEF_")]
    elif choice == "3":
        size = 5
        goal = [list("12345"), list("6789A"), list("BCDEF"), list("GHIJK"), list("LMNO_")]
    else:
        print("Invalid choice. Defaulting to Easy (3x3).")
        size = 3
        goal = [list("123"), list("456"), list("78_")]

    puzzle = [row.copy() for row in goal]
    shuffle_puzzle(puzzle, int(choice)

    print("Arrange the tiles in order, with the blank space (_) at the bottom-right.")
    print("Use w/a/s/d to move the tiles (up/left/down/right).")
    print("Enter 'u' to undo your last move, 'h' for a hint, or 'q' to quit.")

    move_count = 0
    start_time = time.time()
    move_history = []

    while not is_solved(puzzle, goal):
        display_puzzle(puzzle)
        move = input("Enter your move: ").strip().lower()
        empty_pos = find_empty(puzzle)
        x, y = empty_pos

        if move == "w" and x > 0:
            swap(puzzle, (x, y), (x-1, y))
            move_history.append((x, y, x-1, y))
            move_count += 1
        elif move == "a" and y > 0:
            swap(puzzle, (x, y), (x, y-1))
            move_history.append((x, y, x, y-1))
            move_count += 1
        elif move == "s" and x < size-1:
            swap(puzzle, (x, y), (x+1, y))
            move_history.append((x, y, x+1, y))
            move_count += 1
        elif move == "d" and y < size-1:
            swap(puzzle, (x, y), (x, y+1))
            move_history.append((x, y, x, y+1))
            move_count += 1
        elif move == "u" and move_history:
            last_move = move_history.pop()
            swap(puzzle, (last_move[2], last_move[3]), (last_move[0], last_move[1]))
            move_count -= 1
        elif move == "h":
            print("Hint: Try to move the tile that is closest to its correct position.")
        elif move == "q":
            print("Quitting the game. Goodbye!")
            return
        else:
            print("Invalid move! Try again.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Congratulations! You solved the puzzle!")
    print(f"Total moves: {move_count}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    puzzle_game()
