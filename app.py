# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:51:16 2022

@author: ShahzadAnsari
"""

from dash import Dash, html, dcc, Input, Output,dash_table
import dash_bootstrap_components as dbc
import dash
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
            dbc.Col(html.Div(html.H1("Second Table goes here")))
            
        ])
        
    ])
    
    
    
)



app.layout = dbc.Container([
    jumbotron,
    other 
],fluid=True)

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


@app.callback(
    Output('repair', component_property='children'),
    Output('dislocation', component_property='children'),
    Output('eloss', 'children'),
    Input('year-radio', 'value'),
    Input('budget-radio', 'value'))
def set_display_children(year, budget):
    if year == '500 Years':
        if budget == '20% Budget Option':
            a = f'Range of Repair Time: {min(pr.func_500optimal20)} , {max(pr.func_500optimal20)} '
            b = f'Range of Population Dislocation: {min(pr.dislocation_500optimal20)} , {max(pr.dislocation_500optimal20)}'
            c = f'Range of Economic loss($Million Dollar): {min(pr.loss_500optimal20)} , {max(pr.loss_500optimal20)}'
        elif budget == '40% Budget Option':
            a = f'Range of Repair Time: {min(pr.func_500optimal40)} , {max(pr.func_500optimal40)} '
            b = f'Range of Population Dislocation: {min(pr.dislocation_500optimal40)} , {max(pr.dislocation_500optimal40)}'
            c = f'Range of Economic loss($Million Dollar): {min(pr.loss_500optimal40)} , {max(pr.loss_500optimal40)}'
        elif budget == '60% Budget Option':
            a = f'Range of Repair Time: {min(pr.func_500optimal60)} , {max(pr.func_500optimal60)} '
            b = f'Range of Population Dislocation: {min(pr.dislocation_500optimal60)} , {max(pr.dislocation_500optimal60)}'
            c = f'Range of Economic loss($Million Dollar): {min(pr.loss_500optimal60)} , {max(pr.loss_500optimal60)}'
    elif year == '1000 Years':
        if budget == '20% Budget Option':
            a = f'Range of Repair Time: {min(pr.func_1000optimal20)} , {max(pr.func_1000optimal20)} '
            b = f'Range of Population Dislocation: {min(pr.dislocation_1000optimal20)} , {max(pr.dislocation_1000optimal20)}'
            c = f'Range of Economic loss($Million Dollar): {min(pr.loss_1000optimal20)} , {max(pr.loss_1000optimal20)}'
        elif budget == '40% Budget Option':
            a = f'Range of Repair Time: {min(pr.func_1000optimal40)} , {max(pr.func_1000optimal40)} '
            b = f'Range of Population Dislocation: {min(pr.dislocation_1000optimal40)} , {max(pr.dislocation_1000optimal40)}'
            c = f'Range of Economic loss($Million Dollar): {min(pr.loss_1000optimal40)} , {max(pr.loss_1000optimal40)}'
        elif budget == '60% Budget Option':
            a = f'Range of Repair Time: {min(pr.func_1000optimal60)} , {max(pr.func_1000optimal60)} '
            b = f'Range of Population Dislocation: {min(pr.dislocation_1000optimal60)} , {max(pr.dislocation_1000optimal60)}'
            c = f'Range of Economic loss($Million Dollar): {min(pr.loss_1000optimal60)} , {max(pr.loss_1000optimal60)}'
    return a,b,c

@app.callback(
        Output('metricsNoSol','children'),
        Input('year-radio','value'),
    )
def setmetricsNoSol(year):
    return html.H6(f'{year} Event community Metrics without any Strategy')


@app.callback(
        Output('Yr500','children'),
        Input('year-radio','value'),
    )
def setmetricsNoSol(year):
    if year == '500 Years':
        df = pr.Yr500
        return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    else:
        df = pr.Yr1000
        return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

if __name__ == '__main__':
    app.run_server(debug=True)


# if (values is not None and len(values) != 0) and (col_name_list is not None and len(col_name_list) != 0):
#         log_mssg = [html.P(log_mssg + str(dict(zip(col_name_list, i))).replace('{', '').replace('}', '')) for i in values]
#         current_time = [html.P(current_time)] + log_mssg



# app.layout = html.Div([
#     #  html.Div([
#     #     html.H2("Seaborn IN-CORE Dashbord App"),
#     #     html.Img(src="/assets/incore-logo.png")
#     # ], className="banner")
   
#     html.Div([html.H1("Seaborn IN-CORE Dashbord App")]),
#     html.Div([html.H4("Select what budget you want to analyze")]),
#     dcc.Dropdown(['20% Budget Option', '40% Budget Option','60% Budget Option'], '20% Budget Option', id='budget-dropdown'),
#     dcc.RadioItems(['500 years','1000 years'],'500 years',id = 'year-selector'),
#     html.Div(html.Hr()),
#     html.Div(id='repair'),
#     html.Div(id='dislocation'),
#     html.Div(id='eloss'),
   
# ])




# @app.callback(
#         Output('eloss','children'),
#         Input('year-selector','value'),
#     )
# def setYear(year):
#     return year


# @app.callback(
#             #Output('repair', component_property='children'),
#             #Output('dislocation', component_property='children'),
#             Output('eloss', component_property='children'),
#             #Input('budget-dropdown',component_property = 'value'),
#             Input('eloss','options'),
#         )
# def displayRanges(year):
#     return f'{year}'
#     # if year == '500 years':
#     #     if input_value == '20% Budget Option':
#     #         repairTime = f'Range of Repair Time: {min(pr.func_500optimal20)} , {max(pr.func_500optimal20)} '
#     #         dislocaiton = f'Range of Population Dislocation: {min(pr.dislocation_500optimal20)} , {max(pr.dislocation_500optimal20)}'
#     #         eloss = f'Range of Economic loss($Million Dollar): {min(pr.loss_500optimal20)} , {max(pr.loss_500optimal20)}'
#     #         return repairTime, dislocaiton, eloss
#     #     elif input_value == '40% Budget Option':
#     #         repairTime = f'Range of Repair Time: {min(pr.func_500optimal20)} , {max(pr.func_500optimal20)} '
#     #         dislocaiton = f'Range of Population Dislocation: {min(pr.dislocation_500optimal20)} , {max(pr.dislocation_500optimal20)}'
#     #         eloss = f'Range of Economic loss($Million Dollar): {min(pr.loss_500optimal20)} , {max(pr.loss_500optimal20)}'
#     #     elif input_value == '60% Budget Option':
#     #         repairTime = f'Range of Repair Time: {min(pr.func_500optimal20)} , {max(pr.func_500optimal20)} '
#     #         dislocaiton = f'Range of Population Dislocation: {min(pr.dislocation_500optimal20)} , {max(pr.dislocation_500optimal20)}'
#     #         eloss = f'Range of Economic loss($Million Dollar): {min(pr.loss_500optimal20)} , {max(pr.loss_500optimal20)}'

# def set_display_children(year, budget):
#     if year == '500 Years':
#         if budget == '20% Budget Option':
#             a = '1'
#             b = 'a'
#             c = 'a'
#         elif budget == '40% Budget Option':
#             a = '2'
#             b = 'a'
#             c = 'a'
#         elif budget == '60% Budget Option':
#             a = '3'
#             b = 'a'
#             c = 'a'
#     elif year == '1000 Years':
#         if budget == '20% Budget Option':
#             a = '4'
#             b = 'a'
#             c = 'a'
#         elif budget == '40% Budget Option':
#             a = '5'
#             b = 'a'
#             c = 'a'
#         elif budget == '60% Budget Option':
#             a = '6'
#             b = 'a'
#             c = 'a'
#     return a,b,c
