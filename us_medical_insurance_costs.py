import csv
import matplotlib.pyplot as plt

# This class is responsible to handle the data load and analisys

class UsInsuranceData:
	# Initializes lists that will hold the data
	def __init__(self):
		self.age = []
		self.sex = []
		self.bmi = []
		self.children = []
		self.smoker = []
		self.region = []
		self.charges = []
	
	def __repr__(self):
		return 'Represents data on US medical insurance costs'
	
	def load_data(self, file_name):
		# TODO: finish this!
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


data = UsInsuranceData()
data.load_data('insurance.csv')

print(data.age)
