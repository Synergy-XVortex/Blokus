from color import color

# Function to place a piece on the grid, coloring the corresponding "■"
def place_piece(grid, piece, row, column, color_code, anchor_x, anchor_y):
    """
    Places a piece on the grid based on its shape, coordinates, color, and anchor point.
    """
    piece_height = len(piece.shape)  # Height of the piece's matrix
    piece_width = len(piece.shape[0])  # Width of the piece's matrix

    # Starting position in the grid (taking into account the anchor point)
    start_x = row - anchor_x
    start_y = column - anchor_y

    # Dictionary to map color codes to color values
    color_map = {1: color.Cyan, 2: color.Purple, 3: color.Green, 4: color.Red}
    color_code_value = color_map[color_code]

    # Loop through each cell of the piece and place it on the grid
    for x in range(piece_height):
        for y in range(piece_width):
            if piece.shape[x][y] == 1:  # Check if the cell of the piece is occupied
                # Calculate the position on the grid
                grid_x = start_x + x
                grid_y = start_y + y
                # Place the piece on the grid
                grid[grid_x][grid_y] = color_code_value + " ■" + color.Black


