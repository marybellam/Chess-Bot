from datetime import datetime
import chess
import random
import math

# Chess Bot class
class ChessBot:

    piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
    }

    def __init__(self, bot_color=None):
        self.board = chess.Board()
        self.bot_color = bot_color
        self.player_color = None

    # Method to print current date & time
    def today(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%y")
        print("Time: " + date + time)

    # Method to choose computer player
    def computer_player(self):
        while True:
            bot_play = input("Computer Player? (w=white/b=black): ").lower()
            if bot_play == "w" or bot_play == "b":
                self.bot_color = bot_play
                print (self.bot_color)
                if self.bot_color == 'w':
                    self.player_color = 'b'
                else:
                    self.player_color = 'w'
                break
            else:
                print("Enter a valid character.")

    # Method to choose start position
    def board_start_pos(self):
        while True:
            start_pos = input("Starting FEN position? (ENTER for standard starting position): ")
            if start_pos == "":
                print("Using standard starting position.")
                self.board.set_fen(chess.STARTING_FEN)
                break
            else:
                try:
                    self.board.set_fen(start_pos)
                    break
                except ValueError:
                    print("Enter a valid FEN position.")

    # Bot's turn
    def bot_play(self):
        legal_moves = list(self.board.legal_moves)
        captures = [move for move in legal_moves if self.board.is_capture(move)]
        if captures:
            move = random.choice(captures)
        else:
            move = random.choice(legal_moves)
        print(move.uci())
        self.board.push(move)
        
    # Player's turn
    def human_play(self):
        legal_moves = list(self.board.legal_moves)
        move = input("Your move: ")
        while move not in [m.uci() for m in legal_moves]:
            print("Enter a valid move.")
            move = input("Your move: ")
        self.board.push_uci(move)
        print(self.board)

    # Milestone
    def shallow_minmax(self):
        best_score = float('-inf')
        best_move = None
            
        for white_move in list(self.board.legal_moves): #for each white move
            if self.board.is_capture(white_move):
                white_capture = self.board.piece_at(white_move.to_square) #gets the piece being captured
            else:
                white_capture = None
            if white_capture != None:
                value_white = self.piece_values[white_capture.piece_type] #value of piece being captured
            else:
                value_white = 0
            self.board.push(white_move)

            worst_black_score = float('inf')
            for black_move in list(self.board.legal_moves):
                black_capture = self.board.piece_at(black_move.to_square)
                if black_capture != None:
                    value_black = self.piece_values[black_capture.piece_type]
                else:
                    value_black = 0
                    
                score = value_white - value_black

                if score < worst_black_score: #gets lowest score/worst for white score
                    worst_black_score = score
            
            if(worst_black_score > best_score):
                best_score = worst_black_score
                best_move = white_move

            self.board.pop()

        if best_move:
            print(best_move.uci())
            self.board.push(best_move)
        else:
            print("ERROR: no move made")

    def calculate_score(self):
        score = 0
        for piece_type in self.piece_values:
            score += len(self.board.pieces(piece_type, chess.WHITE)) * self.piece_values[piece_type] 
            score -= len(self.board.pieces(piece_type, chess.BLACK)) * self.piece_values[piece_type]
        return score

    def search(self):
        if self.board.is_checkmate(): 
            if self.board.turn == (self.bot_color == "w"): 
                return -9999
            else:
                return 9999
        if self.board.is_stalemate(): 
            return 0
        
        best_score = float('-inf')
        best_move = None

        for move in self.board.legal_moves:
            self.board.push(move)
            score = self.calculate_score()
            self.board.pop()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    # Gameplay
    def game(self):
        while not self.board.is_game_over():
            print(self.board)
            move = str
            if (self.board.turn == True):
                if self.bot_color == "w":
                    print("Bot (as white): ")
                    self.shallow_minmax()
                else:
                    self.human_play()
                print("New FEN position: " + self.board.fen())
            else:
                if self.bot_color == "b":
                    print("Bot (as black): ")
                    self.bot_play()
                else:
                    self.human_play()
                print("New FEN position: " + self.board.fen())
            if self.board.is_game_over():
                break

        print("Game over: ", self.board.result()) # result
 
    # Set up game
    def play(self):
        self.today()
        self.computer_player()
        self.board_start_pos()
        self.game()

# Main method
def main():
    bot = ChessBot()
    bot.play()
    
if __name__ == "__main__":
    main()
