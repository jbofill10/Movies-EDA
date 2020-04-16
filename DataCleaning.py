import ast


def clean_data(meta_df, ratings_df):
    
    meta_df.drop(['belongs_to_collection', 'homepage', 'tagline', 'poster_path', 'overview', 'imdb_id', 'spoken_languages'], inplace=True, axis=1)
    
    column_changes = ['production_companies', 'production_countries']
    
    production_dict = dict({'production_companies': list(), 'production_countries': list()})

    meta_df.dropna(inplace=True)

    for col in column_changes:
        if col == 'production_companies':
            for i in meta_df[col]:
                i = ast.literal_eval(i)
                if len(i) < 1:
                    production_dict['production_companies'].append(None)

                for element in i:
                    production_dict['production_companies'].append(element['name'])
                    break
        else:
            for i in meta_df[col]:
                i = ast.literal_eval(i)
                if len(i) < 1:
                    production_dict['production_countries'].append(None)
                for element in i:
                    production_dict['production_countries'].append(element['iso_3166_1'])
                    break

    for i in column_changes:
        meta_df[i] = production_dict[i]

    meta_df.dropna(inplace=True)

    movie_id_set = set()

    for i in meta_df['id']:
        movie_id_set.add(i)

    ratings_df = ratings_df[~ratings_df['movieId'].isin(movie_id_set)]

    return meta_df, ratings_df
