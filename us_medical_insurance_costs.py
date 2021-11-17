import csv
import pandas as pd
import matplotlib.pyplot as plt
import cmdmenu as cm

# This class is responsible to handle the data load and analisys

class UsInsuranceData:
	# Initializes lists that will hold the data
	def __init__(self, file_name):
		self.data_df = pd.read_csv(file_name)
	
	def __repr__(self):
		return 'Represents data on US medical insurance costs'



# Loads data from CSV file
insurance = UsInsuranceData('insurance.csv')

# Functions
def average(lst):
	return sum(lst) / len(lst)

def summary():
	print(insurance.data_df.head(5))


def smoking_compare():
	pass


# Initializes menu
app = cm.CmdMenu('US Medical Insurance Costs')
app.add(summary, 'Data Summary')
app.add(smoking_compare, 'Smoker VS Non Smoker')
# run the application
app.run()
