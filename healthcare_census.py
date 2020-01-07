import pandas as pd
import numpy as np
import requests
import json

def main():
	states_to_add = ['0400000US01','0400000US02','0400000US04','0400000US05','0400000US06','0400000US08', # List of states we want to loop through
					'0400000US09','0400000US10','0400000US11','0400000US12','0400000US13',
					'0400000US15','0400000US16','0400000US17','0400000US18','0400000US19',
					'0400000US20','0400000US21','0400000US22','0400000US23','0400000US24',
					'0400000US25','0400000US26','0400000US27','0400000US28','0400000US29',
					'0400000US30','0400000US31','0400000US32','0400000US33','0400000US34',
					'0400000US35','0400000US36','0400000US37','0400000US38','0400000US39',
					'0400000US40','0400000US41','0400000US42','0400000US44','0400000US45',
					'0400000US46','0400000US47','0400000US48','0400000US49','0400000US50',
					'0400000US51','0400000US53','0400000US54','0400000US55','0400000US56']
	column_names = ["PWGTP","WGTP","AGEP","CIT","NOP","FPARC","HINS4","HICOV","RC","OC","ST"] # Official codes for column names
	column_names = ["IDX", "ST", "OC", "RC", "HICOV", "HINS4", "FPARC", "NOP", "CIT", "AGEP", "WGTP", "PWGTP"]

	base_2016 = 'https://api.census.gov/data/2016/acs/acs1/pums?get=PWGTP,WGTP,AGEP,CIT,NOP,FPARC,HINS4,HICOV,RC,OC,ST&ucgid=' # Base GET request to plug in states
	censusdf_2016 = pd.DataFrame([np.arange(0,12)], columns = column_names) # Create dataframe with initialized weird row
	for i, state in enumerate(states_to_add): # For each state and its number
		print("State ",i) # Print the current iteration
		this_state = base_2016 + state # Easy variable for GET request
		try:
			response = requests.get(this_state) # Get data for this state
			response.raise_for_status() # Check if request went through
		except requests.exceptions.RequestException as e: # If there is an exception
			print(e) # Print the error
			sys.exit(1) # Exit the program
		formatted_response = json.loads(response.text)[1:] # Put our load response into a json
		formatted_response = [item[::-1] for item in formatted_response] # Format the json
		formatted_df = pd.DataFrame(formatted_response, columns = column_names) # create a df for this state
		censusdf_2016 = censusdf_2016.append(formatted_df)
	censusdf_2016 = censusdf_2016[1:] # Cut off the first row (was just numbers 0-10 to initialize database)
	print(censusdf_2016.head())

	base_2017 = 'https://api.census.gov/data/2017/acs/acs1/pums?get=PWGTP,WGTP,AGEP,CIT,NOP,FPARC,HINS4,HICOV,RC,OC,ST&ucgid=' # Base GET request to plug in states
	censusdf_2017 = pd.DataFrame([np.arange(0,12)], columns = column_names) # Create dataframe with initialized weird row
	for i, state in enumerate(states_to_add): # For each state and its number
		print("State ",i) # Print the current iteration
		this_state = base_2017 + state # Easy variable for GET request
		try:
			response = requests.get(this_state) # Get data for this state
			response.raise_for_status() # Check if request went through
		except requests.exceptions.RequestException as e: # If there is an exception
			print(e) # Print the error
			sys.exit(1) # Exit the program
		formatted_response = json.loads(response.text)[1:] # Put our load response into a json
		formatted_response = [item[::-1] for item in formatted_response] # Format the json
		formatted_df = pd.DataFrame(formatted_response, columns = column_names) # create a df for this state
		censusdf_2017 = censusdf_2017.append(formatted_df) # Append this state's data to our other data
	censusdf_2017 = censusdf_2017[1:] # Cut off the first row (was just numbers 0-10 to initialize database)
	print(censusdf_2017.head())

	base_2018 = 'https://api.census.gov/data/2018/acs/acs1/pums?get=PWGTP,WGTP,AGEP,CIT,NOP,FPARC,HINS4,HICOV,RC,OC,ST&ucgid=' # Base GET request to plug in states
	censusdf_2018 = pd.DataFrame([np.arange(0,12)], columns = column_names) # Create dataframe with initialized weird row
	for i, state in enumerate(states_to_add): # For each state and its number
		print("State ",i) # Print the current iteration
		this_state = base_2018 + state # Easy variable for GET request
		try:
			response = requests.get(this_state) # Get data for this state
			response.raise_for_status() # Check if request went through
		except requests.exceptions.RequestException as e: # If there is an exception
			print(e) # Print the error
			sys.exit(1) # Exit the program
		formatted_response = json.loads(response.text)[1:] # Put our load response into a json
		formatted_response = [item[::-1] for item in formatted_response] # Format the json
		formatted_df = pd.DataFrame(formatted_response, columns = column_names) # create a df for this state
		censusdf_2018 = censusdf_2018.append(formatted_df) # Append this state's data to our other data
	censusdf_2018 = censusdf_2018[1:] # Cut off the first row (was just numbers 0-10 to initialize database)
	print(censusdf_2018.head()) # Print the head of our new database

	# Fix the names bc I accidentally did it backwards
	#censusdf_2016.columns = ["Unnamed", "ST", "OC", "RC", "HICOV", "HINS4", "NOP", "CIT", "AGEP", "WGTP", "PWGTP"]
	#censusdf_2016.drop(['Unnamed'], axis = 1, inplace = True)
	censusdf_2016.to_csv('census_data_2016.csv')

	#censusdf_2017.columns = ["Unnamed", "ST", "OC", "RC", "HICOV", "HINS4", "NOP", "CIT", "AGEP", "WGTP", "PWGTP"]
	#censusdf_2017.drop(['Unnamed'], axis = 1, inplace = True)
	censusdf_2017.to_csv('census_data_2017.csv')

	#censusdf_2018.columns = ["Unnamed", "ST", "OC", "RC", "HICOV", "HINS4", "NOP", "CIT", "AGEP", "WGTP", "PWGTP"]
	#censusdf_2018.drop(['Unnamed'], axis = 1, inplace = True)
	censusdf_2018.to_csv('census_data_2018.csv')

if __name__ == "__main__":
    main()


