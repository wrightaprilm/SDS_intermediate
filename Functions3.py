import sys 

last_name = sys.argv[1]
key = sys.argv[2]

def filter_name(last_name, key):
	"""
	functions have a special kind of comment called a docstring. It is denoted
	with three quotes. These can be multi-line without including the quotes on 
	each line. These are just helpful comments at the novice level, but if you 
	plan to distribute code, are very important. See here for more: 
	http://www.pythonforbeginners.com/basics/python-docstrings 
	"""

        positives = []
        negatives = []
#Regular comments can be embedded in the text after a pound sign.
        for letter in last_name:
            if letter == key:
                positives.append(letter)
            else: 
                negatives.append(letter)
        return([positives, negatives])


def check_type(pos_list):
   assert type(pos_list) == list
   
   
if __name__ == '__main__':
    pos_list = filter_name(last_name,key)[1]
    check_type(pos_list)
