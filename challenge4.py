class challenge4(object):
	def __init__(self):
		self.details={}
		self.password={}
		self.posts=[]
		self.session={}
	def login(self):
		username=input('Enter your username  ')
		password=input('Enter your password  ')
		if username in self.details:
			if password==self.password[username]:
				self.session.update({username:self.details[username]})
			else:
				print('Invalid Credentials')
		else:
			print('Invalid user, please register')
	def logout(self):
		del self.session[input('enter your username')]
	def userInfo(self):
		username=input('enter your username')
		if username in self.session:
			firstname=self.session[username][0]
			lastname=self.session[username][1]
			email=self.session[username][2]
			password=self.password[username]
			print('Username:',username)
			print('Name:',firstname,' ',lastname)
			print('Email Address:',email)
			print('Password :',password)
		else:
			print('please Login to view your detais')
	def register(self):
		firstname=input('Enter your first name  ')
		lastname=input('Enter your last name  ')
		username=input('Enter your username  ')
		password=input('Enter your password  ')
		confirmPassword=input('confirm password  ')
		email=input('Enter your email  ')
		if self.passConfirm(password,confirmPassword):
			
			self.details.update({username:[firstname,lastname,email]})
			self.password.update({username:password})
		else:
			print('password should match')
			register()
	def passConfirm(self,pass1,pass2):
		return pass1==pass2
	def comment(self):
		if input('enter your username') in self.session:
			self.posts.append(input('you can write a comment'))
		else:
			print('please login!')
	def display_comments(self):
		if input('enter your username') in self.session:
			print(self.posts)
		else:
			print('please login')
