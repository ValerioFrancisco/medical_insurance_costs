import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from cmdmenu import CmdMenu

# This class is responsible to handle the data load and analisys

class UsInsuranceData:
	# Initializes dataframe that will hold the data
	def __init__(self, file_name):
		self.df = pd.read_csv(file_name)
	
	def __repr__(self):
		return 'Represents data on US medical insurance costs'
	
	def summary(self):
		# Prints a summary of the data
		print('\n\t*** Data Summary ***')
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
		smoker_count = Counter(self.df['smoker'])['yes']
		print(f'{smoker_count} persons in the data are smokers')

	
	def smoker_comparision(self):
		# Plots a bar graph comparing the insurance charges of smokers vs non smokers
		smoker_mean = self.df.loc[self.df['smoker'] == 'yes']['charges'].mean()
		print(f'Average smoker charges: {smoker_mean:.2f}')
		non_smoker_mean = self.df.loc[self.df['smoker'] == 'no']['charges'].mean()
		print(f'Average non smoker charges: {non_smoker_mean:.2f}')
		plt.figure('Smoker comparision')
		plt.bar(['Smokers', 'Non smokers'], [smoker_mean, non_smoker_mean])
		plt.title('Smoker Vs Non smoker charges')
		plt.ylabel('Average insurance charges')
		plt.show()
	
	def bmi_comparision(self):
		print(self.df['bmi'].max())
		print(self.df['bmi'].min())
		underweight = self.df.loc[self.df['bmi'] < 18.5]['bmi'].count()
		healthy = self.df.loc[(self.df['bmi'] >= 18.5) & (self.df['bmi'] < 25.0)]['bmi'].count()
		overweight = self.df.loc[(self.df['bmi'] >= 25.0) & (self.df['bmi'] < 30.0)]['bmi'].count()
		obese = self.df.loc[self.df['bmi'] >= 30]['bmi'].count()
		print(f'Underweight: {underweight} individuals')
		print(f'Healthy: {healthy} individuals')
		print(f'Overweight: {overweight} individuals')
		print(f'Obese: {obese} individuals')
		plt.figure('BMI Categories')
		plt.title('Individuals per BMI category')
		plt.pie([underweight, healthy, overweight, obese], labels = ['Underweight', \
			'Healthy', 'Overweight', 'Obese'])
		plt.show()
		

# Loads data from CSV file
insurance = UsInsuranceData('insurance.csv')


# Initializes menu
app = CmdMenu('US Medical Insurance Costs')
app.add(insurance.summary, 'Data Summary')
app.add(insurance.smoker_comparision, 'Smoker insurance charges')
app.add(insurance.bmi_comparision, 'People by BMI')
# run the application
app.run()
