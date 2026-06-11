from calendar import calendar

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

import calendar

import data_loader as dl
from eda import calculate_yearly_averages, decadal_analysis, top_warming_countries, seasonal_analysis


if __name__ == "__main__":

    #load and clean data
    global_temps = dl.load_global_temperatures()
    country_temps = dl.load_country_temperatures()

    clean_global = dl.clean_data(global_temps, "global")
    clean_country = dl.clean_data(country_temps, "country")

    #Get analyzed data
    yearly_land = calculate_yearly_averages(clean_global, "land")
    decade_land, _ = decadal_analysis(clean_global, "land")
    top_countries = top_warming_countries(clean_country)
    monthly_avg, hottest, coldest = seasonal_analysis(clean_global)

    
    #chart 1: Global Land Average Temperature Trend
    plt.figure(figsize=(12,6))
    plt.plot(yearly_land['dt'], yearly_land['LandAverageTemperature'], color='red', linewidth=1)
    plt.title('Global Land Temperature Trend (1750-2015)')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True, alpha=0.3)
    plt.show()

    #chart 2: Interactive Plotly Line Chart
    fig = px.line(yearly_land, x='dt', y='LandAverageTemperature', title='Global Land Temperature Trend (Interactive)', labels={'dt': 'Year', 'LandAverageTemperature': 'Average Temperature (°C)'})
    fig.show()

    #chart 3: Top 10 Warming Countries
    top_countries_df = top_countries.reset_index()
    top_countries_df.columns = ['Country', 'Warming']
    print(top_countries_df)

    fig = px.bar(top_countries_df, x='Country', y='Warming', title='Top 10 Countries by Temperature Increase', color='Warming', color_continuous_scale='Reds',labels={'Warming': 'Temperature Increase (°C)'})
    fig.show()
    
    #chart 4: Decadal Temperature Changes
    fig = px.bar(decade_land, x='decade', y='LandAverageTemperature', title='Average Land Temperature by Decade', color='LandAverageTemperature', color_continuous_scale='Oranges', labels={'LandAverageTemperature': 'Average Temperature (°C)'})
    fig.show()
    

    #Chart 5: Seasonal Analysis
    monthly_avg['Month_Name'] = monthly_avg['dt'].apply(lambda x: calendar.month_name[int(x)])
    fig = px.line(monthly_avg, x='Month_Name', y='LandAverageTemperature',
                   title='Seasonal Temperature Pattern (Global Average)',
                   markers=True,
                   labels={'LandAverageTemperature': 'Average Temperature (°C)', 'Month_Name': 'Month'})
    fig.show()
    

    #Chart 6: Land vs Ocean
    yearly_land_and_ocean = calculate_yearly_averages(clean_global, "land_and_ocean")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yearly_land['dt'], y=yearly_land['LandAverageTemperature'], mode='lines', name='Land Only', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=yearly_land_and_ocean['dt'], y=yearly_land_and_ocean['LandAndOceanAverageTemperature'], mode='lines', name='Land & Ocean', line=dict(color='blue')))
    fig.update_layout(title='Global Land vs Land & Ocean Temperature Trends', xaxis_title='Year', yaxis_title='Average Temperature (°C)')
    fig.show()