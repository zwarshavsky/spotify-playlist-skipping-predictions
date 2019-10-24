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
        # dcc.Markdown(
        #     """
        
        #     ## Predictions


        #     """
        # ),
        # html.H6('Model Selection'),
        # dcc.Dropdown(
        #     id='model',
        #     # value=5,
        #     options=[{'label': i, 'value' : i} for i in ['Random Forest','XG Boost']],  
        # ),
        html.Div(id='test',children='output will go here'), 
        html.Br(),
         html.H6('Year of Release'),
        dcc.Slider(
            id='slider-0',
            min=1960,
            max=2020,
            step=1,
            value = 92,
            marks={i:str(i) for i in range(1960,2021,10)},
            
        ),
        # html.H6('Year of Release'),
        # dcc.Dropdown(
        #     id='year-drop',
        #     value=1960,
        #     options=[{'label': i, 'value' : i} for i in [i for i in range(1960,2019)]],  
        # ),
        html.Br(),
        html.H6('US Popularity Level'),
        dcc.Slider(
            id='slider-1',
            min=90,
            max=100,
            value= 45,
            step=.1,
#             marks={i:str(i) for i in range(90,101)},
            
        ),
        html.H6('Beat Strength'),
        dcc.Slider(
            id='slider-2',
            min=.01,
            max=1,
            step=.01,
            value = .5,
#             marks={i:str(i) for i in range(1,11)},
            
        ),
        html.H6('Bounciness'),
        dcc.Slider(
            id='slider-3',
            min=.01,
            max=1,
            step=.01,
            value = .5,
#             marks={i:str(i) for i in range(1,11)},
            
        ),
        html.H6('Danceability'),
        dcc.Slider(
            id='slider-4',
            min=0.01,
            max=1,
            step=0.01,
            value = .5,
#             marks={i:str(i) for i in range(0,2)},
            
        ),
        html.H6('Dynamic Range'),
        dcc.Slider(
            id='slider-5',
            min=0.01,
            max=38,
            step=0.01,
            value = 19,
#             marks={i:str(i) for i in range(0,39)},
            
        ),
        html.H6('Energy'),
        dcc.Slider(
            id='slider-6',
            min=0.01,
            max=1,
            step=0.01,
            value = .5,
#             marks={i:str(i) for i in range(1,11)},
            
        ),
        html.H6('Instrumentalness'),
        dcc.Slider(
            id='slider-7',
            min=0.01,
            max=1,
            step=0.01,
            value = .5,
#             marks={i:str(i) for i in range(0,1)},
            
        ),
        html.H6('Mechanism'),
        dcc.Slider(
            id='slider-8',
            min=0.01,
            max=1,
            step=0.01,
            value = .5,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.H6('Organism'),
        dcc.Slider(
            id='slider-9',
            min=0.01,
            max=1,
            step=0.01,
            value = .5,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.H6('Speechiness'),
        dcc.Slider(
            id='slider-10',
            min=0.1,
            max=1,
            step=0.01,
            value = .5,
#             marks={i:str(i) for i in range(1,9)},
            
        ),
        html.H6('Tempo'),
        dcc.Slider(
            id='slider-11',
            min=60,
            max=240,
            step=5,
            value = 92,
            marks={i:str(i) for i in range(60,241,20)},
            
        ),
    
        html.Br(),
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
        html.Div(id='prediction-text',children='output will go here'), 
        html.Div(id='shapley',children='output will go here'),
        
    ]
)

column3 = dbc.Col(
    [
        # html.Div(id='prediction-text',children='output will go here'), 
        dcc.Markdown(
            """
        
            Instructions: Adjust the attribute sliders. Your prediction outcome will update dynamically. 

            Attribute Definitions:

            * Year of Release - Year the track was released 
            * US Popularity Level - Highest point on Billboard  
            * Beat Strength - The energy level at beat intervals
            * Bounciness - Length of decay of initial beat
            * Danceability - Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. 
            * Dynamic Range - The volumne difference between the loudest and quietest parts of the track
            * Energy - Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
            * Instrumentalness - Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.
            * Mechanism - Whether a song sticks rigidly to a click track or drum machine, or is more organic and "tempo-wandering"
            * Organism - Organism is how human a track sounds, using a live drummer rather than a drum machine for example.
            * Speechiness - Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. 
            * Tempo - The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. 





            """
        ),
        # html.Div(id='shapley',children='output will go here'),
# dcc.Graph(id='my-graph-name', figure=plotly_figure)
        
    ]
)

layout = dbc.Row([column1, column2, column3])     

      