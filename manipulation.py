str_manip = input("Enter the sentence: The wind whispered secrets through the tall green trees")
print(len(str_manip))
last_letter = str_manip[-1]
print(str_manip.replace(last_letter, "@"))
print(str_manip[-3:][::-1])
print(str_manip[0:3] + str_manip[-2:])