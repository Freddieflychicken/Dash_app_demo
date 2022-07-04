from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd


app = Dash(__name__)

#Loading the data
try:
    url = 'https://raw.githubusercontent.com/Freddieflychicken/Dash_app_demo/main/DP_LIVE_01072022105742291.csv'
    df = pd.read_csv(url)
except:
    print("Error! File reading error, no such file or the file path is wrong")

#Set layout of the web app
app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['TIME'].min(),
        df['TIME'].max(),
        step=5,
        value=df['TIME'].min(),
        marks={str(year): str(year) for year in range(df['TIME'].min(), df['TIME'].max()+1, 5)},
        id='year-slider'
    )
])

#Callback function
@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.TIME == selected_year]

    fig = px.bar(filtered_df, x="LOCATION", y="Value", color="LOCATION" )

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)