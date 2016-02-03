"""
Test file containing a regression test of the entire package.
"""

from boids.boid_classes import Swarm
from nose.tools import assert_almost_equal
import os
import yaml

#Load standard swarm behaviour information to contruct Boid and Swarm instances below
behaviour=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','standard_swarm.yml')))

#Regression test for this improved object orientated version of the boids code
def test_OO_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture.yml')))
    boid_data=regression_data["before"]
    swarm = Swarm()
    swarm.hatch_test(boid_data[0],boid_data[1],boid_data[2],boid_data[3],len(boid_data[0]),behaviour)
    swarm.update()

    true_after = regression_data["after"]
    true_x = true_after[0]
    true_y = true_after[1]
    true_vx = true_after[2]
    true_vy = true_after[3]

    test_x, test_y = swarm.boidPositions()
    test_vx, test_vy = swarm.boidVelocities()

    for test_x_val,true_x_val in zip(test_x,true_x):
        assert_almost_equal(test_x_val,true_x_val,delta=0.01)

    for test_y_val,true_y_val in zip(test_y,true_y):
        assert_almost_equal(test_y_val,true_y_val,delta=0.01)

    for test_vx_val,true_vx_val in zip(test_vx,true_vx):
        assert_almost_equal(test_vx_val,true_vx_val,delta=0.01)

    for test_vy_val,true_vy_val in zip(test_vy,true_vy):
        assert_almost_equal(test_vy_val,true_vy_val,delta=0.01)
