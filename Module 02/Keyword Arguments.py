def adder ( a,b,c ):
  print ( f"{a},{b},{c}" )

adder ( a=10, c=30, b=20)


def adder (**kwargs):
  print ( kwargs )

adder ( a=10, c=30, b=20, d=40, n_estimator=50)


def adder (**kwargs):
  for key, value in kwargs.items():
    print (f"key : {value}")
adder ( a=10, c=30, b=20, d=40, n_estimator=50)


