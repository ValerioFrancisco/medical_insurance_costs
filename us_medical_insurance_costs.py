import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from cmdmenu import CmdMenu

# This class is responsible to handle the data load and analisys

class UsInsuranceData:
	# Initializes lists that will hold the data
	def __init__(self, file_name):
		self.df = pd.read_csv(file_name)
	
	def __repr__(self):
		return 'Represents data on US medical insurance costs'
	
	# Prints a summary of the data
	def summary(self):
		print(f'There are {self.df.shape[0]} records in the file.')
		age_mean = self.df['age'].mean()
		print(f'The average age is {age_mean:.2f} years old.')
		bmi_mean = self.df['bmi'].mean()
		print(f'The average bmi is {bmi_mean:.2f}')
		charges_mean = self.df['charges'].mean()
		print(f'The average insurance charges are US${charges_mean:.2f}')
		region_counter = Counter(self.df['region'])
		for key in region_counter:
			print(f'There are {region_counter[key]} persons from the {key}.')
		children_counter = Counter(self.df['children'])
		for key in children_counter:
			print(f'{children_counter[key]} persons have {key} children')


# Loads data from CSV file
insurance = UsInsuranceData('insurance.csv')


# Initializes menu
app = CmdMenu('US Medical Insurance Costs')
app.add(insurance.summary, 'Data Summary')
# run the application
app.run()
