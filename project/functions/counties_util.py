import datetime
import time
import requests
import pandas as pd
from functions import util
import json
import os
import warnings
import requests
import numpy as np



def filter_location(accidents, counties_list):
    """_summary_

    Args:
        accidents (DataFrame): full API call from polisens API
        counties_list (str list): name of counties 

    Returns:
        DataFrame: location only of selected counties
    """
    locations = pd.DataFrame(columns=['name', 'gps'])
    locations['name'] = accidents['location'].apply(lambda x: x['name'])
    locations['gps'] = accidents['location'].apply(lambda x: x['gps'])

    # Filter the locations to only include those in Stockholm's counties
    stockholm_locations = locations[locations['name'].isin(counties_list)]
    return stockholm_locations


def choose_counties(counties: list):
    """counties eg = "01" to "25"  OBS "02" non existent"""

    with open("../../data/kommuner.json", "r") as f:
        kommuner = json.load(f)

    chosen_counties = []
    for county in counties:
        chosen_counties.append(kommuner[county])

    chosen_counties = [kommun for sublist in chosen_counties for kommun in sublist]

    return chosen_counties
