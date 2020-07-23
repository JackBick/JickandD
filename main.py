from class_Sprite import Sprite
from class_Game import Game
from class_Player import Player

_player = Player(2,2,0,0,0)
_game = Game(3,4)

while True:
    move_input = input("Please enter a move")
    _player.move(move_input)
    _game.update_player(_player)
    _game.board_print()
