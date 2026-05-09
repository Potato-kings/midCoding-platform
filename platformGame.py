import pgzrun



# window
TITLE = "Gem Hunter"
WIDTH = 800
HEIGHT = 500
# player variables 
player = Rect((200, 400), (20, 40))
velocity_y = 0
gravity = 1
on_ground = False
# platforms
platforms = [
    Rect((0, 470), (800, 30)),
    Rect((200, 380), (150, 20)),
    Rect((450, 300), (150, 20)),
    Rect((650, 220), (100, 20))
]
# colectibles
coins = [
    Rect((250, 340), (20, 20)),
    Rect((500, 260), (20, 20)),
    Rect((690, 180), (20, 20))
]
score = 0
# Hazards and goal
lava = Rect((350, 450), (100, 20))
goal = Rect((730, 420), (40, 50))
game_won = False

# Resets the player to start pos 
def reset_player():
    player.x = 100
    player.y = 400

def draw():
    # the player
    screen.clear()
    screen.draw.filled_rect(player, "orange")
    # platforms 
    for platform in platforms:
        screen.draw.filled_rect(platform, "gray")
    # collectables
    for coin in coins:
        screen.draw.filled_rect(coin, "green")
    # score
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    # Hazard and goal
    screen.draw.filled_rect(lava, "red")
    screen.draw.filled_rect(goal, "yellow")
    if game_won:
        # Win screen
        screen.draw.text("You Win!", center=(400, 250), fontsize=60, color="yellow")
def update():
    # Globaly accesable
    global velocity_y, on_ground
    global score
    global game_won

    if player.colliderect(goal):
        # Detect if won
        game_won = True
        reset_player()
            
    if player.colliderect(lava):
        #reset when touch lava
        reset_player()
        velocity_y = 0

    for coin in coins[:]:
        # Coin collection system
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
    # Gravity system
    velocity_y += gravity
    player.y += velocity_y

    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True
    # platform hitbox
    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.bottom = platform.top
            velocity_y = 0
            on_ground = True
    # Jump
    if keyboard.up and on_ground:
        velocity_y = -20
        on_ground = False
    # left
    if keyboard.left:
        player.x -= 5
    # right
    if keyboard.right:
        player.x += 5
    # screen barrier
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

pgzrun.go()
