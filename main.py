# Import necessary modules
import string
from piece import pieces  # List of pieces defined in pieces.py
from display import display_pieces, display_piece_with_axes, display_grid, init_grid, highlight_valid_placements, remove_highlight_valid_placements
from piece_placement import place_piece
from rules import check_limits, check_placement_rules, check_first_piece_placement, can_player_play
from color import color
import copy  # For deep copying pieces

# Class representing a player
class Player:
    def __init__(self, name, color):
        """
        Initialize a player with a name, color, and a list of available pieces.
        """
        self.name = name
        self.color = color
        self.remaining_pieces = copy.deepcopy(pieces)  # Independent copy of pieces for each player
        self.has_played_first_piece = False  # Tracks if the player has played their first piece

# Main function for the game flow
def run_game():
    # Initialize the grid and players
    grid = init_grid()
    players = []
    used_names = []
    player_number = 1

    # Ask for the number of players
    while True:
        try:
            num_players = int(input("Choose the number of players (2 or 4): "))
            if num_players not in [2, 4]:
                print("Invalid number of players. Please choose 2 or 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Collect player names and ensure no duplicates
    for player_number in range(1, num_players + 1):
        while True:
            player_name = input(f"Choose player {player_number}'s name: ")
            if player_name.lower() in used_names:
                print("This name is already taken, please choose another one.")
            else:
                used_names.append(player_name.lower())
                players.append(Player(player_name, player_number))
                break

    if num_players == 2:
        players.append(Player(players[0].name, 3))
        players.append(Player(players[1].name, 4))

    # Initial display
    print("\nGame start! Here's the game grid:")

    # Main game loop
    turn = 0
    while True:
        current_player = players[turn % len(players)]

        # Display the current player with the corresponding color
        if current_player.color == 1:
            display_color = "\033[96m"  # Cyan
        elif current_player.color == 2:
            display_color = "\033[35m"  # Purple
        elif current_player.color == 3:
            display_color = "\033[32m"  # Green
        elif current_player.color == 4:
            display_color = "\033[31m"  # Red

        highlight_valid_placements(grid, pieces[0], current_player)
        display_grid(grid)
        remove_highlight_valid_placements(grid, pieces[0], current_player)

        print(f"\n{display_color}{current_player.name}, it's your turn!\033[0m")  # Reset color after display

        # Check if the player has any remaining pieces
        if not current_player.remaining_pieces:
            print(f"{current_player.name} has no remaining pieces.")
            turn += 1
            continue

        # Display remaining pieces for this player
        print("Remaining pieces:")
        display_pieces(current_player.remaining_pieces, current_player.color)  # Display pieces

        # Ask the player to choose a piece
        try:
            piece_choice = int(input("Choose a piece (number): ")) - 1
            chosen_piece = current_player.remaining_pieces[piece_choice]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        # Display the piece before transformations
        print("Here is the piece before transformation:")
        display_piece_with_axes(chosen_piece, current_player.color)

        # Ask if the player wants to rotate or apply symmetry to the piece
        transformation_completed = False
        while not transformation_completed:
            print("\nDo you want to perform a transformation on the piece?")
            print("1. Rotate the piece 90°, -90° or 180°")
            print("2. Apply horizontal symmetry")
            print("3. No transformation, validate the piece\n")

            try:
                transformation_choice = int(input("Choose an option (1, 2, or 3): "))
                if transformation_choice == 1:
                    print("1. Rotate 90°")
                    print("2. Rotate -90°")
                    print("3. Rotate 180°\n")
                    rotation_choice = int(input("Choose an option (1, 2, or 3): "))
                    if rotation_choice == 1:
                        chosen_piece.rotate()
                        print("Piece rotated 90°.")
                    elif rotation_choice == 2:
                        for _ in range(3):
                            chosen_piece.rotate()
                        print("Piece rotated -90°.")
                    elif rotation_choice == 3:
                        for _ in range(2):
                            chosen_piece.rotate()
                        print("Piece rotated 180°.")
                    display_piece_with_axes(chosen_piece, current_player.color)  # Display the piece after rotation

                elif transformation_choice == 2:
                    chosen_piece.flip()
                    print("Horizontal symmetry applied to the piece.")
                    display_piece_with_axes(chosen_piece, current_player.color)  # Display the piece after symmetry

                elif transformation_choice == 3:
                    transformation_completed = True
                    print("No transformation, validating the piece.")
                else:
                    print("Invalid option, no transformation performed.")
            except ValueError:
                print("Invalid choice. No transformation performed.")

        # Ask for the piece placement position
        try:
            highlight_valid_placements(grid, chosen_piece, current_player)
            display_grid(grid)
            remove_highlight_valid_placements(grid, chosen_piece, current_player)

            row_input = int(input("\nEnter the row to place the piece (1-20): "))
            col_input = ord(input("Enter the column to place the piece (A-T): ").upper()) - ord('A') + 1

            number_range = len(chosen_piece.shape)
            column_labels = string.ascii_uppercase[:len(chosen_piece.shape[0])]
            letter_range = column_labels[len(chosen_piece.shape[0]) - 1]
            anchor_x = int(input(f"Enter the row for the piece anchor (1-{number_range}): ")) - 1
            anchor_y = ord(input(f"Enter the column for the piece anchor (A-{letter_range}): ").upper()) - ord('A')
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        # Check if it's the player's first piece
        if not current_player.has_played_first_piece:
            is_valid = check_first_piece_placement(grid, chosen_piece, row_input, col_input, current_player.color, anchor_x, anchor_y)
        else:
            is_valid = (check_limits(grid, chosen_piece, row_input, col_input, current_player.color, anchor_x, anchor_y) and
                        check_placement_rules(grid, chosen_piece, row_input, col_input, current_player.color, anchor_x, anchor_y))

        if is_valid:
            place_piece(grid, chosen_piece, row_input, col_input, current_player.color, anchor_x, anchor_y)
            current_player.has_played_first_piece = True
            current_player.remaining_pieces.remove(chosen_piece)
            print(f"Piece successfully placed by {current_player.name}!")
        else:
            print(f"\n{display_color}Invalid placement. Please try again.\033[0m")
            continue

        # Move to the next player
        turn += 1

        # End condition: If no player can play, the game ends
        if all(not player.remaining_pieces for player in players):
            print("The game is over!")
            break

    # Calculate scores (based on remaining pieces)
    print("\nCalculating scores...")
    for player in players:
        score = sum(len(piece.shape) for piece in player.remaining_pieces)

        # Display the score with the corresponding color
        if player.color == 1:
            display_color = "\033[96m"  # Cyan
        elif player.color == 2:
            display_color = "\033[35m"  # Purple
        elif player.color == 3:
            display_color = "\033[31m"  # Red
        elif player.color == 4:
            display_color = "\033[32m"  # Green

        print(f"{display_color}{player.name}\033[0m : {score} points")  # Reset color after display
    print("Thank you for playing!")

# Program entry point
if __name__ == "__main__":
    run_game()
