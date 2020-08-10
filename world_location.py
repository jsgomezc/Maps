#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:55:35 2020

@author: juancho
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(10,10))

#ax = fig.add_subplot(111)
ax0 = fig.add_subplot(111)
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection='ortho', lat_0=4, lon_0=-72,
              resolution='i', area_thresh=500.0)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='#9c9c9c', lake_color='#ADD8E6')
map.drawmapboundary(fill_color='#ADD8E6')
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

# Drawing the box
lons = [-81, -65, -65, -81, -81]
lats = [-6, -6, 14, 14, -6]

x, y = map(lons, lats)

map.plot(x, y, marker=None, color='r', linewidth=3)


plt.savefig('world_location.png', transparent=True)
