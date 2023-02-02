import random

# List of strings on a standard guitar
string_names = ['e', 'a', 'd', 'g', 'b', 'e']
# list of frets on the guitar
fret_numbers = range(0, 12)

# list of the note names
note_names = ["a", "a sharp", "b", "c", "C sharp", "d", "d sharp", "e", "f", "f sharp", "g", "g sharp"]


# Continuously run the CLI script
# to asks a question after question 
while True:
	# Select a random string and fret number from the guitar
	selected_string = random.choice(string_names)
	selected_fret = random.choice(fret_numbers)
	# Calculate what that note would be
	root_num = note_names.index(selected_string)
	correct_note = note_names[((root_num +  selected_fret) % 12)]
	# Let the user guess to see if they know the answer
	user_guess = input("What is the note at " + selected_string + str(selected_fret))
	# Validate the user's guess and check if it was correct
	# if it is not, then tell the user what the correct answer was
	if (user_guess == correct_note):
		print("correct")
	else:
		print("Incorrect. " + selected_string + str(selected_fret) + " is " + correct_note)