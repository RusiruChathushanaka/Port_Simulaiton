import pandas as pd
import numpy as np
import random
import simpy
import data_loading as dl


# Loading datasets

JCT_CICT = dl.df_JCT_CICT
JCT_SAGT = dl.df_JCT_SAGT

CICT_JCT = dl.df_CICT_JCT
CICT_SAGT = dl.df_CICT_SAGT

SAGT_JCT = dl.df_SAGT_JCT
SAGT_CICT = dl.df_SAGT_CICT


# Creating empty pandas dataframes
to_JCT = pd.DataFrame(columns=JCT_CICT.columns)
to_JCT["Load Terminal"]=[]
to_JCT["Arrival time"]=[]
to_JCT["Prime Mover"]=[]

to_CICT = pd.DataFrame(columns=JCT_CICT.columns)
to_CICT["Load Terminal"]=[]
to_CICT["Arrival time"]=[]
to_CICT["Prime Mover"]=[]

to_SAGT = pd.DataFrame(columns=JCT_CICT.columns)
to_SAGT["Load Terminal"]=[]
to_SAGT["Arrival time"]=[]
to_SAGT["Prime Mover"]=[]


def main():

    pm_list = []
    terminal = ["JCT","CICT","SAGT"]
    prime_mover = []
    speed = []
    start_terminal = []
    end_terminal = []

    for pm in range(50):
        pm = Prime_Mover(np.random.randint(1000),np.random.randint(100000),np.random.randint(50))
        pm_list.append(pm)
    
    print(pm_list)
    print("No of prime movers",len(pm_list))


    env = simpy.Environment()

    JCT = simpy.Resource(env,capacity=1)
    CICT = simpy.Resource(env,capacity=1)
    SAGT = simpy.Resource(env,capacity=1)

    env.process(ITT_Run(env,pm_list,prime_mover,speed,start_terminal,end_terminal,terminal,JCT,CICT,SAGT))
    env.run(until=1440)


    for i in range(len(pm_list)):
        print("Prime Mover",i)
        print(pm_list[i].prime_mover_ID)
        print(pm_list[i].container_ID)
        print(pm_list[i].speed)




class Prime_Mover:
    def __init__(self,prime_mover_ID=99999,container_ID=999999,speed=999):
        self.prime_mover_ID = prime_mover_ID
        self.container_ID = container_ID
        self.speed = speed

        self.data = pd.DataFrame(columns=JCT_CICT.columns)
        self.data["Load Terminal"]=[]
        self.data["Arrival time"]=[]

        