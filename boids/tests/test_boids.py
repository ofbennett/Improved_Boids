from boids.boid_classes import Boid, Swarm
from nose.tools import assert_almost_equal, assert_equal, assert_less, assert_greater
import os
import yaml

behaviour=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','standard_swarm.yml')))

middle_attraction = behaviour['middle_attraction']
avoidance_radius = behaviour['avoidance_radius']
copycat_radius = behaviour['copycat_radius']
copycat_influence = behaviour['copycat_influence']
boid_num = behaviour['boid_num']

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
