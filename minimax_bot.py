from datetime import datetime
import chess
import random
import math

# Chess Bot class
class ChessBot:
    board = chess.Board()
    bot_color = str
    player_color = str
    
def __init__(self, board, bot_color, player_color):
    self.board = board
    self.bot_color = bot_color
    self.player_color = player_color

    # Method to print current date & time
def today():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%d/%m/%y")
    print("Time: " + date + time)

    # Method to choose computer player
def computer_player():
    while True:
        bot_play = input("Computer Player? (w=white/b=black): ").lower()
        if bot_play == "w" or bot_play == "b":
            ChessBot.bot_color = bot_play
            print(ChessBot.bot_color)
            break
        else:
            print("Enter a valid character.")

    # Method to choose start position
def board_start_pos():
    while True:
        start_pos = input("Starting FEN position? (ENTER for standard starting position): ")
        if start_pos == "":
            print("Using standard starting position.")
            ChessBot.board.set_fen(chess.STARTING_FEN)
            break
        else:
            try:
                ChessBot.board.set_fen(start_pos)
                break
            except ValueError:
                print("Enter a valid FEN position.")

    # Bot's turn
def bot_play():
    ChessBot.board.legal_moves.count()
    legal_moves = list(ChessBot.board.legal_moves)
    captures = [move for move in legal_moves if ChessBot.board.is_capture(move)]
    if len(captures) > 0:
        #print("Captures available: ", captures)
        num = random.randint(0, len(captures) - 1)
        move = captures[num]
    else:
        num = random.randint(0, ChessBot.board.legal_moves.count() - 1)
        move = legal_moves[num]
    print (move.uci())
    ChessBot.board.push(move)
        
    # Player's turn
def human_play():
    legal_moves = list(ChessBot.board.legal_moves)
    #print("Legal moves: ", legal_moves)
    move = input("Your move: ")
    while move not in [m.uci() for m in legal_moves]:
        print("Enter a valid move.")
        move = input("Your move: ")
    ChessBot.board.push_uci(move)
    print("check")
    print(ChessBot.board)

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
    }

def shallow_minmax():
    best_score = float('-inf')
    score = int(0)
    best_move = None
    print("doing minmax")
        
    for moveWhite in ChessBot.board.legal_moves: #for each white move
        captured_piece = ChessBot.board.piece_at(moveWhite.to_square) #gets the value of piece going to be captured or none
        valueofWhiteMove = 0
        if captured_piece != None:
            valueofWhiteMove = piece_values[captured_piece.piece_type] #if piece going to be captures get value
        #print("move white" , moveWhite)
        ChessBot.board.push(moveWhite)
        worst_black_score = float('inf')        
        for moveBlack in ChessBot.board.legal_moves:
            captured_white = ChessBot.board.piece_at(moveBlack.to_square)
            valueofBlackMove = 0 #have to assume best move
            if captured_white != None:
                valueofBlackMove = piece_values[captured_white.piece_type]
            score = valueofWhiteMove - valueofBlackMove
            #print("score",score)
            if score < worst_black_score: #gets lowest score/worst for white score
                worst_black_score = score
        
        if(worst_black_score > best_score):
            best_score = worst_black_score
            best_move = moveWhite
        ChessBot.board.pop() #undo white move
        
    if best_move != None:
        print(ChessBot.board)
        print(best_move.uci())
        ChessBot.board.push(best_move)
    else:
        print("ERROR: NO MOVE MADE")

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
def game():
    while not ChessBot.board.is_game_over():
        print(ChessBot.board)
        print(ChessBot.bot_color)
        move = str
        if (ChessBot.board.turn == True):
            if ChessBot.bot_color == "w":
                print("Bot (as white): ")
                shallow_minmax()
            else:
                human_play()
            print("New FEN position: " + ChessBot.board.fen())
        else:
            if ChessBot.bot_color == "b":
                print("Bot (as black): ")
                bot_play()
            else:
                human_play()
            print("New FEN position: " + ChessBot.board.fen())
        if ChessBot.board.is_game_over():
            break
    print("Game over: ", ChessBot.board.result()) # result
 
    # Set up game
def play():
    today()
    computer_player()
    board_start_pos()
    game()

# Main method
def main():
    play()
    
if __name__ == "__main__":
    main()