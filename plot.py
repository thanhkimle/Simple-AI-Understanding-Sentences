# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

len_sentence = [7,7,7,7,19,19,19,19,19,7,5,7,8,5,5,4,6,9,9,5,5,6,6,6,7,7,6,3,7,7,7,7,8,5,9,10,9]
len_question = [4,7,4,5,7,6,7,8,10,5,5,5,7,7,9,3,4,7,4,4,5,5,5,5,6,7,4,4,7,5,5,6,7,4,4,3,5]
us = [199,203,169,275,435,447,389,399,426,169,157,174,220,181,222,115,160,301,193,187,163,208,166,200,183,223,144,117,261,294,259,211,289,225,188,192,187]


print(len(len_sentence))
print(len(len_question))
print(len(us))

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.3,
        alpha = 0.2)

# Creating plot
# ax.scatter3D(len_sentence, len_question, us, color = "green")
# Creating plot
# Creating color map
my_cmap = plt.get_cmap('hsv')

x = len_sentence
y = len_question
z = us
sctt = ax.scatter3D(x, y, z)
 

plt.title("Runtime vs Inputs", fontweight ='bold')
ax.set_xlabel('No. Words in Sentence', fontweight ='bold')
ax.set_ylabel('No. Words in Question', fontweight ='bold')
ax.set_zlabel('Runtime (us)', fontweight ='bold')
 
# fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)

# show plot
plt.show()