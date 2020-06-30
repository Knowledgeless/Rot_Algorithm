#RotAlgorithm To Dcode A Text

class Decoding:

		# If user wants all the rot of 1-27 
	def usr_all(self, user_text):	#starting fuction

		user_text = user_text.lower()		
		result = []
		count = 0
		print("\n")

		for all_root in range(1,27):											# Loop to find next root text
			print("The result using rot {}: \t".format(all_root), end="")		# format of output design
			for loop in range(len(user_text)):									
				count = int(format(ord(user_text[loop]), "d"))					# getting text to decimal 
				if count+all_root > 122:										# checking is the unicode value above of z or not
					count = chr((count+96+all_root) - 122)						# calculating the value and taking to unicode from decimal
					result.append(str(count))									# making a list of all value 
					
				else:
					count = chr(count+all_root)								# adding the root number with the decimal value 
					result.append(str(count))								# making a list of all value

			for i in result:												# to show without ('')
				print(i, end="")
			print("")
			result = []


if __name__ == "__main__":

	try:
		while(True): 				# Options The Users Have 
			print('''
				\t------------------------------------
				\t\t--- Get Your Rot ---\t
				\t\t   Dcode Yourself \t
				\t------------------------------------

				1. Watch all the rot it can be.
				2. Help
				3. Exit

				''')

			choice = int(input("Your choice: "))

			
			if choice == 1:			# Get all the rot of given text. It will take a time.

				user_text = input("Enter your text: \n\t")			# Taking the input text only
				
				obj = Decoding()
				obj.usr_all(user_text)

			elif choice == 2:
				print('''
							\n\t\t\t\tHelp not found! LOL
			Input and ouput is only lower case value.\n''')		# Fun Message

			elif choice == 3:						# To Exit

				feedback = input("\n  [-] Ain't I Helpfull? (Y/n): ")		# Taking Feed Back Before Exit
				if feedback.upper() == "Y":
					print("\n\nThank You :)\n\n")
				elif feedback.upper() == "N":				# Asked To Inform About Bug Or Problem
					print("""\n\n
					Let me know what's the problem. 
				   Find me: https://github.com/Knowledgeless
						\n\n""")
				else: 
					print("\nDon't be angry, calm down, take breath and try again.\nGood Luck \n")
				break
			else:
				print("Choose an option from the given above...")

		# Handling the error

	except ValueError:
		print("\n\tCheck your given value and try again.\n")
	except KeyboardInterrupt:
		print("\n\n\tManually Exiting, Good Bye!\n")
