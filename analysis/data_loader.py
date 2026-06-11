import os
import numpy as np
import pandas as pd

#Data loading
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DATA_DIR=os.path.join(BASE_DIR,"..","data")

#data loading function 1
def load_global_temperatures(filepath=None):
    if filepath is None:
        filepath=os.path.join(DATA_DIR, "GlobalTemperatures.csv")
    df=pd.read_csv(filepath)
    print(f"✅ Loaded GlobalTemperatures: {df.shape}")
    print(f"GlobalTemperatures information: {df.info()}")
    print(f"Missing values in GlobalTemperatures: \n{df.isnull().sum()}")
    return df

def load_country_temperatures(filepath=None):
    if filepath==None:
        filepath=os.path.join(DATA_DIR, "GlobalLandTemperaturesByCountry.csv")
    df=pd.read_csv(filepath)
    print(f"✅ Loaded GlobalLandTemperaturesByCountry: {df.shape}")
    print(f"GlobalLandTemperaturesByCountry information: {df.info()}")
    print(f"Missing values in GlobalLandTemperaturesByCountry: \n{df.isnull().sum()}")
    return df


#Data Cleaning function 2
def clean_data(df, dataset_type):
    
    #converting dt to datetime
    df['dt']=pd.to_datetime(df['dt'], errors='coerce')
    
    #keeping only relevant columns
    if dataset_type=="global":
        df = df[['dt', 'LandAverageTemperature','LandAndOceanAverageTemperature']]
        
        #forward filling missing values
        df['LandAverageTemperature']=df['LandAverageTemperature'].ffill()
        #data legitimately unavailable for LandAndOceanAverageTemperature for some periods, so we won't fill these
       
    elif dataset_type=="country":
        df=df[['dt', 'AverageTemperature', 'Country']]
        df["AverageTemperature"]=df["AverageTemperature"].ffill()

    print(f"✅ Cleaned {dataset_type} dataset: {df.shape}")
    
    #confirming dt is datetime
    print(f"{dataset_type} dt column type: {df['dt'].dtype}")

    #confirming the calues are actually filled
    print(f"Missing values in {dataset_type} after cleaning: \n{df.isnull().sum()}")
    
    #Return clean DataFrame
    return df


#main function
if __name__=="__main__":
    global_temps = load_global_temperatures()
    country_temps = load_country_temperatures()

    clean_global_temps = clean_data(global_temps, "global")
    clean_country_temps = clean_data(country_temps, "country")    