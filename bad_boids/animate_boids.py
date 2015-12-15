from boids import Swarm
from matplotlib import pyplot as plt
from matplotlib import animation

boid_num = 50
behaviour = {'middle_attraction' : 0.01,
             'avoidance_radius' : 10.0,
             'copycat_radius' : 100.0,
             'copycat_influence' : 0.125}

swarm = Swarm()
swarm.hatch(boid_num,behaviour)
boid_xs,boid_ys = swarm.boidPositions()

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boid_xs,boid_ys)

def animate(frame):
	swarm.update()
	xs,ys = swarm.boidPositions()
	scatter.set_offsets(zip(xs,ys))

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
