# Import packages.
import random
import operator
import matplotlib
import agentframework
import csv
import matplotlib.animation 
import matplotlib.pyplot
import tkinter  
import requests  # For scrape web data.
import bs4       # Import Beautiful Soup to scrap data online.
import data

matplotlib.use('TkAgg') # Backend.

# Scrape web data and use it to initialise the model.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

    
num_of_agents = 10      # Make a num_of_agents variable and assign it to 10.
num_of_iterations = 100 # Make a num_of_iterations variable and assign it to 100.
neighbourhood = 20      # Make a neighbourhood variable and assign it to 20.
agents = []             # Creat agents list.
environment = []        # Creat environment list.

# Make animation properties.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# To load in.txt file.
with open("in.txt") as f:
    data = f.read().splitlines() 
# The downloaded text format is not standard, so needs to change.
    for row in data:
        rowlist = []   # Creat rowlist list.
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


#  Make the agents by putting into a for-loop.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, y, x, agents, neighbourhood))
    
    #matplotlib.pyplot.show(environment) 

# Start condition.
carry_on = True

# Define function to update data points.
def update(frame_number):   # Sets the number of animation frames.
    fig.clear()   # Clear a figure.
    global carry_on # carry_on is a global variable.
    
    # Move the agents by putting into nest for-loops.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
             
    # Displays the random points obtained with the for-loop.
    for i in range(num_of_agents):
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.ylim(0, 100)
        matplotlib.pyplot.imshow(environment)  
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)   # Make scatter plot.
   
#matplotlib.pyplot.title(label = "Scatter Plot Animation")

# Define a generator function.
def gen_function(b = [0]):
    a = 0
    global carry_on # Display clearly, even if it is not assigned.
    while (a < num_of_agents) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
 
"""
# Use for-each loop iterator to put out agents.        
for self in agents:
        for agent in agents:
            agentframework.Agent.distance_between(self, agent) # Calling the method from agentframework.py.
"""    
        
# Run the animation.
def run():
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False) #stopping condition.
    #ani.save("AAA")
    canvas.draw()       
  

# Creat main application window.
root = tkinter.Tk()

# Set the properties of the window.
root.wm_title("My Model") # Set window title.
#root.geometry("800x800")
#root.resizeable(width= True, height=True)
#label = tkinter.Label(root, text ="ABC")

# Creat a matplotlib canvas embedded within the window.
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tkinter.TOP, fill = tkinter.BOTH, expand=1)
#canvas.get_tk_widget().grid(column=0, row=1)

# Build a menu on the window.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label = "Model", menu = model_menu)
model_menu.add_command(label = "Run model", command = run)


#root.mainloop()
tkinter.mainloop() # Inter loop.
