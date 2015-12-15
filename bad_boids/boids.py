"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import random
import numpy as np

middle_attraction = 0.01
avoidance_radius = 10.0
copycat_radius = 100.0
copycat_influence = 0.125

class Boid(object):
	def __init__(self,x,y,vx,vy,swarmSize):
		self.position = np.array([x,y])
		self.velocity = np.array([vx,vy])
		self.swarmSize = swarmSize

	def flyTowards(self,other):
		self.velocity += (other.position - self.position)*middle_attraction/self.swarmSize

	def flyAwayFrom(self,other):
		if np.linalg.norm(other.position - self.position) < avoidance_radius:
			self.velocity += (self.position - other.position)

	def copy(self,other):
		if np.linalg.norm(other.position - self.position) < copycat_radius:
			self.velocity += (other.velocity - self.velocity)*copycat_influence/self.swarmSize

	def move(self):
		self.position += self.velocity


class Swarm(object):
	def __init__(self):
		self.members = []
		self.size = 0

	def hatch(self,swarmSize):
		self.members = [Boid(random.uniform(-450,50.0),
							 random.uniform(300.0,600.0),
							 random.uniform(0,10.0),
							 random.uniform(-20.0,20.0),swarmSize) for x in range(swarmSize)]
		self.size = swarmSize

	def hatch_test(self,x,y,vx,vy,swarmSize):
		self.members = [Boid(x[i],y[i],vx[i],vy[i],swarmSize) for i in range(swarmSize)]
		self.size = swarmSize

	def update(self):
		for this in self.members:
			for that in self.members:
				if this is not that:
					this.flyTowards(that)
					this.flyAwayFrom(that)

		for this in self.members:
			for that in self.members:
				if this is not that:
					this.copy(that)

		for this in self.members:
			this.move()

	def boidPositions(self):
		xs = [self.members[x].position[0] for x in range(self.size)]
		ys = [self.members[x].position[1] for x in range(self.size)]
		return [xs,ys]

	def boidVelocities(self):
		vxs = [self.members[x].velocity[0] for x in range(self.size)]
		vys = [self.members[x].velocity[1] for x in range(self.size)]
		return [vxs,vys]
