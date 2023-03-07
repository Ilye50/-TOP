class User:
	
	def __init__(self , login , password):
		self.__login = login
		self.__password = password
		
	def getLogin(self):
		return self.__login
	
	
newUser = User("User_one", "qwegdshsetyh")
print(newUser.getLogin())