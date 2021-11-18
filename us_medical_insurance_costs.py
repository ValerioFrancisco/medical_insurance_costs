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
	
	def summary(self):
		print(f'There are {self.data_df.shape[0]} records in the file.')
		age_mean = self.data_df['age'].mean()
		print(f'The average age is {round(age_mean, 2)} years old.')
		bmi_mean = self.data_df['bmi'].mean()
		print(f'The average bmi is {round(bmi_mean, 2)}')
		charges_mean = self.data_df['charges'].mean()
		print(f'The average insurance charges are US${round(charges_mean, 2)}')
		# TODO: must check this out
		# refresh pandas knowlege


# Loads data from CSV file
insurance = UsInsuranceData('insurance.csv')


# Initializes menu
app = cm.CmdMenu('US Medical Insurance Costs')
app.add(insurance.summary, 'Data Summary')
# run the application
app.run()
