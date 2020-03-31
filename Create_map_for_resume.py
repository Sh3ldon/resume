#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:08:56 2019

@author: sheldon
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pdb
import datetime
from matplotlib.patches import Circle

cities=pd.read_csv('Cities.csv')
jobs=pd.read_csv('Jobs.csv')

fig = plt.figure()
ax=plt.gca()
ax.axis('off') #Do not display outer frame

m = Basemap(projection='cyl',lat_0=0, lon_0=10, llcrnrlon=-140.,llcrnrlat=-50.,urcrnrlon=160.,urcrnrlat=70.)
m.drawcoastlines(linewidth=0.5, color='lightgreen')
m.fillcontinents(color='lightgreen')

for row in cities.iterrows():
     if row[1].Current==False:
          bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="green", lw=2)
          m.scatter(row[1].Longitude,   row[1].Latitude, latlon=True, marker = 'o', color='green', facecolors='green', s=200, zorder=10)
          x, y = m(row[1].Longitude+row[1].Longitude_Offset,   row[1].Latitude+row[1].Latitude_Offset)
          plt.annotate(str(row[1].Interval)+': '+str(row[1].City)+'\n'+str(row[1].Text), xy=(x, y),  xycoords='data', bbox=bbox_props, color='green', wrap=True)
     else:
          bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="blue", lw=2)
          x, y = m(row[1].Longitude+row[1].Longitude_Offset,   row[1].Latitude+row[1].Latitude_Offset)
          plt.annotate(str(row[1].Interval)+': '+str(row[1].City)+'\n'+row[1].Text, xy=(x, y),  xycoords='data', bbox=bbox_props, color='blue', wrap=True)
          
for row in jobs.iterrows():
     m.drawgreatcircle( 7.75, 48.5833, row[1].Longitude , row[1].Latitude, linewidth=2,color='b') 
     m.scatter(row[1].Longitude,   row[1].Latitude, latlon=True, marker = 'h', color='blue', facecolors='blue', s=200, zorder=21)
     xnum, ynum = m(row[1].Longitude-1.2,   row[1].Latitude-1.5)         
     plt.annotate(row[0]+1, xy=(xnum, ynum),  xycoords='data', color='lightgrey', zorder=22)
fig.set_size_inches(15, 7)

plt.savefig('./resume_map.png', dpi=500)