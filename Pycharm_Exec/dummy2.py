import pickle
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import numpy as np

#import chart_studio.plotly as py
import plotly.graph_objs as go
import  AuxiliaryFunctions as AF
import plotly.figure_factory as ff

AF.resample_data()
#Hourly,Monthly,Weekly,Business_Day = AF.clean_dataset()


#
# traces.append(
#     go.Scatter(
#         x=Hourly.index,
#         y=Hourly['mean'],
#         line=dict(color='red', width=1),
#         opacity=0.8,
#         name='mean',
#         visible=False
#     )
# )
#
# traces.append(
#     go.Scatter(
#         x=Hourly.index,
#         y=Hourly['std'],
#         line=dict(color='red', width=1),
#         opacity=0.8,
#         name='std',
#         visible=False
#     )
# )
#
# traces.append(
#     go.Scatter(
#         x=Hourly.index,
#         y=Hourly['sum'],
#         line=dict(color='red', width=1),
#         opacity=0.8,
#         name='sum',
#         visible=False
#     )
# )
