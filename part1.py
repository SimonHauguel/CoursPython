from utils import *

def build_initial_board(board):

    """
    Le but de cette fonction est de placer chaque tuiles et pions sur le plateau au début de la partie

    Par défaut, une case est verte si aucune tuile n'est placée dessus et que aucun pion n'est posé.

    La fonction doit retourner :
        - None si il y a 2+ joueurs connectés
        - une matrice 8*8 de tuiles/pions
    """
    
    for i in range(8):
        for j in range(8):

            pawn = TILE.NO_TILE
            if (i < 3 and not (i+j)%2):  pawn = TILE.BLACK 
            if (i >= 5 and not (i+j)%2): pawn = TILE.WHITE

            board.add_pawn(j, i, pawn)
            board.add_tile(j, i, (i+j)%2)
        
    return board.data_board