import numpy as np
import pandas as pd
import data_loader as dl

#Yearly average temperatures
def calculate_yearly_averages(df, column_name):
    
    if column_name=="land":
        yearly_land = df.groupby(df['dt'].dt.year)['LandAverageTemperature'].mean().reset_index()
        print('\n',yearly_land.head(),'\n')
        return yearly_land

    elif column_name=="land_and_ocean":
        yearly_land_and_ocean = df.groupby(df['dt'].dt.year)['LandAndOceanAverageTemperature'].mean().reset_index()
        print('\n',yearly_land_and_ocean.head(),'\n')
        return yearly_land_and_ocean

    elif column_name=="country":
        yearly_country = df.groupby(df['dt'].dt.year)['AverageTemperature'].mean().reset_index()
        print('\n',yearly_country.head(),'\n')
        return yearly_country


#Decadal average temperatures
def average_temperature_per_decade(df, column_name):
    df['decade'] = (df['dt'].dt.year // 10) * 10
    if column_name=="land":
        decade_land = df.groupby('decade')['LandAverageTemperature'].mean().reset_index()
        print('\n',decade_land.head(),'\n')
        return decade_land

    elif column_name=="land_and_ocean":
        decade_land_and_ocean = df.groupby('decade')['LandAndOceanAverageTemperature'].mean().reset_index()
        print('\n',decade_land_and_ocean.head(),'\n')
        return decade_land_and_ocean

    elif column_name=="country":
        decade_country = df.groupby('decade')['AverageTemperature'].mean().reset_index()
        print('\n',decade_country.head(),'\n')
        return decade_country


#sharpest raise in decade
def sharpest_decadal_increase(df, column_name):
    df['decade'] = (df['dt'].dt.year // 10) * 10
    if column_name=="land":
        decade_land = df.groupby('decade')['LandAverageTemperature'].mean().reset_index()
        decade_land['temp_increase'] = decade_land['LandAverageTemperature'].diff()
        sharpest_increase_land = decade_land.loc[decade_land['temp_increase'].idxmax()]
        print('\n',sharpest_increase_land,'\n')
        return sharpest_increase_land

    elif column_name=="land_and_ocean":
        decade_land_and_ocean = df.groupby('decade')['LandAndOceanAverageTemperature'].mean().reset_index()
        decade_land_and_ocean['temp_increase'] = decade_land_and_ocean['LandAndOceanAverageTemperature'].diff()
        sharpest_increase_land_and_ocean = decade_land_and_ocean.loc[decade_land_and_ocean['temp_increase'].idxmax()]
        print('\n',sharpest_increase_land_and_ocean,'\n')
        return sharpest_increase_land_and_ocean

    elif column_name=="country":
        decade_country = df.groupby('decade')['AverageTemperature'].mean().reset_index()
        decade_country['temp_increase'] = decade_country['AverageTemperature'].diff()
        sharpest_increase_country = decade_country.loc[decade_country['temp_increase'].idxmax()]
        print('\n',sharpest_increase_country,'\n')
        return sharpest_increase_country

if __name__=="__main__":
    
    #load raw data
    global_temps = dl.load_global_temperatures()
    country_temps = dl.load_country_temperatures()

    #clean data
    clean_global = dl.clean_data(global_temps, "global")
    clean_country = dl.clean_data(country_temps, "country")

    #First look at clean data
    print(clean_global.head())
    print(clean_country.head())

    #yearly averages
    land = calculate_yearly_averages(clean_global, "land")
    land_and_ocean = calculate_yearly_averages(clean_global, "land_and_ocean")
    country = calculate_yearly_averages(clean_country, "country")
    

