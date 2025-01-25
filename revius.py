class TicTacToe:
    def __init__(self):
        self.grid = [i for i in range(9)]
        self.current_user = 'P'
    
    def display_grid(self):
        print()
        print(f"""
         ---+---+---
        | {self.grid[0]} | {self.grid[1]} | {self.grid[2]} |
         ---+---+---
        | {self.grid[3]} | {self.grid[4]} | {self.grid[5]} |
         ---+---+---
        | {self.grid[6]} | {self.grid[7]} | {self.grid[8]} |
         ---+---+---
        """)
        print()
    def make_position(self, position):
        
        if position < 0 or position >= 9 or self.grid[position] == 'P' or self.grid[position] == 'Q':
            print('Try again')
            return False

        self.grid[position] = self.current_user
        return True
    
    def switch_user(self):
        self.current_user = 'Q' if self.current_user == 'P' else 'P'
    
    def check_drow(self):
        tab_init = [i for i in range(9)]
        for index in tab_init:
            for g in self.grid:
                if index == g:
                    return False
        return True

    def check_winner(self):
        combinaison_winner = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for tab in combinaison_winner:
            if self.grid[tab[0]] == self.grid[tab[1]] == self.grid[tab[2]]:
                return True

        return False

    def play(self):
        print('WELCOME TO THE GAME TIC TAC TOE')
        while True:
            self.display_grid()
            try:
                position = int(input(f"user : {self.current_user}  Choice your position : (0-8) : "))
                if not self.make_position(position):
                    continue
            except ValueError:
                print("Invalide value, Enter number enter (0-8)")

            if self.check_drow():
                self.display_grid()
                print("Game over")
                break

            if self.check_winner():
                self.display_grid()
                print(f"{self.current_user}  wins")
                break

            self.switch_user()
    
    

if __name__ == '__main__':
    game = TicTacToe()
    game.play()