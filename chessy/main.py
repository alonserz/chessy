# SOURCES:
# https://www.adamberent.com/wp-content/uploads/2019/02/GuideToProgrammingChessEngine.pdf 
import chess
from eval import PAWN_TABLE, KNIGHT_TABLE, BISHOP_TABLE, ROOK_TABLE, QUEEN_TABLE, KING_TABLE_EARLY

def generate_moves(board):
    return list(board.legal_moves)

def evaluate_board(board):
    score = 0
    piece_table = {
        'p': 10,
        'r': 50,
        'n': 30,
        'b': 30,
        'q': 90,
        'k': 900,
    }
    for idx, piece in board.piece_map().items():
        piece_type = str(piece).lower()
        # TODO: at least it works, but must rewrite
        if piece.color == chess.WHITE:
            if piece_type == 'p':
                # pawn
                score += piece_table[piece_type] + PAWN_TABLE[idx]
            elif piece_type == 'b':
                # bishop
                score += piece_table[piece_type] + BISHOP_TABLE[idx]
            elif piece_type == 'n':
                # knight
                score += piece_table[piece_type] + KNIGHT_TABLE[idx]
            elif piece_type == 'k':
                # king
                score += piece_table[piece_type] + KING_TABLE_EARLY[idx]
            elif piece_type == 'q':
                # queen
                score += piece_table[piece_type] + QUEEN_TABLE[idx]
            elif piece_type == 'r':
                # rook
                score += piece_table[piece_type] + ROOK_TABLE[idx]
                pass
        else:
            if piece_type == 'p':
                # pawn
                score -= piece_table[piece_type] + PAWN_TABLE[::-1][idx]
            elif piece_type == 'b':
                # bishop
                score -= piece_table[piece_type] +  BISHOP_TABLE[::-1][idx]
            elif piece_type == 'n':
                # knight
                score -= piece_table[piece_type] + KNIGHT_TABLE[::-1][idx]
            elif piece_type == 'k':
                # king
                score -= piece_table[piece_type] + KING_TABLE_EARLY[::-1][idx]
            elif piece_type == 'q':
                # queen
                score -= piece_table[piece_type] + QUEEN_TABLE[::-1][idx]
            elif piece_type == 'r':
                # rook
                score -= piece_table[piece_type] + ROOK_TABLE[::-1][idx]
                pass
    return score


def search_move(board, depth):
    best_move = None
    best_score = -float('inf') if board.turn == chess.WHITE else float('inf')
    for move in generate_moves(board):
        board.push(move)
        score = alphabeta(board, depth - 1, -float('inf'), float('inf'), True)
        board.pop()
        if board.turn == chess.WHITE and score > best_score:
            best_score = score
            best_move = move
        return best_move


def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    # Implementation of Alpha-beta pruning described here: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    if maximizingPlayer:
        best_score = -float('inf')
        for move in generate_moves(board):
            board.push(move)
            best_score = max(best_score, alphabeta(board, depth - 1, alpha, beta, False))
            board.pop()
            if best_score >= beta:
                break
            alpha = max(alpha, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in generate_moves(board):
            board.push(move)
            best_score = min(best_score, alphabeta(board, depth - 1, alpha, beta, True))
            board.pop()
            if best_score <= alpha:
                break
            beta = min(beta, best_score)
        return best_score

def main():
    board = chess.Board()
    while True:
        print(board)
        move = input("Enter your move (e.g., e2e4): ")
        try:
            board.push_uci(move)
        except chess.IllegalMoveError:
            print(f"Move {move} is illegal")
            continue
        if board.is_game_over():
            break
        move = search_move(board, 4)
        print(f"Engine move: {move}")
        board.push(move)

if __name__ == '__main__':
    main()
