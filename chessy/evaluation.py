import chess
from eval import PAWN_TABLE, KNIGHT_TABLE, BISHOP_TABLE, ROOK_TABLE, QUEEN_TABLE, KING_TABLE_EARLY

def evaluate_board(board):
    score = 0
    pieces_value = {
        'p': 100,
        'n': 320,
        'b': 330,
        'r': 500,
        'q': 900,
        'k': 20000,
    }
    pieces_position_values = {
        'p': PAWN_TABLE,
        'b': BISHOP_TABLE,
        'n': KNIGHT_TABLE,
        'k': KING_TABLE_EARLY,
        'q': QUEEN_TABLE,
        'r': ROOK_TABLE,
    }
    for idx, piece in board.piece_map().items():
        piece_type = str(piece).lower()

        piece_position_value = 0

        if piece.color == chess.WHITE:
            piece_position_value = pieces_position_values[piece_type][idx]
        elif piece.color == chess.BLACK:
            piece_position_value = pieces_position_values[piece_type][::-1][idx]
        
        piece_evaluation = pieces_value[piece_type] + piece_position_value
        
        if piece.color == chess.BLACK:
            piece_evaluation = piece_evaluation * -1

        score += piece_evaluation
    return score
