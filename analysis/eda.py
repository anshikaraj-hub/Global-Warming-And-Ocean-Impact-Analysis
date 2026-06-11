import numpy as np
import pandas as pd
import data_loader as dl
import calendar

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


#Decadal average temperatures &
#sharpest raise in decade
def decadal_analysis(df, column_name):
    df['decade'] = (df['dt'].dt.year // 10) * 10
    
    if column_name=="land":
        decade_land = df.groupby('decade')['LandAverageTemperature'].mean().reset_index()
        print('\n',decade_land.head(),'\n')

        decade_land['temp_increase'] = decade_land['LandAverageTemperature'].diff()
        sharpest_increase_land = decade_land.loc[decade_land['temp_increase'].idxmax()]
        print('\n',sharpest_increase_land,'\n')

        return decade_land, sharpest_increase_land

    elif column_name=="land_and_ocean":
        decade_land_and_ocean = df.groupby('decade')['LandAndOceanAverageTemperature'].mean().reset_index()
        print('\n',decade_land_and_ocean.head(),'\n')

        decade_land_and_ocean['temp_increase'] = decade_land_and_ocean['LandAndOceanAverageTemperature'].diff()
        sharpest_increase_land_and_ocean = decade_land_and_ocean.loc[decade_land_and_ocean['temp_increase'].idxmax()]
        print('\n', sharpest_increase_land_and_ocean, '\n')
        
        return decade_land_and_ocean, sharpest_increase_land_and_ocean

    elif column_name=="country":
        decade_country = df.groupby('decade')['AverageTemperature'].mean().reset_index()
        print('\n',decade_country.head(),'\n')
        
        decade_country['temp_increase'] =decade_country['AverageTemperature'].diff()
        sharpest_increase_country = decade_country.loc[decade_country['temp_increase'].idxmax()]
        print('\n', sharpest_increase_country, '\n')

        return decade_country, sharpest_increase_country


#Top 10 countries sorted by warming 
def top_warming_countries(df):
    results = {}

    for country, group in df.groupby('Country'):
        first_year = group['dt'].dt.year.min()
        last_year = group['dt'].dt.year.max()

        first_decade_avg = group[group['dt'].dt.year <= first_year + 10]['AverageTemperature'].mean()
        last_decade_avg = group[group['dt'].dt.year >= last_year - 10]['AverageTemperature'].mean()

        results[country] = last_decade_avg - first_decade_avg
    
    warming = pd.Series(results)
    
    return warming.sort_values(ascending=False).head(10)


#Month which is consistently the hottest/coldest globally
def seasonal_analysis(df):
    monthly_avg = df.groupby(df['dt'].dt.month)['LandAverageTemperature'].mean().reset_index()
    
    hottest_month = monthly_avg.loc[monthly_avg['LandAverageTemperature'].idxmax()]
    coldest_month = monthly_avg.loc[monthly_avg['LandAverageTemperature'].idxmin()]
    
    print(f"Hottest month: {calendar.month_name[int(hottest_month['dt'])]} with avg temperature {hottest_month['LandAverageTemperature']}")
    print(f"Coldest month: {calendar.month_name[int(coldest_month['dt'])]} with avg temperature {coldest_month['LandAverageTemperature']}")
    
    return monthly_avg, hottest_month, coldest_month


#main function
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
    
    #decadal analysis
    decade_land, sharpest_increase_land = decadal_analysis(clean_global, "land")
    decade_land_and_ocean, sharpest_increase_land_and_ocean = decadal_analysis(clean_global, "land_and_ocean")
    decade_country, sharpest_increase_country = decadal_analysis(clean_country, "country")

    #top warming countries
    top_countries = top_warming_countries(clean_country)
    print('\nTop 10 warming countries:\n', top_countries)

    #seasonal analysis
    monthly_avg, hottest_month, coldest_month = seasonal_analysis(clean_global)