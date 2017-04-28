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
	
	prompt = raw_input(" Do you want to include your current experience? [ y | n ]? ")
	if prompt.lower() == 'y' or prompt.lower() == 'yes' :
   		current_Position = open("queery.txt", "r")
   		currentContent = current_Position.read()
   		current_Position.close()
   		content = content.replace("[QUEERY]", currentContent)
   	else:
   		content = content.replace("[QUEERY]", " ")

	prompt = raw_input(" Do you want to include your NDS experience? [ y | n ]? ")
	if prompt.lower() == 'y' or prompt.lower() == 'yes' :
   		research = open("nds.txt", "r")
   		researchContent = research.read()
   		research.close()
   		content = content.replace("[NDS]", researchContent)
   	else:
   		content = content.replace("[NDS]", " ")

	prompt = raw_input(" Is this a leadership position? [ y | n ]? ")
	if prompt.lower() == 'y' or prompt.lower() == 'yes' :
   		leadership = open("cassa.txt", "r")
   		leadershipContent = leadership.read()
   		leadership.close()
   		content = content.replace("[CASSA]", leadershipContent)
   	else:
   		content = content.replace("[CASSA]", " ")
	
	prompt = raw_input(" Do you need to add clinical experience? [ y | n ]? ")
	if prompt.lower() == 'y' or prompt.lower() == 'yes' :
   		clinical = open("distress.txt", "r")
   		clinicalContent = clinical.read()
   		clinical.close()
   		content = content.replace("[DISTRESS]", clinicalContent)
   	else:
   		content = content.replace("[DISTRESS]", " ")

   	prompt = raw_input(" Does this involve working with children? [ y | n ]? ")
	if prompt.lower() == 'y' or prompt.lower() == 'yes' :
   		children = open("kids.txt", "r")
   		childrenContent = children.read()
   		children.close()
   		content = content.replace("[KIDS]", childrenContent)   
   	else:
   		content = content.replace("[KIDS]", " ")	

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
	output.close()

if __name__ == '__main__':
	main()