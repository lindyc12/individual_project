import pandas as pd
import numpy as np 


def replace(df):

    df = df.replace('Unknown or other', 'other')
    df = df.replace('Darkness - lights unlit', 'Darkness - no lighting')
    df['Age_band_of_casualty'] = df['Age_band_of_casualty'].replace('5', 'Under 18')
    df = df.replace('Unknown or other', 'other')
    df = df.replace('Darkness - lights unlit', 'Darkness - no lighting')
    df['Age_band_of_casualty'] = df['Age_band_of_casualty'].replace('5', 'Under 18')
    df.Area_accident_occured = df.Area_accident_occured.str.strip()
    df['Area_accident_occured'] = df['Area_accident_occured'].replace({'Market areas': 'Other', 'Rural village areas': 'Other', 'Unknown': 'Other', 'Rural village areasOffice areas': 'Other', 'Recreational areas': 'Other', 'Market areas' : 'Other'})
    return df


def fill_missing(df):
    df['Driving_experience'].fillna(df['Driving_experience'].mode()[0], inplace=True)
    df['Age_band_of_driver'].fillna(df['Age_band_of_driver'].mode()[0], inplace=True)
    df['Age_band_of_casualty'].fillna(df['Age_band_of_casualty'].mode()[0], inplace=True)
    df['Type_of_vehicle'].fillna(df['Type_of_vehicle'].mode()[0], inplace=True)
    df['Area_accident_occured'].fillna(df['Area_accident_occured'].mode()[0], inplace=True)
    df['Road_allignment'].fillna(df['Road_allignment'].mode()[0], inplace=True)
    df['Type_of_collision'].fillna(df['Type_of_collision'].mode()[0], inplace=True)
    df['Vehicle_movement'].fillna(df['Vehicle_movement'].mode()[0], inplace=True)
    df['Lanes_or_Medians'].fillna(df['Lanes_or_Medians'].mode()[0], inplace=True)
    df['Types_of_Junction'].fillna(df['Types_of_Junction'].mode()[0], inplace=True)
    df['Casualty_class'].fillna(df['Casualty_class'].mode()[0], inplace=True)   
    df['Casualty_severity'].fillna(df['Casualty_severity'].mode()[0], inplace=True)
    df['Fitness_of_casuality'].fillna(df['Fitness_of_casuality'].mode()[0], inplace=True)
    df['Weather_conditions'].fillna(df['Weather_conditions'].mode()[0], inplace=True)
    return df 




def encode(df):
    df['Driving_experience'] = df.Driving_experience.map({'5-10yr' : 1, '2-5yr' : 2, 'Above 10yr' : 3, '1-2yr' : 4, 'Below 1yr' : 5, 'No Licence' : 0, 'unknown' : 10})
    df['Age_band_of_driver'] = df.Age_band_of_driver.map({'Under 18' : 1, '18-30' : 2, '31-50' : 3, 'Over 51' : 4, 'Unknown' : 10})
    #df['Educational_level'] = df.Educational_level.map({'Illiterate' : 1, 'Writing & reading' : 2, 'Elementary school' : 3, 'Junior high school' : 4, 'High school' : 5, 'Above high school' : 6, 'Unknown' : 10})
    #df['Driving_experience'] = df.Driving_experience.map({'Below 1yr' : 1, '1-2yr' : 2, '2-5yr' : 3, '5-10yr' : 4, 'Above 10yr' : 5, 'No Licence' : 0, 'unknown' : 10})
    df['Light_conditions'] = df.Light_conditions.map({'Darkness - no lighting' : 1, 'Darkness - lights lit' : 2, 'Daylight' : 3})
    df['Age_band_of_casualty'] = df.Age_band_of_casualty.map({'Under 18' : 1, '18-30' : 2, '31-50' : 3, 'Over 51' : 4, 'na' : 10})
    df['Fitness_of_casuality'] = df.Fitness_of_casuality.map({'Normal' : 1, 'NormalNormal' : 2, 'Deaf' : 3, 'Other' : 4, 'Blind' : 5})
    df['Accident_severity'] = df.Accident_severity.map({'Slight Injury' : 1, 'Serious Injury' : 2, 'Fatal injury' : 3})
    df['Casualty_class'] = df.Casualty_class.map({'Driver or rider' : 1, 'Pedestrian' : 2, 'Passenger' : 3})
    #df['Weather_conditions'] = df.Weather_conditions.map({'Normal' : 1, 'Raining' : 2, 'Cloudy' : 3, 'Windy' : 4})
    df['Area_accident_occured'] = df.Area_accident_occured.map({'Office areas' : 1, 'Residential areas' : 2, 'Church areas' : 3, 'Industrial areas' : 4, 'School areas' : 5, 'Recreational areas' : 6, 'Outside rural areas' : 7, 'Hospital areas' : 8, 'Other' : 9})
    return df 

def rename_vals(df):
    df['Educational_level'] = df['Educational_level'].replace(['Junior high school','Elementary school', 'Above high school', 'Writing & reading'], ['Junior High', 'Elementary', 'High School', 'Can read'])
    #df['Area_accident_occured'] = df['Area_accident_occured'].replace(['Residential areas', 'Church areas', 'Industrial areas', 'School areas', 'Recreational areas', 'Outside rural areas', 'Hospital areas'], ['Residential', 'church', 'Industrial', 'Schools', 'Rec', 'Rural', 'Hospitals'])
    #df['Fitness_of_casuality'] = df['Fitness_of_casuality'].replace(['Normal', 'NormalNormal'], ['Can hear', 'Can hear/see'])

                                                                    
    return df

def make_dummy(df):
    dummy_df = pd.get_dummies(df[['Sex_of_driver', \
                                  'Weather_conditions', \
                                 # 'Light_conditions', \
                                  #'Age_band_of_casualty', \
                                  #'Age_band_of_driver', \
                                  'Sex_of_casualty',\
                                  #'Casualty_severity',\
                                  #'Accident_severity',\
                                  'Educational_level']], dummy_na=False, \
                                   drop_first=True)
    
    #Concat dummy dataframe to original 
    df = pd.concat([df, dummy_df], axis=1)

    df = df.drop([ 'Time', 'Educational_level', 'Weather_conditions', 'Educational_level_Unknown', 'Educational_level_Illiterate', 'Lanes_or_Medians', 'Vehicle_movement', 'Types_of_Junction', 'Pedestrian_movement', 'Cause_of_accident', 'Type_of_collision', 'Vehicle_driver_relation', 'Type_of_vehicle', 'Road_surface_type', 'Road_surface_conditions', 'Day_of_week','Road_allignment', 'Work_of_casuality', 'Sex_of_casualty', 'Sex_of_driver', 'Defect_of_vehicle', 'Owner_of_vehicle', 'Service_year_of_vehicle', 'Road_surface_type'], axis=1)
    return df 







def prep_data(df):
    df = fill_missing(df)
    df = replace(df)
    #df = prop_imputer(df)
    df = encode(df)
    df = rename_vals(df)
    df = make_dummy(df)
    return df


