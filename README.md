# Comparing Child Insurance Trends on Nativity of Parent 
Two simple scripts to create six dataframes to view trends in health insurance coverage for children of "native" versus "non-native" born parents.

Requirements:
- Jupyter Notebook
- pandas
- numpy

Recreating the Data:
1. Run *healthcare_census.py*, a program looping through each state for each year, gathering necessary data. Running this will create *census_data_2016.csv*, *census_data_2017.csv* and *census_data_2018.csv*.
2. Run the Jupyter Notebook *healthcare_analysis.ipynb*, a program which organizes information around children, nativity of parents and insurance.
