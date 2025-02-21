# level.py
class Level:
    def __init__(self, width, height):
        self.tile_size = 32
        self.width = width
        self.height = height
        # Simple level: ground at bottom, one platform
        self.tiles = [[0 for _ in range(width)] for _ in range(height)]
        for x in range(width):
            self.tiles[height-1][x] = 1  # Ground
        self.tiles[height-3][5] = 1      # Platform at x=5, two tiles above ground

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[y][x] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (x * 32, y * 32, 32, 32))

# main.py
from level import Level

level = Level(25, 19)  # 25 tiles wide, 19 tiles high (fits 800x600 at 32px/tile)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    player.update()
    screen.fill((0, 0, 0))
    level.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
