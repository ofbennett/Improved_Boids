from boid_classes import Swarm
from matplotlib import pyplot as plt
from matplotlib import animation
import os
import yaml

def animate_boids_func(config_file_name):
    swarm_info=yaml.load(open(os.path.join(os.path.dirname(__file__),'config',config_file_name)))

    boid_num = swarm_info['boid_num']
    behaviour = swarm_info

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

    anim = animation.FuncAnimation(figure, animate,frames=50, interval=50)
    plt.show()

if __name__ == "__main__":
    config_file_name = 'config_standard.yml'
    animate_boids_func(config_file_name)
