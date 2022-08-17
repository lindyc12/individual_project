import pandas as pd

def get_data():
    blank_values = ["n/a", "na", "--"]
    df = pd.read_csv('https://raw.githubusercontent.com/sugatagh/Road-Traffic-Accident-Severity-Classification/main/Dataset/RTA%20Dataset.csv', na_values=blank_values)
    df.to_csv('casualty.csv')
    return df


