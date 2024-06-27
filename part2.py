import utils


def find_all_possible_moves(board, pawn):
    """
    board : Board object
    pawn : coordonnées (x, y) du pion

    Suivant un plateau de jeu, et un pion,
    renvoyer la liste de tous les coups possibles de ce pion.

    La liste retournée sera une liste de 2-tuple
    """

    # TODO

    print(board.get_pawn((3, 4)))
    print(board.get_pawn((3, 4)))

    return [(1, 4), (3, 4)]

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
), (1, 2))) != {(1, 3), (3, 3)}: print("CASE 2 (black): FAILED :( !")
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


