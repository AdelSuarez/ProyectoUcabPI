import pygame
import assets.Assets as asset
import style.style as st
from components.Button import Button
from components.Text import Text
from screen.Screen_game import Screen_game


class Screen_menu:
    def __init__(self, game_over, game_pause, address, map_game) -> None:
        self._font = pygame.font.Font("assets/font.ttf", 100)
        self._font_v = pygame.font.Font("assets/font.ttf", 20)

        self.game_over = game_over
        self.game_pause = game_pause
        self.address = address
        self.map_game = map_game

    def menu(self, screen):
        while not self.game_over:
            screen.fill((52,78,91))

            if self.game_pause:
                #game
                Screen_game(self.game_over, self.address, self.map_game, self.game_pause).game(screen)
            else:
                # Menu
                Text('ROBOTcok', self._font, st.WHITE).draw_text(screen, 130,80)
                Text('v2.4.5.1', self._font_v, st.GREEN_ROBOT).draw_text(screen, 870,780)
                if Button(300, 300, asset.btn_start, 1.5).draw(screen):
                    self.game_pause = True
                elif Button(390,650,asset.btn_exit,1).draw(screen):
                    pygame.quit()

                    self.game_over = True

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_pause = True
                    
            pygame.display.update()