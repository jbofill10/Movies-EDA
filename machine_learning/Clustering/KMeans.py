from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
from plotly.offline import iplot


def do_Kmeans(df):
    scaled_df = df[['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count']]

    smaller_df = scaled_df.copy()

    scalar = MinMaxScaler()

    scaled = scalar.fit_transform(df[['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count']])

    scaled_df = pd.DataFrame(scaled, index=scaled_df.index, columns=scaled_df.columns)

    if not os.path.isfile('Data/pickles/kmeans_pickle'):
        # Get optimal K
        clusters = param_tune(scaled_df)

        scaled_df = apply_kmeans(scaled_df, clusters)

        scaled_df.to_pickle('Data/pickles/kmeans_pickle')
    else:
        scaled_df = pd.read_pickle('Data/pickles/kmeans_pickle')

    smaller_df = smaller_df.join(scaled_df[['cluster_label', 'cluster_string']])

    smaller_df = smaller_df.join(df[['title', 'genres']])

    kmeans_eda(smaller_df)


def param_tune(df):
    scores = {'clusters': list(), 'score': list()}
    for cluster_num in range(1, 31):
        scores['clusters'].append(cluster_num)
        scores['score'].append(KMeans(n_clusters=cluster_num, verbose=1, random_state=0).fit(df).score(df))

    scores_df = pd.DataFrame(scores)

    fig = go.Figure(go.Scatter(
        x=scores_df['clusters'],
        y=scores_df['score']
    ))

    fig.update_layout(
        xaxis_title='Cluster',
        yaxis_title='Score',
        title='Elbow Method Results',
        height=800,
        width=1200
    )

    fig.show()

    return 9


def apply_kmeans(df, clusters):
    kmeans = KMeans(n_clusters=clusters, verbose=1, random_state=0)
    cluster_labels = kmeans.fit(df).labels_
    string_labels = ["c{}".format(i) for i in cluster_labels]
    df['cluster_label'] = cluster_labels
    df['cluster_string'] = string_labels

    return df


'''Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 
'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 
'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 
'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 
'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 
'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 
'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 
'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 
'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 
'bwr', 'bwr_r', 'cividis', 'cividis_r',
'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 
'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 
'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 
'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 
'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 
'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 
'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 
'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 
'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 
'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 
'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r'''


def kmeans_eda(df):
    # Cluster Cardinality
    style.use('seaborn-poster')
    '''fig, ax = plt.subplots(1,1)
    cluster_comb = df.groupby(['cluster_label'])['title'].count().sort_values(ascending=False)
    sns.barplot(y=cluster_comb.index, x=cluster_comb.values, orient='h', palette="Spectral",
                edgecolor='black', linewidth=1)
    plt.ylabel("Cluster", fontsize=18)
    plt.xlabel("Records", fontsize=18)
    plt.title("Records in Each Cluster", fontsize=20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.savefig('Charts/Cluster_Record_Count.png')
    plt.show()

    # Scatter Matrix

    fig = px.scatter_matrix(df, dimensions=['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 'vote_count'],
                            color='cluster_string', hover_data=['title', 'genres'])
    fig.update_layout(
        title='Cluster Scatter Matrix',
        height=1000,
        width=1900
    )
    iplot(fig)'''

    '''['budget', 'popularity', 'revenue', 'runtime', 'vote_average', 
    'vote_count', 'cluster_label', 'cluster_string', 'title', 'genres']'''

    # Clusters and Genres EDA

    '''clusters = list(df['cluster_label'].unique())
    cluster_dict = dict()
    cluster_count = 0
    for col in range(3):
        for row in range(3):
            cluster_df = df[df.cluster_label == clusters[cluster_count]]
            cluster_dict["{},{}".format(str(col), str(row))] = cluster_df['genres'].value_counts()
            cluster_count += 1

    cluster_count = 0

    fig, axs = plt.subplots(3, 3, figsize=(15,15))

    for col in range(3):
        for row in range(3):
            coord = "{},{}".format(str(col), str(row))

            sns.barplot(y=cluster_dict[coord].index, x=cluster_dict[coord].values, orient='h',
                        palette={'Drama': '#94447f',
                                 'Action': '#5796ef',
                                 'Adventure': '#8a59c0',
                                 'Comedy': '#288abf',
                                 'Crime': '#0ab78d',
                                 'Thriller': '#4ed993',
                                 'Fantasy': '#7d3970',
                                 'Horror': '#b3dc67',
                                 'Science Fiction': '#dc560a',
                                 'Animation': '#0079fe',
                                 'Romance': '#98d3a8',
                                 'Mystery': '#d5105a',
                                 'Family': '#d04dcf',
                                 'War': '#58c7a2',
                                 'History': '#7bf1f8',
                                 'Western': '#244155',
                                 'TV Movie': '#587b77',
                                 'Music': '#c64ac2',
                                 'Documentary': '#5e805d',
                                 'Foreign':'#e28872'}, edgecolor='black', linewidth=0.9, ax=axs[col][row])

            title = "Cluster {}'s Genre Distribution".format(cluster_count)
            axs[col][row].set_title(title, fontsize=15, fontweight='bold')
            cluster_count += 1

    plt.tight_layout()

    plt.savefig('Charts/ClustersGenreDist', bbox_inches='tight')

    plt.show()'''

    # Revenue Drama in Clusters
    drama_df = df[(df.genres == 'Drama') & (df.cluster_label.isin([0, 1, 2, 5]))]
    drama_df = drama_df.sort_values('cluster_label')
    '''fig = px.violin(drama_df, y='revenue', x='cluster_string', color='cluster_string', points='all', hover_data=drama_df)

    fig.update_layout(
        title='Revenue Distribution in Drama Movies',
        yaxis_title='Revenue',
        xaxis_title='Cluster',
        height=1000,
        width=1500
    )

    iplot(fig)

    fig = px.violin(drama_df, y='vote_average', x='cluster_string',
                    color='cluster_string', points='all', hover_data=drama_df)

    fig.update_layout(
        title='Vote Average Distribution in Drama Movies',
        yaxis_title='Vote Average',
        xaxis_title='Cluster',
        height=1000,
        width=1500
    )
    
    iplot(fig)

    drama_df = df[(df.genres == 'Drama')]
    drama_df = drama_df.sort_values('cluster_label')
    fig = px.violin(drama_df, y='vote_average', x='cluster_string',
                    color='cluster_string', points='all', hover_data=drama_df)

    fig.update_layout(
        title='Vote Average Distribution in Drama Movies',
        yaxis_title='Vote Average',
        xaxis_title='Cluster',
        height=1000,
        width=1500
    )

    iplot(fig)'''

    drama_df = df
    drama_df = drama_df.sort_values('cluster_label')
    fig = px.violin(drama_df, y='vote_average', x='cluster_string',
                    color='cluster_string', points='all', hover_data=drama_df)
    
    fig.update_layout(
        title='Vote Average Distribution in all Movies',
        yaxis_title='Vote Average',
        xaxis_title='Cluster',
        height=1000,
        width=1500
    )
    
    iplot(fig)
