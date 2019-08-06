import pygame as pg


def update_screen():
    pg.display.flip()


def update_background(screen):
    screen.fill((105, 105, 105))


def player_move(screen, player, player_x, player_y, player_move_x, player_move_y):
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


def food(screen):
    food_x = 150
    food_y = 150
    pg.draw.rect(screen, (255, 0, 0), pg.Rect(food_x, food_y, 50, 50))
    update_screen()
    return food_x, food_y


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
    eaten = False
    update_background(screen)
    screen.blit(player, (0, 0))
    player_x = 0
    player_y = 0
    food_x, food_y = food(screen)
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
            if (food_x == player_x) and (food_y == player_y):
                eaten = True
            if not eaten:
                food_x, food_y = food(screen)

            # End Check
            if event.type == pg.QUIT:
                running = False


if __name__ == "__main__":
    main()
