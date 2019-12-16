from urllib.request import urlretrieve
import os

import pandas as pd

Melbourne_URL = 'https://khansingh.000webhostapp.com/datasets/melb_data.csv'
def get_melb_data(filename = 'melb_data.csv', url = Melbourne_URL, force_download = False):
    """Download and cache melbourne data


    Parameters
    ----------
    filename: string(optional)
        location to dave the data
    url: string(optional)
        web location of data
    force_download: bool (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.Datarame
        The melbourne housing data
    """    

    if force_download or not os.path.exists(filename):
        urlretrieve(url , filename)
    mlb_hs = pd.read_csv('melb_data.csv', parse_dates = True)
    return mlb_hs
