import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app


column1 = dbc.Col(
    [
       dcc.Markdown('''
## Back from the Feature 


As a DJ, sound system nerd, and musician I've spent more 
time arguing, postulating, and sharing unqualified opinions about my favorite (and least favorite)
music than I can quantify. And a lot of these heated discussions centered around what qualities in the music carry greater weight for 
society's universal preferences. 

To answer some of these age-old questions, I've turned to applying several popular machine learning techniques to predict listening behavior around the modern version of the LP: **The Playlist**.  

Resources for Spotify's [Sequential Skip Prediction Challenge](https://www.aicrowd.com/challenges/spotify-sequential-skip-prediction-challenge/dataset_files) contains 350 GBs of playlist 
user interaction data recorded between July 2018 and September 2018 and an additional track list with feature attributes for 1.8 million songs.

My sample is from July 15, 2018. After cross-referencing with the features list, I was left with a total of 1.5 million rows and 50 features.


### Feature Selection Process 


The following hierarchical cluster graph reveals relationships between the features. 

![Hierarchical Clustering Analysis](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/deandro_plot.png "Title")

Red connecting lines reveal 3 key features as possible contenders for our prediction target. 
***

#### Target Selection

Of the 3 binary classification targets, I ultimately chose "Skip-2" which is evenly split. 

![Hierarchical Clustering Analysis](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/classification_distribution.png "Title")

Spotify's "Skip-2" definition: "Boolean indicating if the track was only played briefly"

**Goal:** to predict whether a user will briefly play a track or if they will play the track in full within a Spotify playlist.    

***
#### Feature Leaking

Feature leaking identification and detection can be a tedious process requiring re-running ML models via sheer trial and error, domain knowledge, and ultimately, a generalized Machine Learning model that has been cross-validated.

After preprocessing with [TargetEncoder](https://contrib.scikit-learn.org/categorical-encoding/targetencoder.html), Utilizing Scikitlearn's [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), I attained the following scores:

![Scores](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/Score_1.png "Title")

An incredible improvement! 20% higher validation accuracy than the mean baseline. Too good to be true?

![Hierarchical Clustering Analysis](https://raw.githubusercontent.com/zwarshavsky/spotify-playlist-skipping-predictions/master/assets/Feature_Importances.png "Title")

Let's examine the highest performing features:

* hist_user_behavior_reason_start - E.g. _fwdbtn_ - the user action which led to the current track being played 
* hour_of_day - hour of the day playlist / track was played
* session_position - position of track within the playlist
* session_length - number of total rows in the session
* context_type - playlist type 

What is one important question you can ask to cross-check your thinking around feature selection?

**Would this feature be available prior to the event of the actual output from the prediction model?**

Our Guidelines: 

* Our goal is to predict whether a track will be played briefly or in full
* Spotify playlist recommendation engine does not have the capability to adapt to the user's behavior during playlist playback
* Any information extracted about the track during or after playback should be considered off limits for our prediction model

Conclusion:

* The highest performing features were extracted during or after playback
* These features should be dropped from the dataset 











'''



),

    ],
)

layout = dbc.Row([column1])