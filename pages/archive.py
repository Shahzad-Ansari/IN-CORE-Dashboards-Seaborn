# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:02:13 2022

@author: ShahzadAnsari
"""

import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our Archive page'),

    html.Div(children='''
        This is our Archive page content.
    '''),

])