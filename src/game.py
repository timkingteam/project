from src.map import *
from src.varuables import *
from src.GhostClass import Ghost
from src.PacmanClass import Pacman
import pygame


class Game:
    def __init__(self):
        self.pygame_modules()
        self.generate()
        self.run()

    def pygame_modules(self):
        pygame.font.init()

    def generate(self):
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_event = 'OpenScreen'
        self.coins = []
        self.coin_number = TOTAL_COINS
        GENERATE_WALLS()
        self.pacman = Pacman(START_POSITION, NORMAL_SPEED, self)
        self.ghosts = []
        self.MakeGhosts()
        self.map = pygame.image.load('./images/map.png')
        self.map = pygame.transform.scale(self.map, (WIDTH, HEIGHT))
        self.pacman_img = pygame.image.load('./images/pacman.png')
        self.pacman_img = pygame.transform.scale(
            self.pacman_img, (200, 200))

    def run(self):
        while (True):
            pygame.display.update()
            match(self.current_event):
                case 'OpenScreen':
                    self.OpenScreen()
                case 'MainEvent':
                    self.MainEvent()
                case 'WinScreen':
                    self.WinScreen()
                case 'LoseScreen':
                    self.LoseScreen()
            self.clock.tick(TICK_TIME)

    ########### Events ############
    def OpenScreen(self):
        self.OpenDraw()
        self.OpenKeyboard()

    def MainEvent(self):
        self.PlayDraw()
        self.PlayKeyboard()
        self.PlayUpdate()

    def WinScreen(self):
        self.WinDraw()
        self.WinKeyboard()

    def LoseScreen(self):
        self.LoseDraw()
        self.LoseKeyboard()

    ########## Sub Events ############

    ## Main ##
    def PlayDraw(self):
        self.gameDisplay.blit(self.map, (0, 0))
        for coin in self.coins:
            self.DrawCoin(coin)
        self.DrawScore(TOTAL_COINS - self.coin_number)
        self.pacman.Draw()
        for ghost in self.ghosts:
            ghost.Draw()

    def PlayKeyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match(event.key):
                    case pygame.K_UP:
                        self.pacman.MoveUp()
                    case pygame.K_RIGHT:
                        self.pacman.MoveRight()
                    case pygame.K_DOWN:
                        self.pacman.MoveDown()
                    case pygame.K_LEFT:
                        self.pacman.MoveLeft()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def PlayUpdate(self):
        self.UpdateCoins()
        self.pacman.Update()
        for ghost in self.ghosts:
            ghost.Update()
            if self.pacman.pos == ghost.pos:
                self.pacman.Die()
        if self.pacman.dead:
            self.current_event = 'LoseScreen'

    ## Open ##

    def OpenKeyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.current_event = 'MainEvent'
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def OpenDraw(self):
        self.set_big_font()
        self.draw_text("Pacman", WHITE, WIDTH//2 - 50, 50)
        self.set_small_font()
        self.draw_text("Press space to start the game", WHITE,
                       WIDTH//2 - 100, HEIGHT - 100)
        self.gameDisplay.blit(
            self.pacman_img, (HEIGHT//2 - 100, WIDTH//2 - 100))

    ## WinScreen ##
    def WinDraw(self):
        self.gameDisplay.fill(BLACK)
        self.set_big_font()
        self.draw_text("You Win", GREEN,
                       WIDTH//2 - 50, HEIGHT//2 - 50)

    def WinKeyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    ## LoseScreen ##
    def LoseDraw(self):
        self.gameDisplay.fill(BLACK)
        self.set_big_font()
        self.draw_text("You Lose",
                       RED, WIDTH//2 - 60, HEIGHT//2 - 50)

    def LoseKeyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    ########## Stuff ###############
    def draw_text(self, text, color, posX, posY):
        text_surface = self.my_font.render(text, False, color)
        self.gameDisplay.blit(text_surface, (posX, posY))

    def set_small_font(self):
        self.my_font = pygame.font.SysFont('arial', 16, bold=True)
        pygame.font.Font.bold

    def set_big_font(self):
        self.my_font = pygame.font.SysFont('arial', 32, bold=True)
        pygame.font.Font.bold

    def DrawScore(self, score):
        self.set_small_font()
        self.draw_text("SCORE: {}".format(score), WHITE,
                       WIDTH//2 - 40, 0)

    def DrawCoin(self, coin):
        pos = Vector2(
            coin.x * CELL_SIZE + CELL_SIZE//2, coin.y * CELL_SIZE + CELL_SIZE//2)
        pygame.draw.circle(self.gameDisplay, PEACH,
                           (pos.x, pos.y), CELL_SIZE//4)

    def UpdateCoins(self):
        self.coins = []
        self.coin_number = 0
        for x in range(0, 27):
            for y in range(0, 27):
                if MAP[y][x] == 0:
                    self.coins.append(Vector2(x, y))
                    self.coin_number += 1
        if self.coin_number == 0:
            self.current_event = 'WinScreen'

    def MakeGhosts(self):
        pass
        self.ghosts.append(
            Ghost(GHOST1_POSITION, NORMAL_SPEED, 'Normal', RED, self))
        self.ghosts.append(
            Ghost(GHOST2_POSITION, NORMAL_SPEED, 'DownRight', PINK, self))
        self.ghosts.append(
            Ghost(GHOST3_POSITION, NORMAL_SPEED, 'DownLeft', ORANGE, self))
        self.ghosts.append(
            Ghost(GHOST4_POSITION, SLOW_SPEED, 'Normal', CYAN, self))
