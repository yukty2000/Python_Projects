
# This is a beginner project - we could make it more intelligent by choosing our next word bad=sed on 3 previous words and so on

import string
import graph
import random

# Read text from file
def get_words_from_text(text_path) :

	# read text from the file specified in the text_path
	with open(text_path , "r") as f:
		text = f.read()

	# Pre processing the text
	text = ' '.join(text.split()) # this turns whitespaces into single space

	# convert text to lower case to make comparision easy
	text = text.lower()

	# remove all punctuations
	text = text.translate(str.maketrans('','',string.punctuation))

	words = text.split()
	return words

# Make a markov graph from the list of words
def make_graph(words) :

	G = graph.Graph()
	prev = words[0]
	prev = G.get_vertex(prev)

	for i in range(1,len(words)) :
		next_vertex = G.get_vertex(words[i])
		if words[i] in prev.adjacent.keys():
			prev.increment_edge(words[i])
		else :
			prev.add_edge(words[i])

		prev = next_vertex

	return G

# Compose a chain of x words from the given markov graph G
def compose_chain(G , x):

	markov = []
	prev = random.choice(list(G.vertices.keys()))
	markov.append(prev)
	x -= 1
	
	while (x>0) :
		prev = G.get_vertex(prev)
		next_word = prev.next_word()
		markov.append(next_word)
		prev = next_word

		x -= 1

	markov = ' '.join(markov)
	return markov

def main() :
	# get words from text 
	words = get_words_from_text('texts/hp_sorcerers_stone.txt')

	# make a graph using these words
	G = make_graph(words)

	# print x words ( x is users choice )
	x = int(input("Enter number of words to print - "))
	markov = compose_chain(G,x)

	print(markov)

main()
