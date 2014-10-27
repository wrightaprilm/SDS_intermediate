
# coding: utf-8

# #Functions
# 
# One of the main theme in this bootcamp is the structure of how software can be organized. Functions provide structure for our code, and provide small, simple blocks of code that can be tested (more on this in a bit) The basic idea of a function is like that of an organ in the body: a unit that does a particular task and returns a defined output. Take a minute and look at the below code:
# 

# In[4]:

last_name = ['w','r','i','g','h','t']
test_letter = 'g'
         
positives = []
negatives = []
for letter in last_name:
    if letter == test_letter:
         positives.append(letter)
    else:
         negatives.append(letter)

print positives


# Odds are, we will not want to sit at the command line and type this in every time we need to filter a list. What we're going to do in this module is learn how to take this bit of code, functionize it, save it to a script and make it more generalizeable to different lists and search keys. First, open your graphical text editor and paste in the code.
# 
# A function is defined in the following way:
# 
# ```
# def name_of_function():
# 	code goes here
# ```
# 
# The def() statement tells you the name of the function. In the parenthesis, we can put arguments, or information the function needs. We'll come back to this in a second. Our functionized code, in a clunky way in which you shouldn't write functions, could look like so:
# 

# In[6]:

last_name = ['w','r','i','g','h','t']
key = 'g'

def filter_name(last_name, key):
	positives = []
	negatives = []
	for letter in last_name:
		if letter == key:
			positives.append(letter)
		else: 
			negatives.append(letter)
	return([positives, negatives])


# That last line is called a return statement. It tells Python what we'd like to receive back. This is different than a print statement, as we are creating an object that can be used by other functions, not simply displaying information. The return statement ends a function.
# 

# In[7]:

filter_name(last_name, key)


# In[ ]:



# Time for a break. Here's a break time exercise. 
# + Move one of the variables inside the function. How does this change what arguments the function requires?
# + Save the output of the function to a variable. How can we break apart the two lists? How might we change the function if we only needed one list?
# + What if we want to provide a different list of letters? Try it!
# 
# Use the cell below to test your ideas.

# In[ ]:



