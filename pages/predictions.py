import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly

from app import app


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions


            """
        ),
        html.Br(),
        html.H6('Year of Release'),
        dcc.Dropdown(
            id='year-drop',
            value=1960,
            options=[{'label': i, 'value' : i} for i in [i for i in range(1960,2019)]],  
        ),
        html.Br(),
        html.H6('US_Popularity Estimate'),
        dcc.Slider(
            id='slider-2',
            min=90,
            max=100,
            value= 45,
            step=.1,
#             marks={i:str(i) for i in range(90,101)},
            
        ),
        html.Br(),
        html.H6('Beat Strength'),
        dcc.Slider(
            id='slider-3',
            min=.01,
            max=1,
            step=.01,
            value = .5,
#             marks={i:str(i) for i in range(1,11)},
            
        ),
        html.Br(),
        html.H6('Bounciness'),
        dcc.Slider(
            id='slider-4',
            min=.01,
            max=1,
            step=.01,
#             marks={i:str(i) for i in range(1,11)},
            
        ),
        html.Br(),
        html.H6('Danceability'),
        dcc.Slider(
            id='slider-5',
            min=0.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(0,2)},
            
        ),
        html.Br(),
        html.H6('Dynamic Range'),
        dcc.Slider(
            id='slider-6',
            min=0.01,
            max=38,
            step=0.01,
#             marks={i:str(i) for i in range(0,39)},
            
        ),
        html.Br(),
        html.H6('Energy'),
        dcc.Slider(
            id='slider-7',
            min=0.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(1,11)},
            
        ),
        html.Br(),
        html.H6('Flatness'),
        dcc.Slider(
            id='slider-8',
            min=0.01,
            max=1.1,
            step=0.01,
#             marks={i:str(i) for i in range(0,1)},
            
        ),
        html.Br(),
        html.H6('Instrumentalness'),
        dcc.Slider(
            id='slider-9',
            min=0.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(0,1)},
            
        ),
        html.Br(),
        html.H6('Key'),
        dcc.Slider(
            id='slider-10',
            min=1,
            max=11,
            step=1,
            # marks={i: i for i in ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]},
            # # marks={i for i in ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]},
            
        ),
        html.Br(),
        html.H6('Liveness'),
        dcc.Slider(
            id='slider-11',
            min=0.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.Br(),
        html.H6('Mechanism'),
        dcc.Slider(
            id='slider-12',
            min=0.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.Br(),
        html.H6('Organism'),
        dcc.Slider(
            id='slider-13',
            min=0.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.Br(),
        html.H6('Speechiness'),
        dcc.Slider(
            id='slider-14',
            min=0.1,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.Br(),
        html.H6('Tempo'),
        dcc.Slider(
            id='slider-15',
            min=60,
            max=244,
            step=5,
            marks={i:str(i) for i in range(60,241,20)},
            
        ),
        html.Br(),
        html.H6('Time Signature'),
        dcc.Slider(
            id='slider-16',
            min=1,
            max=5,
            step=1,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.Br(),
        html.H6('Valence'),
        dcc.Slider(
            id='slider-17',
            min=.01,
            max=1,
            step=0.01,
#             marks={i:str(i) for i in range(0,1)},
            
        ),
        html.Br(),
        html.H6('Model Selection'),
        dcc.Dropdown(
            id='model',
            # value=5,
            options=[{'label': i, 'value' : i} for i in ['Random Forest','XG Boost']],  
        ),
        html.Br(),
        html.H6(id='output-message',children='output will go here'), 
        html.Br(),
        html.Br(),
        html.Br(),
        
    ],
    md=4,
)

matplotlib_figure = plt.figure()
x = [10,  8, 13,  9, 11, 14,  6,  4, 12,  7,  5]
y = [ 8,  6,  7,  8,  8,  9,  7,  4, 10,  4,  5]
plt.scatter(x, y)
plotly_figure = mpl_to_plotly(matplotlib_figure)


column2 = dbc.Col(
    [
       
dcc.Graph(id='my-graph-name', figure=plotly_figure)
        
    ]
)

layout = dbc.Row([column1, column2])     

      