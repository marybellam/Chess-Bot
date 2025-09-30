from datetime import datetime
import chess

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
            board = chess.Board(start_pos)
            break
        except ValueError:
            print("Enter a valid FEN position.")

# playing
while not board.is_game_over():
    print(board)
    if (board.turn == True):
        if bot_play == "w":
            print("Bot turn")
        else:
            print("Your turn")
    else:
        if bot_play == "b":
            print("Bot turn")
        else:
            print("Player turn")
    break
print("Game over: ", board.result()) # result

def wait():
    if
def main():
    print("This is a chess bot.")
