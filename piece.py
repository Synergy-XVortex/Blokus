class Piece:
    """
    Represents a piece in the Blokus game.
    - name: The name of the piece (e.g., "Pentomino T")
    - shape: The shape of the piece in a 2D matrix.
    """
    def __init__(self, name, shape):
        self.name = name  # Name of the piece
        self.shape = shape  # Shape of the piece represented as a 2D matrix

    def rotate(self):
        """
        Rotates the piece 90 degrees clockwise.
        """
        self.shape = [list(row) for row in zip(*self.shape[::-1])]  # Rotate using zip and list reversal

    def flip(self):
        """
        Flips the piece horizontally.
        """
        self.shape = self.shape[::-1]  # Reverse the rows for horizontal symmetry

    def display(self):
        """
        Displays the piece in a text format.
        """
        print(f"Piece {self.name}:")
        for row in self.shape:
            print(" ".join(str(cell) for cell in row))  # Print each row of the piece
        print()

# Definition of all piece shapes as 2D matrices
pieces_shapes = {
    "Monomino": [
        [1]
    ],
    "Domino": [
        [1, 1]
    ],
    "Tromino droit": [
        [1, 1, 1]
    ],
    "Tromino L": [
        [1, 0],
        [1, 1]
    ],
    "Tetromino droit": [
        [1, 1, 1, 1]
    ],
    "Tetromino L": [
        [1, 0, 0],
        [1, 1, 1]
    ],
    "Tetromino T": [
        [1, 1, 1],
        [0, 1, 0]
    ],
    "Tetromino carré": [
        [1, 1],
        [1, 1]
    ],
    "Tetromino Z": [
        [1, 1, 0],
        [0, 1, 1]
    ],
    "Pentomino droit": [
        [1, 1, 1, 1, 1]
    ],
    "Pentomino W": [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
    ],
    "Pentomino X": [
        [1, 1, 0, 0],
        [0, 1, 1, 1],
    ],
    "Pentomino P": [
        [1, 1],
        [1, 1],
        [1, 0]
    ],
    "Pentomino U": [
        [1, 0, 1],
        [1, 1, 1]
    ],
    "Pentomino K": [
        [0, 1, 0, 0],
        [1, 1, 1, 1],
    ],
    "Pentomino T": [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ],
    "Pentomino L": [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1]
    ],
    "Pentomino Z": [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ],
    "Pentomino N": [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ],
    "Pentomino F": [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
    ],
    "Pentomino plus": [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
}

# Creating and displaying all pieces
pieces = [Piece(name, shape) for name, shape in pieces_shapes.items()]
