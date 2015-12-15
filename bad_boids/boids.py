"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

middle_attraction = 0.01
avoidance_radius = 10
copycat_radius = 100
copycat_influence = 0.125
boid_num = 50

boids_x=[random.uniform(-450,50.0) for x in range(boid_num)]
boids_y=[random.uniform(300.0,600.0) for x in range(boid_num)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(boid_num)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(boid_num)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

class Boid(object):
	def __init__(self,x,y,vx,vy):
		self.position = np.array([x,y])
		self.velocity = np.array([vx,vy])

	def flyTowards(self,other):
		self.velocity += (other.position - self.position)*middle_attraction/boid_num

	def flyAway(self,other):
		if np.linalg.norm(other.position - self.position) < avoidance_radius:
			self.velocity += (self.position - other.position)

	def copy(self,other):
		if np.linalg.norm(other.position - self.position) < copycat_radius:
			self.velocity += (other.velocity - self.velocity)*copycat_influence/boid_num

	def move(self):
		self.position += self.velocity

class Swarm(object):
	def __init__(self):
		self.members = []
		self.size = 0

	def hatch(self,number):
		self.members = [Boid(random.uniform(-450,50.0),
							 random.uniform(300.0,600.0),
							 random.uniform(0,10.0),
							 random.uniform(-20.0,20.0)) for x in range(number)]
		self.size = number

	def update(self):
		for this in self.members:
			for that in self.members:
				this.flyTowards(that)
				this.flyAway(that)
				this.copy(that)
			this.move()

	def boidPositions(self):
		xs = [self.members[x].position[0] for x in range(self.size)]
		ys = [self.members[x].position[1] for x in range(self.size)]
		return [xs,ys]

swarm = Swarm()
swarm.hatch(boid_num)
boid_xs,boid_ys = swarm.boidPositions()

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(boid_num):
		for j in range(boid_num):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*middle_attraction/boid_num
	for i in range(boid_num):
		for j in range(boid_num):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*middle_attraction/boid_num
	# Fly away from nearby boids
	for i in range(boid_num):
		for j in range(boid_num):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < avoidance_radius**2:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(boid_num):
		for j in range(boid_num):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < copycat_radius**2:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*copycat_influence/boid_num
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*copycat_influence/boid_num
	# Move according to velocities
	for i in range(boid_num):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
# scatter=axes.scatter(boids[0],boids[1])
scatter=axes.scatter(boid_xs,boid_ys)

def animate(frame):
	swarm.update()
	xs,ys = swarm.boidPositions()
	scatter.set_offsets(zip(xs,ys))

 #   	update_boids(boids)
 #   	scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
