# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:01:52 2022

@author: ShahzadAnsari
"""
from dash import Dash, html, dcc, Input, Output,dash_table
import dash_bootstrap_components as dbc
import dash
import plotly.graph_objects as go
import plotting_results as pr


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
    },)

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
                    html.Div("Seaborn IN-CORE Dashbord App", className="display-5"),
                    width = "auto"
                ),
                dbc.Col(card,width = {"size": 3, "order": "last", "offset": 3})
            ],justify ="between"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.P(
                "Data visualization dashboard for Seaborn. Model created by XXXXX Visualizations created by Shahzad Ansari",
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
        html.Div([html.H6("Select what budget and projected year you want to analyze")]),   
        dbc.Row([
            
            dbc.Col(dcc.Dropdown(id='budget-radio',clearable=False)),
            dbc.Col(
                dcc.RadioItems(
                    list(all_options.keys()),
                    year_1,
                    id='year-radio',
                )
            ),
        ]),
        
        dcc.Graph(
            id='graph'
        ),
        
        html.Hr(),
        html.Div(id='repair'),
        html.Div(id='dislocation'),
        html.Div(id='eloss'),
        html.Hr(),
        
        dbc.Row([
            dbc.Col([
                html.Div(id = 'metricsNoSol'), 
                html.Div(id = 'noSolutionDf')   
            ]),
        ]),
        
        dbc.Row([
            dbc.Col([
                html.Div(id = 'metricsWBudget'), 
                html.Div(id = 'Budget1')   
            ]),
        ]),  
    ])
)

app.layout = dbc.Container([
    jumbotron,
    other 
],style={"overflowY":"scroll",'height':"1500px"},fluid=True)



# NoSolutionDF
def getNoSolDF(year):
    # get the noSolution Data given the year could be a csv or a function call to another notebook/package
    
# preatoFrontier
#   -x: repair
#   -y: dislocation
#   -z: eloss


# objective funciton make it generic it may not have repair etc, just make it x y and z. 
# option to wher eyou have a contour plot of the surface frotnier looks like multiple lines , each line has a different dislocaiton. look up contour plot. 2d mul
# format leg  4 dec places. find average between max and min  point and give + - amount. 
# get in contact with samual - s.rodriguez@ou.edu
# remove budget year etc
# connect w samual data priority 1 
# be able to right click on a point and save solution data as csv priority 2

# if 2 obj 2 plot if 3 3d plot
# number of obj should cascasde thorugh the rest
# pass in name of objs to refelct on screen
# clicking on datapoint and get summary data. summarization happen on my side

# def getFrontier(year,budget):
#     # get the frontier for year, budget 
#     # returns df with x,y,z dims for the frontier


# # function to get ranges of the dimensions in the forntier
# def getRanges(preatoFrontier):
#     repairMin = min(preatoFronter[x])
#     repairMax = max(preatoFronter[x])
#     dislocationMin = min(preatoFronter[y])
#     dislocationMax = max(preatoFronter[y])
#     repairMin = min(preatoFronter[z])
#     repairMax = max(preatoFronter[z])
#     return repairMin,repairMax,dislocationMin,dislocationMax,repairMin,repairMax
    

# # Bulding Data with lat and long coords
# def getCoords(x,y,z):
#     # need to get coordinate and the repair  data given the solution to test will just randomly generate. 

@app.callback(
    Output('graph','figure'),
    Input('year-radio', 'value'),
    Input('budget-radio', 'value')
    
    )
def updateGraph():
    fig = go.Figure() # create a figure
    
    #Depending on how many years and budgets you have you may need to add or remove based on the amount you declared above.
    # within each create a df called fronterPoints with the x,y and z of each points. How you get the points up to you. You can call a method from another program or you can pull in a csv. 
    if year == year_1:
        if budget == budget_1:
            pass
        elif budget == budget_2:
            pass
        elif budget == budget_3:
            pass
            
    elif year == year_2:
        if budget == budget_1:
            pass
        elif budget == budget_2:
            pass
        elif budget == budget_3:
            pass
            
   
    fig.add_trace(go.Scatter3d(
                x = frontierPoints[x], # x dim for scatter plot
                y = frontierPoints[y], # y dim for scatter plot
                z = frontierPoints[z], # z dim for scatter plot
                mode = 'markers', # type of points on scatterplot
                name = 'markers', # name of the points on the scatterplot
                # settings for the scatterplot
                marker=dict(
                    size=10, # The size of the markers are set by this 
                    color=frontierPoints[x], # set color to an array/list of desired values
                    colorscale='Viridis',   # choose a colorscale
                    opacity=0.8 # opacity 
                )
            ))
        
    # 3D Scatter plot 
    fig.update_layout(clickmode='event+select') #What happens when you click on a point
    # titles and dimensions
    fig.update_layout(scene = dict(
                        xaxis_title='Economic Loss',
                        yaxis_title='Functionality',
                        zaxis_title='Dislocation'),
                        title="Preto Frontier",
                        width=1200,
                        height=900)
    
    return fig
           
@app.callback(
    Output('budget-radio', 'options'),
    Input('year-radio', 'value'))
def set_budget_options(year):
    return [{'label': i, 'value': i} for i in all_options[year]]

@app.callback(
    Output('budget-radio', 'value'),
    Input('budget-radio', 'options'))
def set_budget_value(available_options):
    return available_options[0]['value']

#--------------------------------------------------------------------------------

@app.callback(
    Output('repair', component_property='children'),
    Output('dislocation', component_property='children'),
    Output('eloss', 'children'),
    Input('year-radio', 'value'),
    Input('budget-radio', 'value'))
def set_display_children(year, budget):
    
    preatoFronter = getFronter(year,budget)
    repairMin,repairMax,dislocationMin,dislocationMax,repairMin,repairMax = getRanges(preatoFrontier)
    
    a = f'Range of Repair Time: {repairMin} , {repairMax} '
    b = f'Range of Population Dislocation: {dislocationMin} , {dislocationMax}'
    c = f'Range of Economic loss($Million Dollar): {repairMin} , {repairMax}'
    
    return a,b,c

@app.callback(
        Output('metricsNoSol','children'),
        Input('year-radio','value'),
    )
def setmetricsNoSol(year):
    return html.H6(f'{year} Event community Metrics without any Strategy')

@app.callback(
        Output('metricsWBudget','children'),
        Input('year-radio','value'),
    )
def setmetricsNoSol(year):
    return html.H6(f'{year} Event soultion with budget')

#--------------------------------------------------------------------------------
# Need to add a no solution DF
@app.callback(
        Output('noSolutionDf','children'),
        Input('year-radio','value'),
    )
def setmetricsNoSol(year):
        df = noSolutionDf
        return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    

#--------------------------------------------------------------------------------
@app.callback(
        Output('Budget1','children'),
        Input('year-radio', 'value'),
        Input('budget-radio', 'value'),
        Input('graph','clickData')
    )
def setbudgetDf(year,budget,clickData):
    
    
    if clickData is None: 
        # replace with default dataframe. 
        #df = pr.getData( 197508874.2, 2338.789178, 166.5928389, year_1 ,budget_1)
    else:
        Econ = clickData['points'][0]['x'] 
        Dis = clickData['points'][0]["y"]
        Func = clickData['points'][0]["z"]
        
        #df with x, y, and z points along with repairtime, number of retrofitted buildings, number of each retrofitted to each option. S 
        
        #df = pr.getData( Econ, Dis, Func, year,budget)
        
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    
#--------------------------------------------------------------------------------    
@app.callback(
    Output('result','children'),
    Input('graph', 'clickData'))
def show_coords(clickData):

        if clickData is None: 
            return "no clickdata chosen"
        else:
            xCoord = clickData['points'][0]['x'] 
            yCoord = clickData['points'][0]["y"]
            zCoord = clickData['points'][0]["z"]
            
            #add flush = True or it wont display the message.
            print(f'xcoord is {xCoord} and ycoord is {yCoord} and zcord is {zCoord}',flush=True)
           
            return "xcoord is {} and ycoord is {} and zcord is {}".format(xCoord,yCoord,zCoord)
        
#--------------------------------------------------------------------------------        
      
if __name__ == '__main__':
    app.run_server(debug=True)



