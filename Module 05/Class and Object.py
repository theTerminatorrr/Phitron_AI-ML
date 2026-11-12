class Phone :
  category = "Electronics"

  #Constructor

  def __init__(self, model, battery, camera ) :
    self.model = model
    self.battery = battery
    self.camera = camera


Apple = Phone( "BB 12", 2400, 48)
BlueBerry = Phone( "BB 12", 2400, 32)
Motorola = Phone( "Edge 70", 3500, 108)

print ( Apple.camera)
print ( BlueBerry.model)
print ( Motorola.battery)