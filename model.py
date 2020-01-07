#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 02:12:23 2020

@author: toriliang
"""

import random
import operator
import matplotlib
import agentframework
import csv
import matplotlib.animation 
import matplotlib.pyplot
import tkinter
import requests
import bs4
import data

matplotlib.use('TkAgg')

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
environment = []


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#xlim = 10
#ylim = 10
#frames, = ax.plot(x, y)


with open("in.txt") as f:
    data = f.read().splitlines() 

    for row in data:
        rowlist = []
        for value in row.split(','):
            if value[-1] == '\\':
                value1 = value[0:(len(value)-1)]
                rowlist.append(int(value1))
            else:
                rowlist.append(int(value))
        environment.append(rowlist)

for line in agents:
    f.write(line)
#f.close()



# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(y, x, environment, agents, neighbourhood))
    
    #matplotlib.pyplot.show(environment) 

carry_on = True

def update(frame_number):
    fig.clear()   
    global carry_on
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move("frame_number")
            agents[i].eat()
            agents[i].share_with_neighbours()
             
    # Set stopping Animation condition.
    #if random.random() < 0.1:
        #carry_on = False
        #print("stopping condition")
    for i in range(num_of_agents):
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.ylim(0, 100)
        matplotlib.pyplot.imshow(environment)  
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)   
   
#matplotlib.pyplot.title(label = "Scatter Plot Animation")
    
def gen_function(b = [0]):
    a = 0
    global carry_on # Display clearly, even if it is not assigned.
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
       
for self in agents:
        for agent in agents:
            agentframework.Agent.distance_between(self, agent) 
    
        
  # Run the animation.
def run():
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #ani.save("AAA")
    print(ani)        
  

#creat main application window
root = tkinter.Tk()
#set the properties window

root.title("My Model")
#root.geometry("800x800")
#root.resizeable(width= True, height=True)
#label = tkinter.Label(root, text ="ABC")


canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#canvas.get_tk_widget().grid(column=0, row=1)


menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label = "Model", menu = model_menu)
model_menu.add_command(label="Run model", command = run)

  

#root.mainloop()

tkinter.mainloop()