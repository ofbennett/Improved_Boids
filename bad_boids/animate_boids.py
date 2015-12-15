from boids import Swarm
from matplotlib import pyplot as plt
from matplotlib import animation

boid_num = 50

swarm = Swarm()
swarm.hatch(boid_num)
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
