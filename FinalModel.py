

# When running in Spyder set graphics prefrences to inline.
'''
This model is agent based model(ABM) run from GUI (graphical user interface)
when you run the model it is expected that window will be appeared in your screen has only one menu bar.
the menu bar has model option on the top left of the screen and it has the "Run model" option. 
'''
#This Code is created by Omran ALRawahi, Student No. 201285265, Dec/2018

"""
This model is creating an agents in an environment,
The agents move, eat and share the resources in the environment and sharing the resources with each other under conditions.
"""


"""
Import operator
import operator which will be used in the model and it is better to import them all on the top of the model
"""
import random
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import requests
import bs4



"""
Step 1: Initiate parameters

parameters can be changed to examin the hanges in the model 
all parameters normaly located on the top of the module to simplify changing any of them.
"""
print ("Step 1: Initiate parameters")
num_of_agents = 20
num_of_iterations = 10
neighbourhood = 20
agents = []
environment = []



"""
Step 2: Get data from the web
"""
print ("Step 2: Get data from the web")
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

"""
print to test
#print(td_ys)
#print(td_xs)
""" 


"""
Step 3: Read the csv file and create a 2D List

csv file stored in the model repository contains integers will be used as an environment
The file will be used to inetiate the spatial environment where the agents will act
"""
print ("Step 3: Read the csv file and create a 2D List")
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

"""
Step 4: Append the csv value to the environment to inetiate the spatial environment where the agents will act
"""
print ("Step 4: Append the csv value to the environment to inetiate the spatial environment where the agents will act")
for row in reader:	# A list of rows
    rowlist = []
    environment.append(rowlist)
    for value in row:	# A list of value
        #print(value) # Floats
        rowlist.append(value)
        
"""
Step 5: Initiatethe agents.

defining the agent based on predefined x and y list from the web from step 2
As the web file has 100 row the number of the agents cant be more than 100 
agents location can be random using random operator  
"""
print ("Step 5: Initiatethe agents.")
for i in range(num_of_agents):
    y = int(td_ys[i].text)# defining y (this can be picked randomly using random operator)
    x = int(td_xs[i].text)# defining x (this can be picked randomly using random operator)
    agents.append(agentframework.Agent(environment, agents, x, y))

    
carry_on = True

"""	    
 Step 6: Update the frame and make the agents animate.
""" 
print (" Step 6: Update the frame and make the agents animate.")
def update(frame_number):
    fig.clear()
    """
    Clear the figure
    """
    global carry_on
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
  
    '''to stop the agents based on condition''' 
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")

 
    ''' Move the agents and make them interact with the environment and with each other'''

    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
#matplotlib.pyplot.show()
#for agent in agents: 
    #print(agent.x,agent.y)
"""
function make the agent keep animating till it reach 100 move or met the stoping condition 
"""

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on == True) :
        yield a			# Returns control and waits next call.
        a = a + 1



#print(a.y, a.x)
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5        
#print(a.y, a.x)

# to calculate the distance between agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
#print (distance) to test teh distence calculation

"""
Step 7: Display the plot
"""
print ("Step 7: Display the plot")
def run():        
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
    canvas.show()

"""
Step 8: Initiat GUI and its properties
"""
print ("Step 8: Initiat GUI and its properties")
root = tkinter.Tk() 
root.wm_title("Model!!")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()