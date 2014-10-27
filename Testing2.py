import sys
last_name = sys.argv[1]
key = sys.argv[2]

def filter_name(filter_list, key):
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
        for letter in filter_list:
            if letter == key:
                positives.append(letter)
            else: 
                negatives.append(letter)
        print negatives
        return([positives, negatives])
        
def check_type(pos_list):
   assert type(pos_list) == list
   
def check_input(last_name):
     new_list = []
     last_name = list(last_name)
     for letter in last_name:
        try:
            new_list.append(int(letter))
        except:
            pass
     for val in new_list:
        if str(val) in last_name:
            last_name.remove(str(val))
     return(last_name)
    
if __name__ == '__main__':
    filter_list = check_input(last_name)
    pos_list = filter_name(filter_list, key)[1]
    check_type(pos_list)
