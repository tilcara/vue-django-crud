class Puta(object):

	def __init__(self, nombre, edad, genero, cache):
		self.nombre = nombre
		self.edad = edad
		self.genero = genero
		self.cache = cache

	def __str__(self):
		return self.nombre

if __name__ == '__main__':
	puta1 = Puta('ariel rebel', 22, 'Fem', 200)
	print(puta1.cache)
		