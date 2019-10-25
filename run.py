# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from joblib import load

rf = load('assets/randomforest.joblib')
xb = load('assets/xgboost.joblib')
shap = load('assets/shapmodel.joblib')
processor = load('assets/processor.joblib')
explainer = load('assets/explainer.joblib')

# Imports from this application
from app import app, server
from pages import index, predictions, insights, process



"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar

NavbarSimple consists of a 'brand' on the left, to which you can attach a link 
with brand_href, and a number nav items as its children. NavbarSimple will 
collapse on smaller screens, and add a toggle for revealing navigation items.

brand (string, optional): Brand text, to go top left of the navbar.
brand_href (string, optional): Link to attach to brand.
children (a list of or a singular dash component, string or number, optional): The children of this component
color (string, optional): Sets the color of the NavbarSimple. Main options are primary, light and dark, default light. You can also choose one of the other contextual classes provided by Bootstrap (secondary, success, warning, danger, info, white) or any valid CSS color of your choice (e.g. a hex code, a decimal code or a CSS color name)
dark (boolean, optional): Applies the `navbar-dark` class to the NavbarSimple, causing text in the children of the Navbar to use light colors for contrast / visibility.
light (boolean, optional): Applies the `navbar-light` class to the NavbarSimple, causing text in the children of the Navbar to use dark colors for contrast / visibility.
sticky (string, optional): Stick the navbar to the top or the bottom of the viewport, options: top, bottom. With `sticky`, the navbar remains in the viewport when you scroll. By contrast, with `fixed`, the navbar will remain at the top or bottom of the page.
"""

navbar = dbc.NavbarSimple(
    brand='Machine Learning for Spotify Playlist Predictions',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='#2FBF62', 
    light=True, 
    dark=False,
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Zhenya Warshavsky', className='mr-2'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:zwarshavsky@gmail.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/zwarshavsky'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/zwarshavsky/'), 
                    # html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/<you>'), 
                ], 
                className='lead'
            )
        )
    )
)

# For more explanation, see: 
# Plotly Dash User Guide, URL Routing and Multiple Apps
# https://dash.plot.ly/urls

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])

@app.callback(
    Output('page-content', 'children'),
              [Input('url', 'pathname')]
              )

def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')

# Prediction Page Interactions
@app.callback(
    [
    # [Output('test', 'children'),
    Output('prediction-text1', 'children'),
    Output('prediction-text2', 'children'),
    Output('prediction-text3', 'children'),
    Output('prediction-text4', 'children'),
    Output('prediction-text5', 'children'),
    Output('prediction-text6', 'children'),
    Output('prediction-text7', 'children')],
    [
            #    [Input('model','value'),
                Input('slider-0','value'), 
               Input('slider-1', 'value'),
               Input('slider-2', 'value'),
               Input('slider-3', 'value'),
               Input('slider-4', 'value'),
               Input('slider-5', 'value'),
               Input('slider-6', 'value'),
               Input('slider-7', 'value'),
               Input('slider-8', 'value'),
               Input('slider-9', 'value'),
               Input('slider-10', 'value'),
               Input('slider-11', 'value'),
               
               ]) 


# def display_results(year,pop,beat,bounce,dance,range,energy,instrument,mechanism,organism,speechiness,tempo):
#     df = pd.DataFrame(columns=['release_year', 'us_popularity_estimate', 'beat_strength', 'bounciness',
#        'danceability', 'dyn_range_mean', 'energy', 'instrumentalness',
#        'mechanism', 'organism', 'speechiness', 'tempo'],data=[[year,pop,beat,bounce,dance,range,energy,instrument,mechanism,organism,speechiness,tempo]])
#     # b = df.head()
#     c = rf.predict(df)
#     if c[0] == True:
#         c = "The track will likely be skipped"
#     else:
#         c = "The track will be played in full"
#     return [f'Inputs: {year,pop,beat,bounce,dance,range,energy,instrument,mechanism,organism,speechiness,tempo}', f'{c}',f'[shapley plot will go here]']

def display_results(year,pop,beat,bounce,dance,range,energy,instrument,mechanism,organism,speechiness,tempo):
    df = pd.DataFrame(columns=['release_year', 'us_popularity_estimate', 'beat_strength', 'bounciness',
       'danceability', 'dyn_range_mean', 'energy', 'instrumentalness',
       'mechanism', 'organism', 'speechiness', 'tempo'],data=[[year,pop,beat,bounce,dance,range,energy,instrument,mechanism,organism,speechiness,tempo]])

    positive_class = 'True'
    positive_class_index = 1
    
    
#     # Get & process the data for the row
    row = df
    row_processed = processor.transform(row)
    print(row_processed)
    
    # Make predictions (includes predicted probability)
    pred = shap.predict(row_processed)[0]
    pred_proba = shap.predict_proba(row_processed)[0, positive_class_index]
    pred_proba *= 100
    if pred == positive_class:
        pred_proba = 100 - pred_proba
    
# Show predictiion & probability
    a = f'The model predicts that this track was only partially played is {pred}, with {pred_proba:.0f}% probability.'
    
    # Get shapley additive explanations
    shap_values = explainer.shap_values(row_processed)
    
    # Get top 3 "pros & cons"
    feature_names = row.columns
    feature_values = row.values[0]
    shaps = pd.Series(shap_values[0], zip(feature_names, feature_values))
    pros = shaps.sort_values(ascending=False)[:3].index
    cons = shaps.sort_values(ascending=True)[:3].index
    
    # Show top 3 reasons for prediction
#     print('\n')
    b = 'Top 3 reasons for prediction:'
    evidence = pros if pred == positive_class else cons
    c = []
    for i, info in enumerate(evidence, start=1):
        feature_name, feature_value = info
        c.append(f'{i}. {feature_name} is {feature_value}.')
    
    # Show top 1 counter-argument against prediction
#     print('\n')
    d = 'Top counter-argument against prediction:'
    evidence = cons if pred == positive_class else pros
    feature_name, feature_value = evidence[0]
    e = f'- {feature_name} is {feature_value}.'
    return [a,b,c[0],c[1],c[2],d,e]

   
    

if __name__ == '__main__':
    app.run_server(debug=True)