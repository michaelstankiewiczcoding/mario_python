# player.py
def update(self, level):  # Pass level as parameter
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        self.vx = -self.speed
    elif keys[K_RIGHT]:
        self.vx = self.speed
    else:
        self.vx = 0
    if keys[K_SPACE] and self.on_ground:
        self.vy = self.jump_power
        self.on_ground = False
    
    # Horizontal movement
    self.x += self.vx
    self.check_collisions_x(level)
    
    # Vertical movement
    self.vy += self.gravity
    self.y += self.vy
    self.check_collisions_y(level)

def check_collisions_x(self, level):
    # Calculate tile indices player overlaps
    left = int(self.x // 32)
    right = int((self.x + self.width) // 32)
    top = int(self.y // 32)
    bottom = int((self.y + self.height) // 32)
    
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            if 0 <= x < level.width and 0 <= y < level.height:
                if level.tiles[y][x] == 1:  # Solid tile
                    if self.vx > 0:  # Moving right
                        self.x = x * 32 - self.width
                    elif self.vx < 0:  # Moving left
                        self.x = (x + 1) * 32
                    self.vx = 0

def check_collisions_y(self, level):
    left = int(self.x // 32)
    right = int((self.x + self.width) // 32)
    top = int(self.y // 32)
    bottom = int((self.y + self.height) // 32)
    
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            if 0 <= x < level.width and 0 <= y < level.height:
                if level.tiles[y][x] == 1:  # Solid tile
                    if self.vy > 0:  # Falling
                        self.y = y * 32 - self.height
                        self.vy = 0
                        self.on_ground = True
                    elif self.vy < 0:  # Jumping
                        self.y = (y + 1) * 32
                        self.vy = 0

# main.py
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    player.update(level)  # Pass level to update
    screen.fill((0, 0, 0))
    level.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
