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

dim = 2
xlab = "Cost or repair"
ylab = "Time to repair"
zlab = "Population Dislocation"

cLat = td.cLat
cLong = td.cLong

noSolution = td.randomNoSolution(dim)

if dim == 3:
    noSolution = noSolution.rename(columns={"x": xlab, "y": ylab,"z":zlab,"b":"Buildings"})
else:
    noSolution = noSolution.rename(columns={"x": xlab, "y": ylab,"b":"Buildings"})
    

preatoFrontier= td.randomPreato(dim)

coords = td.randomLatLong()

solutions = td.getBuildingUpgrades(coords)



if dim == 3:
    preatoFig = px.scatter_3d(preatoFrontier,x = "x",y = "y",z = "z")
elif dim == 2:
    preatoFig = px.scatter(preatoFrontier,x = "x",y = "y")

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

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)
#app.config.suppress_callback_exceptions=True

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

if dim ==2:
        
    TwoContainer = html.Div(
        
        dbc.Container([
            
          
            html.Hr(),
            
            dcc.Graph(
                id='2dgraph',
                figure = preatoFig
            ),
            html.P(id='2dresult'),
            dbc.Row([
                html.P("{xlab} slider".format(xlab = xlab)),
                dcc.RangeSlider(
                    id='x-range-slider',
                    min=preatoFrontier['x'].min(), max=preatoFrontier['x'].max(), step=1, tooltip={"placement": "bottom", "always_visible": True} ,
                    marks = {preatoFrontier['x'].min():str(preatoFrontier['x'].min()),preatoFrontier['x'].max():str(preatoFrontier['x'].max())},
                    value=[preatoFrontier['x'].min(), preatoFrontier['x'].max()]
                ),
                
                 
                  html.P("{ylab} slider".format(ylab = ylab)),
                  dcc.RangeSlider(
                      id='y-range-slider',
                      min=preatoFrontier['y'].min(), max=preatoFrontier['y'].max(), step=1, tooltip={"placement": "bottom", "always_visible": True},
                      marks = {preatoFrontier['y'].min():str(preatoFrontier['y'].min()),preatoFrontier['y'].max():str(preatoFrontier['y'].max())},
                      value=[preatoFrontier['y'].min(), preatoFrontier['y'].max()]
                  ),
                      
                
            ]),
           
            html.Hr(),
            
            dbc.Row([
                dbc.Col([
                    html.H6("Metrics with no mitigation steps taken"),
                    dbc.Table.from_dataframe(noSolution,striped=True,bordered=True,hover=True)
                       
                ]),
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.Div(id = 'metricsWBudget'), 
                      
                ]),
            ]),  
        ])
    )

    
if dim == 3:
    ThreeContainer = html.Div(
        dbc.Container([
            
          
            html.Hr(),
            
            dcc.Graph(
                id='graph',
                figure = preatoFig
            ),
            html.P(id='3dresult'),
            dbc.Row([
                html.P("{xlab} slider".format(xlab = xlab)),
                dcc.RangeSlider(
                    id='x-range-slider',
                    min=preatoFrontier['x'].min(), max=preatoFrontier['x'].max(), step=1, tooltip={"placement": "bottom", "always_visible": True} ,
                    marks = {preatoFrontier['x'].min():str(preatoFrontier['x'].min()),preatoFrontier['x'].max():str(preatoFrontier['x'].max())},
                    value=[preatoFrontier['x'].min(), preatoFrontier['x'].max()]
                ),
                
                 
                  html.P("{ylab} slider".format(ylab = ylab)),
                  dcc.RangeSlider(
                      id='y-range-slider',
                      min=preatoFrontier['y'].min(), max=preatoFrontier['y'].max(), step=1, tooltip={"placement": "bottom", "always_visible": True},
                      marks = {preatoFrontier['y'].min():str(preatoFrontier['y'].min()),preatoFrontier['y'].max():str(preatoFrontier['y'].max())},
                      value=[preatoFrontier['y'].min(), preatoFrontier['y'].max()]
                  ),
                      
                    html.P("{zlab} slider".format(zlab = zlab)),
                    dcc.RangeSlider(
                        id='z-range-slider',
                        min=preatoFrontier['z'].min(), max=preatoFrontier['z'].max(), step=1, tooltip={"placement": "bottom", "always_visible": True},
                        marks = {preatoFrontier['z'].min():str(preatoFrontier['z'].min()),preatoFrontier['z'].max():str(preatoFrontier['z'].max())},
                        value=[preatoFrontier['z'].min(), preatoFrontier['z'].max()]
                    ),
                
            ]),
           
            html.Hr(),
            
            dbc.Row([
                dbc.Col([
                    html.H6("Metrics with no mitigation steps taken"),
                    dbc.Table.from_dataframe(noSolution,striped=True,bordered=True,hover=True)
                       
                ]),
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.Div(id = 'metricsWBudget'), 
                      
                ]),
            ]),  
        ])
    )


if dim == 3:
    MainContainer = ThreeContainer
else:
    MainContainer = TwoContainer

app.layout = dbc.Container([
    jumbotron,
    MainContainer 
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
                        width=900,
                        height=900)

    return fig
   

@app.callback(
    Output("2dgraph", "figure"), 
    Input("x-range-slider", "value"),
    Input("y-range-slider", "value"))
def update_2_chart(x_range,y_range):
    df = preatoFrontier # replace with your own data source
    xlow, xhigh = x_range
    ylow, yhigh = y_range
    xmask = (df.x > xlow) & (df.x < xhigh)
    ymask = (df['y']> ylow) & (df['y'] < yhigh)
    df = df[xmask]
    df = df[ymask]
    fig = go.Figure() # create a figure
  
    fig.add_trace(go.Scatter(
                x = df['x'], # x dim for scatter plot
                y = df['y'], # y dim for scatter plot
               # z = df['z'], # z dim for scatter plot
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
    fig.update_layout(
                        xaxis_title= xlab,
                        yaxis_title= ylab,
                        title="Preto Frontier",
                        width=900,
                        height=900
                    )

    return fig



#--------------------------------------------------------------------------------    
@app.callback(
    Output('3dresult','children'),
    Input('graph', 'clickData'))
def show_coords_3d(clickData):

        if clickData is None: 
            return ""
        else:
            xCoord = clickData['points'][0]['x'] 
            yCoord = clickData['points'][0]["y"]
            zCoord = clickData['points'][0]["z"]
            
            #add flush = True or it wont display the message.
            print(f'Selected [{xCoord},{yCoord},{zCoord}]',flush=True)
           
            return "Selected : [{},{},{}]".format(xCoord,yCoord,zCoord)
        
        
@app.callback(
    Output('2dresult','children'),
    Input('2dgraph', 'clickData'))
def show_coords_2d(clickData):

        if clickData is None: 
            return ""
        else:
            xCoord = clickData['points'][0]['x'] 
            yCoord = clickData['points'][0]["y"]
           
            
            #add flush = True or it wont display the message.
            print(f'Selected [{xCoord},{yCoord}]',flush=True)
           
            return "Selected : [{},{}]".format(xCoord,yCoord)
            
            
            
                
        
        
        
        
        
        
        
        
        
# @app.callback(
#         Output('noSolutionDf','children'),
#         ,
#     )
# def setmetricsNoSol(year):
#         df = noSolution
#         return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    