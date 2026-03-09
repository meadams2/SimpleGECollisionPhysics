"""physicsTest.py
Testing Physics Portion of Collision Physics
Marianne Adams, 2026"""

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

class CollisionOut(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (500, 30)
        self.size = (300, 30)
        self.fgColor = "black"
        self.bgColor = "white"
        self.clearBack = True

class CollisionScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("gray")
        self.setCaption("Test Physics with Collisions")
        
        self.moveSprite = MoveSprite(self, "red", (60, 60), 300, 300, 30)
        self.driveSprite = DriveSprite(self, "blue", (100, 40), 500, 200, -20)
        self.collisionLbl = CollisionOut()
        
        self.sprites = [self.moveSprite, self.driveSprite, self.collisionLbl]
        
    def update(self):
        super().update()
        
        moveSpriteAABB = self.moveSprite.collidesWith(self.driveSprite)
        moveSpriteSAT = self.moveSprite.resolveCollision(self.driveSprite, "bounce", 1, False)
        
        self.collisionLbl.text = f"SAT: {moveSpriteSAT}, AABB: {moveSpriteAABB}"

def main():
    game = CollisionScene()
    game.start()

if __name__ == "__main__":
    main()
    