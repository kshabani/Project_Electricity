import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly
from dash.dependencies import Input, Output
import  AuxiliaryFunctions as AF
import plotly.express as px
import pandas as pd

Hourly,Monthly,Weekly,Business_Day = AF.clean_dataset()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

fig = go.Figure()


tab_1 = dcc.Tab(label='Analysis of Summary Statistics',value='tab_1',children=[
    html.Div(children='''
            Choose the Statistics
        '''),
    dcc.Dropdown(
        id = "statistics_drop_down",
        options=[
            {'label':'sum', 'value':'sum'}

            ],
        value='sum',
        multi=False
    ),
    html.Div(children='''
           Choose the resampler
       '''),
    dcc.Dropdown(
        id="resample_drop_down",
        options=[{
            'label': 'hourly', 'value': 'hourly'},
            {'label': 'Business days', 'value': 'Business_Day'},
            {'label': 'weekly', 'value': 'weekly'},
            {'label':'monthly','value':'monthly'}],
        value='hourly',
        multi=False
    )
    ,
    html.Div(children='''
          Choose Year
      '''),
    dcc.Dropdown(

        id="Years",
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': '2016','value':'2016'},
            {'label': '2017', 'value':'2017'},
            {'label':'2018', 'value': '2018'}
        ],
        value='all',
        multi=False
    )
   ]

    )

tab_2 = dcc.Tab(label='Analysis of Detrended Data',value='tab_2')

app.layout = html.Div(children=[
    html.H1(children='Exploratory Analysis of Data'),
    dcc.Tabs(id = 'my_tabs',value='tab_1',children=[tab_1,tab_2]),

    dcc.Graph(
        id='presentation',
        figure=fig
    )
])

@app.callback(
    Output('presentation','figure'),
    [Input('my_tabs','value'),
     Input("statistics_drop_down",'value'),
     Input("resample_drop_down",'value'),
     Input("Years","value")
     ]
)

def update_figure(tab,statistics,resampler,years):


    val=dict(sum = 'sum')


    if tab == "tab_1":

        datas = AF.what(years,resampler,Hourly,Weekly,Monthly,Business_Day)




        datasum = go.Scatter(
                x=Hourly.index,
                y=Hourly['sum'],
                line=dict(color='orange', width=1),
                opacity=0.8,
                name='sum',
                visible=False
            )




        layout = go.Layout(showlegend=True,
                           title=resampler + " Analysis",
                           hovermode="x unified",
                           updatemenus=[
                               dict(
                                   type="buttons",
                                   direction="right",
                                   active=0,
                                   x=0.2,
                                   y=1.9,
                                   buttons=list([
                                       dict(label="Plot Now-->Always click on after statistics)",
                                            method="update",
                                            args=[{
                                                "visible": val[statistics]}
                                            ]
                                            ),

                                   ]

                                   )

                               )

                           ],
                           xaxis=dict(title="Date",
                                      rangeslider=dict(
                                          visible=True
                                      ),
                                      type="date"
                                      ),
                           yaxis=dict(title="KWh")
                           )
        fig = go.Figure(data=[datasum],layout = layout)
        return fig











if __name__ == '__main__':
    app.run_server(debug=True)