# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
from lat_lon_parser import parse
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('Local_Nature_Reserves_England_6224075941597999982.csv'
                 , usecols=('LNR_NAME', 'LONGITUDE', 'LATITUDE', ))

df['longitude'] = df['LONGITUDE'].apply(parse) 
df['latitude'] = df['LATITUDE'].apply(parse)
df.drop(columns=['LONGITUDE', 'LATITUDE'], inplace=True)
df['size'] = 1


fig = go.Figure(go.Scattermap(
    lat=df['latitude'],
    lon=df['longitude'],
    mode='markers',
    marker=dict(size=14),
    hovertext=df['LNR_NAME']
))


fig.layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='map',
        figure=fig,
        style={'height': '100vh'}
    )
])

if __name__ == '__main__':
    app.run(debug=True)
