import pygame
import sys
import os
from src.Game import Game
from src.ui.LevelSelectScreen import LevelSelectScreen
from src.ui.Menu import Menu
from src.ui.GameScreen import GameScreen
from src.ui.EditorScreen import EditorScreen

def main():
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 900
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("AtomicGram 1.0")
    clock = pygame.time.Clock()

    background_image = pygame.image.load(os.path.join("assets", "images", "background.jpg"))
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    game = Game(screen)
    #game.run()
    menu = Menu(game)
    game_screen = GameScreen(game)
    editor_screen = EditorScreen(game)
    level_select_screen = LevelSelectScreen(game)

    screens = {
        "menu": menu,
        "game": game_screen,
        "editor": editor_screen,
        "level_select": level_select_screen

    }
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    mouse_speed = 5
    console_controller_x, console_controller_y = pygame.mouse.get_pos()

    while True:
        current_screen = screens[game.current_screen]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Parte del mando
            if event.type == pygame.JOYAXISMOTION:
                #Derecha o izquierda
                x_axis = joystick.get_axis(0)
                #Arriba o abajo
                y_axis = joystick.get_axis(1)

                console_controller_x += x_axis * mouse_speed
                console_controller_y += y_axis * mouse_speed
                mouse_x = max(0, min(console_controller_x))
                mouse_y = max(0, min(console_controller_y))
                pygame.mouse.set_pos(mouse_x, mouse_y)
            current_screen.handle_event(event)

        current_screen.update()
        screen.blit(background_image, (0, 0))
        current_screen.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()