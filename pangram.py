import string
def isPangram(str):

	alphabet="abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
    		    return False
	return True

string = input()
if(isPangram(string) == True):
	print("pangram")
else:
	print("no")