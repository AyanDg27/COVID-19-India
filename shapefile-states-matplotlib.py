# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:00:00 2020

@author: Ayan Dasgupta
"""

import matplotlib.pyplot as plt
#%matplotlib inline

import geopandas as gpd

shapefile = 'IND_adm1.shp'

gdf = gpd.read_file(shapefile)[['ID_1', 'NAME_1', 'geometry']]
gdf.columns = ['state_code', 'state', 'geometry']
gdf.head(37)

#gdf.plot()

import pandas as pd
datafile = 'r0-states.csv'
#Read csv file using pandas
df = pd.read_csv(datafile, names = ['State', 'R0'], skiprows = 1)
df.head()

merged = gdf.merge(df, left_on = 'state', right_on = 'State')

merged.head(37)

variable = 'R0'

# set the range for the choropleth
vmin, vmax = 1, 1.8

# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

# create map
merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8')
ax.axis('off')

# add a title
ax.set_title('COVID-19 R0 of Indian States and UTs', fontdict={'fontsize': '15', 'fontweight' : '2'})
# create an annotation for the data source
ax.annotate('Source: ICMR' ,xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm._A = []
# add the colorbar to the figure
cbar = fig.colorbar(sm)


