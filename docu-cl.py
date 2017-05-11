import subprocess

# I added a feature

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

def main():
	f = open("letter.txt", "r")
	content = f.read()
	f.close()

	date = raw_input("What is the date of the letter? : ")
	address = raw_input("What is the address of the job? : ")
	greeting = raw_input("Who are you sending this out to? : ")
	position = raw_input ("What is the position? : ")
	place_of_position = raw_input("What is the place you want to work? : ")
	posting_origin = raw_input("Where did you find this posting? : ")
	interest = raw_input("Why are you interested in this job? : ")
	name = raw_input("What is your name? : ")

   	templates = [
	   	["Do you want to include your current experience? [ y | n ]?", "queery.txt", "[QUEERY]"],
	   	["Do you want to include your NDS experience? [ y | n ]?]", "nds.txt", "[NDS]"],
	   	["Is this a leadership position? [ y | n ]?", "cassa.txt", "[CASSA]"], 
	   	["Do you need to add clinical experience? [ y | n ]?", "distress.txt", "[DISTRESS]"],
	   	["Does this involve working with children? [ y | n ]?", "kids.txt", "[KIDS]"]
   	]

   	for template in templates:
   		prompt = raw_input(template[0])
   		if prompt.lower() == 'y' or prompt.lower() == 'yes' :
   			updatedContent = open(template[1])
   			current_content = updatedContent.read()
   			updatedContent.close()
   			content = content.replace(template[2], current_content)
   		else:
   			content = content.replace(template[2], " ")


	save_name = raw_input("Name your output file : ")

	content = content.replace("[DATE]", date)
	content = content.replace("[ADDRESS]", address)
	content = content.replace("[GREETING]", greeting)
	content = content.replace("[POSITION]", position)
	content = content.replace("[PLACE OF POSITION]", place_of_position)
	content = content.replace("[POSTING ORIGIN]", posting_origin)
	content = content.replace("[INTEREST]", interest)
	content = content.replace("[NAME]", name)
	print(content)

	output = open(save_name + ".txt", "w+")
	output.write(content)
	write_to_clipboard(content)
	output.close()

if __name__ == '__main__':
	main()