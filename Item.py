# item.py
class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))

# main.py
from item import Item

items = [Item(180, 436)]  # Above ground
score = 0
font = pygame.font.Font(None, 36)

def check_player_item_collisions(player, items):
    global score
    for item in items[:]:
        if (player.x < item.x + item.width and
            player.x + player.width > item.x and
            player.y < item.y + item.height and
            player.y + player.height > item.y):
            items.remove(item)
            score += 10

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    player.update(level)
    for enemy in enemies:
        enemy.update(level)
    check_player_enemy_collisions(player, enemies)
    check_player_item_collisions(player, items)
    
    screen.fill((0, 0, 0))
    level.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for item in items:
        item.draw(screen)
    player.draw(screen)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
