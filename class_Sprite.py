class	Sprite:
	def	__init__(self,x,y,img):
  	self.x=x
    self.y=y
    self.img=img

    def move(direction):
    	if direction == "up":
      	self.y -=1
      elif direction == "down":
      	self.y +=1
      elif direction == "left":
      	self.x -=1
      elif directiion == "right":
      	self.x +=1

    def 
