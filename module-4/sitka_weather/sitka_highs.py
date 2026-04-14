import csv

#|Importing Libraries...
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


from datetime import datetime

#|Importing Widhets... 
from matplotlib.widgets import Button


filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

   

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        #| Getting the low temperatures for the graph.
        low = int(row[6])
        lows.append(low)



# Plot the high temperatures.
#plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

#|l This is a variable used to make 2DLines. Which is very important in updating the graph information. 
#|Reference : https://matplotlib.org/stable/gallery/widgets/buttons.html
#|I have a loose grasp on this variable. 
#|For this program, I used the comma as placeholder to be able to use methods like related to 2DLines.
#|The two indexs are empty to create placeholders for X,Y coordinates. 
#|lw=2 stands for line width and the number represents the thickness. 

l, = ax.plot([], [], lw=2)

#|Opens up instructions. I didn't like it being on the output or terminal, I'd rather it open up in a seperate window. I've seen this before in other programs I've used.
subprocess.run(["notepad.exe", "instruct.txt"])

#|For a long time, I struggled trying to use the Artist method and Index method together. 
#|The struggle was to stop the two graphs from overlapping, or to at least erase the other graph with clf or clr, or Artist.remove().
#|However, none of these methods worked, which evenutally led me to this post:https://stackoverflow.com/questions/4981815/how-to-remove-lines-in-a-matplotlib-plot.
#|Actuley there was another post that was much better than this one, but I did eventually rage quit and deleted, and redid the entire project, I had the link saved on the previous project.
#|I also had to reinstall Anaconda which restarted my PC which... Anyways, I know the stack overflow post is out there somewhere. 


#|
def plot1():
    return dates, highs, "Daily High Temperatures", "red"

def plot2():
    return dates, lows, "Daily Low Temperatures", "blue"

funcs = [plot1, plot2]

#|I redid this so many times. At first, Next and Prev used to be High and Low.
#|However they were also how the buttons incremented. Very messy. I had the increment, and plot being drawn in the same functions. 
#|At some point I realized that I had to just make a new function that would take care of the updating seperatly. 
#|This also meant reorganizing a lot of data.
#|^^^ So now High and Low became Plot1 and Plot2 that passed information to index update.
#|And the Index increment had it's own seperate function, and would update every time the button was pressed.

#|Now, in the update function, it was acutley possible to clear the previous graphs. 

class Index:
    ind = 0
    def next(self, event):
        self.ind += 1
        self.update()

    def prev(self, event):
        self.ind -= 1
        self.update()

    def update(self):
        ax.clear()
        
        #|Limits the length of the index
        i = self.ind % len(funcs)

        #|The information from the plots passed to Update which be redrawn. 
        x, y, name, color = funcs[i]()
        
        ax.plot(x, y, lw=2, color=color)
        ax.set_title(name, fontsize=24)
        ax.set_ylabel("Temperature", fontsize=16)
        
        # There was some issues getting the dates to settle down and not rotate or become crazy numbers. 
        if isinstance(x[0], datetime):
            fig.autofmt_xdate()
        plt.draw()

# Formatting

fig.autofmt_xdate()
plt.ylabel("Value", fontsize=16)

callback = Index()
callback.update() # Run once to show the first plot immediately

#|Buttons are buttons. 
#|I believe I just followed an example from the Matplotlib documentation for this.
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Prev')
bprev.on_clicked(callback.prev)

plt.show()

def main():
    return 0 
  

if __name__=="__main__" : 
    main()
    print("System Exit")
    sys.exit(main())
