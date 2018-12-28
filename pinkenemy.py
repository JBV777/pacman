class Pinkenemy:

    def __init__(self,protagonistx,protagonisty,enemyx,enemyy):
        self.protagonistx=protagonistx
        self.protagonisty=protagonisty
        self.enemyx=enemyx
        self.enemyy=enemyy

    def xmovement(self):
        if (self.enemyx>self.protagonistx):
            self.enemyx-=5
        elif (self.enemyx<self.protagonistx):
            self.enemyx+=5
        return self.enemyx

    def ymovement(self):
        if (self.enemyy>self.protagonisty):
            self.enemyy-=5
        elif (self.enemyy<self.protagonisty):
            self.enemyy+=5
        return self.enemyy

    def gameover(self):
        if (self.protagonistx==self.enemyx and self.protagonisty==self.enemyy):
            return True
        else:
            return False