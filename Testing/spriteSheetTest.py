"""Testing SpriteSheet
Creating and using Spritesheet with Collisions
Sprites from LPC generator
https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/
Marianne Adams, 2026"""

import CollisionPhysics, simpleGE, pygame

class Player(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene):
        super().__init__(scene)
        self.walkAnim = simpleGE.SpriteSheet("characterSprite.png", (64, 64), 4, 9, .1)
        
        # Define smaller hitbox size for better collisions
        self.hitboxSize = (30, 30)
        
        # LPC sprites usually have upper space and feet near bottom. Positive Y in offset moves hitbox down
        self.setHitboxOffset(0, 10)
        self.walkAnim.startCol = 1
        self.animRow = 2
        self.moveSpeed = 2
    
        self.copyImage(self.walkAnim.getCellImage(0, self.animRow))
        
    def process(self):
        moveX = 0
        moveY = 0
        walking = False
        
        if self.isKeyPressed(pygame.K_UP):
            self.animRow = 0
            moveY =- self.moveSpeed
            walking = True
        
        if self.isKeyPressed(pygame.K_LEFT):
            self.animRow = 1
            moveX =- self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_DOWN):
            self.animRow = 2
            moveY = self.moveSpeed
            walking = True
        if self.isKeyPressed(pygame.K_RIGHT):
            self.animRow = 3
            moveX = self.moveSpeed
            walking = True
            
        # Try movement
        self.x += moveX
        self.y += moveY
        
        # Animation
        if walking:
            self.copyImage(self.walkAnim.getNext(self.animRow))
        else:
            self.copyImage(self.walkAnim.getCellImage(0, self.animRow))
        
class Box(CollisionPhysics.CollisionPhysics):
    def __init__(self, scene, angle=0):
        super().__init__(scene)
        self.colorRect("blue", (120, 60))
        self.x = 300
        self.y = 300
        self.hitboxSize = (120, 60)
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
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill(pygame.Color("white"))
        self.setCaption("Arrows to move player around screen")
        
        self.player = Player(self)
        self.box = Box(self)
        self.collisionLbl = CollisionOut()
        self.angleLbl = AngleOut()
        
        self.sprites = [self.player, self.box, self.collisionLbl, self.angleLbl]
        
    def update(self):
        super().update()
        
        testSAT = False
        testAABB = False
        
        collisionNormal = None
        collisionAngle = 0
        
        playerSAT, collisionNormal, collisionAngle = self.player.collidesWithAdvanced(self.box)
        playerAABB = self.player.collidesWith(self.box)
        
        boxSAT, collisionNormal, collisionAngle = self.box.collidesWithAdvanced(self.player)
        boxAABB = self.box.collidesWith(self.player)
        
        if playerSAT or boxSAT:
            testSAT = True
            self.angleLbl.text = f"Angle: {collisionAngle: .2f}"
        else:
            self.angleLbl.text = "Angle: None"
            
        if playerAABB or boxAABB:
            testAABB = True
        
        self.collisionLbl.text = f"SAT: {testSAT}, AABB: {testAABB}"

def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
        
        

