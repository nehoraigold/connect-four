class Board:
    def __init__(self):
        self.matrix = self.get_empty_matrix()
        self.selected_column = None

    def display(self):
        string = '\n'.join([' '.join(row) for row in self.matrix])
        print(string)

    def select_valid_column(self):
        self.selected_column = input("\nWhat column do you choose? ")
        while not self.validate_column(self.selected_column):
            self.select_valid_column()
        return int(self.selected_column)

    def add_marker(self, player, column):
        for row in reversed(self.matrix):
            if row[column - 1] == " ":
                row[column - 1] = player.marker
                return True
        return False

    def get_empty_matrix(self):
        matrix = [[" "] * 7 for x in range(7)]
        matrix.append([str(i + 1) for i in range(7)])
        return matrix

    def validate_column(self, column):
        try:
            column = int(column)
            return all([
                1 <= column <= 7,
                not self.column_is_full(column)
            ])
        except:
            return False

    def column_is_full(self, column):
        return self.matrix[0][column - 1] != " "

    def is_full(self):
        return all([self.column_is_full(i) for i in range(len(self))])

    def has_connect_four(self):
        for row in self.matrix:
            for i in range(len(self) - 4):
                if all([
                    row[i] != " ",
                    row[i] == row[i + 1],
                    row[i] == row[i + 2],
                    row[i] == row[i + 3]
                ]):
                    return True
        # In a column
        for i in range(len(self) - 2):
            for x in range(len(self) - 4):
                if all([
                    self.matrix[x][i] != " ",
                    self.matrix[x][i] == self.matrix[x + 1][i],
                    self.matrix[x][i] == self.matrix[x + 2][i],
                    self.matrix[x][i] == self.matrix[x + 3][i]
                ]):
                    return True
        # Diagonal \
        for i in range(len(self) - 5):
            for x in range(len(self) - 4):
                if all([
                    self.matrix[x][i] != " ",
                    self.matrix[x][i] == self.matrix[x + 1][i + 1],
                    self.matrix[x][i] == self.matrix[x + 2][i + 2],
                    self.matrix[x][i] == self.matrix[x + 3][i + 3]
                ]):
                    return True
        # Diagonal /
        for i in range(len(self) - 5):
            for x in range(3, len(self) - 1):
                if all([
                    self.matrix[x][i] != " ",
                    self.matrix[x][i] == self.matrix[x - 1][i + 1],
                    self.matrix[x][i] == self.matrix[x - 2][i + 2],
                    self.matrix[x][i] == self.matrix[x - 3][i + 3]
                ]):
                    return True
        return False

    def __len__(self):
        return len(self.matrix)
