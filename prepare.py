import pandas as pd
import numpy as np 


def replace(df):

    df = df.replace('Unknown or other', 'other')
    df = df.replace('Darkness - lights unlit', 'Darkness - no lighting')
    df['Age_band_of_casualty'] = df['Age_band_of_casualty'].replace('5', 'Under 18')

    return df


def fill_missing(df):
    df['Driving_experience'].fillna(df['Driving_experience'].mode().values[0], inplace=True)
    df['Age_band_of_driver'].fillna(df['Age_band_of_driver'].mode().values[0], inplace=True)
    df['Age_band_of_casualty'].fillna(df['Age_band_of_casualty'].mode().values[0], inplace=True)
    df['Type_of_vehicle'].fillna(df['Type_of_vehicle'].mode().values[0], inplace=True)
    df['Area_accident_occured'].fillna(df['Area_accident_occured'].mode().values[0], inplace=True)
    df['Road_allignment'].fillna(df['Road_allignment'].mode().values[0], inplace=True)
    df['Type_of_collision'].fillna(df['Type_of_collision'].mode().values[0], inplace=True)
    df['Vehicle_movement'].fillna(df['Vehicle_movement'].mode().values[0], inplace=True)
    df['Lanes_or_Medians'].fillna(df['Lanes_or_Medians'].mode().values[0], inplace=True)
    df['Types_of_Junction'].fillna(df['Types_of_Junction'].mode().values[0], inplace=True)
    df['Casualty_class'].fillna(df['Casualty_class'].mode().values[0], inplace=True)   
    return df 


def prop_imputer(df):
    df_prop = df.copy(deep = True)
    missing_cols = df_prop.isna().sum()[df_prop.isna().sum() != 0].index.tolist()
    for col in missing_cols:
        values_col = df_prop[col].value_counts(normalize = True).index.tolist()
        probabilities_col = df_prop[col].value_counts(normalize = True).values.tolist()
        df_prop[col] = df_prop[col].fillna(pd.Series(np.random.choice(values_col, p = probabilities_col, size = len(df))))
    return df


def encode(df):
    df['Driving_experience'] = df.Driving_experience.map({'Below 1yr' : 1, '1-2yr' : 2, '2-5yr' : 3, '5-10yr' : 4, 'Above 10yr' : 5, 'No Licence' : 0, 'unknown' : 10})
    return df 

def make_dummy(df):
    dummy_df = pd.get_dummies(df[['Area_accident_occured', \
                              'Weather_conditions', \
                              'Light_conditions', \
                              'Age_band_of_casualty', \
                              'Age_band_of_driver', \
                              'Sex_of_casualty',\
                              'Casualty_severity',\
                              'Accident_severity',\
                              'Educational_level']], dummy_na=False, \
                              drop_first=True)
    
    # Concat dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)

    df = df.drop(['Casualty_severity', 'Area_accident_occured', 'Accident_severity', 'Educational_level', 'Light_conditions', 'Weather_conditions', 'Age_band_of_casualty', 'Age_band_of_driver', 'Educational_level_Unknown', 'Educational_level_Illiterate', 'Time', 'Lanes_or_Medians', 'Vehicle_movement', 'Types_of_Junction', 'Pedestrian_movement', 'Cause_of_accident', 'Type_of_collision', 'Vehicle_driver_relation', 'Type_of_vehicle', 'Road_surface_type', 'Road_surface_conditions', 'Day_of_week','Road_allignment', 'Fitness_of_casuality', 'Work_of_casuality', 'Sex_of_driver', 'Sex_of_casualty', 'Defect_of_vehicle', 'Owner_of_vehicle', 'Service_year_of_vehicle', 'Road_surface_type'], axis=1)
    return df 

def prep_data(df):
    df = replace(df)
    df = fill_missing(df)
    df = prop_imputer(df)
    df = encode(df)
    df = make_dummy(df)
    return df


