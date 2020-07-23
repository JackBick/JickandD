class Game:
    def __init__(self,x,y):
        board = [[0] * x for i in range(y)]
        self.board=board

    def board_print(self):
        for i in range(len(self.board[0])):
            for j in range(len(self.board[i])):
                print(self.board[j][i],end ="")
            print()

    def update_player(self,player):
        self.board[player.x][player.y]="P"

    def old_player(self,player):
        self.board[player.x][player.y]="0"
