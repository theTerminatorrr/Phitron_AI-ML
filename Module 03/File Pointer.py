with open ( "./sample_data/test.txt", "r") as file :
  print ( file.tell() )
  print (file.read())
  print ( file.tell() )
  # Last theke pora shuru korse...
  print (file.read())



with open("./sample_data/test.txt", "r") as file:
      print(file.tell())
      print(file.read(10))
      print(file.tell())

      print(file.read())
      print(file.tell())



# Seek
with open ( "./sample_data/test.txt", "r") as file :
  print ( file.tell() )
  print ( file.read ( 10 ) )
  print ( file.tell() )

  file.seek( 0 )

  print ( file.tell() )
  print ( file.read ( ) )
  print ( file.tell() )
