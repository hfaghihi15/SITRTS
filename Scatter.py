from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel("SitRTS-Results.xlsx")
Data = []

check = 0
for i in data:
    count = 0
    for j in data[i]:
        if not check:
            Data.append([j])
        else:
            if j == 'Decision Tree' or j == "Opening":
                j = 1
            elif j == "SitRS" or j == "SITRS" or j == "Closing":
                j = 2
            elif j == "SitRTS" or j == "SITRTS" or j == "Educating":
                j = 3
            elif j == "Working":
                j = 4
            Data[count].append(j)
        count += 1
    check = 1

Separated_data = [[],[],[],[]]
XAsis = ['1','2','3','4','5','6']
for item in Data:
    Separated_data[item[3]-1].append(item)



new_data = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]


for key,i in enumerate(Separated_data):
    for j in i:
        new_data[key][j[2]-1].append(j[1])


plt.title('Working Situation')
plt.xlabel('Round')
plt.ylabel('accuracy')

df = pd.DataFrame({'x': XAsis, 'y1': new_data[3][0], 'y2': new_data[3][1], 'y3': new_data[3][2] })
plt.plot('x', 'y3', data=df,  marker='o', markerfacecolor='skyblue', markersize=12, color='blue', linewidth=4, label="SitRTS")
plt.plot('x', 'y2', data=df, marker='*', color='red', linewidth=2, label="SitRS",markersize=9)
plt.plot('x', 'y1', data=df,marker='', color='green', linewidth=2, linestyle='dashed', label="Decision Tree")
plt.yticks(np.arange(56, 104, 2))
plt.legend()
plt.show()



# Data = [
#     [1,1,1,81],
#     [1,1,2,100],
#     [1,2, 1, 26],
#     [1,2,2,80],
#     [2,1,1,89],
#     [2,1,2,89.75],
#     [2,2,1, 72],
#     [2,2,2,85],
# ]
#
markers = [".", "o", "*", "<"]
colors = ['r','g','b']



#make a sample dataset

# plt.yticks(np.arange(56, 100, 0.5))
#
# for i in Data: #for each of the 7 features
#     try:
#         mi = markers[i[3]-1]  # marker for ith feature
#     except:
#         print(i[3])
#         exit(0)
#     xi =  [i[0]]#x array for ith feature .. here is where you would generalize      different x for every feature
#     yi =  [i[1]]#y array for ith feature
#     try:
#         ci = colors[i[2]-1] #color for ith feature
#     except:
#         print(i[2])
#         exit(0)
#     plt.scatter(xi,yi,marker=mi, color=ci)
# plt.show()