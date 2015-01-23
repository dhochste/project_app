import re

def model_music(input_string,model):
	"""
	Runs the gensim Doc2Vec model with the input string after parsing for
	positive and negative terms
	"""
	# Convert from unicode to strings
	add_str = str(input_string[0])
	sub_str = str(input_string[1])

	# parse strings for actual terms
	add_terms = re.findall(r'(\w+)[,\s]*', add_str)
	sub_terms = re.findall(r'(\w+)[,\s]*', sub_str)

	# make everything lower-case:
	add_terms = [x.lower() for x in add_terms]
	sub_terms = [x.lower() for x in sub_terms]

	# add_terms = ['hard','rock']
	# sub_terms = []
	results = model.most_similar_cosmul(positive= add_terms, 
		negative=sub_terms, topn=10)

	return results