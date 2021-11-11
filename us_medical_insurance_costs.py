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

	def get_average_age(self):
		return sum(self.age) / len(self.age)

	def get_average_bmi(self):
		return sum(self.bmi) / len(self.bmi)

	def get_average_charges(self):
		return sum(self.charges) / len(self.charges)


# Application

data = UsInsuranceData('insurance.csv')
app = cm.CmdMenu('US Medical Insurance Costs')

app.run()
