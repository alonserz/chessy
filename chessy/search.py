import chess
from evaluation import evaluate_board

def legal_moves(board):
    return list(board.legal_moves)

def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    if maximizingPlayer:
        best_score = -float('inf')
        for move in legal_moves(board):
            board.push(move)
            best_score = max(best_score, alphabeta(board, depth - 1, alpha, beta, False))
            board.pop()
            if best_score >= beta:
                break
            alpha = max(alpha, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in legal_moves(board):
            board.push(move)
            best_score = min(best_score, alphabeta(board, depth - 1, alpha, beta, True))
            board.pop()
            if best_score <= alpha:
                break
            beta = min(beta, best_score)
        return best_score

def search_move(board, depth):
    best_move = None
    best_score = -float('inf') if board.turn == chess.WHITE else float('inf')
    for move in legal_moves(board):
        board.push(move)
        score = alphabeta(board, depth - 1, -float('inf'), float('inf'), True)
        board.pop()
        if board.turn == chess.WHITE and score >= best_score:
            best_score = score
            best_move = move
        if board.turn == chess.BLACK and score <= best_score:
            best_score = score
            best_move = move
    return best_move

