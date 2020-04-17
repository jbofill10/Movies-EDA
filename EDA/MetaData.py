import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import numpy as np

def metadata_eda(meta_df, ratings_df):

    '''fig = px.scatter(meta_df, x='budget', y='revenue', hover_data=['title'], color='genres', width=1600, height=800)
    fig.update_layout(
        title='The Relationship between Budget and Revenue',
        xaxis_title='Budget',
        yaxis_title='Revenue',
        font=dict(
            size=16
        )
    )
    fig.show()'''


    genre_budget_df = meta_df.groupby(['genres'])['budget'].sum()

    print(genre_budget_df.shape)

    fig = go.Figure([
        go.Bar(
            x=genre_budget_df.index,
            y=genre_budget_df.values,
            text=genre_budget_df.values,
            textposition='auto',
            marker_color=['#94447f',
                          '#5796ef',
                          '#8a59c0',
                          '#288abf',
                          '#0ab78d',
                          '#4ed993',
                          '#7d3970',
                          '#b3dc67',
                          '#dc560a',
                          '#0079fe',
                          '#98d3a8',
                          '#d5105a',
                          '#d04dcf',
                          '#58c7a2',
                          '#7bf1f8',
                          '#244155',
                          '#587b77',
                          '#c64ac2',
                          '#5e805d',
                          '#ebab95']
        )])

    fig.update_layout(
        title='Sum of all Movie Budgets in each Genre',
        xaxis_title='Genre',
        yaxis_title='Total Budget',
        width=1600,
        height=800,
        font=dict(
            size=16
        )
    )

    fig.layout.template = 'seaborn'


    fig.show()


