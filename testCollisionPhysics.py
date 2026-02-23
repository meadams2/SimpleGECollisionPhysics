"""testCollisions.py
Testing Frame for Collision Physics
Marianne Adams, 2025"""

import CollisionPhysics, simpleGE, pygame

class MoveSprite(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene, color, size, x, y, angle=0):
        super().__init__(scene)
        self.colorRect(color, size)
        self.x = x
        self.y = y
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

class DriveSprite(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene, color, size, x, y, angle=0):
        super().__init__(scene)
        self.colorRect(color, size)
        self.x = x
        self.y = y
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

class LblOut(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 30)
        self.size = (500, 30)
        self.fgColor = "blue"
        self.bgColor = "white"
        self.clearBack = True
                
class CollisionScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        self.setCaption("SAT Collision Test. WASD for blue, arrows for red. q (or e) to change red angle, n (or m) to change blue.")
        
        self.sprite1 = MoveSprite(self, "red", (120, 60), 300, 300, 30)
        self.sprite2 = DriveSprite(self, "blue", (100, 40), 500, 200, -20)
        self.lblOut = LblOut()
    
        self.sprites = [self.sprite1, self.sprite2, self.lblOut]
        
    def update(self):
        super().update()
        
        testSAT = False
        testAABB = False
        
        sprite1SAT = self.sprite1.collidesWithAdvanced(self.sprite2)
        sprite1AABB = self.sprite1.collidesWith(self.sprite2)
        
        sprite2SAT = self.sprite2.collidesWithAdvanced(self.sprite1)
        sprite2AABB = self.sprite2.collidesWithAdvanced(self.sprite1)
        
        if sprite1SAT or sprite2SAT:
            testSAT = True
        
        if sprite1AABB or sprite2AABB:
            testAABB = True
        
        self.lblOut.text = f"SAT: {testSAT} , AABB: {testAABB}"
        
def main():
    game = CollisionScene()
    game.start()
        
if __name__ == "__main__":
    main()