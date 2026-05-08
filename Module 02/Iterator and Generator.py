s = { 10, 20, 30, 40, 50}
s_iter = iter(s)
print ( next (s_iter ) )
print ( next (s_iter ) )
print ( next (s_iter ) )
print ( next (s_iter ) )
print ( next (s_iter ) )

print ( "\n" )
for i in s :
  print ( i )



list = [ x for x in range (500) ]
print ( list )



list = [ x for x in range (500) ]
print ( list )

def data_loader (chunk_size, list) :
  for i in range ( 0, len(list) ,chunk_size ):
    yield list [ i : i+chunk_size ]

x = data_loader ( 5, list )
print  ( next (x) )
print  ( next (x) )
print  ( next (x) )