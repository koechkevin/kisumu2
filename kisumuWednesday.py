class Signin(object):
	def __init__(self):
		self.database={}
	def register(self):
		firstname=input('Enter your first name  ')
		lastname=input('Enter your last name  ')
		username=input('Enter your username  ')
		password=input('Enter your password  ')
		email=input('Enter your email  ')
		self.reg(firstname,lastname,username,password,email)
	def login(self):
		username=input('Enter your username  ')
		password=input('Enter your password  ')
		self.log(username,password)
	def reg(self,firstname,lastname,username,password,email):
		self.database.update({username:password})
		print('successful registration for '+username)
	def log(self,username,password):
		if username in self.database:
			if password==self.database[username]:
				print('Welcome to our website')
			else:
				print('Invalid Credentials')
		else:
			print('Invalid user, please register')
