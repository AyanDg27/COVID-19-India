# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 06:39:56 2020

@author: Ayan Dasgupta
"""

#importing the case count file
import pandas as pd
df = pd.read_csv('r0-india-states.csv')
df.head()

import numpy as np

#Claculating R0
for i in range(1, 39):
    if df[list(df)[i]][0] == 0:
        print(list(df)[i], ":", 1)
    else:
        print(list(df)[i], ":", ((np.log(130000000/((1/(df[list(df)[i]][4]/(df[list(df)[i]][0]*130000000)))-1)))/4)+1)