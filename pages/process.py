import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


column1 = dbc.Col(
    [
       dcc.Markdown('''
## Future Features (or how I learned to love Permutation Importances) 
***
***

As a DJ, sound system nerd, and musician I've spent more 
time arguing, postulating, and sharing unqualified opinions about my favorite (and least favorite)
music than I can quantify. And a lot of these heated discussions centered around what qualities in the music carry greater weight for 
society's universal preferences. 

To answer some of these age-old questions, I've turned to applying several popular machine learning techniques to predict listening behavior around the modern version of the LP: **The Playlist**.  

Resources for Spotify's [Sequential Skip Prediction Challenge](https://www.aicrowd.com/challenges/spotify-sequential-skip-prediction-challenge/dataset_files) contains 350 GBs of playlist 
user interaction data recorded between July 2018 and September 2018 and an additional track list with feature attributes for 1.8 million songs.

My sample is from July 15, 2018. After cross-referencing with the features list, I was left with a total of 1.5 million rows and 50 features.
***

### Feature Selection Process 


The following hierarchical cluster graph reveals relationships between the features. 

![Hierarchical Clustering Analysis](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/deandro_plot.png "Title")

In red connecting line reveal 3 key features as possible contenders for our prediction target. 
***

#### Target Selection

Of the 3 binary classification targets, I ultimately chose "Skip-2" which is evenly split. 

![Hierarchical Clustering Analysis](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/blob/master/assets/classification_distribution.png "Title")

Official "Skip-2" definition: "Boolean indicating if the track was only played briefly"
**Goal:** to predict whether a user will briefly play a track within a playlist or if they will play the track in full.    


#### Feature Leaking

Feature leaking identification and detection can be a tedious process requiring trial and error, domain knowledge, and ultimately, a generalized robust Machine Learning model that has been cross-validated.




![Hierarchical Clustering Analysis](https://github.com/zwarshavsky/spotify-playlist-skipping-predictions/blob/master/assets/Feature_Importances.png "Title")












Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

'''



),

    ],
)

layout = dbc.Row([column1])