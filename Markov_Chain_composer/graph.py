# This will create a Markov graph ( words connected to words that follow then like vertices of a graph with weighted edges)

import random

# Vertex object

class Vertex : 
	def __init__(self, value) :
		self.value = value
		# dictionary to store adjacent vertices and weights of edges to these vertices
		self.adjacent = {}

	def add_edge(self, vertex, weight = 1) :
		self.adjacent[vertex] = weight

	def increment_edge(self, vertex) :
		self.adjacent[vertex] = self.adjacent[vertex] + 1

	# We get the next word based on weights - special random.choice
	def next_word(self) :
		# random choices in this case returns a list of 1 item
		 return random.choices(list(self.adjacent.keys()) , weights = list(self.adjacent.values()))[0]

# Graph object

class Graph :
	def __init__(self) :
		self.vertices = {}

	def get_vertex_values(self):
		return set(self.vertices.keys())

	# Create a new vertex
	def add_vertex(self, value):
		if value not in self.vertices.keys():
			self.vertices[value] = Vertex(value)

	# returns the vertex object with the specified value
	def get_vertex(self,value) :
		if value not in self.vertices.keys():
			self.add_vertex(value)
		return self.vertices[value]

	




# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.keys()

# print(list(x))
