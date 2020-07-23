from class_Sprite import Sprite
from class_Game import Game
from class_Player import Player

_player = Player(0,0,0,0,0)
_game = Game(8,8)

while True:
    move_input = input("Please enter a move ")
    _game.old_player(_player)
    _player.move(move_input)
    _game.update_player(_player)
    _game.board_print()
