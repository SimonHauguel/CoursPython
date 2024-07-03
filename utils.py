import dataclasses

@dataclasses.dataclass
class TILE:
    NO_TILE : int = -1
    BLACK : int = 0
    WHITE : int = 1

@dataclasses.dataclass
class PAWN:
    NO_PAWN : int = -1
    BLACK : int = 0
    WHITE : int = 1

class Board:

    """
    Represente le plateau de jeu et toutes les informations necessaires

    Voici une liste des informations accessibles :
        
        - board.def_board est une matrice 8*8 d'objets representant une tuile du jeu. 
          Une tuile a une couleur, et la couleur du pion, si pion.
        
        - board.actual_player est une couleur representant le joueur qui doit jouer

        - board.players est une liste de maximum 2 elements, contenant les pseudos des joueurs connectes.
    """

    def __init__(self, def_board=None):
        """
        Pas important
        """
        if def_board==None:
            self.data_board = [[{"tile" : TILE.NO_TILE, "pawn" : PAWN.NO_PAWN} for _ in range(8)] for _ in range(8)]
        else: self.data_board = def_board
        self.actual_player = TILE.WHITE
        self.players = []

    def get_pawn(self, coord):
        return self.data_board[coord[1]][coord[0]]["pawn"]

    def add_pawn(self, x, y, color):
        """
        Ajoute un pion de couleur `color` a l'emplacement (`x`, `y`)
        Change la couleur si un pion est deja place a l'emplacement (`x`, `y`)
        """
        assert color in (PAWN.BLACK, PAWN.WHITE, PAWN.NO_PAWN), f"Erreur pour l'ajout d'un pion : {color} n'est pas une couleur connue"
        self.data_board[y][x]["pawn"] = color

    def add_tile(self, x, y, color):
        """
        Ajoute un pion de couleur `color` a l'emplacement (`x`, `y`)
        Change la couleur si un pion est deja place a l'emplacement (`x`, `y`)
        """
        assert color in (TILE.BLACK, TILE.WHITE, TILE.NO_TILE), f"Erreur pour l'ajout d'une case : {color} n'est pas une couleur connue"
        self.data_board[y][x]["tile"] = color

    def __reversed__(self):
        """
        Pas important
        """
        return reversed(self.data_board)

    def toggle_player(self):
        """
        Inverse le joueur actuel (Si noir devient blanc, si blanc devient noir)
        """
        self.actual_player = self.actual_player == TILE.BLACK

    def __str__(self):
        acc = "<Board object : \n"

        for line in self.data_board:
            for v in line:
                pawn = v["pawn"]
                if pawn == PAWN.BLACK: acc += "o"
                elif pawn == PAWN.WHITE: acc += "x"
                else: acc += " "
            acc += "\n"

        return acc[:-1] + ">"

def new_def_board(board):
    
    board = board.split("\n")
    board.pop(0)

    if (len(board) != 8 and len(board[0]) != 8): return

    acc = [[{"tile" : (i+j)%2, "pawn" : PAWN.WHITE if v=="x" else (PAWN.BLACK if v=="o" else PAWN.NO_PAWN)} for j, v in enumerate(line)] for i, line in enumerate(board)]

    return Board(acc)