"""testCollisions.py
Testing Frame for Collision Physics
Marianne Adams, 2025"""

import collisionPhysics, simpleGE, pygame

class MovingObject(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Green", (50, 50))
        
    def process(self):
        """Tests movement, checks for barrier collisions and calls collisionPhysics accordingly"""

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
            
            """Tests angle of reflection when colliding against barrier"""
            
            if self.isKeyPressed(pygame.K_UP):
                self.speed += .1
            if self.isKeyPressed(pygame.K_DOWN):
                self.speed -= .1
            if self.isKeyPressed(pygame.K_LEFT):
                self.imageAngle += 5
                self.moveAngle += 5
            if self.isKeyPressed(pygame.K_RIGHT):
                self.imageAngle -= 5
                self.moveAngle -= 5
            
            if self.isKeyPressed(pygame.K_w):
                self.boundAction = self.WRAP
            elif self.isKeyPressed(pygame.K_b):
                self.boundAction = self.BOUNCE
            
            self.scene.lblOut.text = f"m: {self.moveAngle}, i: {self.imageAngle}"
            
            barrier = self.scene.barrier
            angle = self.moveAngle % 360
            
            if angle < 45:
                direction = "right"
            elif angle <135:
                direction = "up"
            elif angle < 225:
                direction = "left"
            elif angle < 315:
                direction = "down"
            else:
                direction = "right"
                
            if self.collidesWith(barrier):
                collisionResult = collisionPhysics.handleAngleOfCollision(self, barrier)
            
            