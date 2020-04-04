# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:17:38 2020

@author: Ayan Dasgupta
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

#df = pd.read_csv('icmr.csv')
df = pd.read_csv('covid19indiaorg.csv')

growth = df['Growth'].values

growth = growth.astype('float32')

size = len(growth)

train, test = growth[14: 30], growth[30+1:]

model = ARIMA(train, order=(0,1,1))
model_fit = model.fit(disp = True)
model_fit.plot_predict(1, len(train)+30, alpha = 0.05)
model_fit.summary()

plt.ylabel('Case Growth')
plt.xlabel('No. of Days')
plt.title('ARIMA Forecast')
plt.show()

