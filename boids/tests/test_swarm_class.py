"""
Test file containing unit tests of the swarm class.
"""

from boids.boid_classes import Swarm
from nose.tools import assert_equal, assert_less, assert_greater
import os
import yaml

#Load standard swarm behaviour information to contruct Boid and Swarm instances below
behaviour=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','standard_swarm.yml')))

def test_Swarm_initialisation():
    swarm = Swarm()
    assert hasattr(swarm,'members')
    assert hasattr(swarm,'size')
    assert_equal(len(swarm.members),0)
    assert_equal(swarm.size,0)

def test_Swarm_hatch():
    swarm = Swarm()
    swarm.hatch(50,behaviour)

    assert_equal(swarm.size,50)
    assert_equal(len(swarm.members),50)

    for boid in swarm.members:
        assert_greater(boid.position[0],-450)
        assert_less(boid.position[0],50)
        assert_greater(boid.position[1],300)
        assert_less(boid.position[1],600)
        assert_greater(boid.velocity[0],0)
        assert_less(boid.velocity[0],10)
        assert_greater(boid.velocity[1],-20)
        assert_less(boid.velocity[1],20)

def test_Swarm_hatch_test():
    xs = [0.0,1.0,2.0]
    ys = [1.0,2.0,3.0]
    vxs = [4.0,5.0,6.0]
    vys = [5.0,6.0,7.0]

    swarm = Swarm()
    swarm.hatch_test(xs,ys,vxs,vys,len(xs),behaviour)

    assert_equal(swarm.size,3)

    for i in range(3):
        for j in range(2):
            assert_equal(swarm.members[i].position[j],i+j)

    for i in range(3):
        for j in range(2):
            assert_equal(swarm.members[i].velocity[j],i+j+4)

def test_Swarm_update():
        xs = [0.0]
        ys = [1.0]
        vxs = [2.0]
        vys = [3.0]
        swarm = Swarm()
        swarm.hatch_test(xs,ys,vxs,vys,len(xs),behaviour)
        swarm.update()

        assert_equal(swarm.members[0].position[0],0.0+2.0)
        assert_equal(swarm.members[0].position[1],1.0+3.0)
        assert_equal(swarm.members[0].velocity[0],2.0)
        assert_equal(swarm.members[0].velocity[1],3.0)


def test_Swarm_boidPositions():
    xs = [0.0,1.0,2.0]
    ys = [1.0,2.0,3.0]
    vxs = [4.0,5.0,6.0]
    vys = [5.0,6.0,7.0]

    swarm = Swarm()
    swarm.hatch_test(xs,ys,vxs,vys,len(xs),behaviour)

    assert_equal(swarm.boidPositions()[0],xs)
    assert_equal(swarm.boidPositions()[1],ys)

def test_Swarm_boidVelocities():
    xs = [0.0,1.0,2.0]
    ys = [1.0,2.0,3.0]
    vxs = [4.0,5.0,6.0]
    vys = [5.0,6.0,7.0]

    swarm = Swarm()
    swarm.hatch_test(xs,ys,vxs,vys,len(xs),behaviour)

    assert_equal(swarm.boidVelocities()[0],vxs)
    assert_equal(swarm.boidVelocities()[1],vys)
