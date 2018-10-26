#standard library
import os

# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go

# pydata stack
import pandas as pd
from sqlalchemy import create_engine

# set params
#DB_URI=sqlite:///db/example.db
conn = create_engine('sqlite:///db/example.db')
#conn = create_engine(os.environ['DB_URI'])


###########################
# Data Manipulation / Model
###########################

def fetch_data(q):
    df = pd.read_sql(
        sql=q,
        con=conn
    )
    return df


#########################
# Dashboard Layout / View
#########################

# Set up Dashboard and create layout
app = dash.Dash()
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

app.layout = html.Div([

    # Page Header
    html.Div([
        html.H1('Project Header')
    ]),

])


#############################################
# Interaction Between Components / Controller
#############################################

# Template
@app.callback(
    Output(component_id='selector-id', component_property='figure'),
    [
        Input(component_id='input-selector-id', component_property='value')
    ]
)
def ctrl_func(input_selection):
    return None

#########################
# Dashboard Layout / View
#########################

def generate_table(dataframe, max_rows=10):
    '''Given dataframe, return template generated using Dash components
    '''
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


def onLoad_division_options():
    '''Actions to perform upon initial page load'''

    division_options = (

        [{'label': division, 'value': division}
         for division in get_divisions()]
    )
    return division_options
def get_divisions():
    '''Returns the list of divisions that are stored in the database'''

    division_query = (
        f'''
        SELECT DISTINCT division
        FROM results
        '''
    )
    divisions = fetch_data(division_query)
    divisions = list(divisions['division'].sort_values(ascending=True))
    return divisions



# Set up Dashboard and create layout
app = dash.Dash()
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

app.layout = html.Div([

    # Page Header
    html.Div([
        html.H1('Soccer Results Viewer')
    ]),

    # Dropdown Grid
    html.Div([
        html.Div([
            # Select  Dropdown
            html.Div([
                html.Div('Select Division', className='three columns'),
                html.Div(dcc.Dropdown(id='division-selector',
                                      options=onLoad_division_options()),
                         className='nine columns')
            ]),

            # Select Season Dropdown
            html.Div([
                html.Div('Select Season', className='three columns'),
                html.Div(dcc.Dropdown(id='season-selector'),
                         className='nine columns')
            ]),

            # Select Team Dropdown
            html.Div([
                html.Div('Select Team', className='three columns'),
                html.Div(dcc.Dropdown(id='team-selector'),
                         className='nine columns')
            ]),
        ], className='six columns'),

        # Empty
        html.Div(className='six columns'),
    ], className='twleve columns'),

    # Match Results Grid
    html.Div([

        # Match Results Table
        html.Div(
            html.Table(id='match-results'),
            className='six columns'
        ),

        # Season Summary Table and Graph
        html.Div([
            # summary table
            dcc.Graph(id='season-summary'),

            # graph
            dcc.Graph(id='season-graph')
            # style={},

        ], className='six columns')
    ]),
])


# start Flask server
if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='0.0.0.0',
        port=8050
)
