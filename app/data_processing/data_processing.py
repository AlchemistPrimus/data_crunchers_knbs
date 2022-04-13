"""Preprocessing of data goes here:
Removing missing values from the dataset
Inputing mission values from the dataset if possible
selection of relevant features"""

import numpy as np
import pandas as pd
import geopandas as gpd


#files=["ML_tests/2018_2019_health_staff_per_10000.csv","ML_tests/2019_County_Population.csv","ML_tests/IRIS.csv"]
    
#opening the datasets
def load_data(file_name=None):
    """takes csv file as parameter and returns it exception is raised incase of error during opening of the file."""
    try:
        df=pd.read_csv(file_name)
        return df
    except Exception as e:
        raise "File open failed due to {} error".format(e)
    
#Identifying missing values
#Identifying missing values
def missing_values(file):
    """Takes an iterable of file objects and returns true if there is a null value and false otherwise"""
    try:
        f_ile=pd.DataFrame(load_data(file))
        val=f_ile.isna().sum()
        mis_val_list=val.values.tolist()
        if sum(mis_val_list)>0:
            """Missing values were found return true"""
            #print the dataframe
            print("Missing values:\n{}".format(f_ile.isna().sum()))
            return True
        else:
            """Missing values were not found in the dataset hence return false for each of the dataset."""
            #print the dataframe
            print("No missing value:\n{}".format(f_ile.isnull().sum()))
            return False
    except Exception as e:
        #Shows the error captured
        print("{}".format(e))
    


#working with features with missing values
def missing_values_operation(files):
    """Will take iterable file objects and eliminate features or samples with missing values or inputing missing values if necessary"""
    for i in files:
            with open(i,'rw') as f:
                if missing_values(f)==True:
                    file_data=load_data(i)
                    #Dropping rows with missing values
                    file_data.dropna(axis=0)
                    #Dropping columns with missing values
                    file_data.dropna(axis=1)
                    return "dropped rows and columns"
                else:
                    return "no values to be dropped"
                

#Grouping data
def group_by(column_):
    """Return data grouped by column specified as the parameter"""
    pass

#Working with shape file hence dropping the longitudes and latitudes if present since shape file already contains the polygons
def polygons(lat,long):
    """Drop polygons if necessary since they are already present in shape file. Add necessary polygons"""
    pass

#Transpose table to plot
def plot_transpose(data_):
    """Create a transpose of the dataframe"""
    #Each column corresponds to each county
    pass

#Reading kenya map shape file with geopandas library
def read_map(shape_f):
    """Returns geo data frame that will be used to generate plots"""
    pass