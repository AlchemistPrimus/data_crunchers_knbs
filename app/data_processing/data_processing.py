"""Preprocessing of data goes here:
Removing missing values from the dataset
Inputing mission values from the dataset if possible
selection of relevant features"""
import pandas as pd
import numpy as np
from typing import List
        
import numpy as np
import pandas as pd


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
def missing_values(file):
    """Takes an iterable of file objects and returns true if there is a null value and false otherwise"""
    try:
        f_ile=pd.DataFrame(load_data(file))
        if f_ile.isnull():
            """Missing values were found return true"""
            print("Missing values:\n{}".format(f_ile.isnull().sum()))
            return True
        else:
            """Missing values were not found in the dataset hence return false for each of the dataset."""
            return False
    except Exception as e:
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