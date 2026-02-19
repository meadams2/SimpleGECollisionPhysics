"""testCollisions.py
Testing Frame for Collision Physics
Marianne Adams, 2025"""

import CollisionPhysics, simpleGE, pygame

class TestSprite(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene, color, size, x, y, angle=0, active=False):
        super().__init__(scene)
        self.colorRect(color, size)
        self.x = x
        self.y = y
        self.setAngle(angle)
        self.moveAngle = angle
        self.speed = 0
        self.active = active
    
    def process(self):
        # Allow for movement of first sprite only to test
        if self.active:
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

class CollisionScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("SAT Collision Test")
        
        self.sprite1 = TestSprite(self, "red", (120, 60), 300, 300, 30, active=True)
        self.sprite2 = TestSprite(self, "blue", (100, 40), 500, 200, -20)
        
        self.sprites = [self.sprite1, self.sprite2]
        
    def update(self):
        super().update()
        
        testSAT = self.sprite1.collidesWithAdvanced(self.sprite2)
        testSimple = self.sprite1.collidesWith(self.sprite2)
        
        print(f" SAT: {testSAT} | Simple: {testSimple}")
        
if __name__ == "__main__":
    scene = CollisionScene()
    scene.start()