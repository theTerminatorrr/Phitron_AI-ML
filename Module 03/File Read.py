file = open ( "Sample.txt", "r")

content = file.read()

print ( content )
print ( type(content ))
print ( file.closed )
print ( "\n" )

file = open ( "Sample.txt", "r")
content = file.readlines()

print ( content )
print ( type(content ))
file.close ()

print ( file.closed )
print ( "\n" )


with open ( "Sample.txt", "r") as file :
  content = file.readlines()
  print ( content )

print ( file.closed )



print ( "\n" )
with open ( "./sample_data/Sample.txt", "r") as file :
  for line in file :
    print ( line, end = "" )
