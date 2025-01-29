class Tic_tac_toe:
    def __init__(self):
        self.board = [i for i in range(9)]
        self.current_turn = 'X'

    def display_board(self):
        print()
        print(f"""
         ---+---+---
        | {self.board[0]} | {self.board[1]} | {self.board[2]} |
         ---+---+---
        | {self.board[3]} | {self.board[4]} | {self.board[5]} |
         ---+---+---
        | {self.board[6]} | {self.board[7]} | {self.board[8]} |
         ---+---+---
        """)
        print()
    
    def make_position(self, position):
        if position < 0 or position >= 9 or self.board[position] == 'X' or self.board[position] == 'O':
            print('Try again')
            return False
        
        self.board[position] = self.current_turn
        return True

    def switch_turn(self):
        self.current_turn = 'Y' if self.current_turn == 'X' else 'X'
    
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
            if self.board[tab[0]] == self.board[tab[1]] == self.board[tab[2]]:
                return True
            
        return False
    
    def check_drow(self):
        tab_init = [i for i in range(9)]
        for index in tab_init:
            for case in self.board:
                if index == case:
                    return False
        return True
    
    def play(self):
        print('Welcome to the game Tic Tac Toe')
        while True:
            try:
                self.display_board()
                position = int(input(f'Player {self.current_turn}, enter a position: '))
                if not self.make_position(position):
                    continue

            except ValueError:
                print('Please enter a valid number')
                continue
        
            if self.check_drow():
                print('Drow Completed, game over')
                break
            
            if self.check_winner():
                print(f'Player {self.current_turn} win the game')
                break
            
            self.switch_turn()

if __name__ == '__main__':
    game = Tic_tac_toe()
    game.play()
    