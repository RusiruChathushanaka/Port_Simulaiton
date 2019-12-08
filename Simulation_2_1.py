import pandas as pd
import numpy as np
import random
import itertools
import simpy
import data_loading as dl


# Loading datasets

JCT_CICT = dl.df_JCT_CICT
JCT_SAGT = dl.df_JCT_SAGT

CICT_JCT = dl.df_CICT_JCT
CICT_SAGT = dl.df_CICT_SAGT

SAGT_JCT = dl.df_SAGT_JCT
SAGT_CICT = dl.df_SAGT_CICT

JCT_to_Other = dl.df_JCT_to_Other
CICT_to_Other = dl.df_CICT_to_Other
SAGT_to_Other = dl.df_SAGT_to_Other


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




class Prime_Mover(object):
    
    id_iter = itertools.count()

    current_terminal="park"
    next_terminal="park"
    start_terminal="park"
    end_terminal="park"

    global to_CICT
    global to_JCT
    global to_SAGT


    def __init__(self,env,current_terminal="park",next_terminal="park",start_terminal="park",end_terminal="park"):

        self.env = env
        self.id = next(Prime_Mover.id_iter)

        self.vehicle_load_details = pd.DataFrame(columns=JCT_to_Other.columns)
        self.vehicle_load_details["Load Terminal"] = []
        self.vehicle_load_details["Departure time"] = []
        self.vehicle_load_details["Arrival time"] = []

        self.current_terminal = current_terminal
        self.next_terminal = next_terminal
        self.start_terminal = start_terminal
        self.end_terminal = end_terminal

        self.action = env.process(self.run(env))

        

        # yield PARKING.put(1)


    def run(self,env):

        while True:
            #print("************************",JCT_to_Other.at[0,"Destination Terminal"])
            yield env.timeout(np.random.randint(5,10))
            print(self.id)
            print("hjvjvj")
            print(PARKING._level)
            print(self.current_terminal)

            if self.current_terminal == "park":
                terminals = ["JCT","CICT","SAGT"]
                randint = random.randint(0,2)
                if randint==0:
                    self.next_terminal = "JCT"
                elif randint==1:
                    self.next_terminal = "CICT"
                elif randint==2:
                    self.next_terminal = "SAGT"
                else:
                    print("No Next Terminal from Park...")
                self.env.timeout(np.random.randint(2,10))
                self.current_terminal = self.next_terminal
                print("ooooooooooooooooooooooooooooooooooo")

            else:
                print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")

                print("Current Terminal - ",self.current_terminal)
                print("Next Terminal - ",self.next_terminal)
                print("Start Terminal - ",self.start_terminal)
                print("End Terminal - ",self.end_terminal)

                env.process(self.terminal_loading(env))
                # self.terminal_loading(env)

                print("Current Terminal - ",self.current_terminal)
                print("Next Terminal - ",self.next_terminal)
                print("Start Terminal - ",self.start_terminal)
                print("End Terminal - ",self.end_terminal)

                env.process(self.moving(env))
                # self.moving(env)

                env.process(self.terminal_unloading(env))
                # self.terminal_unloading(env)

                print(env.now)


    def moving(self,env):

        if (self.current_terminal == "JCT") & (self.next_terminal == "CICT"):
            yield env.timeout(5)
            self.current_terminal = self.next_terminal

        elif (self.current_terminal == "JCT") & (self.next_terminal == "SAGT"):
            yield env.timeout(6)
            self.current_terminal = self.next_terminal

        elif (self.current_terminal == "CICT") & (self.next_terminal == "JCT"):
            yield env.timeout(7)
            self.current_terminal = self.next_terminal

        elif (self.current_terminal == "CICT") & (self.next_terminal == "SAGT"):
            yield env.timeout(8)
            self.current_terminal = self.next_terminal

        elif (self.current_terminal == "SAGT") & (self.next_terminal == "JCT"):
            yield env.timeout(9)
            self.current_terminal = self.next_terminal

        elif (self.current_terminal == "SAGT") & (self.next_terminal == "CICT"):
            yield env.timeout(10)
            self.current_terminal = self.next_terminal

        else:
            print("Error in moving")

        

 
    def terminal_unloading(self,env):

        global to_CICT
        global to_JCT
        global to_SAGT

        print("...........Unloading.............")

        if self.current_terminal == "JCT":
            with JCT.request() as request:
                yield request
                to_JCT = to_JCT.append(self.vehicle_load_details.iloc[-1])
                to_JCT.iloc[-1]["Arrival time"] = self.env.now
                yield env.timeout(10)

        elif self.current_terminal == "CICT":
            with CICT.request() as request:
                yield request
                to_CICT = to_CICT.append(self.vehicle_load_details.iloc[-1])
                to_CICT.iloc[-1]["Arrival time"] = self.env.now
                yield env.timeout(10)

        elif self.current_terminal == "SAGT":
            with SAGT.request() as request:
                yield request
                to_SAGT = to_SAGT.append(self.vehicle_load_details.iloc[-1])
                to_SAGT.iloc[-1]["Arrival time"] = self.env.now
                yield env.timeout(10)

        else:
            print("Error in terminal Unloading")





    def terminal_loading(self,env):

        global JCT_to_Other
        global CICT_to_Other
        global SAGT_to_Other

        print("...........Loading.............")

        if self.current_terminal == "JCT":
            #print(JCT_to_Other)
            if len(JCT_to_Other.index)>0:
                self.start_terminal = "JCT"
                self.end_terminal = JCT_to_Other.iloc[0]["Destination Terminal"]
                self.next_terminal = self.end_terminal
                self.vehicle_load_details = self.vehicle_load_details.append(JCT_to_Other.iloc[0])
                self.vehicle_load_details.iloc[-1]["Load Terminal"] = "JCT"
                JCT_to_Other = JCT_to_Other.iloc[1:]
                yield env.timeout(10)
                self.vehicle_load_details.iloc[-1]["Departure time"] = self.env.now
            else:
                pass

        elif self.current_terminal == "CICT":
            #print(CICT_to_Other)
            if len(CICT_to_Other.index)>0:
                self.start_terminal = "CICT"
                self.end_terminal = CICT_to_Other.iloc[0]["Destination Terminal"]
                self.next_terminal = self.end_terminal
                self.vehicle_load_details = self.vehicle_load_details.append(CICT_to_Other.iloc[0])
                self.vehicle_load_details.iloc[-1]["Load Terminal"] = "CICT"
                CICT_to_Other = CICT_to_Other.iloc[1:]
                yield env.timeout(10)
                self.vehicle_load_details.iloc[-1]["Departure time"] = self.env.now
            else:
                pass

        elif self.current_terminal == "SAGT":
            #print(SAGT_to_Other)
            if len(SAGT_to_Other.index)>0:
                self.start_terminal = "SAGT"
                self.end_terminal = SAGT_to_Other.iloc[0]["Destination Terminal"]
                self.next_terminal = self.end_terminal
                self.vehicle_load_details = self.vehicle_load_details.append(SAGT_to_Other.iloc[0])
                self.vehicle_load_details.iloc[-1]["Load Terminal"] = "JCT"
                SAGT_to_Other = SAGT_to_Other.iloc[1:]
                yield env.timeout(10)
                self.vehicle_load_details.iloc[-1]["Departure time"] = self.env.now
            else:
                pass

        else:
            print("Error in terminal loading")



def main(env):

    pm_list = []
    terminal = ["JCT","CICT","SAGT"]


    # pm = Prime_Mover(env)


    # for i in range(50):
    #     env.process(pm.run(env))

    print(len(pm_list))

    # while True:

    if len(pm_list) == 0:
        for pm in range(25):
            pm = Prime_Mover(env)
            pm_list.append(pm)
            yield PARKING.put(1)
            print(len(pm_list))
            print("Prime Mover ID = ",pm.id)

    for i in range(len(pm_list)):
        print("Prime Mover ID = ",pm_list[i].id)

    # yield 0


# env = simpy.RealtimeEnvironment(factor=1,strict=True)
env = simpy.Environment()

JCT = simpy.Resource(env,capacity=1)
CICT = simpy.Resource(env,capacity=1)
SAGT = simpy.Resource(env,capacity=1)

PARKING = simpy.Container(env,capacity=100,init=0)

env.process(main(env))
env.run(until=1440)

to_CICT.fillna(0)
to_JCT.fillna(0)
to_SAGT.fillna(0)

print(to_JCT)
print(to_CICT)
print(to_SAGT)

with pd.ExcelWriter('output.xlsx') as writer:  # doctest: +SKIP
    to_JCT.to_excel(writer, sheet_name='to_JCT')
    to_CICT.to_excel(writer, sheet_name='to_CICT')
    to_SAGT.to_excel(writer, sheet_name='to_SAGT')

print("Done")