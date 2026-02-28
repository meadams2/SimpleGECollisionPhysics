"""Collisions with Basic Image
Showing how collisions work with Sprite Image
Marianne Adams, 2026"""

import pygame, simpleGE, CollisionPhysics

class Charlie(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene, angle=0):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.position = (100, 100)
        self.setAngle(angle)
        self.moveAngle = angle
        self.speed = 0
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= 1
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += 1
        if self.isKeyPressed(pygame.K_UP):
            self.y -= 1
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += 1
        
        # Rotation
        if self.isKeyPressed(pygame.K_q):
            self.imageAngle += 1
            self.moveAngle += 1
        if self.isKeyPressed(pygame.K_e):
            self.imageAngle -= 1
            self.moveAngle -= 1
class MovyThing(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene, angle=0):
        super().__init__(scene)
        self.colorRect("blue", (120, 60))
        self.x = 300
        self.y = 300
        self.setAngle(angle)
        self.moveAngle = angle
        self.speed = 0
        
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.x -= 1
        if self.isKeyPressed(pygame.K_d):
            self.x += 1
        if self.isKeyPressed(pygame.K_w):
            self.y -= 1
        if self.isKeyPressed(pygame.K_s):
            self.y += 1
        
        # Rotation
        if self.isKeyPressed(pygame.K_n):
            self.imageAngle += 1
            self.moveAngle += 1
        if self.isKeyPressed(pygame.K_m):
            self.imageAngle -= 1
            self.moveAngle -= 1

class CollisionOut(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (500, 30)
        self.size = (300, 30)
        self.fgColor = "blue"
        self.bgColor = "white"
        self.clearBack = True
        
class AngleOut(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (100, 30)
        self.size = (300, 30)
        self.fgColor = "blue"
        self.bgColor = "white"
        self.clearBack = True
        
class CollisionScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("white")
        self.setCaption("SAT Collision Test. Arrows for Cardinal, WASD for box")
        
        self.charlie = Charlie(self, 30)
        self.box = MovyThing(self, -20)
        self.collisionLbl = CollisionOut()
        self.angleLbl = AngleOut()
        
        self.sprites = [self.charlie, self.box, self.collisionLbl, self.angleLbl]
        
    def update(self):
        super().update()
        
        testSAT = False
        testAABB = False
        
        collisionNormal = None
        collisionAngle = 0
        
        charlieSAT, collisionNormal, collisionAngle = self.charlie.collidesWithAdvanced(self.box)
        charlieAABB = self.charlie.collidesWith(self.box)
        
        boxSAT, collisionNormal, collisionAngle = self.box.collidesWithAdvanced(self.charlie)
        boxAABB = self.box.collidesWith(self.charlie)
        
        if charlieSAT or boxSAT:
            testSAT = True
            self.angleLbl.text = f"Angle: {collisionAngle:.2f}"
        else:
            self.angleLbl.text = "Angle: None"
            
        if charlieAABB or boxAABB:
            testAABB = True
        
        self.collisionLbl.text = f"SAT: {testSAT}, AABB: {testAABB}"
def main():
    game = CollisionScene()
    game.start()

if __name__ == "__main__":
    main()
