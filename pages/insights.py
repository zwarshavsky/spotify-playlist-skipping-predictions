import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

### The Realistic Model

The final model consists **ONLY** of attributes that could have been collected about the data prior to the playback event. 

Our metrics appear much more realistic and generalized after rerunning our model:

![Scores](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/Score_2.png "Title")

We run the robust Permutation Importance analysis on our remaining features and get the following:

![Permutation Importance](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/perm_importance.png "Title")

This confirms our findings previously. Only a few additional features can be filtered out of our model. Accuracy score remains static.   


####

![PDP Interaction Plot](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/pdp_interaction.png "Title")

This particular partial dependence plot reveals that the two most influential attributes on outcome, *release year* and *us popularity estimate*, 
play a greater role in the prediction when a track lacks popularity and is contemporary.    


![PDP Interaction Plot 2](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/pdp_interaction2.png "Title")

The two features *speechiness* and *instrumentalness* refer to opposite qualities in the track. As you can see when a track is 100% instrumental, there is a much lower rate of speechiness, 
a quality depicting spoken word elements.  




    """
        ),

dcc.Markdown(
            """


#### The Infamous Shap Force Plot
![PDP Interaction Plot 2](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/shap_force.png "Shap")

 """

),
        
    ],
    md=4,
)


column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])