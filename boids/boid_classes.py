"""
Implementations of the Boid and Swarm classes.
"""

import random
import numpy as np

#Each instance of the Boid class represents a particular boid in the group
class Boid(object):
	def __init__(self,x,y,vx,vy,swarmSize,behaviour):
		self.position = np.array([x,y])
		self.velocity = np.array([vx,vy])
		self.swarmSize = swarmSize
		self.middle_attraction = behaviour['middle_attraction']
		self.avoidance_radius = behaviour['avoidance_radius']
		self.copycat_radius = behaviour['copycat_radius']
		self.copycat_influence = behaviour['copycat_influence']

	def flyTowards(self,other):
		self.velocity += (other.position - self.position)*self.middle_attraction/self.swarmSize

	def flyAwayFrom(self,other):
		if np.linalg.norm(other.position - self.position) < self.avoidance_radius:
			self.velocity += (self.position - other.position)

	def copy(self,other):
		if np.linalg.norm(other.position - self.position) < self.copycat_radius:
			self.velocity += (other.velocity - self.velocity)*self.copycat_influence/self.swarmSize

	def move(self):
		self.position += self.velocity

#An instance of the Swarm class represents a group of Boid objects all 
#interacting with each other.
class Swarm(object):
	def __init__(self):
		self.members = []
		self.size = 0

	def hatch(self,swarmSize,behaviour):
		self.members = [Boid(random.uniform(-450,50.0),
							 random.uniform(300.0,600.0),
							 random.uniform(0,10.0),
							 random.uniform(-20.0,20.0),swarmSize,behaviour) for x in range(swarmSize)]
		self.size = swarmSize

	def hatch_test(self,x,y,vx,vy,swarmSize,behaviour):
		self.members = [Boid(x[i],y[i],vx[i],vy[i],swarmSize,behaviour) for i in range(swarmSize)]
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
