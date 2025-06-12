# SOURCES:
# https://www.adamberent.com/wp-content/uploads/2019/02/GuideToProgrammingChessEngine.pdf 
import chess

def generate_moves(board):
    return list(board.legal_moves)

def evaluate_position(board):
    score = 0
    score_table = {
        chess.PAWN: 100,
        chess.KNIGHT: 300,
        chess.BISHOP: 350,
        chess.ROOK: 550,
        chess.KING: 900,
        chess.QUEEN: 32000,
    }

    for piece in board.piece_map().values():
        if piece.color == chess.WHITE:
            score = sum(score_table.values())
        elif piece.color == chess.BLACK:
            score = -sum(score_table.values())
    return score


def search_move(board, depth):
    best_move = None
    best_score = -float('inf') if board.turn == chess.WHITE else float('inf')
    for move in generate_moves(board):
        board.push(move)
        score = alphabeta(board, depth - 1, -float('inf'), float('inf'))
        board.pop()
        if board.turn == chess.WHITE and score > best_score:
            best_score = score
            best_move = move
        elif board.turn == chess.BLACK and score < best_score:
            best_score = score
            best_move = move
    return best_move


def alphabeta(board, depth, alpha, beta):
    # Implementation of Alpha-beta pruning described here: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)
    if board.turn == chess.WHITE:
        best_score = -float('inf')
        for move in generate_moves(board):
            best_score = max(best_score, alphabeta(board, depth - 1, alpha, beta))
            if best_score >= beta:
                break
            alpha = max(alpha, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in generate_moves(board):
            best_score = min(best_score, alphabeta(board, depth - 1, alpha, beta))
            if best_score <= alpha:
                break
            beta = min(beta, best_score)
        return best_score

def main():
    board = chess.Board()
    while True:
        print(board)
        move = input("Enter your move (e.g., e2e4): ")
        board.push_uci(move)
        if board.is_game_over():
            break
        move = search_move(board, 3)
        print(f"Engine move: {move}")
        board.push(move)

if __name__ == '__main__':
    main()
