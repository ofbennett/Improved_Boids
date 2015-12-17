This is the README file for the Improved_Bad-Boids package

By Oscar Bennett, UCL
Student Number - 14087294

This is an improved implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406). Original worse code obtained from https://github.com/jamespjh/bad-boids which was then then refactored in multiple ways.

The package is installed by running the setup.py script:

python setup.py install

This package generates an animation of the simulated movement of 'boids'. The number of boids in the simulated group along with some behavioural characteristics of the boids can be either user defined or assigned to default settings.

The command line interface is shown below. The entry point script boids.py either needs to be in the current directory or in the systems's search path to be run!

usage: boids.py [-h] [--size SIZE] [--middle_attraction MIDDLE_ATTRACTION]
                  [--avoidance_radius AVOIDANCE_RADIUS]
                  [--copycat_radius COPYCAT_RADIUS]
                  [--copycat_influence COPYCAT_INFLUENCE]
                  [--config_file CONFIG_FILE] [--existing_file]

A program which displays an animation of a swarm of boids with user defined
behaviour and size

optional arguments:

  -h, --help            show this help message and exit

  --size SIZE, -s SIZE  Number of boids in the swarm. Default is 50.

  --middle_attraction MIDDLE_ATTRACTION, -m MIDDLE_ATTRACTION
                        The attraction that a boid feels to stay near the
                        centre of the swarm. Default value is 0.01

  --avoidance_radius AVOIDANCE_RADIUS, -a AVOIDANCE_RADIUS
                        The distance where two boids start trying to avoid
                        getting closer. Default is 10

  --copycat_radius COPYCAT_RADIUS, -cr COPYCAT_RADIUS
                        The distance where two boids start trying to match
                        eachother's velocity. Default is 100.

  --copycat_influence COPYCAT_INFLUENCE, -ci COPYCAT_INFLUENCE
                        The extent to which boids alter their velocity to
                        match the velocities of the boids near them. Default
                        is 0.125.

  --config_file CONFIG_FILE, -f CONFIG_FILE
                        The name of the config file which is generated
                        containing all the parameters passed to the program.
                        Default is config_most_recent.yml
                        
  --existing_file, -e   Flag to include if the progam is to be run by loading
                        arguments from an existing config file in the config
                        folder. The name of this file must be specified with
                        the [--config_file] [-f] argument.)
