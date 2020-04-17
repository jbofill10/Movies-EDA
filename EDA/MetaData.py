import plotly.express as px
import plotly.graph_objs as go

def metadata_eda(meta_df, ratings_df):

    fig = px.scatter(meta_df, x='budget', y='revenue', hover_data=['title'], color='genres', width=1200, height=800)
    fig.update_layout(
        title='The Relationship between Budget and Revenue',
        xaxis_title='Budget',
        yaxis_title='Revenue',
        font=dict(
            size=16
        )
    )
    fig.show()

    genre_budget_df = meta_df.groupby(['genres'])['budget'].sum()

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
        width=1200,
        height=800,
        font=dict(
            size=16
        )
    )

    fig.layout.template = 'seaborn'


    fig.show()

    fig = px.scatter(meta_df, x='budget', y='runtime', hover_data=['title'], color='genres', width=1200, height=800)
    fig.update_layout(
        title='The Relationship between Budget and Movie Runtime',
        xaxis_title='Budget',
        yaxis_title='Runtime',
        font=dict(
            size=16
        )
    )
    fig.show()

    fig = px.scatter(meta_df, x='runtime', y='revenue', hover_data=['title'], color='genres', width=1200, height=800)
    fig.update_layout(
        title='The Relationship between Runtime and Movie Revenue',
        xaxis_title='Runtime',
        yaxis_title='Revenue',
        font=dict(
            size=16
        )
    )
    fig.show()

    fig = go.Figure(go.Box(
        y=meta_df['vote_count']
    ))

    fig.update_layout(
        title='Vote Count Distribution',
        yaxis_title='Vote Count',
        width=1200,
        height=800
    )
    fig.show()

    quart_df = meta_df[meta_df['vote_count'] >= 58]
    fig = go.Figure(go.Box(
        y=quart_df['vote_count']
    ))

    fig.update_layout(
        title='Vote Count Distribution',
        yaxis_title='Vote Count',
        width=1200,
        height=800
    )

    fig.show()




