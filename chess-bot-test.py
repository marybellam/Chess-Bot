from datetime import datetime
import chess
import random

def botPlay(board):
    board.legal_moves.count()
    legal_moves = list(board.legal_moves)
    num = random.randint(0, board.legal_moves.count() - 1)
    move = legal_moves[num]
    print("Bot plays: " + move.uci())
    board.push(move)
    print(board)
    
def humanPlay(board):
    legal_moves = list(board.legal_moves)
    move = input("Your move: ")
    while move not in legal_moves:
        print("Enter a valid move.")
        move = input("Your move: ")
    print("Human plays: " + move.uci())
    board.push(move)
    print(board)
    
# print date & time
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.strftime("%d/%m/%y")
print("Today is: " + date + ". The time is: " + time + ".")

# choose computer player
while True:
    bot_play = input("Computer Player? (W for white or B for black): ").lower()
    if bot_play == "w" or bot_play == "b":
        break
    else:
        print("Enter a valid character.")
print("You entered: " + bot_play)

# choose start position
while True:
    start_pos = input("Starting FEN position? (ENTER for standard starting position): ")
    if start_pos == "":
        print("Using standard starting position.")
        board = chess.Board()
        break
    else:
        try:
            board = chess.Board(start_pos) #use set_fen()?
            break
        except ValueError:
            print("Enter a valid FEN position.")

# playing
print(board)
while not board.is_game_over():
    if (board.turn == True): #whites turn
        if bot_play == "w":
            print("Bot turn")
            botPlay(board)
        else:
            print("Player turn")
            humanPlay(board)
    else:
        if bot_play == "b":
            print("Bot turn")
            botPlay(board)
        else:
            print("Player turn")
            humanPlay(board)
print("Game over: ", board.result()) # result


def main():
    print("This is a chess bot.")
