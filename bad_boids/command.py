from argparse import ArgumentParser
from animate_boids import animate_boids_func

def process():
    parser = ArgumentParser(description = 'A program which displays an animation of a swarm of boids with user defined behaviour and size')
    parser.add_argument('--size','-s',default = 50, help = 'Number of boids in the swarm. Default is 50.',type = int)
    parser.add_argument('--middle_attraction','-m',default = 0.01, help = 'The attraction that a boid feels to stay near the centre of the swarm. Default value is 0.01',type = float)
    parser.add_argument('--avoidance_radius','-a',help = 'The distance where two boids start trying to avoid getting closer. Default is 10',default = 10.0,type = float)
    parser.add_argument('--copycat_radius','-cr',default = 100.0, help = "The distance where two boids start trying to match eachother's velocity. Default is 100.",type = float)
    parser.add_argument('--copycat_influence','-ci',default = 0.125, help = 'The extent to which boids alter their velocity to match the velocities of the boids near them. Default is 0.125.',type = float)
    parser.add_argument('--config_file','-f',default = 'config_most_recent.yml', help = 'The name of the config file which is generated containing all the parameters passed to the program. Default is config_most_recent.yml')
    arguments = parser.parse_args()

    if (arguments.size <0 or arguments.middle_attraction <0 or arguments.avoidance_radius <0
    or arguments.copycat_radius <0 or arguments.copycat_influence <0):
        raise ValueError('Arguments cannot be negative.')



if __name__ == '__main__':
    process()