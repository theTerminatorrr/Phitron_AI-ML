def adder ( a,b,c ):
  print ( f"{a},{b},{c}" )

adder ( 10, 30, 20)


def adder ( *args ):
  print ( args )

adder ( 10, 20, 30, 40, 50)



def adder ( *args ) :
  for i in args :
    print ( i )

adder ( 10, 20, 30, 70 )

