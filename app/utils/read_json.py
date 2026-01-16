import pandas as pd

def read_json(path):

    book_data = pd.read_json(path_or_buf=path)

    book_data_list = list(book_data.to_dict()['books'].values())

    return book_data_list
