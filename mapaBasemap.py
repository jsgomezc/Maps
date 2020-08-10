#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:25:37 2020

@author: juancho
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#from obspy.geodetics import kilometers2degrees
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1 import make_axes_locatable



fig = plt.figure(figsize=(10,15))

#ax = fig.add_subplot(111)
ax0 = fig.add_subplot(111)

map = Basemap(llcrnrlon=-80, llcrnrlat=-5, urcrnrlon=-66, urcrnrlat=13, epsg=3116, resolution='h')
#http://server.arcgisonline.com/arcgis/rest/services

map.arcgisimage(service='World_Imagery', xpixels = 1500, verbose= True)

map.drawcountries(linewidth = 0.6, color='white')
map.drawcoastlines(linewidth = 0.6, color='white')
map.drawstates(linewidth = 0.3, color='white')
#map.drawrivers(color='blue')
map.drawparallels(range(-4, 15, 4), labels=[True,False,False,True],dashes=[2,2], fontsize=20)
map.drawmeridians(range(-87, -61, 4), labels=[True,False,False,True], dashes=[2,2], fontsize=20)

# USME
lon = -74.126777
lat = 4.480951

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='r', s=100)
#map.scatter(x, y, marker='o', color='r', s=135000, alpha=0.2, linewidth=3, edgecolor='r')
plt.text(x, y, 'USME',fontsize=15, fontweight='bold', color='white')
'''
dist = kilometers2degrees(500)

lons = [-74.126777, -74.126777]
lats = [4.480951, 4.480951+dist]

x, y = map(lons, lats)

map.plot(x, y, marker=None,color='r')

lon = -74.6
lat = 6.3

x, y = map(lon, lat)

plt.text(x, y, '$500km$',fontsize=17, fontweight='bold', color='white', rotation=90)
'''

# TUNJ
lon = -73.357760
lat = 5.533368

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='r', s=100)
plt.text(x, y, 'TUNJ',fontsize=15, fontweight='bold', color='white')


'''
# VCIO
lon = -73.592480
lat = 4.111264

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='r', s=100)
#plt.text(x, y, 'VCIO',fontsize=7, fontweight='bold', color='white')

# ZIPA
lon = -74.0693056
lat = 5.07930556

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='y', s=100)
#plt.text(x, y, 'ZIPA',fontsize=7, fontweight='bold', color='white')

# CUSI
lon = -72.6811086
lat = 5.01782219

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='y', s=100)
#plt.text(x, y, 'CUSI',fontsize=7, fontweight='bold', color='white')

# SJRS
lon = -74.5832194
lat = 4.86000107

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='y', s=100)
#plt.text(x, y, 'CUSI',fontsize=7, fontweight='bold', color='white')

# BUPI
lon = -72.969383 	
lat = 4.568678

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='y', s=100)
#plt.text(x, y, 'BUPI',fontsize=7, fontweight='bold', color='white')

# CHRL
lon = -74.973338 	 	
lat = 4.22324604

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='y', s=100)
#plt.text(x, y, 'CHRL' ,fontsize=7, fontweight='bold', color='white')

# ICZO
lon = -74.600273	 	
lat = 4.174588

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='y', s=100)
#plt.text(x, y, 'ICZO' ,fontsize=7, fontweight='bold', color='white')
'''
# Plotear los sismos

lons  = [-74.184, -74.154, -74.168, -74.161]
lats  = [3.462, 3.465, 3.425, 3.426]
depth = [13, 12, 10, 19]
mag   = [6, 5.8, 4.7, 4.7]

# Increasing difference in Magnitude
s = [(1/8000)*n**9 for n in mag]

x, y = map(lons, lats)

events = map.scatter(x, y, marker='o', c=depth, s=s, edgecolor='white')

#divider = make_axes_locatable(ax0)
#cax = divider.append_axes("right", size="5%", pad=0.05)

#cb = fig.colorbar(events, fraction=0.03, pad=-0.15)
#cb.set_label(label='$Earthquake$ $depth$ $(km)$', size=20, color='white')
#cb.ax.tick_params(labelsize=15, labelcolor='white')

# Legend Elements
legend_elements = [Line2D([0], [0], marker='v', color='r', lw=0,label='Multiparametric\nstations',
                          markersize=15)
                   ,Line2D([0], [0], marker='o', color='#572364', lw=0,label='Seismic events',
                          markersize=15)]

legend = ax0.legend(handles=legend_elements, loc='lower left', fontsize=20)
# plt.setp(legend.get_texts(), color='w')

x, y = map(-78.2, 12.2)
x2, y2 = map(-78.35, 10.7)

plt.annotate('N', xy=(x, y),
                xytext=(x2, y2),
                color='white',
                arrowprops=dict( arrowstyle="fancy", color='white'),
                fontsize=20
                )

map.drawmapscale(-69, -3.7, -74.5, 4.5, 400, barstyle='fancy', fontcolor='white', fontsize=17)

# Drawing the box
lons = [-75.3, -71.8, -71.8, -75.3, -75.3]
lats = [2, 2, 6.5, 6.5, 2]

x, y = map(lons, lats)

map.plot(x, y, marker=None, color='r', linewidth=1)

#plt.savefig('mapaLocalizacion.png')
plt.show()
#---------------------------------------------------------------------



