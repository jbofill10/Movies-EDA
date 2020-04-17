import ast


def clean_data(meta_df, ratings_df):
    
    meta_df.drop(['belongs_to_collection', 'homepage', 'tagline', 'poster_path', 'overview', 'imdb_id', 'spoken_languages'], inplace=True, axis=1)
    
    column_changes = ['production_companies', 'production_countries', 'genres']
    
    json_shrinker_dict = dict({'production_companies': list(), 'production_countries': list(), 'genres': list()})

    meta_df.dropna(inplace=True)

    for col in column_changes:
        if col == 'production_companies':
            for i in meta_df[col]:
                i = ast.literal_eval(i)
                if len(i) < 1:
                    json_shrinker_dict['production_companies'].append(None)

                for element in i:
                    json_shrinker_dict['production_companies'].append(element['name'])
                    break
        elif col == 'production_countries':
            for i in meta_df[col]:
                i = ast.literal_eval(i)
                if len(i) < 1:
                    json_shrinker_dict['production_countries'].append(None)
                for element in i:
                    json_shrinker_dict['production_countries'].append(element['iso_3166_1'])
                    break
        else:
            for i in meta_df[col]:
                i = ast.literal_eval(i)
                if len(i) < 1:
                    json_shrinker_dict['genres'].append(None)

                for element in i:
                    json_shrinker_dict['genres'].append(element['name'])
                    break

    for i in column_changes:
        meta_df[i] = json_shrinker_dict[i]

    meta_df.dropna(inplace=True)

    movie_id_set = set()

    for i in meta_df['id']:
        movie_id_set.add(i)

    ratings_df = ratings_df[~ratings_df['movieId'].isin(movie_id_set)]

    meta_df['budget'] = meta_df['budget'].astype(int)

    return meta_df, ratings_df
