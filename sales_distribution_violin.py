import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load the dataset
data = pd.read_excel("C:/Users/Chandru/OneDrive/Desktop/Python Visuals/Sample - Superstore.xls", sheet_name="Orders")

# Color mapping for regions
color_map = {
    'Central': 'blue',
    'East': 'red',
    'South': 'orange',
    'West': 'pink'
}
data['Color'] = data['Region'].map(color_map)

# Create a Dash application
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in data['Region'].unique()],
        value=data['Region'].unique(),
        multi=True
    ),
    dcc.Graph(id='violin-chart')
])

# Define callback to update graph
@app.callback(
    Output('violin-chart', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_graph(selected_regions):
    filtered_data = data[data['Region'].isin(selected_regions)]
    fig = px.violin(filtered_data, x='Region', y='Sales', color='Color', box=True, points="all", title='Sales Distribution by Region')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8061)
