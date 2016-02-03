"""
Test file containing unit tests of the boid class
"""

from boids.boid_classes import Boid
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml

#Load standard swarm behaviour information to contruct Boid and Swarm instances below
behaviour=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','standard_swarm.yml')))

middle_attraction = behaviour['middle_attraction']
avoidance_radius = behaviour['avoidance_radius']
copycat_radius = behaviour['copycat_radius']
copycat_influence = behaviour['copycat_influence']
boid_num = behaviour['boid_num']

def test_Boid_initialisation():
    boid = Boid(1,2,3,4,boid_num,behaviour)
    assert_equal(boid.position[0],1)
    assert_equal(boid.position[1],2)
    assert_equal(boid.velocity[0],3)
    assert_equal(boid.velocity[1],4)

def test_Boid_flyTowards():
    this_boid = Boid(0.0,0.0,1.0,1.0,boid_num,behaviour)
    that_boid = Boid(10.0,0.0,1.0,1.0,boid_num,behaviour)
    this_boid.flyTowards(that_boid)

    assert_almost_equal(this_boid.velocity[0],1.0+ 10*(middle_attraction/boid_num))
    assert_almost_equal(this_boid.velocity[1],1.0)
    assert_equal(this_boid.position[0],0.0)
    assert_equal(this_boid.position[1],0.0)


def test_Boid_flyAwayFrom():
    this_boid = Boid(5.0,0.0,1.0,1.0,boid_num,behaviour)
    that_boid = Boid(0.0,0.0,1.0,1.0,boid_num,behaviour)
    another_boid = Boid(15.0,0.0,1.0,1.0,boid_num,behaviour)
    this_boid.flyAwayFrom(that_boid)
    another_boid.flyAwayFrom(that_boid)

    assert_almost_equal(this_boid.velocity[0],1.0 + 5)
    assert_almost_equal(this_boid.velocity[1],1.0)
    assert_almost_equal(another_boid.velocity[0],1.0)
    assert_almost_equal(another_boid.velocity[1],1.0)
    assert_equal(this_boid.position[0],5.0)
    assert_equal(this_boid.position[1],0.0)

def test_Boid_copy():
    this_boid = Boid(10.0,0.0,1.0,11.0,boid_num,behaviour)
    that_boid = Boid(0.0,0.0,11.0,1.0,boid_num,behaviour)
    another_boid = Boid(200.0,0.0,1.0,1.0,boid_num,behaviour)
    this_boid.copy(that_boid)
    another_boid.copy(that_boid)

    assert_almost_equal(this_boid.velocity[0],1.0 + 10*copycat_influence/boid_num)
    assert_almost_equal(this_boid.velocity[1],11.0 - 10*copycat_influence/boid_num)
    assert_almost_equal(another_boid.velocity[0],1.0)
    assert_almost_equal(another_boid.velocity[1],1.0)
    assert_equal(this_boid.position[0],10.0)
    assert_equal(this_boid.position[1],0.0)

def test_Boid_move():
    boid = Boid(1.0,1.0,2.0,3.0,boid_num,behaviour)
    boid.move()

    assert_almost_equal(boid.position[0],3.0)
    assert_almost_equal(boid.position[1],4.0)
