import os
import pandas as pd
import DataCleaning

from EDA import index as eda_index
from machine_learning import Index as ml_index


def main():
    if not os.path.isfile('Data/pickles/meta_pickle'):
        files_wanted = ['movies_metadata.csv']
        file_paths = list()
        for dirname, _, filenames in os.walk('Data/movies-dataset'):
            for filename in filenames:
                if filename in files_wanted:
                    file_paths.append(str(dirname + "/" + filename))

        meta_df = pd.read_csv(file_paths[0], low_memory=False)

        meta_df = DataCleaning.clean_data(meta_df)

        meta_df.to_pickle('Data/pickles/meta_pickle')

    else:
        meta_df = pd.read_pickle('Data/pickles/meta_pickle')

    #eda_index.run(meta_df)

    meta_df = meta_df[meta_df['vote_count'] >= meta_df['vote_count'].quantile(.75)]

    ml_index.do_ml(meta_df)


if __name__ == '__main__':
    main()