print "\033[1;32mProgram Working\033[1;m"

class BankAccount(object): # making class
	def _init_ (self, name, accountNumber, balance): # objects withing the class
		self.name_str = name # varaibles assocaites with itself
		self.accountNumber_int = accountNumber
		self.balance_float = balance

# the functions use the objects from the _init_ 
	def makeWithdrawal(self, amount):
		self.balance_float -= amount # functions using the objects

	def makeDeposit(self, amount):
		self.balance_float += amount

	def getBalance(self):
		return self.balance_float  
