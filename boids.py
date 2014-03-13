"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
from numpy import array

# Will now add an Eagle to Boids

class Boid(object):
    def __init__(self,x,y,xv,yv,owner,species="Starling"):
        self.position=array([x,y])
        self.velocity=array([xv,yv])
        self.owner=owner
        self.species=species

    def interaction(self,other):
        delta_v=array([0.0,0.0])
        separation=other.position-self.position
        separation_sq=separation.dot(separation)
 
        if other.species=="Eagle":
            # Flee the Eagle
            if separation_sq < self.owner.eagle_avoidance_radius**2:
                delta_v-=(separation*self.owner.eagle_fear)/separation.dot(separation)
                return delta_v

        if self.species=="Eagle":
            # Hunt the boids
            delta_v+=separation*self.owner.eagle_hunt_strength
        else:

            # Fly towards the middle
            if separation_sq < 2000**2:
                delta_v+=separation*self.owner.flock_attraction
            
            # Fly away from nearby boids
            if separation_sq < self.owner.avoidance_radius**2:
                delta_v-=separation

            # Try to match speed with nearby boids
            if separation_sq < self.owner.formation_flying_radius**2:
                delta_v+=(other.velocity-self.velocity)*self.owner.speed_matching_strength

        return delta_v


# Deliberately terrible code for teaching purposes
class Boids(object):
    def __init__(self,
           flock_attraction,avoidance_radius,
            formation_flying_radius,speed_matching_strength,
            eagle_avoidance_radius=100, eagle_fear=5000, eagle_hunt_strength=0.00005,
            max_speed=30.0,
            bounds=None):
        self.flock_attraction=flock_attraction
        self.avoidance_radius=avoidance_radius
        self.formation_flying_radius=formation_flying_radius
        self.speed_matching_strength=speed_matching_strength
        self.eagle_avoidance_radius=eagle_avoidance_radius
        self.eagle_fear=eagle_fear
        self.eagle_hunt_strength=eagle_hunt_strength
        self.bounds=bounds
        self.max_speed=max_speed


    def initialise_random(self,count):
        if self.bounds:
            self.boids=[Boid(random.uniform(self.bounds[0],self.bounds[2]),
                random.uniform(self.bounds[1],self.bounds[3]),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0),self) for i in range(count)]
        else:
            self.boids=[Boid(random.uniform(-450,50.0),
                random.uniform(300.0,600.0),
                random.uniform(0,10.0),
                random.uniform(-20.0,20.0),self) for i in range(count)]

    def add_eagle(self,x,y,xv,yv):
        self.boids.append(Boid(x,y,xv,yv,self,species="Eagle"))

    def initialise_from_data(self,data):
        self.boids=[Boid(x,y,xv,yv,self) for x,y,xv,yv in zip(*data)]

    def update(self):
        for me in self.boids:
            delta_v=array([0.0,0.0])
            for him in self.boids:
                if me is him:
                    continue
                delta_v+=me.interaction(him)
            # Accelerate as stated
            me.velocity+=delta_v
            # Move according to velocities

            if me.velocity.dot(me.velocity)>=self.max_speed**2:
                me.velocity=self.max_speed*me.velocity/(me.velocity.dot(me.velocity)**0.5)

            me.position+=me.velocity

            if self.bounds:
                if me.position[0]>self.bounds[2]:
                    me.position[0]-=self.bounds[2]-self.bounds[0]

                if me.position[0]<self.bounds[0]:
                    me.position[0]+=self.bounds[2]-self.bounds[0]

                if me.position[1]>self.bounds[3]:
                    me.position[1]-=self.bounds[3]-self.bounds[1]

                if me.position[1]<self.bounds[1]:
                    me.position[1]+=self.bounds[3]-self.bounds[1]
