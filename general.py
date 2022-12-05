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
import plotly.express as px


# get test data. 


cLat = td.cLat
cLong = td.cLong

noSolution = td.randomNoSolution()
 
preatoFrontier= td.randomPreato()

coords = td.randomLatLong()

solutions = td.getBuildingUpgrades(coords)

# get configData

dims = 3
xlab = "cost"
ylab = "time"
zlab = "dislocation"

preatoFig = px.scatter_3d(preatoFrontier,x = "x",y = "y",z = "z")

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
                "Data visualization dashboard for general data sets. Model created by general visualizations created by Shahzad Ansari tt",
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
            id='graph',
            figure = preatoFig
        ),
        
        dbc.Row([
            html.P("{xlab} slider".format(xlab = xlab)),
            dcc.RangeSlider(
                id='x-range-slider',
                min=preatoFrontier['x'].min(), max=preatoFrontier['x'].max(), step=1,
                marks = {preatoFrontier['x'].min():str(preatoFrontier['x'].min()),preatoFrontier['x'].max():str(preatoFrontier['x'].max())},
                value=[preatoFrontier['x'].min(), preatoFrontier['x'].max()]
            ),
            
             
              html.P("{ylab} slider".format(ylab = ylab)),
              dcc.RangeSlider(
                  id='y-range-slider',
                  min=preatoFrontier['y'].min(), max=preatoFrontier['y'].max(), step=1,
                  marks = {preatoFrontier['y'].min():str(preatoFrontier['y'].min()),preatoFrontier['y'].max():str(preatoFrontier['y'].max())},
                  value=[preatoFrontier['y'].min(), preatoFrontier['y'].max()]
              ),
             
              html.P("{zlab} slider".format(zlab = zlab)),
              dcc.RangeSlider(
                  id='z-range-slider',
                  min=preatoFrontier['z'].min(), max=preatoFrontier['z'].max(), step=1,
                  marks = {preatoFrontier['z'].min():str(preatoFrontier['z'].min()),preatoFrontier['z'].max():str(preatoFrontier['z'].max())},
                  value=[preatoFrontier['z'].min(), preatoFrontier['z'].max()]
              ),
            
        ]),
       
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
    Input("x-range-slider", "value"),
    Input("y-range-slider", "value"),
    Input("z-range-slider", "value"))
def update_bar_chart(x_range,y_range,z_range):
    df = preatoFrontier # replace with your own data source
    xlow, xhigh = x_range
    ylow, yhigh = y_range
    zlow, zhigh = z_range
    xmask = (df.x > xlow) & (df.x < xhigh)
    ymask = (df['y']> ylow) & (df['y'] < yhigh)
    zmask = (df['z']> zlow) & (df['z'] < zhigh)
    df = df[xmask]
    df = df[ymask]
    df = df[zmask]
    fig = go.Figure() # create a figure
  
    fig.add_trace(go.Scatter3d(
                x = df['x'], # x dim for scatter plot
                y = df['y'], # y dim for scatter plot
                z = df['z'], # z dim for scatter plot
                mode = 'markers', # type of points on scatterplot
                name = 'markers', # name of the points on the scatterplot
                # settings for the scatterplot
                marker=dict(
                    size=10, # The size of the markers are set by this 
                    color=df['x'], # set color to an array/list of desired values
                    colorscale='Viridis',   # choose a colorscale
                    opacity=0.8 # opacity 
                )
            ))
        
    # 3D Scatter plot 
    fig.update_layout(clickmode='event+select') #What happens when you click on a point
    # titles and dimensions
    fig.update_layout(scene = dict(
                        xaxis_title=xlab,
                        yaxis_title=ylab,
                        zaxis_title=zlab),
                        title="Preto Frontier",
                        width=1200,
                        height=900)

    return fig
   
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    