import csv
import matplotlib.pyplot as plt
import cmdmenu as cm

# This class is responsible to handle the data load and analisys

class UsInsuranceData:
	# Initializes lists that will hold the data
	def __init__(self, file_name):
		self.age = []
		self.sex = []
		self.bmi = []
		self.children = []
		self.smoker = []
		self.region = []
		self.charges = []
		self.load_data(file_name)
	
	def __repr__(self):
		return 'Represents data on US medical insurance costs'
	
	def load_data(self, file_name):
		with open(file_name, newline='') as csv_file:
        		reader = csv.DictReader(csv_file)
        		for row in reader:
            			self.age.append(int(row['age']))
            			self.sex.append(row['sex'])
            			self.bmi.append(float(row['bmi']))
            			self.children.append(int(row['children']))
            			self.smoker.append(row['smoker'])
            			self.region.append(row['region'])
            			self.charges.append(float(row['charges']))



# Loads data from CSV file
data = UsInsuranceData('insurance.csv')

# Functions
def average(lst):
	return sum(lst) / len(lst)

def summary():
	print('\n\tData Summary:')
	print(f'There are {len(data.age)} records on the data.')
	print(f'The average age is {round(average(data.age), 2)}.')
	print(f'The average body mass index is {round(average(data.bmi), 2)}.')
	print(f'The average insurance charges are ${round(average(data.charges), 2)}.')
	print(f'There are {data.sex.count("male")} males and {data.sex.count("female")} females.')
	print(f'From the data, {data.smoker.count("yes")} persons smoke.')
	print(f'{data.children.count(0)} people have no children.')


def smoking_compare():
	smoker_total = 0
	non_smoker_total = 0
	for idx, _ in enumerate(data.smoker):
		if data.smoker[idx] == 'yes':
			smoker_total += data.charges[idx]
		else:
			non_smoker_total += data.charges[idx]
	avg_smoker = smoker_total / data.smoker.count('yes')
	avg_non_smoker = non_smoker_total / data.smoker.count('no')
	print(f'Smokers have in average ${round(avg_smoker, 2)} USD insurance charges.')
	print(f'Non smokers have in average ${round(avg_non_smoker, 2)} USD insurance charges.')
	# Shows a bar plot of this data.
	data_lst = [avg_smoker, avg_non_smoker]
	names = ['Smokers', 'Non smokers']
	plt.bar(names, data_lst)
	plt.title('Smoker Vs Non smoker comparision.')
	plt.ylabel('Charges ($USD)')
	plt.show()


# Initializes menu
app = cm.CmdMenu('US Medical Insurance Costs')
app.add(summary, 'Data Summary')
app.add(smoking_compare, 'Smoker VS Non Smoker')
# run the application
app.run()
