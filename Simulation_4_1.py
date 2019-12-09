import simpy
import random
import itertools
# import data_loading as dl

class Car(object):
    id_iter = itertools.count()
    def __init__(self, env):
        self.env = env
        # Start the run process everytime an instance is created.
        self.id = next(Car.id_iter)
        self.action = env.process(self.run_car())

    def run_car(self):
        while True:
            print(self.id)
            print(' Car %d Start parking and charging at %d' % (self.id,self.env.now))
            # charge_duration = random.randint(1,4)
            # We yield the process that process() returns
            # to wait for it to finish
            # yield self.env.process(self.charge(charge_duration))

            num = random.randint(0,2)

            if  num==0:
                yield self.env.process(self.JCT_Operation(env,JCT))
            elif num==1:
                yield self.env.process(self.CICT_Operation(env,CICT))
            else:
                yield self.env.process(self.SAGT_Operation(env,SAGT))

            # The charge process has finished and
            # we can start driving again.
            # print('Car %d Start driving at %d' % (self.id,self.env.now))
            trip_duration = random.randint(1,8)
            # yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

    def JCT_Operation(self,env,JCT):
        with JCT.request() as requestJ:
            yield requestJ
            yield env.timeout(random.randint(200,300))
            print("JCT Operation")
            print('Car %d JCT Operation at %d' % (self.id,self.env.now))

    def CICT_Operation(self,env,CICT):
        with CICT.request() as requestC:
            yield requestC
            yield env.timeout(random.randint(1,5))
            print("CICT Operation")
            print('Car %d CICT Operation at %d' % (self.id,self.env.now))

    def SAGT_Operation(self,env,CICT):
        with SAGT.request() as requestS:
            yield requestS
            yield env.timeout(random.randint(1,5))
            print("SAGT Operation")
            print('Car %d SAGT Operation at %d' % (self.id,self.env.now))


# def JCT_Operation(env,JCT):
#     with JCT.request() as request:
#         yield request
#         yield env.timeout(3)
#         print("JCT Operation")
#         print('Car %d Start driving at %d' % (self.id,self.env.now))

# def CICT_Operation(env,CICT):
#     with CICT.request() as request:
#         yield request
#         yield env.timeout(4)
#         print("CICT Operation")

# def SAGT_Operation(env,SAGT):
#     with SAGT.request() as request:
#         yield request
#         yield env.timeout(5)
#         print("SAGT Operation")

env = simpy.Environment()
# env = simpy.RealtimeEnvironment(factor=.5)

JCT  = simpy.Resource(env,capacity=1)
CICT = simpy.Resource(env,capacity=1)
SAGT = simpy.Resource(env,capacity=1)

car0 = Car(env)
car1 = Car(env)
car2 = Car(env)
car3 = Car(env)
car4 = Car(env)
car5 = Car(env)
car6 = Car(env)
car7 = Car(env)
car8 = Car(env)
car9 = Car(env)
car10 = Car(env)
car11 = Car(env)
car12 = Car(env)
car13 = Car(env)
car14 = Car(env)
car15 = Car(env)
car16 = Car(env)
car17 = Car(env)
car18 = Car(env)
car19 = Car(env)
car20 = Car(env)

env.run(until=1500)