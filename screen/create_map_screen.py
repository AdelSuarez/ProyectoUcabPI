import pygame
import style.style as st

class Create_map_screen:
    def __init__(self, map_game, screen, robot, address, bomb, goal, victory, game_over):
        self._over = game_over
        self._victory = victory
        self._goal = goal
        self._bomb = bomb
        self.address = address
        self._robot = robot
        self._screen = screen
        self.map_game = map_game
        self.create_map()

    
    def create_map(self):
        for row in range(len(self.map_game)):
            for index_column, column in enumerate(self.map_game[row]):
                self._color_position(st.GREY, index_column, row)

                self._sensor_left( row, index_column, column)
                
                self._sensor_top( row, index_column, column)

                self._sensor_right( row, index_column, column)

                self._sensor_lower( row, index_column, column)

                if column == '>' or column == '<' or column == 'v' or column == '^':
                    self._color_robot_top( row, column, index_column)

                    self._color_robot_left( row, column, index_column)

                    self._color_robot_right( row, column, index_column)

                    self._color_robot_lower( row, column, index_column)
                                            
                    self._screen.blit(self._robot, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN-5,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-8,
                                st.HIGH,
                                st.LONG])
                    

                elif column == '*':
                    
                    self._screen.blit(self._bomb, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN+2,
                                (st.MARGIN+st.LONG) * row + st.MARGIN+5,
                                st.HIGH,
                                st.LONG])
                


                elif column == 'H':
                    self._screen.blit(self._goal, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN+2,
                                (st.MARGIN+st.LONG) * row + st.MARGIN+2,
                                st.HIGH,
                                st.LONG])
                    
                elif column == '#':
                    self._screen.blit(self._over, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-3,
                                st.HIGH,
                                st.LONG])
                    
                elif column == '@':
                    self._color_position(st.GOAL, index_column, row)
                    self._screen.blit(self._victory, [(st.MARGIN+st.HIGH) * index_column + st.MARGIN-7,
                                (st.MARGIN+st.LONG) * row + st.MARGIN-5,
                                st.HIGH,
                                st.LONG])

    def _color_position(self, color, index_column, row):
        pygame.draw.rect(self._screen,
                                color,
                                [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                                (st.MARGIN+st.LONG) * row + st.MARGIN,
                                st.HIGH,
                                st.LONG])


    def _collesion(self, robot, index_column, row, fila):
        for j in self.map_game[fila]:
            if j == robot:
                pygame.draw.rect(self._screen,
                    st.GREY,
                    [(st.MARGIN+st.HIGH) * index_column + st.MARGIN,
                    (st.MARGIN+st.LONG) * row + st.MARGIN,
                    st.HIGH,
                    st.LONG])
                break

    def _error_collesion_right(self, row, index_column):
        for j in self.map_game[row][-1]:
            if j =='>':
                self._color_position(st.WHITE, index_column, row)
                break

    def _sensor_left(self, row, index_column, column):
        try:
            if self.map_game[row][index_column+1] == '<' and column == ' ' and self.address == 'O':
                self._color_position(st.GREEN_ROBOT, index_column, row)

            elif self.map_game[row][index_column+1] == '<' and column == '*' and self.address == 'O':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif self.map_game[row][index_column+1] == '<' and column == 'H' and self.address == 'O':
                self._color_position(st.GOAL, index_column, row)

        except Exception:
            pass
    
    def _sensor_right(self, row, index_column, column):
        if self.map_game[row][index_column-1] == '>' and column == ' ' and self.address == 'E':
            self._color_position(st.GREEN_ROBOT, index_column, row)
            self._error_collesion_right(row, index_column)
            
        elif self.map_game[row][index_column-1] == '>' and column == '*' and self.address == 'E':
            self._color_position(st.RED_SCREEN, index_column, row)
            self._error_collesion_right(row, index_column)

        elif self.map_game[row][index_column-1] == '>' and column == 'H' and self.address == 'E':
            self._color_position(st.GOAL, index_column, row)

    def _sensor_top(self, row, index_column, column):
        try:
            if self.map_game[row+1][index_column] == '^' and column == ' ' and self.address == 'N':
                self._color_position(st.GREEN_ROBOT, index_column, row)

            elif self.map_game[row+1][index_column] == '^' and column == '*' and self.address == 'N':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif self.map_game[row+1][index_column] == '^' and column == 'H' and self.address == 'N':
                self._color_position(st.GOAL, index_column, row)
                
        except Exception:
            pass

    def _sensor_lower(self, row, index_column, column):
        if self.map_game[row-1][index_column] == 'v' and column == ' ' and self.address == 'S':
            self._color_position(st.GREEN_ROBOT, index_column, row)
            self._collesion('v', index_column, row, -1)

        elif self.map_game[row-1][index_column] == 'v' and column == '*' and self.address == 'S':
            self._color_position(st.RED_SCREEN, index_column, row)
            self._collesion('v', index_column, row, -1)
            
        elif self.map_game[row-1][index_column] == 'v' and column == 'H' and self.address == 'S':
            self._color_position(st.GOAL, index_column, row)

    def _color_robot_top(self, row, column, index_column):
        if column == '^' and (self.map_game[row-1][index_column] == '*' or row == 0):
            self._color_position(st.RED_SCREEN, index_column, row)

        elif column == '^' and self.map_game[row-1][index_column] == 'H':
            self._color_position(st.GOAL, index_column, row)
            
        else:
            self._color_position(st.GREEN_ROBOT, index_column, row)

    def _color_robot_left(self, row, column, index_column):
        if index_column-1 == -1 and self.address == 'O':
            self._color_position(st.RED_SCREEN, index_column, row)

        elif column == '<' and self.map_game[row][index_column-1] == '*' :
            self._color_position(st.RED_SCREEN, index_column, row)

        elif column == '<' and self.map_game[row][index_column-1] == 'H' :
            self._color_position(st.GOAL, index_column, row)

    def _color_robot_right(self, row, column, index_column):
        try:
            if column == '>' and self.map_game[row][index_column+1] == '*':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif column == '>' and self.map_game[row][index_column+1] == 'H':
                self._color_position(st.GOAL, index_column, row)
                
        except  IndexError:
            self._color_position(st.RED_SCREEN, index_column, row)


    def _color_robot_lower(self, row, column, index_column):
        try:
            if column == 'v' and self.map_game[row+1][index_column] == '*':
                self._color_position(st.RED_SCREEN, index_column, row)

            elif column == 'v' and self.map_game[row+1][index_column] == 'H':
                self._color_position(st.GOAL, index_column, row)

        except  IndexError:
            self._color_position(st.RED_SCREEN, index_column, row)  