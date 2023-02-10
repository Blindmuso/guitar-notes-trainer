import random
# Ask the user which string they would like to practice
chosen_string = input("Which string to practice (e, a, d, g, b, e or all")
# Ask the user how many frets they would like to practice
chosen_max_frets = int(input("How many frets? "))

# list of frets on the guitar
fret_numbers = range(0, chosen_max_frets + 1)

# list of the note names
# Two variables have been made to allow for the notes that can be called
# either sharp or flat
note_names_with_sharps = ["a", "a sharp", "b", "c", "c sharp", "d", "d sharp", "e", "f", "f sharp", "g", "g sharp"]
note_names_with_flats = ["a", "b flat", "b", "c", "d flat", "d", "e flat", "e", "f", "g flat", "g", "a flat"]


# Continuously run the CLI script
# to asks a question after question 
while True:
	# Select a random string and fret number from the guitar
	selected_string = random.choice(string_names)
	selected_fret = random.choice(fret_numbers)

	# make the exception if one string was chosen 
	if (chosen_string != "all"):
		selected_string = chosen_string

	# Calculate what that note would be
	root_num = note_names_with_sharps.index(selected_string)
	correct_note_with_sharps = note_names_with_sharps[((root_num +  selected_fret) % 12)]  
	correct_note_with_flats  = note_names_with_flats[((root_num + selected_fret) % 12)]
	# Speak the question to the user and let them guess
	question = "What is the note at " + selected_string + str(selected_fret) + "? "

	user_guess = input(question)
	# Validate the user's guess and check if it was correct
	# if it is not, then tell the user what the correct answer was
	if ((user_guess == correct_note_with_sharps) or (user_guess == correct_note_with_flats)):
		print("correct")
	else:
		if ("sharp" in correct_note_with_sharps):
			print("Incorrect. " + selected_string + str(selected_fret) + " is " + correct_note_with_sharps + " or " + correct_note_with_flats)
		else:
			print("Incorrect. " + selected_string + str(selected_fret) + " is " + correct_note_with_sharps)