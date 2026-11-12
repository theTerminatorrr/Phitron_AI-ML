class Phone:
    category = "Electronics"

    # Constructor
    def __init__(self, model, battery, camera, battery_percentage=100):
        self.model = model
        self.battery = battery
        self.camera = camera
        self.battery_percentage = battery_percentage

    def charge(self, hour):
        self.battery_percentage = min(100, self.battery_percentage + hour * 10)
        print(f"Charge completed for {self.model}. Battery: {self.battery_percentage}%")

    def capture(self, photo):
        if self.battery_percentage <= 0:
            print("No charge. Cannot take photo.")
        else:
            self.battery_percentage = max(0, self.battery_percentage - photo)
            print(f"Photo captured on {self.model}. Battery: {self.battery_percentage}%")


class Cooling_Mechanism:
    def __init__(self, cooling_method):
        self.cooling_method = cooling_method

    def cooling_on(self):
        print(f"The system is being cooled by {self.cooling_method}")


class SmartPhone(Phone):
    def __init__(self, model, battery, camera, processor):
        super().__init__(model, battery, camera)
        self.processor = processor

    def charge(self, hour):
        print("Fast charging in progress...")
        super().charge(hour)

apple    = Phone("iPhone 17", 3000, 40)
blueberry = Phone("B-17", 4000, 30)
motorola  = Phone("M-17", 3500, 35)

apple.capture(10)
print(motorola.battery_percentage)

print(apple.camera)
print(blueberry.model)
print(motorola.battery_percentage)

pro = SmartPhone("X", 5000, 100, "SnapDragon")
print(pro.model)
pro.charge(1)

