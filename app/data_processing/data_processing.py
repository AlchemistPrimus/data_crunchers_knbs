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
        return "File open failed due to {} error".format(e)
    
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
        return "{}".format(e)
    


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
def group_by(file_=None,column_=None):
    """Return data of the file grouped by column specified as the parameter"""
    data=load_data(file_)
    return data.groupby(column_)
    


#Working with shape file hence dropping the longitudes and latitudes if present since shape file already contains the polygons
def polygons(cords):
    """Drop polygons if necessary since they are already present in shape file. Add necessary polygons, return a pair of polygons that represents the co-ordinates. Takes a list of two items and returns list object of the two"""
    try:
        if isinstance(cords,list) and len(cords)==2:
            for i in cords:
                if not (isinstance(i,int) or isinstance(i,float)):
                    return "All values must be integer or float"
            return [cords[0],cords[1]]
        else:
            return "Please enter a list containing two numbers(int or float)"
    except Exception as e:
        return "{} ocurred".format(e)
#Transpose table to plot
def data_transpose(data_):
    """Create a transpose of the dataframe."""
    #Each column corresponds to each county
    data=load_data(data_)
    return data.T

#Reading kenya map shape file with geopandas library
def read_map(shape_f):
    """Takes shape file as a parameter and returns geo data frame that will be used to generate the plots an error is raised if file fails to open"""
    try:
        kenya_gdf=gpd.read_file(shape_f)
        return kenya_gdf
    except Exception as e:
        return "Failed to open geo dataframe due to{}.".format(e)
    
import os

dir=os.path.dirname("/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/data_processing/open_source_data_values/")

csv_files=['2009_County_Population.csv','2013_health_staff_per_10000.csv','2018_2019_health_staff_per_10000.csv','2019_County_Population.csv','list_of_community_health_units.csv','list_of_hospitals_and_number_of_beds.csv','list_of_pharmacies.csv','number_of_hospital_beds.csv']

def file_finder(dir,csv_files):
    for i in csv_files:
        loc=os.path.join(dir,i)
        d=load_data(loc)
        return d.head(5)

#print(file_finder(dir,csv_files))

