from classes.Square import Square

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 8
        self.tile_height = height // 8
        self.squares = self.generate_squares()

    def generate_squares(self):
        squares = []
        
        for x in range(8):
            for y in range(8):
                squares.append(Square(x,  y, self.tile_width, self.tile_height))
        
        return squares
    
    def draw(self, display):
        for square in self.squares:
            square.draw(display)