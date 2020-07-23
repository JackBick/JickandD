from class_Sprite import Sprite
from class_Game import Game
from class_Player import Player

_player = Player(0,0,0,0,img)
_game = Game(3,4)

while True:
    move_input = input("Please enter a move")
    _game.move(move_input)
