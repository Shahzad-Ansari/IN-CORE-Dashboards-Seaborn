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
from dash import dash_table
import pandas as pd
import statistics


# get test data. 

dim = 2
xlab = "Cost of repair"
ylab = "Time to repair"
zlab = "Population Dislocation"

cLat = td.cLat
cLong = td.cLong

noSolution = td.randomNoSolution(dim)

    

preatoFrontier= td.randomPreato(dim)

coords = td.coords

solutions = td.solutionList
   


if dim == 3:

    stats_df = pd.DataFrame()
    noSolution = noSolution.rename(columns={"x": xlab, "y": ylab,"z":zlab,"b":"Buildings"})
    xmin = preatoFrontier['x'].min()
    ymin = preatoFrontier['y'].min()
    zmin = preatoFrontier['z'].min()
    xmax = preatoFrontier['x'].max()
    ymax = preatoFrontier['y'].max()
    zmax = preatoFrontier['z'].max()
    xmid = (xmax-xmin)/2
    ymid = (ymax-ymin)/2
    zmid = (zmax-zmin)/2
    stats_df['Variable'] = [xlab,ylab,zlab]
    stats_df['minimum'] = [xmin,ymin,zmin]
    stats_df['midpoint'] = [xmid,ymid,zmid]
    stats_df['maximum'] = [xmax,ymax,zmax]
    stats_df['mean'] = [statistics.mean(preatoFrontier['x']),statistics.mean(preatoFrontier['y']),statistics.mean(preatoFrontier['z'])]
    stats_df['SD'] = [statistics.pstdev(preatoFrontier['x']),statistics.pstdev(preatoFrontier['y']),statistics.pstdev(preatoFrontier['z'])]
    stats_df['Variance'] = [statistics.pvariance(preatoFrontier['x']),statistics.pvariance(preatoFrontier['y']),statistics.pvariance(preatoFrontier['z'])]
    
else:
    
    stats_df = pd.DataFrame()
    noSolution = noSolution.rename(columns={"x": xlab, "y": ylab,"b":"Buildings"})
    xmin = preatoFrontier['x'].min()
    ymin = preatoFrontier['y'].min()
    xmax = preatoFrontier['x'].max()
    ymax = preatoFrontier['y'].max()
    xmid = (xmax-xmin)/2
    ymid = (ymax-ymin)/2
    stats_df['Variable'] = [xlab,ylab]
    stats_df['minimum'] = [xmin,ymin,]
    stats_df['midpoint'] = [xmid,ymid]
    stats_df['maximum'] = [xmax,ymax]
    stats_df['mean'] = [statistics.mean(preatoFrontier['x']),statistics.mean(preatoFrontier['y'])]
    stats_df['SD'] = [statistics.pstdev(preatoFrontier['x']),statistics.pstdev(preatoFrontier['y'])]
    stats_df['Variance'] = [statistics.pvariance(preatoFrontier['x']),statistics.pvariance(preatoFrontier['y'])]
    
 
  
# solutionRow = preatoFrontier.loc[(preatoFrontier['x'] == xCoord)&(preatoFrontier['y'] == yCoord)&(preatoFrontier['z'] == zCoord)]

# solId = int(solutionRow['SolId'])

# solution = td.getSolution(solutions, solId)     


#-------------------------
# xCoord = 153
# yCoord = 609
# zCoord = 882

# solutionRow = preatoFrontier.loc[(preatoFrontier['x'] == xCoord)&(preatoFrontier['y'] == yCoord)&(preatoFrontier['z'] == zCoord)]

# solId = int(solutionRow['SolId'])

# #solId = 49

# solution = td.getSolution(solutions, solId)       

# color = []
# for row in solution['upGrade']:
#     if row == 0:
#         color.append('grey')
#     if row == 1:
#         color.append('green')
#     if row == 2:
#         color.append('blue')
#     if row == 3:
#         color.append('red')

# solution['color'] = color


#--------------------------
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
    
    maps = html.Div(
            dbc.Container([
                
                
                    dbc.Row([
                        dbc.Col(
                           dcc.Graph(id='map'),
                           width = {"size": 6, "offset": -5},
                        ),
                    ])
    
                ])
        
        )
    MainContainer = ThreeContainer
    
else:
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
    
    maps = html.Div(
            dbc.Container([
                
                
                    dbc.Row([
                        dbc.Col(
                           dcc.Graph(id='2dmap'),
                           width = {"size": 6, "offset": -5},
                        ),
                    ])
    
                ])
        
        )
    MainContainer = TwoContainer

left_col = dbc.Row(
    [
        dbc.Col([
            MainContainer,
            maps
        ]),
        dbc.Col([
                    html.H6("Statistics over solution set"),
                    dbc.Table.from_dataframe(stats_df,striped=True,bordered=True,hover=True)

                 ]),
    ]
)

app.layout = dbc.Container([
    dbc.Row([
        jumbotron
        ]),
        left_col

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
            
            type1 = type(xCoord)
            
            #add flush = True or it wont display the message.
            print(f'Selected [{xCoord},{yCoord},{zCoord}]',flush=True)
           
            return "Selected : [{},{},{}, type is :{}]".format(xCoord,yCoord,zCoord,type1)
        
        
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
            
@app.callback(
    Output('map','figure'),
    Input('graph', 'clickData'))
# =============================================================================
#   Block 11: Callback Function
# =============================================================================
def update_map(clickData):
    # insert your own mapbox token
    mapbox_access_token = 'pk.eyJ1IjoicHJvbWFjaG9zIiwiYSI6ImNsNG5hYjkyYjFhZXYzanA0cTVwNjA3dm4ifQ.pcuIpf5FRuFB7SxT8k05Xw'
    
# =============================================================================
#     P1. Render Map when no point is clicked
# =============================================================================
    # If No point has been clicked
    if clickData is None:
        
        maps = go.Figure(go.Scattermapbox(
            lat=coords['lat'], # set lat and long
            lon=coords['long'],
            mode='markers', 
            marker =({'size':5.5}) # make markers size variable 
        ))
    
        # set up map layout
        
        maps.update_layout(
            autosize=True, # Autosize
            hovermode='closest', # Show info on the closest marker
            showlegend=True, # show legend of colors
            mapbox=dict(
                accesstoken=mapbox_access_token, # token
                bearing=0, # starting facing direction
                # starting location
                center=dict(
                    lat=td.cLat,
                    lon=td.cLong
                ),
                #angle and zoom
                pitch=0,
                zoom=12
            ),
            #height and width
            width=1000,
            height=1000
        )
        return maps
    else:

       
        xCoord = int(clickData['points'][0]['x'])
        yCoord = int(clickData['points'][0]["y"])
        zCoord = int(clickData['points'][0]["z"])
        
        
        solutionRow = preatoFrontier.loc[(preatoFrontier['x'] == xCoord)&(preatoFrontier['y'] == yCoord)&(preatoFrontier['z'] == zCoord)]

        solId = int(solutionRow['SolId'])

        #solId = 49

        solution = td.getSolution(solutions, solId)       

        color = []
        for row in solution['upGrade']:
            if row == 0:
                color.append('grey')
            if row == 1:
                color.append('green')
            if row == 2:
                color.append('blue')
            if row == 3:
                color.append('red')

        solution['color'] = color
        
        #print(f'solution id is {solId}',flush=True)
        # get the rows that coorespond to that solution ID
        
        
        # render the map with the new solution data        
        maps = go.Figure(go.Scattermapbox(
            lat=solution['lat'],
            lon=solution['long'],
            mode='markers', 
            #marker =({'color':solution['color']},{'size':5.5})
            
            marker=dict(
                        size=12,
                        color=solution['color'], #set color equal to a variable
                        colorscale='Viridis', # one of plotly colorscales
                        showscale=True
                    )

        ))
        
#=============================================================================
# P3. Map Layout
#=============================================================================
        
        #set up map layout
        maps.update_layout(
            autosize=True, # Autosize
            hovermode='closest', # Show info on the closest marker
            showlegend=True, # show legend of colors
            mapbox=dict(
                accesstoken=mapbox_access_token, # token
                bearing=0, # starting facing direction
                # starting location
                center=dict(
                    lat=td.cLat,
                    lon=td.cLong
                ),
                #angle and zoom
                pitch=0,
                zoom=10
            ),
            #height and width
            width=1000,
            height=1000
        )

        return maps
        
         
@app.callback(
    Output('2dmap','figure'),
    Input('2dgraph', 'clickData'))
# =============================================================================
#   Block 11: Callback Function
# =============================================================================
def update_map_2d(clickData):
    # insert your own mapbox token
    mapbox_access_token = 'pk.eyJ1IjoicHJvbWFjaG9zIiwiYSI6ImNsNG5hYjkyYjFhZXYzanA0cTVwNjA3dm4ifQ.pcuIpf5FRuFB7SxT8k05Xw'
    
# =============================================================================
#     P1. Render Map when no point is clicked
# =============================================================================
    # If No point has been clicked
    if clickData is None:
        #make a map
        maps = go.Figure(go.Scattermapbox(
            lat=coords['lat'], # set lat and long
            lon=coords['long'],
            mode='markers', 
            marker =({'size':5.5}) # make markers size variable 
        ))
    
        # set up map layout
        maps.update_layout(
            autosize=True, # Autosize
            hovermode='closest', # Show info on the closest marker
            showlegend=True, # show legend of colors
            mapbox=dict(
                accesstoken=mapbox_access_token, # token
                bearing=0, # starting facing direction
                # starting location
                center=dict(
                    lat=td.cLat,
                    lon=td.cLong
                ),
                #angle and zoom
                pitch=0,
                zoom=12
            ),
            #height and width
            width=1000,
            height=1000
        )
        return maps
    else:

       
        xCoord = int(clickData['points'][0]['x'])
        yCoord = int(clickData['points'][0]["y"])
        
        
        
        solutionRow = preatoFrontier.loc[(preatoFrontier['x'] == xCoord)&(preatoFrontier['y'] == yCoord)]

        solId = int(solutionRow['SolId'])

        #solId = 49

        solution = td.getSolution(solutions, solId)       

        color = []
        for row in solution['upGrade']:
            if row == 0:
                color.append('grey')
            if row == 1:
                color.append('green')
            if row == 2:
                color.append('blue')
            if row == 3:
                color.append('red')

        solution['color'] = color
        
        #print(f'solution id is {solId}',flush=True)
        # get the rows that coorespond to that solution ID
        
        
        # render the map with the new solution data        
        maps = go.Figure(go.Scattermapbox(
            lat=solution['lat'],
            lon=solution['long'],
            mode='markers', 
            #marker =({'color':solution['color']},{'size':5.5})
            
            marker=dict(
                        size=12,
                        color=solution['color'], #set color equal to a variable
                        colorscale='Viridis', # one of plotly colorscales
                        showscale=True
                    )

        ))
        
#=============================================================================
# P3. Map Layout
#=============================================================================
        
        #set up map layout
        maps.update_layout(
            autosize=True, # Autosize
            hovermode='closest', # Show info on the closest marker
            showlegend=True, # show legend of colors
            mapbox=dict(
                accesstoken=mapbox_access_token, # token
                bearing=0, # starting facing direction
                # starting location
                center=dict(
                    lat=td.cLat,
                    lon=td.cLong
                ),
                #angle and zoom
                pitch=0,
                zoom=10
            ),
            #height and width
            width=1000,
            height=1000
        )

        return maps
        
  
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
    
    