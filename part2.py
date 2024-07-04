import utils

def find_all_possible_moves(board, pawn):
    """
    board : Board object
    pawn : coordonnées (x, y) du pion
 
    Suivant un plateau de jeu, et un pion,
    renvoyer la liste de tous les coups possibles de ce pion.
 
    La liste retournée sera une liste de 2-tuple
    """
    result = manger_pion(board, pawn)
    return result

def manger_pion(board, pawn):
    couleur_pion = board.get_pawn(pawn)
    
    coup_possibles = []
    x = pawn[0]
    y = pawn[1]

    if couleur_pion == 1: # blanc
        coup_possibles = [(x + 1, y - 1), (x - 1, y - 1)]
        if x == 0:
            coup_possibles = [(x + 1, y - 1)]
        if x == 7:
            coup_possibles = [(x - 1, y - 1)]
        if y == 0:
            coup_possibles = []
        
        coup_possibles = list(filter(lambda x: board.get_pawn(x) == -1 ,coup_possibles))

        if len(coup_possibles) == 2:
            return coup_possibles
        if len(coup_possibles) == 1:
            if x == 0 or x == 7:
                return coup_possibles
            
            if board.get_pawn((x + 1, y - 1)) == 1:
                return coup_possibles
            if board.get_pawn((x - 1, y - 1)) == 1:
                return coup_possibles
            
            if board.get_pawn((x + 1, y - 1)) == 0:
                if y == 1:
                    return coup_possibles
                if x == 6:
                    return coup_possibles
                if board.get_pawn((x + 2, y - 2)) == -1:
                    coup_possibles += [(x + 2, y - 2)]
                    return coup_possibles
                else:
                    return coup_possibles
            
            if board.get_pawn((x - 1, y - 1)) == 0:
                if y == 1:
                    return coup_possibles
                if x == 1:
                    return coup_possibles
                if board.get_pawn((x - 2, y - 2)) == -1:
                    coup_possibles += [(x - 2, y - 2)]
                    return coup_possibles
                else:
                    return coup_possibles

            
        if len(coup_possibles) == 0:
            if x == 0:
                return coup_possibles
            if x == 7:
                return coup_possibles

    




    if couleur_pion == 0: # noir
        coup_possibles = [(x + 1, y + 1), (x - 1, y + 1)]
        if x == 0:
            coup_possibles = [(x + 1, y + 1)]
        if x == 7:
            coup_possibles = [(x - 1, y + 1)]
        if y == 7:
            coup_possibles = []

        coup_possibles = list(filter(lambda x: board.get_pawn(x) == -1 ,coup_possibles)) # TODO

        if len(coup_possibles) == 2:
            return coup_possibles
        if len(coup_possibles) == 1:
            if x == 0 or x == 7:
                return coup_possibles
            
            if board.get_pawn((x + 1, y + 1)) == 0:
                return coup_possibles
            if board.get_pawn((x - 1, y + 1)) == 0:
                return coup_possibles
            
            if board.get_pawn((x + 1, y + 1)) == 1:
                if y == 6:
                    return coup_possibles
                if x == 6:
                    return coup_possibles
                if board.get_pawn((x + 2, y + 2)) == -1:
                    coup_possibles += [(x + 2, y + 2)]
                    return coup_possibles
                else:
                    return coup_possibles
            
            if board.get_pawn((x - 1, y + 1)) == 1:
                if y == 6:
                    return coup_possibles
                if x == 1:
                    return coup_possibles
                if board.get_pawn((x - 2, y + 2)) == -1:
                    coup_possibles += [(x - 2, y + 2)]
                    return coup_possibles
                else:
                    return coup_possibles


    return coup_possibles

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
        
x x x x 
 x x x x
x x x x 
"""
), (2, 5))) != {(1, 4), (3, 4)}: print("CASE 1 (white): FAILED :( !")
else : print("CASE 1 (white): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
        
x x x x 
 x x x x
x x x x 
"""
), (1, 2))) != {(0, 3), (2, 3)}: print("CASE 2 (black): FAILED :( !")
else : print("CASE 2 (black): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
        
x x x x 
 x x x x
x x x x 
"""
), (0, 5))) != {(1, 4)}: print("CASE 3 (white with side wall): FAILED :( !")
else : print("CASE 3 (white with wall): SUCCESS :) !")


if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
        
x x x x 
 x x x x
x x x x 
"""
), (7, 2))) != {(6, 3)}: print("CASE 4 (black with side wall): FAILED :( !")
else : print("CASE 4 (black with wall): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 x o o o
o o o o 
 o o o o
        
        
x x x x 
 x x x x
x x x x 
"""
), (1, 0))) != set(): print("CASE 5 (white with upper wall): FAILED :( !")
else : print("CASE 5 (white with upper wall): SUCCESS :) !")


if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
        
x x x x 
 x x x x
o x x x 
"""
), (0, 7))) != set(): print("CASE 6 (black with lower wall): FAILED :( !")
else : print("CASE 6 (black with lower wall): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
    o   
   o    
x x x x 
 x x x x
x x x x 
"""
), (0, 5))) != {(1, 4)}: print("CASE 7 (white with opponent): FAILED :( !")
else : print("CASE 7 (white with opponent): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
    x   
   x    
x x x x 
 x x x x
x x x x 
"""
), (5, 2))) != {(6, 3)}: print("CASE 8 (black with opponent): FAILED :( !")
else : print("CASE 8 (black with opponent): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
  o     
 o      
x x x x 
 x x x x
x x x x 
"""
), (0, 5))) != set(): print("CASE 9 (white with opponent): FAILED :( !")
else : print("CASE 9 (white with opponent): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
      x 
     x  
x x x x 
 x x x x
x x x x 
"""
), (7, 2))) != set(): print("CASE 10 (black with opponent and wall): FAILED :( !")
else : print("CASE 10 (black with opponent and wall): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
   o    
x x x x 
 x x x x
x x x x 
"""
), (2, 5))) != {(1, 4), (4, 3)}: print("CASE 11 (white with eatable opponent): FAILED :( !")
else : print("CASE 11 (white with eatable opponent): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
    x   
        
x x x x 
 x x x x
x x x x 
"""
), (5, 2))) != {(3, 4), (6, 3)}: print("CASE 12 (black with eatable opponent): FAILED :( !")
else : print("CASE 12 (black with eatable opponent): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
        
o x x x 
 x x x x
x x x x 
"""
), (1, 6))) != set(): print("CASE 13 (white with eatable opponent but wall): FAILED :( !")
else : print("CASE 13 (white with eatable opponent but wall): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o x
        
        
x x x x 
 x x x x
x x x x 
"""
), (1, 7))) != set(): print("CASE 14 (black with eatable opponent but wall): FAILED :( !")
else : print("CASE 14 (black with eatable opponent but wall): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
 o o    
x x x x 
 x x x x
x x x x 
"""
), (2, 5))) != {(0, 3), (4, 3)}: print("CASE 15 (white with 2 eatable opponents): FAILED :( !")
else : print("CASE 15 (white with 2 eatable opponents): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
  x x   
        
x x x x 
 x x x x
x x x x 
"""
), (3, 2))) != {(1, 4), (5, 4)}: print("CASE 16 (black with 2 eatable opponents): FAILED :( !")
else : print("CASE 16 (black with 2 eatable opponents): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
 o x    
x x x x 
 x x x x
x x x x 
"""
), (2, 5))) != {(0, 3)}: print("CASE 17 (white with 1 eatable opponent and 1 friend): FAILED :( !")
else : print("CASE 17 (white with 1 eatable opponent and 1 friend): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
  o x   
        
x x x x 
 x x x x
x x x x 
"""
), (3, 2))) != {(5, 4)}: print("CASE 18 (black with 1 eatable opponent and 1 friend): FAILED :( !")
else : print("CASE 18 (black with 1 eatable opponent and 1 friend): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
        
 x x    
x x x x 
 x x x x
x x x x 
"""
), (2, 5))) != set(): print("CASE 19 (white with 2 friends): FAILED :( !")
else : print("CASE 19 (white with 2 friends): SUCCESS :) !")

if set(find_all_possible_moves(
    utils.new_def_board(
"""
 o o o o
o o o o 
 o o o o
  o o   
        
x x x x 
 x x x x
x x x x 
"""
), (3, 2))) != set(): print("CASE 20 (black with 2 friends): FAILED :( !")
else : print("CASE 20 (black with 2 friends): SUCCESS :) !")