# White pieces
# SOURCE: https://github.com/lhartikk/simple-chess-ai/blob/master/script.js 

PAWN_TABLE =  [
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
        1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
        0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
        0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
        0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
        0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
]


KNIGHT_TABLE =  [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0
]

BISHOP_TABLE = [
     -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
     -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
     -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
     -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
     -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
     -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
     -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
     -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
]


ROOK_TABLE = [
      0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
      0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
     -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
      0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0
]


QUEEN_TABLE = [
     -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
     -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
     -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
     -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
      0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
     -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
     -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
     -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
]

KING_TABLE_EARLY = [

     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
     -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
     -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
      2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ,
      2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 
]
