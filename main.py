import pandas as pd
import geopandas as gpd
import folium
import numpy as np

ff_df = pd.read_csv('https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/assets/choropleth-maps-python-folium/fatal-police-shootings-data.csv', parse_dates = ['date'])

ff_df.info()

counties = gpd.read_file('https://raw.githubusercontent.com/programminghistorian/jekyll/gh-pages/assets/choropleth-maps-python-folium/cb_2021_us_county_5m.zip')

counties = counties.rename(columns={'GEOID':'FIPS'})

counties[(counties['NAME']=='Suffolk') & (counties['STUSPS']=='MA')].plot()

counties = counties[['FIPS','NAME','geometry']]

counties.info()