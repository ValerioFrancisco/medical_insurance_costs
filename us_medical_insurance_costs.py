import csv
import matplotlib.pyplot as plt

# This class is responsible to handle the data load and analisys

class UsInsuranceData:
	# Initializes lists that will hold the data
	def __init__(self):
		self.age = []
		self.ex = []
		self.bmi = []
		self.children = []
		self.smoker = []
		self.region = []
		self.charges = []
	
	def __repr__(self):
		return 'Represents data on US medical insurance costs'
	
	def load_data(self, file_name):
		# TODO: finish this!
		pass
