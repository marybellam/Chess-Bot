from datetime import datetime
import chess
import random

# Chess Bot class
class ChessBot:
    board = chess.Board()
    bot_color = str
    player_color = str

# Constructor
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
        ChessBot.bot_play = input("Computer Player? (w=white/b=black): ").lower()
        if ChessBot.bot_play == "w" or ChessBot.bot_play == "b":
            bot_color = ChessBot.bot_play
            print (bot_color)
            break
        else:
            print("Enter a valid character.")
    #print("You entered: " + ChessBot.bot_play)

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
    #captures = []
    #for i in range(ChessBot.board.legal_moves.count() - 1):
    #    if ChessBot.board.is_capture(legal_moves[i]) == True:
    #        captures.append(legal_moves[i])
    if len(captures) > 0:
        #print("Captures available: ", captures)
        num = random.randint(0, len(captures) - 1)
        move = captures[num]
        #move = random.choice(captures)
    else:
        num = random.randint(0, ChessBot.board.legal_moves.count() - 1)
        move = legal_moves[num]
        #move = random.choice(legal_moves)

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

# Gameplay
def game():
    while not ChessBot.board.is_game_over():
        print(ChessBot.board)
        move = str
        if (ChessBot.board.turn == True):
            if ChessBot.bot_play == "w":
                print("Bot (as white): ")
                bot_play()
            else:
                #move = input("Your move (as white): ")
                human_play()
            print("New FEN position: " + ChessBot.board.fen())
        else:
            if ChessBot.bot_play == "b":
                print("Bot (as black): ")
                bot_play()
            else:
                #move = input("Your move (as black): ")
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