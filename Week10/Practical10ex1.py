print "\033[1;32mProgram Working\033[1;m"

class BankAccount(object):
	def _init_ (self, name, accountNumber, balance):
		self.name_str = name
		self.accountNumber_int = accountNumber
		self.balance_float = balance

	def makeWithdrawal(self, amount):
		self.balance_float -= amount

	def makeDeposit(self, amount):
		self.balance_float += amount

	def getBalance(self):
		return self.balance_float  
