from celestialbody import CelestialBody  # Imports the Ball-class from the ball.py tab
from math import sqrt

planets = []
sun = CelestialBody(1.989E30, 0, 0, 0, 0, 'star')

#constants
G = 6.67408E-11
dt = 60*60*24 # Time step one day

def setup():
    size(600,600) # Sets the size of the window
    
    sun = CelestialBody(1.989E30, 0, 0, 0, 0, 'star')
    planet = CelestialBody(5.972E24, 1.496E11, 0, 0, 2.0E4, 'planet')
    planets.append(planet)

def draw():
    background(3);  # Sets the background colour to (234, 234, 234)

    for planet in planets:
        # calculate the gravitational force from distance between planet and sun
        dx = sun.x - planet.x
        dy = sun.y - planet.y
        l = planet.distance(sun)
        
        # gravitational force 
        Fg = G*sun.m*planet.m/l**2
        # gravitational force komposants
        Fgx = Fg * dx/l
        Fgy = Fg * dy/l

        planet.applyForce(Fgx, Fgy) # Applying a downwards force sqrt(dx**2 + dy**2)
        planet.update(dt) # Updating the position of each ball, dt = 0.1
        planet.show() # tell the ball to show itself on the screen.
        
    #  Remove planets that crash in to the star
    for planet in planets[:]:
        l1 = planet.distance(sun)
        l2 = planet.r + sun.r
        if (planet.distance(sun) < planet.r + sun.r):
            planets.remove(planet) 
    
    sun.show()
