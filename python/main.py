def createBackground(position,backdrop,vertical,backdrop_edit):
	backdrop_num = 0
	for x in range (1,8):
		print(backdrop_num)
		if backdrop_num == vertical:
			print(backdrop_edit)
		else:
			print(backdrop)
		backdrop_num += 1

def movement(position,vertical,horizontal,backdrop_edit):
	while True:
		backdrop = ["0","0","0","0","0","0","0","0"]
		backdrop_edit = ["0","0","0","0","0","0","0","0"]
		keyboard_input = input("Next move: ")
		if keyboard_input == "d":
			horizontal += 1
			backdrop_edit[horizontal] = "1"
		elif keyboard_input == "a":
			horizontal -= 1
			backdrop_edit[horizontal] = "1"
		elif keyboard_input == "s":
			vertical += 1
			backdrop_edit[horizontal] = "1"
		elif keyboard_input == "w":
			vertical -= 1
			backdrop_edit[horizontal] = "1"
		print("vertical:" + str(vertical) + "horizontal: " + str(horizontal))
		createBackground(position,backdrop,vertical,backdrop_edit)

backdrop = []
backdrop_edit = []
vertical = 0
horizontal = 0

movement(backdrop,vertical,horizontal,backdrop_edit)
