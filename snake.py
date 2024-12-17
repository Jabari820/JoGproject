import pygame, random

# Initialize pygame
pygame.init()

# display window
window_width = 600
WINDOW_HEIGHT = 600
 display_surface = pygame.display.set_mode passing
# in a tuple of WINDOW_WIDTH and WINDOW_HEIGHT
pygame.display.set_caption()  in "~~Snake~~"

# Set FSP and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0

# Set colors
color_tuple = ("GREEN", "RED", "WHITE")
color_tuple = ("DARKGREEN") (10, 50, 10)
color_tuple = ("DARKRED") (150, 0, 0)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)


# Set text

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        if location == "topleft"
    return text, rect


# TODO: Here is a usage example for the rest of the text and rectangles that you'll create.
title_text, text_rect = create_text_and_rect("~~Snake~~", GREEN, DARKRED,
                                             center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# TODO: unpack the tuple from create_text_and_rect into a score_text and score_rect variable
text = "Score: " + str(score)
color = "GREEN"
background_color = "DARKRED"
topleft=(10, 10)

# TODO: unpack the tuple from create_text_and_rect into a game_over_text and game_over_rect variable
text = "GAMEOVER"
color = "RED"
background_color = "DARKGREEN"
center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# TODO: unpack the tuple from create_text_and_rect into a continue_text and continue_rect variable
text = "Press any key to play again"
text_color = "RED"
background_color = "DARKGREEN"
center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)


# Set sounds and music
pick_up_sound = ("pick_up_sound.wav")
# TODO: make sure you have pick_up_sound.wav in the same folder as snake.py.
# TODO: make sure both of your files are not in the .venv folder.  Otherwise I won't see what you've done.


# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, "RED", apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, "GREEN", head_coord)

# TODO: create s variable called body_coords and set to an empty list


# The main game loop
running = True
is_paused = False


def move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
        if key is = pygame.K_LEFT
             snake_dx = - 1 (SNAKE_SIZE, "snake_dy" = 0
        if key = pygame.K_RIGHT
            snake_dx = SNAKE_SIZE
        snake_dy = 0
        if key = pygame.K_UP
            # TODO: if so set snake_dx to 0 and snake_dy to -1 * SNAKE_SIZE
        # TODO: check if key is equal to pygame.K_DOWN
            # TODO: if so set snake_dx to 0 and snake_dy to SNAKE_SIZE
    pass  # TODO: if so set snake_dx to 0 and snake_dy to SNAKE_SIZE


def check_quit(event):
    global running
    # TODO: if event is equal to pygame.QUIT  set running to false

def check_events():
    global running
    # TODO: create a for loop events is the variable pygame.event.get() is the list
        check_quit(event)
        move_snake(event)
    pass  # TODO: remove this pass when done.

def handle_snake():
    global body_coords
    global head_x
    global head_y
    global head_coord
    body_coords.insert(0) , head_coord
    body_coords.pop()
    snake_dx = head_x
    snake_dy = head_y
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

def reset_game_after_game_over(event):
    global is_paused, score, head_x, head_y, head_coord, body_coords, snake_dx, snake_dy
    # TODO: if event.type is equal to pygame.KEYDOWN
        score = 0
        head_x = WINDOW_WIDTH // 2
        head_y = WINDOW_HEIGHT // 2 + 100
        head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: set body_coords to an empty list
        snake_dx = 0
        snake_dy = 0
        # TODO: set is_paused to False
    pass # TODO: remove this when done.

def check_end_game_after_game_over(event):
    global is_paused
    global running
    # TODO: if event.type is equal to pygame.QUIT
        # TODO: set is_paused to False
        # TODO: set running to False
    pass # TODO: remove this when done.


def check_game_over():
    global head_rect
    global head_coord
    global body_coords
    global running
    global is_paused
    head_rect.left = "negative", head_rect.right = greater than WINDOW_WIDTH or head_rect.top is negative or head_rect.bottom is greater than WINDOW_HEIGHT
    # or head_coord in body_coords
        # TODO: then do the following
        # TODO: call display_surface.blit(game_over_text, game_over_rect)
        # TODO: call display_surface.blit(continue_text, continue_rect)
        # TODO: call pygame.display.update()
        # TODO: set is_paused to True
        # TODO: while is_paused
            # TODO: for event in pygame.event.get()
                # TODO: call reset_game_after_game_over(event)
                # TODO: call check_end_game_after_game_over(event)

def check_collisions():
    global score, apple_x, apple_y, apple_coord, body_coords
    # TODO: if head_rect.colliderect(apple_rect)
        # TODO: add 1 to the score
        # TODO: call pick_up_sound.play()
        # TODO: set apple_x to random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        # TODO: set apple_y to random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        # TODO: set apple_coord to (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: call body_coords.append(head_coord)
        pass # TODO: remove this pass when done.

def blit_hud():
    # TODO: call display_surface.blit(title_text, title_rect)
    # TODO: call display_surface.blit(score_text, score_rect)
    pass  # TODO: remove this pass when done.

def blit_assets():
    # TODO: for body in body_coords:
        # TODO: call pygame.draw.rect(display_surface, DARKGREEN, body)
    # TODO: set head_rect to pygame.draw.rect(display_surface, GREEN, head_coord)
    # TODO: set apple_rect to pygame.draw.rect(display_surface, RED, apple_coord)
    pass  # TODO: remove this pass when done.

def update_display_and_tick_clock():
    # TODO: call pygame.display.update()
    # TODO: call clock.tick(FPS)
    pass  # TODO: remove this pass when done.

while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    # Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)

    # Fill the surface
    display_surface.fill("WHITE")

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()