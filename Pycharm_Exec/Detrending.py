
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller,kpss
#import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

## Offline mode
from plotly.offline import init_notebook_mode, iplot

path = '/mnt/368AE7F88AE7B313/Files_Programming/Git/Project_Electricity/' \
       'data/Processed/1002_processed_single_datetime.pkl'
data = pd.read_pickle(path)

data_2016 = data[(data.index.year == 2017)].copy()
#data_2016 = data[(data.index.year == 2017)].copy()
hourly = data.resample('W')
hourly_min = hourly.max()
hourly_min.fillna(method='ffill',inplace=True)
#hourly_min = hourly_min.iloc[1:2000,:].copy()
np.all(np.isfinite(hourly_min['messwert_kwh']))

result_mul = seasonal_decompose(hourly_min['messwert_kwh'],
                  model='multiplicative',
                  extrapolate_trend='freq')
result_add = seasonal_decompose(hourly_min['messwert_kwh'],
                   model='additive',
                   extrapolate_trend='freq')

# Quick Plot
plt.figure()
plt.rcParams.update({'figure.figsize': (10,10)})
result_mul.plot().suptitle('Multiplicative Decompose', fontsize=22)
#result_add.plot().suptitle('Additive Decompose', fontsize=22)
plt.show()