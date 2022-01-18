import re


file_read = open('fives.txt', "r")
lines = file_read.readlines()

text_match = input("What string do you have so far: ")
pattern = re.compile(text_match)

yellow = input("Are there any yellow letters: ")
yellow_group = ""
if yellow:
	for char in yellow:
		yellow_group += "(?=.*" + char + ")"
print(yellow_group)

greys = input("Are there any grey letters: ")
grey_group = ""
if greys:
	for char in greys:
		grey_group += "(?!.*" + char + ")"
print(grey_group)

others = yellow_group + grey_group
o_pattern = re.compile(others)

for line in lines:
	# print("**")
	match = pattern.match(line)
	# the initial pattern matches
	if match:
		# there are grey or yellow letters
		if o_pattern:
			match_2 = o_pattern.match(line)
			if match_2:
				print(line, end='')
		# there are no yellow letters
		else:
			print(line, end='')
