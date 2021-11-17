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
		mean = self.data_df['age'].mean()
		print(f'The average age is {round(mean, 2)} years old.')
		



# Loads data from CSV file
insurance = UsInsuranceData('insurance.csv')


# Initializes menu
app = cm.CmdMenu('US Medical Insurance Costs')
app.add(insurance.summary, 'Data Summary')
# run the application
app.run()
