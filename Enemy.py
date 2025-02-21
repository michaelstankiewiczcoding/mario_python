# enemy.py
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.vx = -2  # Move left initially
        self.vy = 0

    def update(self, level):
        self.x += self.vx
        # Simple AI: reverse direction at platform edges or walls (to be implemented)
        self.y += self.vy  # For gravity if needed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 165, 0), (self.x, self.y, self.width, self.height))

# main.py
from enemy import Enemy

enemies = [Enemy(200, 468)]  # Start on ground (500 - 32)

def check_player_enemy_collisions(player, enemies):
    for enemy in enemies[:]:
        if (player.x < enemy.x + enemy.width and
            player.x + player.width > enemy.x and
            player.y < enemy.y + enemy.height and
            player.y + player.height > enemy.y):
            if player.vy > 0 and player.y + player.height - enemy.y < 10:  # Jumped on top
                enemies.remove(enemy)
            else:  # Side collision
                print("Player hurt!")  # Placeholder for damage

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    player.update(level)
    for enemy in enemies:
        enemy.update(level)
    check_player_enemy_collisions(player, enemies)
    
    screen.fill((0, 0, 0))
    level.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
