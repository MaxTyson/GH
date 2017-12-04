''' Напишіть програму в стилі ООП, що задовольняє наступним умовам: у програмі повинні бути
два класи та два об"єкта, що належать різним класам; один об"єкт за допомогою методу свого 
класу повинен так чи інакше змінювати дані іншого об"єкта '''

class Fighter:
	''' Make symple fighter '''
	def __init__(self, nickname, level, health):
		self.nickname = nickname
		self.level = 1
		self.health = 100
		
	def showFighter(self):
		''' Show some info about fighter '''
		print('{}: heals - {}%, level - {}.\n'.format(self.nickname, self.health, self.level))

class SuperFighter(Fighter):
	''' Make symple fighter '''
	def __init__(self, nickname, level, health, race):
		Fighter.__init__(self, nickname, level, health)
		self.race = race
	def levelUp(self):
		''' Method changes fighter's level '''
		self.level += 1
	def damage(self):
		''' Method changes fighter's heals '''
		self.health -= 10
		if self.health <= 0:
			print(self.nickname + ' lost!')

''' Examples '''
man = SuperFighter('Jeki Chan', 2, 100, 'Asian')
man.showFighter()
man.levelUp()
man.damage()
man.showFighter()
man.damage()
man.showFighter()