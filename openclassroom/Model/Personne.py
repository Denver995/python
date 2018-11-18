import os
class Personne:
	"""docstring for Personne"""
	def __init__(self):
		self.userName = "denver99"
		self.name = "djo"
		self.email = "denverclaude99@gmail.com"
		self._profession = "profession"
	
	"""fuction that will be call when we want the profession valu"""
	def _get_profession(self):
		return self._profession
	
	"""fuction that will be call when we want to change profession valu"""
	def _set_profession(self, new_profession):
		self._profession = new_profession
		print("the new profession is ", new_profession)

	profession = property(_get_profession, _set_profession) 

	def describe(self):
		print("the Personne's is: ", self.name, " and her user name is: ", self.email)

	#super(Personne, self).__init__()
	if __name__ == '__main__':
		pers1 = Personne("developper")
		pers1.describe()
		os.system("pause")