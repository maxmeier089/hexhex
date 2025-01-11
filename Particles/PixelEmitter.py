from Particles.PixelParticle import PixelParticle
from Particles.Emitter import Emitter

class PixelEmitter(Emitter):
    
    def __init__(self, pos, vel, delay, ttl, color):
        super().__init__(pos, vel, delay, ttl, color)

    def createParticle(self, pos, vel, ttl, startColor, endColor):
        self.particles.add(PixelParticle(pos, vel, ttl, startColor, endColor))
