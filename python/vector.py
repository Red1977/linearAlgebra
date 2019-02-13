#!/usr/bin/python

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

mvVec = Vector([1.2, 2.5, 6.3])
print mvVec