class CelestialBody:
    def __init__(self, m, x, y, v0x, v0y, bodyType):
        self.x = x 
        self.y = y
        
        self.m = m  
        self.vx = v0x
        self.vy = v0y
        self.ax = 0
        self.ay = 0

        self.bodyType = bodyType
        if bodyType == 'star':
            self.displayr = 10
        elif bodyType == 'planet':
            self.displayr = 5
        
        self.r = self.displayr*5.0*1.496E11/300
    
        
    def show(self):
        # Scale system to show 5 earth orbits on screen
        a = 1.496E11
        x_pixel = self.x*300/5.0/1.496E11 + 300 #(self.x/a+0.5)*300
        y_pixel = self.y*300/5.0/1.496E11 + 300 #(self.y/a+0.5)*300

        if self.bodyType == 'star':
            fill(204, 102, 0)
        elif self.bodyType == 'planet':
            fill(20,100,30)
        
        ellipse( x_pixel, y_pixel, self.displayr*2 , self.displayr*2)

        
    def applyForce(self, fx, fy):
        self.ax += fx/self.m
        self.ay += fy/self.m
        
    def distance(self, body):
        dx = self.x - body.x
        dy = self.y - body.y
        return sqrt(dx**2 + dy**2)      
                
    def update(self, dt):
        # delta_v/delta_t = a gives that  delta_v = a*delta_t
        self.vx += self.ax*dt
        self.vy += self.ay*dt
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.ax = 0
        self.ay = 0
