class TicTacToe:
    def __init__(self):
        # Initialize the grid and player symbols
        self.grid = [" " for _ in range(9)]  # 1D list representing a 3x3 grid
        self.current_player = "X"  # Player 1 starts with "X"

    def display_grid(self):
        # Display the grid in a 3x3 format
        print(f"""
         {self.grid[0]} | {self.grid[1]} | {self.grid[2]}
        ---+---+---
         {self.grid[3]} | {self.grid[4]} | {self.grid[5]}
        ---+---+---
         {self.grid[6]} | {self.grid[7]} | {self.grid[8]}
        """)

    def make_move(self, position):
        # Validate and make a move
        if position < 0 or position >= 9 or self.grid[position] != " ":
            print("Invalid move! Try again.")
            return False
        self.grid[position] = self.current_player
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
        for combo in winning_combinations:
            if self.grid[combo[0]] == self.grid[combo[1]] == self.grid[combo[2]] and self.grid[combo[0]] != " ":
                return True
        return False

    def check_draw(self):
        # Check if all cells are filled and there's no winner
        return " " not in self.grid

    def switch_player(self):
        # Switch the current player
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        # Main game loop
        print("Welcome to Tic Tac Toe!")
        while True:
            self.display_grid()
            try:
                # Ask the current player for their move
                position = int(input(f"Player {self.current_player}, choose a position (0-8): "))
                if not self.make_move(position):
                    continue
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 8.")
                continue

            # Check for a winner
            if self.check_winner():
                self.display_grid()
                print(f"Player {self.current_player} wins! 🎉")
                break

            # Check for a draw
            if self.check_draw():
                self.display_grid()
                print("It's a draw! 🤝")
                break

            # Switch players
            self.switch_player()


# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
