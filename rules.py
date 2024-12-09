from color import color

def check_first_piece_placement(grid, piece, row, col, color_ID, anchor_x, anchor_y):
    """
    Checks that the first piece is correctly placed in its assigned corner 
    without exceeding the grid or touching the first row or column (used as references).
    
    Args:
        grid (list of list of int): The game grid.
        piece (Piece): The piece being placed.
        row (int): The row to place the piece.
        col (int): The column to place the piece.
        color_ID (int): The ID of the color of the piece.
        anchor_x (int): The x offset for the anchor point within the piece.
        anchor_y (int): The y offset for the anchor point within the piece.
    
    Returns:
        bool: True if the piece is correctly placed in its assigned corner, False otherwise.
    """
    # Dictionary of allowed corners for the first piece of each color
    allowed_corners = {
        1: (1, 1),  # Cyan - top-left corner
        2: (1, len(grid[0]) - 1),  # Purple - top-right corner
        3: (len(grid) - 1, len(grid[0]) - 1),  # Green - bottom-right corner
        4: (len(grid) - 1, 1),  # Red - bottom-left corner
    }

    # Get the assigned corner for the given color
    corner_row, corner_col = allowed_corners[color_ID]

    # Calculate the actual starting coordinates by adjusting for the anchor
    start_x = row - anchor_x
    start_y = col - anchor_y

    # Check if the piece exceeds the grid or touches the first row or column
    piece_height = len(piece.shape)
    piece_width = len(piece.shape[0])

    if color_ID == 1:
        if anchor_x != 0 or anchor_y != 0:
            return False
    if color_ID == 2:
        if anchor_x != 0 or anchor_y != piece_width - 1:
            return False
    if color_ID == 3:
        if anchor_x != piece_height - 1 or anchor_y != piece_width - 1:
            return False
    if color_ID == 4:
        if anchor_x != piece_height - 1 or anchor_y != 0:
            return False

    for x in range(piece_height):
        for y in range(piece_width):
            if piece.shape[x][y] == 1:
                grid_x = start_x + x
                grid_y = start_y + y

                # Check if the piece is within the grid bounds (excluding first row and column)
                if grid_x < 1 or grid_y < 1 or grid_x >= len(grid) or grid_y >= len(grid[0]):
                    return False

                # Ensure the piece touches the assigned corner
                if (grid_x, grid_y) == (corner_row, corner_col):
                    return True

    # If no '1' in the correct corner, return False
    return False

def check_limits(grid, piece, row, col, color_ID, anchor_x, anchor_y):
    """
    Checks that the piece is fully inside the grid boundaries
    and does not overlap with other pieces.
    """
    piece_height = len(piece.shape)
    piece_width = len(piece.shape[0])
    start_x = row - anchor_x
    start_y = col - anchor_y

    for x in range(piece_height):
        for y in range(piece_width):
            if piece.shape[x][y] == 1:
                grid_x = start_x + x
                grid_y = start_y + y
                
                # Check grid boundaries
                if grid_x < 0 or grid_x >= len(grid) or grid_y < 0 or grid_y >= len(grid[0]):
                    return False

                # Check for overlap
                if grid[grid_x][grid_y] != " ■" and not grid[grid_x][grid_y].startswith(color.White) and not grid[grid_x][grid_y].startswith(color.Black):
                    return False

    return True

def check_placement_rules(grid, piece, row, col, color_ID, anchor_x, anchor_y):
    """
    Checks the placement rules:
    - Pieces must touch at least one corner of a piece of the same color.
    - Pieces must not be adjacent by edges to a piece of the same color.
    - The anchor point must touch a corner of the same color piece.
    """
    if piece.shape[anchor_x][anchor_y] == 0:
        return False
    
    corner_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    edge_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    touches_corner = False
    color_mapping = {1: color.Cyan, 2: color.Purple, 3: color.Green, 4: color.Red}
    color_code = color_mapping[color_ID]

    piece_height = len(piece.shape)
    piece_width = len(piece.shape[0])
    start_x = row - anchor_x
    start_y = col - anchor_y

    # Ensure that the anchor point is touching a corner of a piece of the same color
    anchor_grid_x = start_x + anchor_x
    anchor_grid_y = start_y + anchor_y

    for dx, dy in corner_directions:
        a, b = anchor_grid_x + dx, anchor_grid_y + dy
        if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b].startswith(color_code):
            touches_corner = True
            break

    if not touches_corner:
        return False

    # Check the rest of the piece placement
    for x in range(piece_height):
        for y in range(piece_width):
            if piece.shape[x][y] == 1:
                grid_x = start_x + x
                grid_y = start_y + y

                # Check edge adjacency to same color piece
                for dx, dy in edge_directions:
                    a, b = grid_x + dx, grid_y + dy
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                        if grid[a][b].startswith(color_code):
                            return False

    return True

def can_player_play(grid, player):
    """
    Checks if the given player can make any valid move with their remaining pieces.

    Args:
        grid (list): The current game grid.
        player (Player): The player to check for possible moves.

    Returns:
        bool: True if the player can play, False otherwise.
    """
    for remaining_piece in player.remaining_pieces:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                for row_piece in range(len(remaining_piece.shape)):
                    for col_piece in range(len(remaining_piece.shape[0])):
                        if player.has_played_first_piece:
                            if (check_placement_rules(grid, remaining_piece, row, col, player.color, row_piece, col_piece) and
                                check_limits(grid, remaining_piece, row, col, player.color, row_piece, col_piece)):
                                return True
                        else:
                            if check_first_piece_placement(grid, remaining_piece, row, col, player.color, row_piece, col_piece):
                                return True
    return False
