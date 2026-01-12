"""testCollisions.py
Testing Frame for Collision Physics
Marianne Adams, 2025"""

import collisionPhysics, simpleGE, pygame

class MovingObject(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Green", (50, 50))
        
    def process(self):
        """Handles movement, checks for barrier collisions and calls collisionPhysics accordingly"""

        self.speed = 0

        # Movement
        if self.isKeyPressed(pygame.K_a):
            self.dx = -5
            self.dir = "left"
        elif self.isKeyPressed(pygame.K_d):
            self.dx = 5
            self.dir = "right"
        elif self.isKeyPressed(pygame.K_w):
            self.dy = -5
            self.dir = "up"
        elif self.isKeyPressed(pygame.K_s):
            self.dy = 5
            self.dir = "down"

        # Barrier Checking
        barrier = self.scene.barrier
        if self.collidesWith(barrier):
            collisionResult = collisionPhysics.handleCollisionOfTwoObjects(self, barrier)
        
    class DrivingObject(simpleGE.Sprite):
        def __init__(self, scene):
            super().__init__(scene)
            self.colorRect("blue", (50, 20))
            self.setAngle(45)
        
        def process(self):