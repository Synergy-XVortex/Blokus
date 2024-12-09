from color import color
from rules import check_limits, check_placement_rules, check_first_piece_placement
import string

# Function to display all available pieces
def display_pieces(pieces, color_code):
    """
    Displays each piece with its shape (replaces 1 with "■" and 0 with spaces).
    """
    piece_counter = 1
    max_height = max(len(piece.shape) for piece in pieces)

    # Loop through each row of the maximum height
    for i in range(max_height + 1):
        for piece in pieces:   
            if i == 0:
                for m in range(len(piece.shape[i])):
                    if m == 0:
                        if piece_counter < 10:
                            print(piece_counter, end=" ")
                        else:
                            print(piece_counter, end="")
                        piece_counter += 1
                    if 0 < m < len(piece.shape[i]):
                        print(" ", end=" ")
            if 0 < i < len(piece.shape) + 1:
                for j in range(len(piece.shape[i - 1])):
                    if piece.shape[i - 1][j] == 1:
                        # Print the piece with the corresponding color
                        if color_code == 1:
                            print(color.Cyan + "■ " + color.Black, end="")
                        elif color_code == 2:
                            print(color.Purple + "■ " + color.Black, end="")
                        elif color_code == 3:
                            print(color.Green + "■ " + color.Black, end="")
                        elif color_code == 4:
                            print(color.Red + "■ " + color.Black, end="")
                    else:
                        print(" ", end=" ")
            if i >= len(piece.shape) + 1:
                # Fill the remaining space for alignment
                print(len(piece.shape[0]) * "  ", end="")
            print(" ", end=" ")
        print("")

def display_piece_with_axes(piece, color_code):
    """
    Displays a single piece with row (numbers) and column (letters) axes.
    """
    # Generate column labels (A-T)
    column_labels = string.ascii_uppercase[:len(piece.shape[0])]

    # Print the column labels
    print("   " + " ".join(column_labels))

    # Loop through each row in the piece's shape
    for i, row in enumerate(piece.shape):
        # Print the row label (numbers)
        print(f"{i + 1:2} ", end="")

        # Print each cell in the row
        for cell in row:
            if cell == 1:
                if color_code == 1:
                    print(color.Cyan + "■ " + color.Black, end="")
                elif color_code == 2:
                    print(color.Purple + "■ " + color.Black, end="")
                elif color_code == 3:
                    print(color.Green + "■ " + color.Black, end="")
                elif color_code == 4:
                    print(color.Red + "■ " + color.Black, end="")
            else:
                print("  ", end="")
        print()  # Newline after each row

# Function to initialize the game grid
def init_grid():
    """
    Creates an empty 21x21 grid with labels for rows and columns.
    """
    letters = list(string.ascii_uppercase[:20])  # Labels for columns (A-T)
    grid = [['■ ' for _ in range(21)] for _ in range(21)]  # 21x21 grid

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Handle column labels
            if i == 0 and j > 0:
                grid[i][j] = f' {letters[j-1]}'
            # Handle row labels
            elif j == 0:
                grid[i][j] = f' {i}' if i < 10 else f'{i}'
            # Fill the rest of the grid with empty spaces
            else:
                grid[i][j] = ' ■'
    return grid

# Function to display the game grid
def display_grid(grid):
    """
    Displays the game grid with the specified colors.
    """
    for row in grid:
        print(color.Black + ''.join(row))

def highlight_valid_placements(grid, chosen_piece, current_player):
    """
    Highlights valid placements on the grid for the given piece and player.

    Args:
        grid (list): The current game grid.
        chosen_piece (Piece): The piece the player wants to place.
        current_player (Player): The current player trying to place the piece.
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            for row_piece in range(len(chosen_piece.shape)):
                for col_piece in range(len(chosen_piece.shape[0])):
                    if not current_player.has_played_first_piece:
                        if check_first_piece_placement(grid, chosen_piece, row, col, current_player.color, row_piece, col_piece):
                            grid[row][col] = color.White + " ■" + color.Black
                    else:
                        if (check_placement_rules(grid, chosen_piece, row, col, current_player.color, row_piece, col_piece) and
                            check_limits(grid, chosen_piece, row, col, current_player.color, row_piece, col_piece)):
                            grid[row][col] = color.White + " ■" + color.Black

def remove_highlight_valid_placements(grid, chosen_piece, current_player):
    """
    Remove highlights valid placements on the grid for the given piece and player.

    Args:
        grid (list): The current game grid.
        chosen_piece (Piece): The piece the player wants to place.
        current_player (Player): The current player trying to place the piece.
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            for row_piece in range(len(chosen_piece.shape)):
                for col_piece in range(len(chosen_piece.shape[0])):
                    if not current_player.has_played_first_piece:
                        if check_first_piece_placement(grid, chosen_piece, row, col, current_player.color, row_piece, col_piece):
                            grid[row][col] = color.Black + " ■" + color.Black
                    else:
                        if (check_placement_rules(grid, chosen_piece, row, col, current_player.color, row_piece, col_piece) and
                            check_limits(grid, chosen_piece, row, col, current_player.color, row_piece, col_piece)):
                            grid[row][col] = color.Black + " ■" + color.Black