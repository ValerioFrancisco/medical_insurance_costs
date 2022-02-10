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

	def age_distribution(self):
		fig, ax = plt.subplots(figsize=(6, 4))
		ax = plt.hist(self.df.age, bins=20)
		plt.show()

	def smoker_comparision(self):
		# Plots a bar graph comparing the insurance charges of smokers vs non smokers
		# Prints raw data tpo terminal
		smoker_mean = self.df.loc[self.df['smoker'] == 'yes']['charges'].mean()
		print(f'Average smoker charges: {smoker_mean:.2f}')
		non_smoker_mean = self.df.loc[self.df['smoker'] == 'no']['charges'].mean()
		print(f'Average non smoker charges: {non_smoker_mean:.2f}')
		# Plots bar graph
		plt.figure('Smoker comparision')
		plt.bar(['Smokers', 'Non smokers'], [smoker_mean, non_smoker_mean], color = ['red', 'green'])
		plt.title('Smoker Vs Non smoker charges')
		plt.ylabel('Average insurance charges')
		plt.show()
	
	def bmi_per_individual(self):
		# Shows a pie chart of the number of individuals by BMI category
		underweight = self.df.loc[self.df['bmi'] < 18.5]['bmi'].count()
		healthy = self.df.loc[(self.df['bmi'] >= 18.5) & (self.df['bmi'] < 25.0)]['bmi'].count()
		overweight = self.df.loc[(self.df['bmi'] >= 25.0) & (self.df['bmi'] < 30.0)]['bmi'].count()
		obese = self.df.loc[self.df['bmi'] >= 30]['bmi'].count()
		# Prints these to the terminal
		print(f'Underweight: {underweight} individuals')
		print(f'Healthy: {healthy} individuals')
		print(f'Overweight: {overweight} individuals')
		print(f'Obese: {obese} individuals')
		# Plots data
		plt.figure('BMI Categories')
		plt.title('Individuals per BMI category')
		plt.pie([underweight, healthy, overweight, obese], labels = ['Underweight', \
			'Healthy', 'Overweight', 'Obese'])
		plt.show()

	def bmi_charges_comparision(self):
		# Plots the charges associated with the bmi categories
		underweight = self.df.loc[self.df['bmi'] < 18.5]['charges'].mean()
		healthy = self.df.loc[(self.df['bmi'] >= 18.5) & (self.df['bmi'] < 25.0)]['charges'].mean()
		overweight = self.df.loc[(self.df['bmi'] >= 25.0) & (self.df['bmi'] < 30.0)]['charges'].mean()
		obese = self.df.loc[self.df['bmi'] >= 30]['charges'].mean()
		# Prints to the terminal
		print(f'Underweight mean charges: US${underweight:.2f}')
		print(f'Heathy mean charges: US${healthy:.2f}')
		print(f'overweight mean charges: US${overweight:.2f}')
		print(f'Obese mean charges: US${obese:.2f}')
		# Plots data
		plt.figure('BMI insurance charges correlation')
		plt.title('BMI mean charges per category')
		plt.bar(['Underweight', 'Healthy', 'Overweight', 'Obese'], [underweight,\
			 healthy, overweight, obese], color = ['blue', 'green', 'orange', 'red'])
		plt.show()

	def age_comparision(self):
		# Plots the charges by age
		ages = self.df.groupby('age').charges.mean().reset_index()
		plt.figure('Charges by age')
		plt.title('Insurance charges per age in the US')
		plt.xlabel('age')
		plt.ylabel('Charges in US$')
		plt.plot(ages.age, ages.charges)
		plt.show()

	def region_comparision(self):
		# shows a bar plot with a comparision between average charges and region
		regions = self.df.groupby('region').charges.mean().reset_index()
		plt.figure('Regions')
		plt.title('Average charges per region')
		plt.bar(regions.region, regions.charges)
		plt.show(block = True)

def main():
	# Loads data from CSV file
	insurance = UsInsuranceData('insurance.csv')


	# Initializes menu
	app = CmdMenu('US Medical Insurance Costs')
	app.add(insurance.summary, 'Data Summary')
	app.add(insurance.age_distribution, 'Age distribution')
	app.add(insurance.smoker_comparision, 'Smoker insurance charges')
	app.add(insurance.bmi_per_individual, 'Individuals per BMI category')
	app.add(insurance.bmi_charges_comparision, 'Insurance charges and bmi correlation')
	app.add(insurance.age_comparision, 'Age charge plot')
	app.add(insurance.region_comparision, 'Region Comparision...')
	# run the application
	app.run()

if __name__ == '__main__':
	main()