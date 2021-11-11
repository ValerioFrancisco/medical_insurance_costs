'''
This class serves to implement an application menu to be used in general applications.
'''

class CmdMenu:
	def __init__(self, appname):
		self._appname = appname
		self._function_list = [(self.exit, 'Exit')]
		self._decoration = ''
		self._exit = False
	
	def __repr__(self):
		return f'Menu class for the {self._appname} application.'

	def add(self, function, description):
		self._function_list.append((function, description))
	
	def get_appname():
		return self._appname

	def set_decoration(self, decoration):
		self._decoration = decoration

	def display_header(self):
		offset = 40 - int(len(self._appname) / 2)
		print(self._decoration)
		print(' ' * offset, self._appname)
		print(self._decoration)
	
	def display_footer(self):
		print(self._decoration)

	def display_menu(self):
		if len(self._function_list) > 1:
			for index in range(1, len(self._function_list)): 
				print('\t',index, '-', self._function_list[index][1])
		# TODO: Rethink this separator
		print('\t-----------------------------------------')
		print('\t', 0, '-', self._function_list[0][1])
		
	def exit(self):
		self._exit = True
		print('Goodbye...')

	# Runs a menu on a loop, this is the main method for the class
	def run(self):
		self._exit = False
		while not self._exit:
			self.display_header()
			self.display_menu()	
			self.display_footer()
			try:
				res = int(input('Choose your option: '))
			except Exception as e:
				print(e)
			else:
				if res in range(len(self._function_list)):
					function = self._function_list[res][0]
					function()
				else:
					print('Error: Choose a valid option')

