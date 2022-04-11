# Importing the pandas library
import pandas as pd
import numpy as np
import math

#########################
# CORE HEALTHWORKFORCE #
########################

#Loading the datasets

#List of health staff in 2013 from Africa open data
Health_staff_2013 = pd.read_csv("https://open.africa/dataset/4acc4709-cd40-43da-ad95-3b4a1224f97c/resource/ec2b86a8-9083-451d-b524-eba3f06382e7/download/cfafrica-_-data-team-_-outbreak-_-covid-19-_-data-_-openafrica-uploads-_-kenya-health-staff-per-.csv")

#List of health staff in 2019 from Africa open data
Health_staff_2019 = pd.read_csv("https://open.africa/dataset/4acc4709-cd40-43da-ad95-3b4a1224f97c/resource/43cea114-a929-4984-bd1c-b665d4a7ea5e/download/cfafrica-_-data-team-_-outbreak-_-covid19-_-data-_-openafrica-uploads-_-kenya-healthworkers.csv")


def core_healthworkforce(Health_staff_2013, Health_staff_2019):
    # Renaming the columns
    Health_staff_2013.columns = ['counties', 'core_health_workforce_2013']
    Health_staff_2019.columns = ['counties', 'core_health_workforce_2019']

    # Changing all counties to lower case
    Health_staff_2013['counties'] = Health_staff_2013['counties'].apply(lambda x: x.lower())
    Health_staff_2019['counties'] = Health_staff_2019['counties'].apply(lambda x: x.lower())

    # Sorting the counties alphabetically
    Health_staff_2013.sort_values(by='counties', ascending=True, inplace=True)
    Health_staff_2019.sort_values(by='counties', ascending=True, inplace=True)

    # Resetting the indeces
    Health_staff_2013.reset_index(drop=True, inplace=True)
    Health_staff_2019.reset_index(drop=True, inplace=True)

    # Replacing 2019 Health workforce counties with 2013 counties list - This is to enable joining
    Health_staff_2019['counties'] = Health_staff_2013['counties']

    # Merging/Joining the two dataframes
    core_healthworkforce_df = Health_staff_2013.merge(Health_staff_2019, how='left', on='counties')

    # Finding the percentage change of core healthworkforce between 2013 and 2019
    core_healthworkforce_df['Percentage_change'] = round(
        np.divide(np.subtract(core_healthworkforce_df['core_health_workforce_2019'],
                              core_healthworkforce_df['core_health_workforce_2013']),
                  core_healthworkforce_df['core_health_workforce_2013']) * 100, 2)

    core_healthworkforce_df.columns = ['counties', '2013', '2019', '% change']
    return (core_healthworkforce_df)

#############################
# HOSPITAL OPERATION STATUS #
#############################

#List of hospitals and beds from Africa Open data
Hospitals_data = pd.read_csv("https://open.africa/dataset/bb87c99a-78f8-4b8c-8186-4b0f4d935bcd/resource/6d13d7ff-ce54-4c8e-8879-da24fd3b456d/download/cfafrica-_-data-team-_-outbreak-_-covid19-_-data-_-openafrica-uploads-_-kenya-hospital-ke.csv")


def hospital_operation_status(Hospitals_data):
    # Sorting in Ascending order
    Hospitals_data.sort_values(by='County', ascending=True, inplace=True)

    # Changing all counties and Facility type, to lower case
    Hospitals_data['County'] = Hospitals_data['County'].apply(lambda x: x.lower())
    Hospitals_data['Facility type'] = Hospitals_data['Facility type'].apply(lambda x: x.lower())

    # Getting rid of hospitals that only offer specialised services
    filt = ((Hospitals_data['Facility type'] == 'dental clinic') |
            (Hospitals_data['Facility type'] == 'vct') |
            (Hospitals_data['Facility type'] == 'laboratory') |
            (Hospitals_data['Facility type'] == 'rehab. center - drug and substance abuse') |
            (Hospitals_data['Facility type'] == 'ophthalmology') |
            (Hospitals_data['Facility type'] == 'dialysis center') |
            (Hospitals_data['Facility type'] == 'radiology clinic') |
            (Hospitals_data['Facility type'] == 'blood bank') |
            (Hospitals_data['Facility type'] == 'regional blood transfusion centre') |
            (Hospitals_data['Facility type'] == 'pharmacy') |
            (Hospitals_data['Facility type'] == 'farewell home'))

    Hospitals_data = Hospitals_data.loc[~filt]

    # Creating a dataframe with our variables of interest
    hospital_status_df = Hospital_status_df = Hospitals_data[
        ['County', 'Owner type', 'Open_whole_day', 'Open_public_holidays',
         'Open_weekends', 'Open_late_night']]

    # Owner type can be: 'Ministry of Health', 'Private Practice', 'Non-Governmental Organizations', 'Faith Based Organization'

    owner_type = input("Enter the owner type: ")

    # Operating time can be: 'Open_whole_day', 'Open_public_holidays', 'Open_weekends', 'Open_late_night'

    operating_time = input("Enter the operating time: ")

    # Filtering by owner type
    owner_filter = (Hospital_status_df['Owner type'] == owner_type)
    Hospital_status_df = Hospital_status_df.loc[owner_filter]

    # Grouping operational status of hospitals per county
    Hospital_status_df = Hospital_status_df.groupby(['County', operating_time], as_index=False).size().pivot('County',
                                                                                                             operating_time)
    # Removing the pivoting extra columns
    Hospital_status_df = Hospital_status_df.droplevel(0, axis=1).reset_index().rename_axis(columns=None)
    # Replacing all NaN with zero
    Hospital_status_df.fillna(0, inplace=True)

    size = Hospital_status_df['size'] = Hospital_status_df.loc[:, 'No':'Yes'].sum(axis=1)

    Hospital_status_df = round(Hospital_status_df.loc[:, 'No':'Yes'].div(Hospital_status_df['size'], axis=0) * 100, 2)

    # counties
    counties = Hospitals_data['County'].unique()
    Hospital_status_df.insert(loc=0, column='counties', value=counties)

    # Total Hospitals
    Hospital_status_df.insert(loc=1, column='Total Hospitals', value=size)

    return (Hospital_status_df)

###############
# CENSUS DATA #
###############

# Internet coverage
def internet(Population_data, Household_data):
    # Sorting data into ascending order
    Population_data.sort_values(by='COUNTY', ascending=True, inplace=True)
    Household_data.sort_values(by='COUNTY', ascending=True, inplace=True)

    # Converting counties into lower case
    Population_data['COUNTY'] = Population_data['COUNTY'].apply(lambda x: x.lower())
    Household_data['COUNTY'] = Household_data['COUNTY'].apply(lambda x: x.lower())

    # Extracting counties
    counties = Population_data['COUNTY'].unique()

    # Part to be included on the website
    choose = input(
        "Choose among the following (You can type either Internet_users, Internet_through_mobile, Fixed_internet_at_home")

    # Checking the internet users per county
    if choose == "Internet_users":
        Internet_users = Population_data.groupby(['COUNTY', 'P57'], as_index=False).size().pivot('COUNTY', 'P57')
        Internet_users = Internet_users.droplevel(0, axis=1).reset_index().rename_axis(columns=None)
        # Calculating population per county
        county_population = Population_data.groupby('COUNTY', as_index=False).size().sum(axis=1, numeric_only=True)
        # Adding the county population to the internet users dataframe
        Internet_users['county_population'] = county_population

        # Converting into percentages
        Internet_users = Internet_users.loc[:, 'No':'Yes'].div(Internet_users['county_population'], axis=0) * 100

        # Adding counties column
        Internet_users.insert(loc=0, column='counties', value=counties)

        Internet_users.insert(loc=1, column='Population size', value=county_population)

        return (Internet_users)

    # Households accessing the internet through Mobile
    elif choose == "Internet_through_mobile":
        Internet_through_mobile = Household_data.groupby(['COUNTY', 'H39_6'], as_index=False).size().pivot('COUNTY',
                                                                                                           'H39_6')
        Internet_through_mobile = Internet_through_mobile.droplevel(0, axis=1).reset_index().rename_axis(columns=None)
        # Calculating number of households per county
        county_household_population = Household_data.groupby('COUNTY', as_index=False).size().sum(axis=1,
                                                                                                  numeric_only=True)

        Internet_through_mobile['county_household_population'] = county_household_population

        # Converting into percentages
        Internet_through_mobile = Internet_through_mobile.loc[:, 'No':'Yes'].div(
            Internet_through_mobile['county_household_population'],
            axis=0) * 100

        # Adding counties column
        Internet_through_mobile.insert(loc=0, column='counties', value=counties)

        Internet_through_mobile.insert(loc=1, column='Population size', value=county_household_population)

        return (Internet_through_mobile)

    # Households access the internet through fixed internet e.g Fiber, Satellite, dish, LAN, Wi-Fi
    else:
        Fixed_internet_at_home = Household_data.groupby(['COUNTY', 'H39_7'], as_index=False).size().pivot('COUNTY',
                                                                                                          'H39_7')
        Fixed_internet_at_home = Fixed_internet_at_home.droplevel(0, axis=1).reset_index().rename_axis(columns=None)
        # Calculating number of households per county
        county_household_population = Household_data.groupby('COUNTY', as_index=False).size().sum(axis=1,
                                                                                                  numeric_only=True)

        Fixed_internet_at_home['county_household_population'] = county_household_population

        Fixed_internet_at_home = round(
            Fixed_internet_at_home.loc[:, 'No':'Yes'].div(Fixed_internet_at_home['county_household_population'],
                                                          axis=0) * 100, 2)

        # Adding counties column
        Fixed_internet_at_home.insert(loc=0, column='counties', value=counties)

        Fixed_internet_at_home.insert(loc=1, column='Population Size', value=county_household_population)

        return (Fixed_internet_at_home)

#  Place of Birth

def place_of_birth(Population_data):
    # Sorting data into ascending order
    Population_data.sort_values(by='COUNTY', ascending=True, inplace=True)

    # Converting counties into lower case
    Population_data['COUNTY'] = Population_data['COUNTY'].apply(lambda x: x.lower())

    # Checking the place of birth per county
    Place_of_birth = Population_data.groupby(['COUNTY', 'P36'], as_index=False).size().pivot('COUNTY', 'P36')
    Place_of_birth = Place_of_birth.droplevel(0, axis=1).reset_index().rename_axis(columns=None)
    total_births = Place_of_birth['size'] = Place_of_birth.loc[:, "DK":"Non Health Facility"].sum(axis=1)

    # Adding counties
    counties = Population_data['COUNTY'].unique()

    # Converting into percentages
    Place_of_birth = round(Place_of_birth.loc[:, 'DK':'Non Healthy Facility'].div(Place_of_birth['size'], axis=0) * 100,
                           2)

    # Adding the counties column
    Place_of_birth.insert(loc=0, column='counties', value=counties)

    Place_of_birth.insert(loc=1, column='Total births', value=total_births)

    return (Place_of_birth)

# Main source of drinking water

def source_of_drinking_water(Household_data):
    # Sorting data into ascending order
    Household_data.sort_values(by='COUNTY', ascending=True, inplace=True)

    # Converting counties into lower case
    Household_data['COUNTY'] = Household_data['COUNTY'].apply(lambda x: x.lower())

    # counties
    counties = Household_data['COUNTY'].unique()

    # Main source of drinking water for households
    Main_source_of_drinking_water = Household_data.groupby(['COUNTY', 'H33'], as_index=False).size().pivot('COUNTY',
                                                                                                           'H33')
    Main_source_of_drinking_water = Main_source_of_drinking_water.droplevel(0, axis=1).reset_index().rename_axis(
        columns=None)  # Removing the pivoting extra columns

    total_households = Main_source_of_drinking_water.loc[:, ' Water Vendor':'Unprotected Well'].sum(axis=1)

    # Improved drinking water sources
    improved_list = ['Borehole/Tube well', 'Bottled water', 'Piped  to yard/plot', 'Piped into dwelling',
                     'Protected Spring',
                     'Protected Well', 'Public tap/Standpipe', 'Rain/Harvested water']
    improved_sources_df = Main_source_of_drinking_water.loc[:, improved_list]
    improved_sources_df['improved_size'] = improved_sources_df.sum(axis=1)
    improved_sources_df.insert(loc=0, column='counties', value=counties)
    improved_sources_df = improved_sources_df.loc[:, ['counties', 'improved_size']]

    # Unimproved drinking water sources
    unimproved_list = [' Water Vendor', 'Dam', 'Lake', 'Pond', 'Stream/River', 'Unprotected Spring', 'Unprotected Well']
    unimproved_sources_df = Main_source_of_drinking_water.loc[:, unimproved_list]
    unimproved_sources_df['unimproved_size'] = unimproved_sources_df.sum(axis=1)
    unimproved_sources_df.insert(loc=0, column='counties', value=counties)
    unimproved_sources_df = unimproved_sources_df.loc[:, ['counties', 'unimproved_size']]

    # Creating a data frame containing county, improved water sources, and unimproved water sources
    drinking_water_df = improved_sources_df.merge(unimproved_sources_df, how='left', on='counties')

    drinking_water_df['total_size'] = drinking_water_df.loc[:, 'improved_size':'unimproved_size'].sum(axis=1)
    drinking_water_df = round(
        drinking_water_df.loc[:, 'improved_size':'unimproved_size'].div(drinking_water_df['total_size'],
                                                                        axis=0) * 100, 2)

    # Adding the counties column
    drinking_water_df.insert(loc=0, column='counties', value=counties)

    # Renaming columns
    drinking_water_df.columns = ['counties', 'Safe', 'Unsafe']
    drinking_water_df.insert(loc=1, column='Total Households', value=total_households)

    return (drinking_water_df)



