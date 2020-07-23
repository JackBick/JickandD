class Tile():
    def __init__(self):
        self.item=None
        self.is_wall=False
        self.has_player=False
        self.output=" "
        self.torch=Torch()
        self.original_tile="a"
