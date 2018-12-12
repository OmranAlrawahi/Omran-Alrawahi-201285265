
'''
Agent framework has the basic agent class. Agents move in 2d raster environment.
The Agents move and eat from the resources and share the resurses with orther agents
based on defined condetion witin the agent class.
'''
#This Code is created by Omran ALRawahi, Student No. 201285265, Dec/2018



#Import the random operator whhic will be used to initiat the agents
import random 

#initiate agent class
class Agent ():
    ''' Intiate the agent'''
        #Selecting x and y either from random or predefind list from the web 
    def __init__ (self,environment,agents,x,y):
       self.x = x #random.randint(0,99) it can be used if we need to make the x picked randomly
       self.y = y #random.randint(0,99) it can be used if we need to make the y picked randomly
       self.environment = environment
       self.agents = agents
       self.store = 0
       
    '''
    Postional arguments:
     environment -- Environment in raster format shared by the agents and the agents do their activities. 
     agents -- All agents which live in the environment
     x -- The agent location coordinate in the x axis 
     y -- The agent location coordinate in the y axis 
    '''

    def move(self):
        '''
        Move the agent based on the x and y coordinates conditions. 
        '''
        if random.random() < 0.5:
            self.y = ( self.y + 1) % 100
        else:
            self.y = ( self.y - 1) % 100 

        if random.random() < 0.5:
            self.x = ( self.x + 1) % 100 
        else:
            self.x = ( self.x - 1) % 100

          
    def eat(self): 
        '''
        Agent eats from the environment 10 if the the environnment is more than 10. 
        '''
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10


    def share_with_neighbours(self, neighbourhood):
        '''
        Agent shares their store with the neibours based on distance defined in the
    
        PosPostional arguments: 
            neighbourhood -- the distance which make the agent share some of the store
        '''
        for agent in self.agents:
            distance = self.distance_between(agent) 
            if distance <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(distance) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    '''
    calculate the distance between agents 
    Return the distnce based on self and agents coordinates in the enviromnment
    '''

                