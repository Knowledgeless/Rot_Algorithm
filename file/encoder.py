
class Encoding:
	def usr(self, user_text, user_root):	#starting function
		user_text = user_text.lower()
		result = []
		
		for loop in range(len(user_text)):
			counter = int(format(ord(user_text[loop]), 'd'))
				
			if counter - user_root < 97:
				a1 = counter - user_root		# encoding calculation
				counter = 122 - (96-a1)
				result.append(counter)
					
			else: 
				counter = counter - user_root
				result.append(counter)

		print("\n\tYour Encoded Text => ", end="")
		for show in result:
			print(chr(show), end="")
		print("\n")