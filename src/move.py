class Move:
    _movement_made = False

    def __init__(self, address, map_game):
        self.address = address
        self.map_game = map_game

    def advance(self):
        # Ciclo que mueve el robot segun la direccion, verificando si se encuentra con colisiones en el camino
        Move._movement_made = False

        for index_row, row in enumerate(self.map_game):
            for index_column, column in enumerate(row):

                if column == '>' and self.address == 'E':
                    # Arroja un error que cuando llega al limite derecho de la lista se inserta el robot en una posicion que no existe. es lo que genera la colision
                    try:
                        if row[index_column+1] == '*':
                            # Verifica si al lado derecho se encuentra una mina, si la hay el robot explota
                            self._movement_to_the_right(row, index_column, '#')
                            break

                        elif row[index_column+1] == 'H':
                            # Verifica si al lado derecho se encuentra la meta
                            self._movement_to_the_right(row, index_column, '@')
                            break

                        else:
                            # Si no se encnuetra niguna mina o la meta, mueve al robot una casilla a la derecha
                            self._movement_to_the_right(row, index_column, '>')
                            break

                    except IndexError:
                        # Si se intenta mover una casilla mas de la que se puede en la lista, va generar un error que esta fuera de rango, que es lo que se usa para detectar la colision 
                        row[index_column] = '#'
                        break

                elif column == '<' and self.address == 'O':
                    if index_column-1 == -1:
                        # Verifica que si llega a la colision de la izquierda y quiere continuar, el robot explota
                        row[index_column] = ' '
                        row[index_column] = '#'
                        Move._movement_made = True
                        break
                    elif row[index_column-1] == '*':
                        # Verifica si al lado izquierdo se encuentra una mina, si la ahi el robot explota
                        self._movement_to_the_left(row, index_column, '#')   
                        break

                    elif row[index_column-1] == 'H':
                        # Verifica si al lado izquierdo se encuentra una mina, si la ahi el robot explota
                        self._movement_to_the_left(row, index_column, '@')   
                        break

                    else: 
                        # El robot avanza si no encuentra colision 
                        self._movement_to_the_left(row, index_column, '<')   
                        break

                elif column == '^' and  self.address == 'N':
                   
                    self._collision(0, row, index_column, '^')

                    if Move._movement_made:
                            # Para cerrar el ciclo y no siga verificando las columnas
                            break
                    
                    if self.map_game[index_row-1][index_column] == '*':
                        # Verifica el lado superior, para saber si ahi un mina, si la ahi el robot explota
                        self._upward_movement(row, index_column, index_row,  '#')
                        break

                    elif self.map_game[index_row-1][index_column] == 'H':
                        # Verifica el lado superior, para saber si ahi un mina, si la ahi el robot explota
                        self._upward_movement(row, index_column, index_row,  '@')
                        break

                    else:
                        # Mueve el robot si no encuentra colision en direccion N
                        self._upward_movement(row, index_column, index_row,  '^')
                        break

                elif column == 'v' and self.address == 'S':
                    self._collision(-1, row, index_column, 'v')

                    if Move._movement_made:
                        break

                    if self.map_game[index_row+1][index_column] == '*':
                        # Verifica el lado inferior, para saber si ahi un mina, si la ahi el robot explota
                        self._movement_down( row, index_column, index_row,  '#')
                        break

                    elif self.map_game[index_row+1][index_column] == 'H':
                        # Verifica el lado inferior, para saber si ahi un mina, si la ahi el robot explota
                        self._movement_down( row, index_column, index_row,  '@')
                        break

                    else:
                        # Mueve el robot si no se ha encontrado en la ultima fila
                        self._movement_down( row, index_column, index_row,  'v')
                        break

            if Move._movement_made:
            # * Este bucle esta para que los movimientos en N y S no se hagan de manera infinita por los bucles internos 
                break

    def _collision(self, fila, row, index_column, robot ):

        for j in self.map_game[fila]:
            if j == robot:
                row[index_column] = '#'
                Move._movement_made = True
                break

    def _movement_to_the_right(self, row, index_column, asset):
        row[index_column] = ' '
        row[index_column+1] = asset
        Move._movement_made = True

    def _movement_to_the_left(self, row, index_column, asset):
        row[index_column] = ' '
        row[index_column-1] = asset
        Move._movement_made = True
    
    def _upward_movement(self, row, index_column, index_row,  asset):
        row[index_column] = ' '
        self.map_game[index_row-1][index_column] = asset
        Move._movement_made = True

    def _movement_down(self, row, index_column, index_row,  asset):
        row[index_column] = ' '
        self.map_game[index_row+1][index_column] = asset
        Move._movement_made = True
