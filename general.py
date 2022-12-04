# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:00:47 2022

@author: ShahzadAnsari
"""

from dash import Dash, html, dcc, Input, Output,dash_table
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objects as go
import testData as td


# get test data. 


cLat = td.cLat
cLong = td.cLong

noSolution = td.randomNoSolution()

preatoFrontier = td.randomPreato()

coords = td.randomLatLong()

solutions = td.getBuildingUpgrades(coords)

# get configData

dims = 3
xlab = "cost"
ylab = "time"
zlab = "dislocation"


#https://dashcheatsheet.pythonanywhere.com/
#https://getbootstrap.com/docs/4.0/utilities/colors/

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


jumbotronStyle = {
    
    "position" : "fixed",
    "background-color":"#92a8d1"    
    
    
    
}

card = dbc.Card(
    [
        dbc.CardImg(
            src="assets/incore-logo.png",
            top=True,
            style={"opacity": 1},
        ),
        
    ],
    style={
            "width": "10rem",
    },
)

img = dbc.Card(
        [
            dbc.CardImg(
                src="assets/Figure_1.png",
                top=True,
                style={"opacity": 1},
            ),
            
        ]
    )

jumbotron = html.Div(
    dbc.Container(
        [
            dbc.Row([
                
                dbc.Col(
                    html.Div("General Visualization IN-CORE Dashbord App", className="display-5"),
                    width = "auto"
                ),
                dbc.Col(card,width = {"size": 3, "order": "last", "offset": 3})
            ],justify ="between"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.P(
                "Data visualization dashboard for general data sets. Model created by general visualizations created by Shahzad Ansari",
                className="lead",
            ),
            html.Hr(className="my-2"),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-dark text-light rounded-3",
    #style = jumbotronStyle,
    
)

other = html.Div(
    dbc.Container([
        
        html.Div(id='result'),
        html.Hr(),
        
        dcc.Graph(
            id='graph'
        ),
        
        dbc.Row([
            html.P("{xlab} slider".format(xlab = xlab))
            dcc.RangeSlider(
                id='x-range-slider',
                min=preatoFrontier['x'].min(), max=preatoFrontier['x'].max(), step=1,
                marks={min: str(min), max: str(max)},
                value=[min, max]
            ),
            
            html.P("{ylab} slider".format(ylab = ylab))
            dcc.RangeSlider(
                id='y-range-slider',
                min=preatoFrontier['y'].min(), max=preatoFrontier['y'].max(), step=1,
                marks={min: str(min), max: str(max)},
                value=[min, max]
            ),
            
            
            html.P("{zlab} slider".format(zlab = zlab))
            dcc.RangeSlider(
                id='z-range-slider',
                min=preatoFrontier['z'].min(), max=preatoFrontier['z'].max(), step=1,
                marks={min: str(min), max: str(max)},
                value=[min, max]
            ),
        ])
       
        
        
        
        # html.Hr(),
        # html.Div(id='repair'),
        # html.Div(id='dislocation'),
        # html.Div(id='eloss'),
        html.Hr(),
        
        dbc.Row([
            dbc.Col([
                html.Div(id = 'metricsNoSol'), 
                   
            ]),
        ]),
        
        dbc.Row([
            dbc.Col([
                html.Div(id = 'metricsWBudget'), 
                  
            ]),
        ]),  
    ])
)

app.layout = dbc.Container([
    jumbotron,
    other 
],style={"overflowY":"scroll",'height':"1500px"},fluid=True)


@app.callback(
    Output("graph", "figure"), 
    Input("x-range-slider", "value")
    Input("y-range-slider", "value")
    Input("z-range-slider", "value"))
def update_bar_chart(slider_range):
    df = preatoFrontier # replace with your own data source
    low, high = slider_range
    mask = (df.petal_width > low) & (df.petal_width < high)

    fig = px.scatter_3d(df[mask], 
        x='sepal_length', y='sepal_width', z='petal_width',
        color="species", hover_data=['petal_width'])
    return fig



   
if __name__ == '__main__':
    app.run_server(debug=True)