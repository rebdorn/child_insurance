# Comparing Child Insurance Trends on Nativity of Parent 
Two simple scripts to create a dataframe *children_nativity_insurance.csv* with trends in health insurance coverage for children of "native" versus "foreign" born parents.

Required Libraries:
- pandas
- numpy

Recreating the Database:
1. Run *healthcare_census.py*, a program looping through each state for each year, gathering necessary data. Running this will create *census_data_2016.csv*, *census_data_2017.csv* and *census_data_2018.csv*.
2. Run *analyze_census.py*, a program which organizes information around children, nativity of parents and insurance. Unfortunately the file it creates exceeds Github's file size limit. Please contact me if you would like access to the data and have trouble running the scripts.
