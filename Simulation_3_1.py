import pandas as pd
import numpy as np
import random
import itertools
import simpy


random.seed(1)

class Prime_Mover(object):
    
    id_iter = itertools.count()

    def __init__(self,env,JCT,CICT,SAGT,current_terminal="park",next_terminal="park",start_terminal="park",end_terminal="park"):

        self.env = env
        self.id = next(Prime_Mover.id_iter)

        self.current_terminal = current_terminal
        self.next_terminal = next_terminal
        self.start_terminal = start_terminal
        self.end_terminal = end_terminal

    def run(env,JCT,CICT,SAGT):
        while True:
            env.process(JCT_Operation(env,JCT))
            env.process(CICT_Operation(env,CICT))
            env.process(SAGT_Operation(env,SAGT))







def main(env):

    pm_list = []
    terminal = ["JCT","CICT","SAGT"]

    print(len(pm_list))

    # while True:

    if len(pm_list) == 0:
        for pm in range(25):
            pm = Prime_Mover(env)
            pm_list.append(pm)
            yield env.timeout(random.randint(0,10))
            print(len(pm_list))
            print("Prime Mover ID = ",pm.id)
            print("Time now : ",env.now)

    for pmop in len(pm_list):
        pm_list[pmop].run()

def JCT_Operation(env,JCT):
    with JCT.request() as request:
        yield request
        env.timeout(3)
        print("JCT Operation")

def CICT_Operation(env,CICT):
    with CICT.request() as request:
        yield request
        env.timeout(4)
        print("CICT Operation")

def SAGT_Operation(env,SAGT):
    with SAGT.request() as request:
        yield request
        env.timeout(5)
        print("SAGT Operation")


# env = simpy.RealtimeEnvironment(factor=1,strict=True)
env = simpy.Environment()

JCT  = simpy.Resource(env,capacity=1)
CICT = simpy.Resource(env,capacity=1)
SAGT = simpy.Resource(env,capacity=1)

# PARKING = simpy.Container(env,capacity=100,init=0)

env.process(main(env))
env.run(until=1440)