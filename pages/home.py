# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:50:19 2022

@author: ShahzadAnsari
"""

import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is our Home page content.
    '''),

])