# IMPORT MODULES

import dash
from dash import dcc
from dash import html
import plotly.express as px

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

app = dash.Dash(__name__)

# paramètres généraux de la page web
colors = {
    'background': '#9fc0c0',
    'text': '#000000'
}


# création du dataframe
df = pd.read_csv('./data/donnees-hospitalieres-covid19-2021-09-20-19h05.csv', sep=';')
# colonne jour as a datetime et en index
df.jour = pd.to_datetime(df.jour)
df= df.set_index('jour')
df.drop(['rad','hosp','rea'],axis=1)


# Création d'un bar plot avec plotly express

d=df.pivot_table(index='dep', columns='sexe', values='dc')
d['per_cent_h']= round(d[1] * 100/ d[0],1)
d=d.sort_values('per_cent_h', ascending=False)

fig = px.bar(d, y="per_cent_h", x=d.index, barmode="group", color_discrete_sequence =['black']*len(df))


for data in fig.data:
    data["width"] = 0.8 #Change this value for bar widths
fig.update_layout(
                width=1600, height=500, bargap=0.1,
                plot_bgcolor=colors['background'],
                paper_bgcolor=colors['background'],
                font_color=colors['text'])


# Création d'un line chart avec plotly express

df1 = df[df.sexe==0].groupby ('jour')['dc'].sum()

fig1 = px.line(df1, title='Nombre cumulé des décès')

fig1.update_layout(
                plot_bgcolor=colors['background'],
                paper_bgcolor=colors['background'],
                font_color=colors['text'])

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
    html.Div(children='Pourcentage de personnes de sexe masculin décédées du COVID par département sur toute la période', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    # ajoute une figure
    dcc.Graph(
        id='graph-ratio-homme',
        figure=fig
     ),

    # ajoute une 2e figure
    html.Div([
            dcc.Graph(
                id='graph-deces-tps',
                figure=fig1
            )  
        ]),
    ])


if __name__ == '__main__':
    app.run_server(debug=True) # rafraichit automatiquement la page web quand une modif est faite
