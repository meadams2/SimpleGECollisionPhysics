"""CollisionPhysics.py
Marianne Adams, 2025
Created to be used in conjunction with SimpleGE for more advanced collisions"""

import simpleGE
from pygame.math import Vector2

class CollisionPhysics(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.originPolygon = []
    
    def collidesWithAdvanced(self, target):
        """Boolean function. Returns True if the sprite
           is currently colliding with the target sprite,
           false otherwise.
           Utilizes SAT collision detection"""
        # Check visibility
        if not self.visible or not target.visible:
            return False
        
        # Convert sprite edges to geometric vectors
        spritePolygon = self.spriteToPolygon()
        targetPolygon = target.spriteToPolygon()
        
        # Get edges from both shapes
        spriteEdges = self.getEdges(spritePolygon)
        targetEdges = self.getEdges(targetPolygon)
        
        for edge in spriteEdges + targetEdges:
            # Get perpendicular axis
            axis = self.getNormal(edge)
            
            # Project both polygons onto axis
            minSprite, maxSprite = self.getProjection(spritePolygon, axis)
            minTarget, maxTarget = self.getProjection(targetPolygon, axis)
            
            # Check for separating axis
            if maxSprite < minTarget:
                return False
            if maxTarget < minSprite:
                return False
            
        return True
        
        
    def buildRectangularPolygon(self):
        """Gets Rectangular polygon based on imageMaster.
           Helper function.
           Centered at origin."""
        width = self.imageMaster.get_width()
        height = self.imageMaster.get_height()
        
        self.originPolygon = [
            Vector2(-width/2, -height/2),
            Vector2(width/2, -height/2),
            Vector2(width/2, height/2),
            Vector2(-width/2, height/2)]
    
    def spriteToPolygon(self):
        """Rectangular polygon is rotated by the image angle and shifted by x and y.
           Sprite's actual screen position & represents real shape
           Geometry conversion"""
        
        if len(self.originPolygon) == 0:
            self.buildRectangularPolygon()
        
        polygonEdgePoints = []
        
        for point in self.originPolygon:
            rotated = point.rotate(-self.imageAngle)
            # Calculate point not centered at origin
            calculatedPoint = rotated + Vector2(self.x, self.y)
            polygonEdgePoints.append(calculatedPoint)
        
        return polygonEdgePoints
    
    def getEdges(self, polygon):
        """Extracts side vectors to from sprite.
           Determines direction vectors of the polygon's sides
           Assumes polygon is convex"""
        edges = []
        numberEdges = len(polygon)
        
        for i in range(numberEdges):
            point1 = polygon[i]
            point2 = polygon[(i+1) % numberEdges] # Wraps around to get 1st point
            edge = point2 - point1
            edges.append(edge)
        
        return edges
    
    def getNormal(self, edge):
        """Gets the normal vector for the given edge."""
        normal = edge.rotate(90)
        if normal.length() != 0:
            normal = normal.normalize() # Method comes from pygame.math.Vector2
            
        return normal
    
    def getProjection(self, polygon, axis):
        """The polygon is a list of Vector2 points
           The axis is a normalized vector
           Projects every vertex of a polygon onto a single axis
           Returns minimum and maximum scalar values
           Uses dot product of vectors to get orthogonal projection"""
        minimumProjection = polygon[0].dot(axis)
        maximumProjection = minimumProjection
        
        for point in polygon[1:]:
            projection = point.dot(axis)
            
            if projection < minimumProjection:
                minimumProjection = projection
            elif projection > maximumProjection:
                maximumProjection = projection
        
        return minimumProjection, maximumProjection
        
    
            
        
        
        
        
    


    