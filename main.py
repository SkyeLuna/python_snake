import pygame as pg
from random import randint
import math

def roundup(x):
    return int(math.ceil(x / 50.0)) * 50


def update_screen():
    pg.display.flip()


def update_background(screen):
    screen.fill((105, 105, 105))


def player_move(screen, player, player_x, player_y, player_move_x, player_move_y):
    # Check if player is on screen
    if (player_x == 0) and (player_move_x == -50):
        return player_x, player_y
    elif (player_y == 0) and (player_move_y == -50):
        return player_x, player_y
    elif (player_x == 450) and (player_move_x == 50):
        return player_x, player_y
    elif (player_y == 450) and (player_move_y == 50):
        return player_x, player_y
    # Move Player
    player_x += player_move_x
    player_y += player_move_y
    # Remove Old Player Pos
    update_background(screen)
    # Update Screen
    update_screen()
    # Trigger Player Move
    screen.blit(player, (player_x, player_y))
    # Update Screen
    update_screen()
    # Return New Location
    return player_x, player_y


def food(foodpos, screen):
    pg.draw.rect(screen, (255, 0, 0), pg.Rect(foodpos[0], foodpos[1], 50, 50))
    update_screen()


def main():
    # Setting up game
    pg.init()
    logo = pg.image.load("imgs/icon.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("Snake")

    screen_x = 500
    screen_y = 500

    screen = pg.display.set_mode((screen_x, screen_y))
    player = pg.image.load("imgs/player.png")
    player = pg.transform.scale(player, (50, 50))
    running = True
    update_background(screen)
    screen.blit(player, (0, 0))
    player_x = 0
    player_y = 0
    foodpos = [roundup(randint(0, screen_x-50)), roundup(randint(0, screen_y-50))]
    food(foodpos, screen)
    update_screen()

    # Main Loop
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                # Player Movement
                if pg.key.get_pressed()[pg.K_s]:  # If S Key Is Pressed
                    player_x, player_y = player_move(screen, player, player_x, player_y, 0, 50)
                if pg.key.get_pressed()[pg.K_d]:  # If D Key Is Pressed
                    player_x, player_y = player_move(screen, player, player_x, player_y, 50, 0)
                if pg.key.get_pressed()[pg.K_w]:  # If W Key Is Pressed
                    player_x, player_y = player_move(screen, player, player_x, player_y, 0, -50)
                if pg.key.get_pressed()[pg.K_a]:  # If A Key Is Pressed
                    player_x, player_y = player_move(screen, player, player_x, player_y, -50, 0)
                # End Player Movement
                # Player Simple Exit
                if pg.key.get_pressed()[pg.K_ESCAPE]:
                    running = False
                # End Player Simple Exit

            # Checking if player touches food
            if (foodpos[0] == player_x) and (foodpos[1] == player_y):
                foodpos = [roundup(randint(0, screen_x-50)), roundup(randint(0, screen_y-50))]
                food(foodpos, screen)
            else:
                food(foodpos, screen)

            # End Check
            if event.type == pg.QUIT:
                running = False


if __name__ == "__main__":
    main()
