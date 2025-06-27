import chess
from search import search_move

def main():
    board = chess.Board()
    pretty_pieces = {
        'p': "♟",
        'P': "♙",
        'K': "♔",
        'k': "♚",
        'Q': "♕",
        'q': "♛",
        'R': "♖",
        'r': "♜",
        'B': "♗",
        'b': "♝",
        'N': "♘",
        'n': "♞",
    }
    while True:
        board_str = str(board).translate(str.maketrans(pretty_pieces))
        splited_board = board_str.split('\n')
        for idx in range(len(splited_board)):
            splited_board[idx] = splited_board[idx] + f" {8 - idx}"
        splited_board.append("a b c d e f g h")
        board_str = '\n'.join(splited_board)
        print(board_str)
        move = input("Enter your move (e.g., e2e4): ")
        try:
            board.push_uci(move)
        except chess.IllegalMoveError:
            print(f"Move {move} is illegal")
            continue
        if board.is_game_over():
            break
        move = search_move(board, 3)
        print(f"Engine move: {move}")
        board.push(move)
        print()

if __name__ == '__main__':
    main()
