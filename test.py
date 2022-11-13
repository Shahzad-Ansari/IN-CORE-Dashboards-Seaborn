# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:30:05 2022

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


#(loss_500optimal60,dislocation_500optimal60,c=func_500optimal60,cmap =plt.cm.get_cmap('Blues', 10))




all_options = {
    '500 Years': ['20% Budget Option', '40% Budget Option','60% Budget Option'],
    '1000 Years': ['20% Budget Option', '40% Budget Option','60% Budget Option']
}

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
        
        
        html.Hr(),
        html.Div([html.H6("Select what budget and projected year you want to analyze")]),   
        dbc.Row([
            
            dbc.Col(dcc.Dropdown(id='budget-radio',clearable=False)),
            dbc.Col(
                dcc.RadioItems(
                    list(all_options.keys()),
                    '500 Years',
                    id='year-radio',
                )
            ),
        ]),
        
        dcc.Graph(
            id='graph',
            figure=fig
        ),
        
        html.Hr(),
        html.Div(id='repair'),
        html.Div(id='dislocation'),
        html.Div(id='eloss'),
        html.Hr(),
        
        dbc.Row([
            dbc.Col([
                html.Div(id = 'metricsNoSol'), 
                html.Div(id = 'Yr500')   
            ]),
        ]),
        
        dbc.Row([
            dbc.Col([
                html.Div(id = 'metricsWBudget'), 
                html.Div(id = 'Budget1')   
            ]),
        ]),
        dbc.Row([
              dbc.Col(
                  img,width = {"size": 15, "order": "last", "offset": 0}
                    
              )
        ]),
        

    ])
    
    
    
)

@app.callback(
    Output('budget-radio', 'value'),
    Input('budget-radio', 'options'))
def set_budget_value(available_options):
    return available_options[0]['value']





app.layout = dbc.Container([
    jumbotron,
    other 
],style={"overflowY":"scroll",'height':"1500px"},fluid=True)











