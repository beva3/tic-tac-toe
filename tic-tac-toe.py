class TicTacToe:
    def __init__(self):
        # Initialize the grid and player symbole
        self.grid = [space for space in range(9)]
        self.current_player = "X"
    
    def display_grid(self):
        print(f"""
         {self.grid[0]} | {self.grid[1]} | {self.grid[2]}
        ---+---+---
         {self.grid[3]} | {self.grid[4]} | {self.grid[5]}
        ---+---+---
         {self.grid[6]} | {self.grid[7]} | {self.grid[8]}
        ---+---+---
        """)
    def make_position(self, position):
        # valide and make move
        
        if position < 0 or position >= 9 or self.grid[position] == "X" or self.grid[position] == "O":
            print("Invalide move, Try Again")
            return False

        self.grid[position] = self.current_player
        return True

    def switch_player(self):
        # switch the current player :
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_drow(self):
        my_list = [i for i in range(9)]
        for index in my_list :
            for g in self.grid:
                if g == index:
                    return False
        return True

    def check_winner(self):
        # Check for all winning combinations
        winning_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal from top-left
            [2, 4, 6],  # Diagonal from top-right
        ]
        for combi in winning_combinations:
            if self.grid[combi[0]] == self.grid[combi[1]] == self.grid[combi[2]] and self.grid[combi[0]] != " ":
                return True
        return False

    def play(self):
        # Main game loop
        print("Welcome to Tic Tac Toe")
        while True:
            self.display_grid()
            try :
                # Ask the current player for their move
                position = int(input(f"Player : {self.current_player} chose a position (0-8) "))
                if not self.make_position(position):
                    # print("not make position lesy") rehefa false no dikamio
                    continue
                
            except ValueError:
                print("Invalide input, please enter a number between 0 and 8")
                continue

            
            # Check for a winner
            if self.check_winner():
                self.display_grid()
                print(f"Player {self.current_player} wins! 🎉")
                break

            # check dfor a drow:
            if self.check_drow():
                self.display_grid()
                print("FENOOOOOO")
                break;

            # after move switch player :
            self.switch_player()
            
# Run the game 
if __name__ == "__main__":
    game = TicTacToe()
    game.play()