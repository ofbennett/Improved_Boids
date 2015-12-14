"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

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
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
