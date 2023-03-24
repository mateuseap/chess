import pygame

class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (238, 238, 210, 255) if self.color == 'light' else (118, 150, 86, 255)
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.x * width,
            self.y * height,
            self.width,
            self.height
        )

    # Obtém a coordenada do quadrado seguindo a notação formal (ex: a3)
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        pygame.draw.rect(display, self.draw_color, self.rect)