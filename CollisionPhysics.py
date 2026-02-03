"""CollisionPhysics.py
Marianne Adams, 2025
Created to be used in conjunction with SimpleGE for more advanced collisions"""

import simpleGE, pygame

class CollisionPhysics(simpleGE.Sprite):
    
    def collidesWithAdvanced(self, target):
        """Boolean function. Returns True if the sprite
           is currently colliding with the target sprite,
           false otherwise."""
        collision = False
        if self.visible:
            if target.visible:
                polygonSprite = spriteToPolygon(self)
                polygonTarget = spriteToPolygon(target)
                
                for polygon in (polygonSprite, polygonTarget):
                    edges = getEdges(polygon)
                    
                    for edge in edges:
                        axis = getLeftNormal(edge)
                        
                        minSprite, maxSprite = getProjection(polygonSprite, axis)
                        minTarget, maxTarget = getProjection(polygonTarget, axis)
                        
                        # If there's a separating axis, no collision
                        if maxSprite < minTarget:
                            collision = False
                        if maxTarget < minSprite:
                            collision = False
        return collision
    
    def spriteToPolygon(self):
        """Handles n edges to handle more complex shapes"""
        
        sprite_width = self.imageMaster.get_width()
        sprite_height = self.imageMaster.getHeight()
        
    
        
        
    


    