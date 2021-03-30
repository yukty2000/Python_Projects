
# Madlibs is a game where a paragraph with blanks is given and the user fills it up with words
# of his choice 

noun1 = input("Noun - ")
verb1 = input("Verb - ")
noun2 = input("Noun - ")
noun3 = input("Noun - ")
adj1 = input("Adjective - ")
verb2 = input("Verb - ")
verb3 = input("Verb - ")
adj2 = input("Adjective - ")


madlib = f"Today I went to the zoo. I saw a \
{noun1} jumping up and down in its tree. He {verb1} through the large tunnel  that led to its {noun2}. \
I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. \
Feeding that animal made me hungry. I went to get a {adj1} scoop of ice cream. It filled my stomach. \
Afterwards I had to {verb2} to catch our bus. When I got home I {verb3} my mom \
for a {adj2} day at the zoo. "

print(madlib)