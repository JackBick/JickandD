from class_Sprit import Sprite

class Player(Sprite):
    def move(self,direction):
    	if direction == "up":
      	    self.y -=1
        if direction == "down":
      	    self.y +=1
        if direction == "left":
      	    self.x -=1
        if directiion == "right":
      	    self.x +=1
