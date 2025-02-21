# player.py
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.vx = 0          # Horizontal velocity
        self.vy = 0          # Vertical velocity
        self.speed = 5
        self.jump_power = -10
        self.gravity = 0.5
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        # Horizontal movement
        if keys[K_LEFT]:
            self.vx = -self.speed
        elif keys[K_RIGHT]:
            self.vx = self.speed
        else:
            self.vx = 0
        
        # Jumping
        if keys[K_SPACE] and self.on_ground:
            self.vy = self.jump_power
            self.on_ground = False
        
        # Apply gravity
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy

        # Temporary ground collision
        if self.y > 500 - self.height:
            self.y = 500 - self.height
            self.vy = 0
            self.on_ground = True

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

# main.py
from player import Player

player = Player(100, 100)  # Start at position (100, 100)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    player.update()
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
