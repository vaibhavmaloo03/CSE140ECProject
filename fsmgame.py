import time
import random


IDLE = 0
PLAYING = 1
GAME_OVER = 2

class CatchGame:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height

        self.state = IDLE
        self.score = 0

        self.paddle_x = self.width // 2
        self.object_x = random.randint(0, self.width - 1)
        self.object_y = 0
        self.move_delay = 0.5

    def reset_game(self):
        self.state = IDLE
        self.score = 0
        self.paddle_x = self.width // 2
        self.object_x = random.randint(0, self.width - 1)
        self.object_y = 0

    def print_game_state(self):
        print("\n" + "="*20)
        if self.state == IDLE:
            print("STATE: IDLE")
            print("Press 's' to start the game.")
        elif self.state == PLAYING:
            print("STATE: PLAYING")
            print(f"Score: {self.score}")
            self.print_board()
            print("Use 'a' to move left, 'd' to move right, 'q' to quit.")
        elif self.state == GAME_OVER:
            print("STATE: GAME OVER")
            print(f"Final Score: {self.score}")
            print("Press 'r' to reset, 'q' to quit.")
        print("="*20 + "\n")

    def print_board(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y == self.object_y and x == self.object_x:
                    row.append("O")  # Falling object
                elif y == self.height - 1 and x == self.paddle_x:
                    row.append("P")  # Paddle
                else:
                    row.append(".")
            print("".join(row))

    def handle_input_idle(self, user_input):
        if user_input == 's':
            self.state = PLAYING

    def handle_input_playing(self, user_input):
        if user_input == 'a' and self.paddle_x > 0:
            self.paddle_x -= 1
        elif user_input == 'd' and self.paddle_x < self.width - 1:
            self.paddle_x += 1
        elif user_input == 'q':
            return False
        return True

    def handle_input_game_over(self, user_input):
        if user_input == 'r':
            self.reset_game()
        elif user_input == 'q':
            return False
        return True

    def update_game(self):

        if self.state == PLAYING:

            time.sleep(self.move_delay)
            self.object_y += 1

            if self.object_y == self.height - 1:

                if self.object_x == self.paddle_x:
                    self.score += 1
                    # Reset object to top
                    self.object_y = 0
                    self.object_x = random.randint(0, self.width - 1)
                else:
    
                    self.state = GAME_OVER

    def run(self):
        running = True
        while running:
            self.print_game_state()

            if self.state == IDLE:
                user_input = input("Input: ")
                self.handle_input_idle(user_input)


            elif self.state == PLAYING:

                self.update_game()

                if self.state == PLAYING:
                    # ask for input
                    user_input = input("Move (a/d) or quit (q): ")
                    cont = self.handle_input_playing(user_input)
                    if not cont:
                        running = False

        
            elif self.state == GAME_OVER:
                user_input = input("Input: ")
                cont = self.handle_input_game_over(user_input)
                if not cont:
                    running = False

        print("Exiting game. Goodbye!")

if __name__ == "__main__":
    game = CatchGame()
    game.run()