from class_Sprite import Sprite

class Player(Sprite):
    def move(self,direction):
        if direction == "w":
      	    self.y -=1
        if direction == "s":
      	    self.y +=1
        if direction == "a":
      	    self.x -=1
        if direction == "d":
      	    self.x +=1
