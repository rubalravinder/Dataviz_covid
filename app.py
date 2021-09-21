# IMPORT MODULES

import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
import plotly.express as px

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app = dash.Dash(__name__)

# paramètres généraux de la page web
colors = {
    'background': '#9fc0c0',
    'text': '#000000'
}


# création du dataframe
df = pd.read_csv('./data/donnees-hospitalieres-covid19-2021-09-20-19h05.csv', sep=';')
# colonne jour as a datetime
df.jour = pd.to_datetime(df.jour)


# création d'un bar plot avec plotly express
# fig = px.bar(df, x="jour", y="dc", color="dep", barmode="group")

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

# création du layout de la page web
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # écrit le text en gras
    html.H1(
        children='Dashboard - donnees hospitalieres sur le COVID-19',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    
    # écrit un texte
    html.Div(children='Periode : du 18 mars 2020 au 20 septembre 2021', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    # ajoute une figure
    # dcc.Graph(
    #     id='example-graph-2',
    #     figure=fig
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True) # rafraichit automatiquement la page web quand une modif est faite
