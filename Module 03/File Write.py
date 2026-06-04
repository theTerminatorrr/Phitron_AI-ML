with open ( "/test.txt", "w") as file :
  file.write ( " Bhalo acho Bondhu? \n")
  file.write ( " Poralekha kemon cole? ")

#with existing file
with open ( "/test.txt", "w") as file :
  file.write ( " Learning with Phitron is going fast....\n")
  file.write ( " But amar to bhalo lage naaa reeeee! \n")

#no overwriting, just Append
with open ( "/test.txt", "a") as file :
  file.write ( " The learning of AI ML is fun. \n")
  file.write ( " I'm enjoying. ")

strings = ['Hello', ' hi', ' good bye ']
with open ( "/test2.txt", "a") as file :
  file.writelines( strings )

