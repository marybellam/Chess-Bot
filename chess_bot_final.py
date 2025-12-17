from datetime import datetime
import chess
import math
from chess import Move

# Chess Bot class
class ChessBot:
    piece_values = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 0
    }
    
    pawn_table = [
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
        1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
        0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
        0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
        0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
        0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
    ]
    
    knight_table = [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0
    ]
    
    bishop_table = [
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
        -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
        -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
        -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
        -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
        -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
    ]
    rook_table = [
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
        -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
        -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
        -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
        -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
        -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
        0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0
    ]
    
    queen_table = [
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
        -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
        -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
        0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
        -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
        -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
    ]
    
    king_table = [
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
        -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
        2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ,
        2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 
    ]
    
    piece_pst = {
        chess.PAWN: pawn_table,
        chess.KNIGHT: knight_table,
        chess.BISHOP: bishop_table,
        chess.ROOK: rook_table,
        chess.QUEEN: queen_table,
        chess.KING: king_table
    }

    def __init__(self):
        self.board = chess.Board()
        self.bot_color = None
        self.player_color = None

    # Method to print current date & time
    def today(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d/%m/%y")
        print("Time: " + date + time)

    def computer_player(self):
        """Choosing Computer Player"""
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

    def board_start_pos(self):
        """Sets start position of game"""
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
                    
    def human_play(self):
        """Gets Players Move"""
        legal_moves = list(self.board.legal_moves)
        move = input("Your move: ")
        while move not in [m.uci() for m in legal_moves]:
            if move == "Q" or move == "q":
                return False
            print("Enter a valid move.")
            move = input("Your move: ")
        self.board.push_uci(move)
        print(self.board)
        return True
    def getMobility(self):
        return self.board.legal_moves.count() * .05
    def evalBoard(self): 
        """Get board score from white's perspective"""
        score:int|float = 0
        mobility = self.getMobility()
        for square in chess.SQUARES:
            piece = self.board.piece_at(square) 
            if piece is not None:
                val = self.piece_values[piece.piece_type]
                pos_val = 0
                if piece.color == chess.WHITE:
                    arr = self.piece_pst[piece.piece_type]
                    pos_val:float = arr[chess.square_mirror(square)] #need to mirror the square
                    score = score + val + pos_val + mobility
                else:
                    arr = self.piece_pst[piece.piece_type]
                    pos_val:float = arr[square] #no need to mirror the square
                    score = score - (val + pos_val + mobility)
        print("score:",score)
        return score
    
    def Min(self,depth:int,alpha:float, beta:float)-> tuple[int|float, Move|None]:
        """ Gets min of opponent's turn"""
        if self.board.is_checkmate():
            return math.inf, None # opponent is checkmated
        if depth == 0 or self.board.is_game_over():
            eval_score = self.evalBoard()
            if self.bot_color == "b":
                eval_score = -eval_score
            return eval_score, None
        best_score:float|int = math.inf
        best_move = None
        for move in self.board.legal_moves: 
            self.board.push(move)
            score,_ = self.Max(depth-1, alpha, beta)
            self.board.pop()
            if(score < best_score):
                best_score = score
                best_move = move
                if best_score < beta:
                    beta = best_score #new min
                if beta <= alpha:
                    break #stop searching
        return best_score, best_move
    
    def Max(self,depth:int, alpha:float, beta:float) -> tuple[int|float, Move|None]:
        """Gets max of plater/bots turn"""
        if self.board.is_checkmate():
            return -math.inf, None
        if depth == 0 or self.board.is_game_over():
            eval_score = self.evalBoard()
            if self.bot_color == "b":
                eval_score = -eval_score
            return eval_score, None
        best_score = -math.inf
        best_move = None
        for move in self.board.legal_moves: 
            self.board.push(move)
            score,_ = self.Min(depth-1, alpha, beta)
            self.board.pop()
            if(score > best_score):
                best_score = score
                best_move = move
                if best_score > alpha:
                    alpha = best_score #alpha is max
                if beta <= alpha: 
                    break #stop searching, min won't chose this        
        return best_score, best_move
    
    def game(self):
        """Gamplay, printing the board and checking for game over """
        while not self.board.is_game_over():
            current_turn_w =self.board.turn
            bot = (current_turn_w and self.bot_color == "w") or (not current_turn_w and self.bot_color == "b")
            if bot == True:
                color_name = "white"
                if self.bot_color == "b":
                    color_name = "black"
                print("Bot (as",color_name,"): ") 
                _,move = self.Max(4, -math.inf,math.inf)
                if move == None:
                    print("ERROR")
                else:
                    print(move.uci())
                    self.board.push(move)
            else:
                play = self.human_play()
                if play == False:
                    break
            print(self.board)
            print("New FEN position: " + self.board.fen())
            if self.board.is_game_over():
                break
        print(self.board)
        print("Game over: ", self.board.result()) # result
 
    # Set up game
    def play(self):
        self.today()
        self.computer_player()
        self.board_start_pos()
        print("Press 'Q' to quit")
        print(self.board)
        self.game()

# Main method
def main():
    bot = ChessBot()
    bot.board = chess.Board()
    bot.board.push_uci('b2b4')
    print(bot.board)
    print(bot.evalBoard())
    #bot.play()
    
if __name__ == "__main__":
    main()
