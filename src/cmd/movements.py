class Movements:
    def __init__(self, address, map_game):
        self.address = address
        self.map_game = map_game

    def left(self):
        movement_made = False
        for row in self.map_game:
            for index_column, column in enumerate(row):
                if column == '>':
                    self.address = 'N'
                    row[index_column] = '^'
                    movement_made = True
                    break

                elif column == '^':
                    self.address = 'O'
                    row[index_column] = '<'
                    movement_made = True
                    break

                elif column == '<':
                    self.address = 'S'
                    row[index_column] = 'v'
                    movement_made = True
                    break

                elif column == 'v':
                    self.address = 'E'
                    row[index_column] = '>'
                    movement_made = True
                    break

            if movement_made:
                break
            
        return self.address



    def right(self):
        # Cambia la direccion del robot, solo direccion derecha
        movimiento_realizado = False
        for row in self.map_game:
            for index_column, column in enumerate(row):
                if column == '>':
                    direccion = 'S'
                    row[index_column] = 'v'
                    movimiento_realizado = True
                    break

                elif column == 'v':
                    direccion = 'O'
                    row[index_column] = '<'
                    movimiento_realizado = True
                    break

                elif column == '<':
                    direccion = 'N'
                    row[index_column] = '^'
                    movimiento_realizado = True
                    break

                elif column == '^':
                    direccion = 'E'
                    row[index_column] = '>'
                    movimiento_realizado = True
                    break
            if movimiento_realizado:
                break

        return self.address