
# coding: utf-8

# ## Matplotlib Practice

# In[3]:


import matplotlib.pyplot as plt


# In[23]:


list(range(10))
print(*range(5))


# ## Draw a line

# In[13]:


x = list(range(0,50))
y = [ value*3 for value in x]

#Sete x & y values for drawing plot
plt.plot(x,y)
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set title
plt.title('Draw a line')
#Show plot
plt.show()


# ## 2 Sample graph

# In[26]:


x = [1,2,3]
y = [2,4,1]

#Sete x & y values for drawing plot
plt.plot(x,y)
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set title
plt.title('Sample graph!')
#Show plot
plt.show()


# ## Read x and y values from text file and draw sample graph

# In[58]:


f = open('text.txt', "w")
f.write('1 2 3')


# In[59]:


f.write('\n2 4 1')


# In[61]:


f = open('text.txt')


# In[62]:


data = f.read()


# In[63]:


data


# In[76]:


x,y = data.split('\n')
x,y = x.split(' '),y.split(' ')


# In[77]:


#Set x & y values for drawing plot
plt.plot(x,y)
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set title
plt.title('Sample graph!')
#Show plot
plt.show()


# ## Read data from csv and draw line charts

# In[85]:


# Create csv file and copy data to the file
# Read csv file using pandas
import pandas as pd


# In[90]:


df = pd.read_csv('test.csv',parse_dates=True,index_col=0)


# In[91]:


df


# In[92]:


df.plot()


# ## Draw two or more lines on same plot with suitable legends

# In[102]:


x1 = [10,20,30]
y1 = [20,40,10]
#Set x & y values for drawing plot
plt.plot(x1,y1,label='Line1')

x2 = [10,20,30]
y2 = [20,10,30]

#Set x2 and y2 values
plt.plot(x2,y2,label='Line2')
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set legend
plt.legend()
#Set title
plt.title('Two or more lines on same plot with suitable legends ')
#Show plot
plt.show()


# In[106]:


x1 = [10,20,30]
y1 = [20,40,10]
#Set x & y values for drawing plot
plt.plot(x1,y1,color='blue',linewidth=3,label='Line1')

x2 = [10,20,30]
y2 = [20,10,30]

#Set x2 and y2 values
plt.plot(x2,y2,color='green',linewidth=3,label='Line2')
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set legend
plt.legend()
#Set title
plt.title('Two or more lines on same plot with suitable legends ')
#Show plot
plt.show()


# In[108]:


x1 = [10,20,30]
y1 = [20,40,10]
#Set x & y values for drawing plot
plt.plot(x1,y1,color='blue',linewidth=3,linestyle = 'dotted',label='Line1-dotted')

x2 = [10,20,30]
y2 = [20,10,30]

#Set x2 and y2 values
plt.plot(x2,y2,color='red',linewidth=3,linestyle = 'dashed',label='Line2-dashed')
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set legend
plt.legend()
#Set title
plt.title('Two or more lines on same plot with suitable legends ')
#Show plot
plt.show()


# In[111]:


x1 = [10,20,30]
y1 = [20,40,10]
#Set x & y values for drawing plot
plt.plot(x1,y1,color='blue',linewidth=3,linestyle = 'dashdot',marker='o',label='Line1-dashdot')

x2 = [10,20,30]
y2 = [20,10,30]

#Set x2 and y2 values
plt.plot(x2,y2,color='red',linewidth=3,linestyle = 'dashed',marker='o',label='Line2-dashed')
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set legend
plt.legend()
#Set title
plt.title('Two or more lines on same plot with suitable legends ')
#Show plot
plt.show()


# In[112]:


x1 = [10,20,30]
y1 = [20,40,10]
#Set x & y values for drawing plot
plt.plot(x1,y1,color='blue',linewidth=3,linestyle = 'dashdot',marker='o',markerfacecolor='red',label='Line1-dashdot')

x2 = [10,20,30]
y2 = [20,10,30]

#Set x2 and y2 values
plt.plot(x2,y2,color='red',linewidth=3,linestyle = 'dashed',marker='o',markerfacecolor='blue',label='Line2-dashed')
#Set x-axis label
plt.xlabel('x-axis')
#Set y-axis label
plt.ylabel('y-axis')
#Set legend
plt.legend()
#Set title
plt.title('Two or more lines on same plot with suitable legends ')
#Show plot
plt.show()


# In[113]:



# x axis values
x = [1,4,5,6,7]
# y axis values
y = [2,6,3,6,3]

# plotting the points 
plt.plot(x, y, color='red', linestyle='dashdot', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
#Set the y-limits of the current axes.
plt.ylim(1,8)
#Set the x-limits of the current axes.
plt.xlim(1,8)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('Display marker')
# function to show the plot
plt.show()


# In[116]:


X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
#print(plt.axis())
plt.axis([0,100,0,200])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


# In[122]:


import numpy as np
import pylab as pl
# Make an array of x values
x1 = [2, 3, 5, 6, 8]
# Make an array of y values for each x value
y1 = [1, 5, 10, 18, 20]
# Make an array of x values
x2 = [3, 4, 6, 7, 9]
# Make an array of y values for each x value
y2 = [2, 6, 11, 20, 22]
# set new axes limits
pl.axis([0, 10, 0, 30]) 
# use pylab to plot x and y as red circles
pl.plot(x1, y1,'g*', x2, y2, 'ro')
# show the plot on the screen
pl.show()


# In[123]:


import numpy as np
import pylab as pl

t = np.arange(0.,5.,0.2)
pl.plot(t,t,'g--',t,t*2,'bs',t,t*3,'r^')
pl.show()


# In[132]:


import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date,value) in data]
y = [value for (date,value) in data]

fig = plt.figure()

#Add subplot
graph = fig.add_subplot(111)

graph.plot(x,y,'r-o')


graph.set_xticks(x)

graph.set_xticklabels([date.strftime("%Y-%m-%d") for (date,value) in data])
       
plt.show()


# In[133]:


import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)

# Plot the data as a red line with round markers
graph.plot(x,y,'r-o')

# Set the xtick locations
graph.set_xticks(x)

# Set the xtick labels
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Closing Value')
 # giving a title  
plt.title('Closing stock value of Alphabet Inc.') 
# Customize the grid
plt.grid(linestyle='-', linewidth='0.5', color='blue')
plt.show()


# In[139]:


import matplotlib.pyplot as plt
fig = plt.figure()
fig.subplots_adjust(bottom=0.020, left=0.020, top = 0.900, right=0.800)

plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())

plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())

plt.show()

