	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.
		
	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
	word_list = list(input.lower())

	#Checks if the last two letters of the word contains "p" and "y"
	if word_list[len(word_list)-1] == "y" and word_list[len(word_list)-2] == "p":
		return True
	else:
		return False

print(endsPy("hello"))
print(endsPy("ilovepy"))
print(endsPy("pyistasty"))
print(endsPy("welovepyforreal"))
print(endsPy("coolpY"))