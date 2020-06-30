

try:
	from file import encoder as encode
	from file import decoder as decode


	while True:
		print('''\n
					Rot Text Encoding/Decoding
				-----------------------------------------
					1. Encode
					2. Dcode
					3. Exit
				-----------------------------------------
					''')

		choice = int(input("[+] Choose An Option: "))
		if choice == 1: 
			obj = encode.Encoding()
			user_text = input("Enter your text: ")
			user_root = int(input("Enter the root: "))
			obj.usr(user_text, user_root)

		elif choice == 2:
			obj = decode.Decoding()
			user_text = input("Enter your text: ")
			obj.usr_all(user_text)

		elif choice == 3 or choice.lower == 'exit':
			print('\nGood Bye...\n')
			break

		else:
			print("\nWrong Input, Try Again..!\n")

except ImportError:
	print('''\n
			You Messed Up With Files.
			Keep Files As It Is.\n 
		''')
except KeyboardInterrupt:
	print("\nAbort...\n")
except ValueError:
	print("\nBe Cool & Try Again...\n")
