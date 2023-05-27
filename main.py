import pygame, sys

from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Solitaire")

red = pygame.Color(255, 0, 0)
darkgreen = pygame.Color(86, 100, 86)
green = pygame.Color(166, 178, 162)
blue = pygame.Color(7, 11, 61)
cream = pygame.Color(231, 231, 221)



BG = pygame.image.load("assets/Background.png")
GBG = pygame.image.load("assets/GameBackground.png")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("BLACK")
        SCREEN.blit(GBG, (0, 0))

        PLAY_TEXT = get_font(30).render("Solitaire", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(60, 25))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(1220, 25),
                           text_input="Menu", font=get_font(25), base_color="White", hovering_color="#e3aacc")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="e3aacc")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(150).render("Solitaire", True, "#870955")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Button.png"), pos=(300, 250),
                             text_input="PLAY", font=get_font(50), base_color="#e3aacc", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Button.png"), pos=(300, 400),
                                text_input="OPTIONS", font=get_font(50), base_color="#e3aacc", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Button.png"), pos=(300, 550),
                             text_input="QUIT", font=get_font(50), base_color="#e3aacc", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()