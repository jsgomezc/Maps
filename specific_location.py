#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:14:16 2020

@author: juancho
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


fig = plt.figure(figsize=(10,15))

#ax = fig.add_subplot(111)
ax0 = fig.add_subplot(111)

map = Basemap(llcrnrlon=-75.3, llcrnrlat=2.1, urcrnrlon=-71.8, urcrnrlat=6.5, epsg=3116, resolution='i')
#http://server.arcgisonline.com/arcgis/rest/services

map.arcgisimage(service='World_Imagery', xpixels = 1500, verbose= True)

#map.drawstates(linewidth = 0.1, color='white')
#map.drawrivers(color='blue')
map.drawparallels(range(-4, 15, 1), labels=[True,False,False,True],dashes=[2,2], fontsize=30)
map.drawmeridians(range(-87, -61, 1), labels=[True,False,False,True], dashes=[2,2], fontsize=30)

map.readshapefile('/home/juancho/Documentos/GeneralGeo/FallasColombia/FallasColombia', 'faults', color='white', linewidth=0.3)

# USME
lon = -74.126777
lat = 4.480951

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='r', s=250)
#map.scatter(x, y, marker='o', color='r', s=135000, alpha=0.2, linewidth=3, edgecolor='r')
plt.text(x, y, 'USME',fontsize=25, fontweight='bold', color='white')


# TUNJ
lon = -73.357760
lat = 5.533368

x, y = map(lon, lat)

map.scatter(x, y, marker='v', color='r', s=250)
plt.text(x, y, 'TUNJ',fontsize=25, fontweight='bold', color='white')



# Plotear los sismos

lons  = [-74.184, -74.154, -74.168, -74.161]
lats  = [3.462, 3.465, 3.425, 3.426]
depth = [13, 12, 10, 19]
mag   = [6, 5.8, 4.7, 4.7]

# Increasing difference in Magnitude
s = [(1/4000)*n**9 for n in mag]

x, y = map(lons, lats)

scatter = map.scatter(x, y, marker='o', c=depth, s=s, edgecolor='white')

#kw = dict(prop="sizes", num=4,  color='black', func=lambda s: (8000*s**(1/9)))
#legend2 = ax0.legend(*scatter.legend_elements(**kw), loc=2, title="Mag.")

#divider = make_axes_locatable(ax0)
#cax = divider.append_axes("right", size="5%", pad=0.05)

cb = fig.colorbar(scatter, fraction=0.03, pad=-0.18)
cb.set_label(label='$Earthquake$ $depth$ $(km)$', size=23, color='white')
cb.ax.tick_params(labelsize=23, labelcolor='white')

# Legend Elements
legend_elements = [Line2D([0], [0], marker='o', markeredgewidth=1, markeredgecolor='white', color='#2b7cde', lw=0,label='$M_w=6$',
                          markersize=31)
                   ,Line2D([0], [0], marker='o', markeredgewidth=1, markeredgecolor='white', color='#fdff64', lw=0,label='$M_w=4.7$',
                          markersize=17)
                   ,Line2D([0], [0], lw=1, color='w', label='Faults',
                          markersize=30)]

legend = ax0.legend(handles=legend_elements, loc='lower left', fontsize=23)
# plt.setp(legend.get_texts(), color='w')

x, y = map(-75, 6.2)
x2, y2 = map(-75.05, 5.8)

plt.annotate('N', xy=(x, y),
                xytext=(x2, y2),
                color='white',
                arrowprops=dict(arrowstyle="fancy", color='white'),
                fontsize=25
                )


map.drawmapscale(-72.5, 2.45, -73.9, 3.25, 100, barstyle='fancy', fontcolor='white', fontsize=27)



#plt.savefig('mapaLocalizacion.png')
plt.show()
#---------------------------------------------------------------------