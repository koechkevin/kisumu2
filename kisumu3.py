class Signin(object):
    def __init__(self):
        self.database={}
    def register(self):
        firstname=input('Enter your first name  ')
        lastname=input('Enter your last name  ')
        username=input('Enter your username  ')
        password=input('Enter your password  ')
        email=input('Enter your email  ')
        reg(firstname,lastname,username,password,email)
    def login(self):
        username=input('Enter your username  ')
        password=input('Enter your password  ')
        log(username,password)
    def reg(self,firstname,lastname,username,password,email):
        self.database.update({username:password})
        print('successful registration for '+username)
    def log(self,username,password):
        
        if password==self.database[username]:
            print('Welcome to our website')
        else :
            print('Invalid Credentials')
