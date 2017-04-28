def main():
	f = open("letter.txt", "r")
	content = f.read()
	f.close()

	date = raw_input("What is the date of the letter? : ")
	address = raw_input("What is the address of the job? :")
	greeting = raw_input("Who are you sending this out to? :")
	position = raw_input ("What is the position? : ")
	place_of_position = raw_input("What is the place you want to work? :")
	posting_origin = raw_input("Where did you find this posting? :")
	interest = raw_input("Why are you interested in this job? :")
	save_name = raw_input("Name your output file: ")

	content = content.replace("[DATE]", date)
	content = content.replace("[ADDRESS]", address)
	content = content.replace("[GREETING]", greeting)
	content = content.replace("[POSITION OF POSITION]", place_of_position)
	content = content.replace("[POSTING ORIGIN]", posting_origin)
	content = content.replace("[INTEREST]", interest)
	print(content)

	output = open(save_name + ".txt", "w+")
	output.write(content)
	output.close()

if __name__ == '__main__':
	main()