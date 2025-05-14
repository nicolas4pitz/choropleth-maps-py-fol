import pandas as pd
import geopandas as gpd
import folium
import numpy as np

ff_df = pd.read_csv('https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/assets/choropleth-maps-python-folium/fatal-police-shootings-data.csv', parse_dates = ['date'])

ff_df.info()