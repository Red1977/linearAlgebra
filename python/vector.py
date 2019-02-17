#!/usr/bin/python

from math import sqrt
from math import arccos

class Vector(object):
	"""Generic vec3 for point vector normal etc."""
	def __init__(self, coordinates):
		super(Vector, self).__init__()
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('Must supply coordinates')

		except TypeError:
			raise TypeError('Coordinates must be iterable list')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, v):
		return self.coordinates == v.coordinates

	def __add__(self, v):
		return [x + y for x,y in zip(self.coordinates,v.coordinates)]

	def __sub__(self, v):
		return [x - y for x,y in zip(self.coordinates,v.coordinates)] 

	def mag(self):
		coordsSquared = [x**2 for x in self.coordinates]
		return sqrt(sum(coordsSquared))

	def normalise(self):
		mag = self.mag()
		if mag > 0.:
			return [x * 1./mag for x in self.coordinates]
		else:
			print('Cant normalise zero vector')
			return [0.,0.,0.]


	def dot(self, v):
		#implement dot product
		pass

	def angle(self, v):
		#implement angle between vectors
		pass
