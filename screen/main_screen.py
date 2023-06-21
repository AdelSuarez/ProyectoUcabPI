import pygame
# from src.create_map import Create_map
from src.create_map import Create_map
import style.style as st
from src.move import Move
from src.robot_rotation import Robot_rotation
from screen.create_map_screen import Create_map_screen

class Main_screen:
    def __init__(self):
        self.address = 'E'
        self.map_game = Create_map(17,23).maker()
        # self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot.png"), (40, 40))
        self._robot= pygame.transform.scale(pygame.image.load("screen/assets/robot1.png"), (50, 50))

        self._bomb= pygame.transform.scale(pygame.image.load("screen/assets/bomba.png"), (35, 35))
        self._goal= pygame.transform.scale(pygame.image.load("screen/assets/unavainaloca.png"), (35, 35))
        self._over= pygame.transform.scale(pygame.image.load("screen/assets/explosion.png"), (45, 45))
        self._victory= pygame.transform.scale(pygame.image.load("screen/assets/victory.png"), (50, 50))

        self.settings()
        self.widget_main()

    def settings(self):
        self._game_over = False
        self._size = (1042, 772)
        pygame.init()
        self._screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption('ROBOTcok')
        self._clock = pygame.time.Clock()

    def widget_main(self):
        # self._menu()
        self._game()

    def _game(self):
         while not self._game_over:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if key == 'a':
                        Move(self.address, self.map_game).advance()
                    elif key == 'd':
                        self.address = Robot_rotation(self.address, self.map_game).right()
                    elif key == 'i':
                        self.address = Robot_rotation(self.address, self.map_game).left()

            self._screen.fill(st.BLACK)
            Create_map_screen(self.map_game, self._screen, self._robot, self.address, self._bomb, self._goal, self._victory, self._over)


            self._clock.tick(60)
            pygame.display.update()

    def _menu(self):
        #! No funciona
         while not self._game_over:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self._game_over = True
                if event.type == pygame.KEYDOWN:
                    tecla = pygame.key.name(event.key)
                    if tecla == 'a':
                        self._game_over = True
                        
                    

            self._screen.fill(st.BLACK)


            self._clock.tick(60)
            pygame.display.update()

