import pygame as pg


def update_screen():
    pg.display.flip()


def update_background(screen):
    screen.fill((105, 105, 105))


def player_move_right(screen, player, player_x, player_y):
    player_move_x = 50
    player_move_y = 0
    # Check if player is on screen
    if player_x > 500 - 50 or player_x < 0:
        player_move_x = -player_move_x
    if player_y > 500 - 50 or player_y < 0:
        player_move_y = - player_move_y
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


def player_move_left(screen, player, player_x, player_y):
    player_move_x = -50
    player_move_y = 0
    # Check if player is on screen
    if player_x > 500 - 50 or player_x < 0:
        player_move_x = -player_move_x
    if player_y > 500 - 50 or player_y < 0:
        player_move_y = - player_move_y
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


def player_move_down(screen, player, player_x, player_y):
    player_move_x = 0
    player_move_y = 50
    # Check if player is on screen
    if player_x > 500 - 50 or player_x < 0:
        player_move_x = -player_move_x
    if player_y > 500 - 50 or player_y < 0:
        player_move_y = - player_move_y
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


def player_move_up(screen, player, player_x, player_y):
    player_move_x = 0
    player_move_y = -50
    # Check if player is on screen
    if player_x > 500 - 50 or player_x < 0:
        player_move_x = -player_move_x
    if player_y > 500 - 50 or player_y < 0:
        player_move_y = - player_move_y
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


def main():
    # Setting up game
    pg.init()
    logo = pg.image.load("imgs/icon.png")
    pg.display.set_icon(logo)
    pg.display.set_caption("Snake")
    screen = pg.display.set_mode((500, 500))
    player = pg.image.load("imgs/player.png")
    player = pg.transform.scale(player, (50, 50))
    running = True

    # Set Background
    update_background(screen)
    # Set Player Size
    screen.blit(player, (50, 50))
    # Set Player Start Location
    player_x = 50
    player_y = 50
    # Update Screen For Start
    update_screen()

    # Main Loop
    while running:
        for event in pg.event.get():
            # Player Movement
            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_s]:  # If S Key Is Pressed
                    player_x, player_y = player_move_down(screen, player, player_x, player_y)
                if pg.key.get_pressed()[pg.K_d]:  # If D Key Is Pressed
                    player_x, player_y = player_move_right(screen, player, player_x, player_y)
                if pg.key.get_pressed()[pg.K_w]:  # If W Key Is Pressed
                    player_x, player_y = player_move_up(screen, player, player_x, player_y)
                if pg.key.get_pressed()[pg.K_a]:  # If A Key Is Pressed
                    player_x, player_y = player_move_left(screen, player, player_x, player_y)
            if event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == "__main__":
    main()
