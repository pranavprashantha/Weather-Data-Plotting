# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:52:34 2023

@author: raopr
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name: Pranav Rao
# Section: 564
# Assignment: 12.14 Lab
# Date: 11/15/2023
#
#
# YOUR CODE HERE
#

#imports
import numpy as np
import matplotlib.pyplot as plt

file = open("WeatherDataCLL.csv",'r')
lines = file.readlines()
row_array = []
for line in lines:
    row_array.append(line)
del row_array[0]

new_arr = []

for i in row_array:
    new_arr.append(i.split(','))

file.close()

maxs = np.array([])
wind = np.array([])
precip = np.array([])
humid = np.array([])
temp_avg = np.array([])

for i in new_arr:
    
    if i[-2] != "":
        maxs = np.append(maxs,float(i[-2]))
    else:
        maxs = np.append(maxs,np.nan)
    if i[1] != "":
        wind = np.append(wind, float(i[1]))
    else:
        wind = np.append(wind,np.nan)
    if i[2] != "":
        precip = np.append(precip, float(i[2]))
    else:
        precip = np.append(precip, np.nan)
    if i[3] != "":
        humid = np.append(humid, float(i[3]))
    else:
        humid = np.append(humid, np.nan)
    if i[4] != "":
        temp_avg = np.append(temp_avg, float(i[4]))
    else:
        temp_avg = np.append(temp_avg, np.nan)
    
fig, axs = plt.subplots(2,2)
fig.tight_layout()

axs[0,0].plot(maxs,'r',label="Max temperature")
axs[0,0].set_title("Maximum Temperature and Average Wind Speed")
axs[0,0].set_ylabel("Maximum temperature, F")
axs[0,0].set_xlabel('Date')
ax2 = axs[0,0].twinx()
ax2.plot(wind,color="Blue",label="Average Wind Speed, mph")
ax2.set_ylabel("Average Wind Speed, mph")

axs[0,1].hist(wind, 40, color="cyan", edgecolor = 'black')
axs[0,1].title.set_text("Histogram of Average Wind Speed")
axs[0,1].set_ylabel("Number of Days")
axs[0,1].set_xlabel("Average Wind Speed (mph)")


axs[1,0].scatter(humid,precip,color="Black")
axs[1,0].title.set_text("Precipitation vs Average Relative Humidity")
axs[1,0].set_ylabel("Precipitation (in)")
axs[1,0].set_xlabel("Average Relative Humitidy (%)")

month = np.zeros(12)
month_num = np.zeros(12)
month_max = np.zeros(12)
month_min = np.full(12, 120)


for i in new_arr:
    temp = i[0].split("/")
    n = int(temp[0])-1
    if i[4] != "":
        month[n] += int(i[4])
        month_num[n] += 1
        
    if i[-2] != "" and i[-2] != "\n":
        if int(i[-2]) > month_max[n]:
            month_max[n] = int(i[-2])
    
    if i[-1] != '' and i[-1] != "\n":
        if int(i[-1]) < month_min[n]:
            month_min[n] = int(i[-1])
        
for i in range(12):
    month[i] = int(month[i] / month_num[i])
    
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
axs[1,1].bar(nums, month, color = 'orange')
axs[1,1].plot(nums,month_max, color = 'green')
axs[1,1].plot(nums,month_min, color = 'red')
axs[1,1].title.set_text("Temperature by Month")
axs[1,1].set_ylabel("Average Temperature, F")
axs[1,1].set_xlabel("Month")
axs[1,1].set_xticks(nums)

plt.show()
