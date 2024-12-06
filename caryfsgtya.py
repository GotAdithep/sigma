class Car:
    def __init__(self, gas, burning_gas_rate):
        self.gas = gas
        self.burning_gas_rate = burning_gas_rate

    def get_gas(self):
        return self.gas
    def set_gas(self,set_gas):
        self.gas = set_gas
    def get_burning_rate(self):
        return self.burning_gas_rate
    def set_burning_rate(self,burning_gas_rate):
        self.burning_gas_rate = burning_gas_rate

    def drive(self, distance):
        used_gas = distance/self.burning_gas_rate
        self.gas = self.gas - used_gas
        return self.gas

    def fill_gas(self, new_gas):
        self.gas = self.gas + new_gas

    def __str__(self):
        return f"Gas: {self.gas}, Burning rate: {self.burning_gas_rate}"

skibidi = Car(1000,50)
while True:
    choice = int(input(f"drive (1), fillgas (2), setgas (3), or Exit (0): "))
    if choice == 0:
        break
    elif choice == 1:
        amount = float(input("Enter your drive distance: "))
        skibidi .drive(amount)
        print(skibidi)
    elif choice == 2:
        amount = float(input("Enter your gas fill: "))
        skibidi .fill_gas(amount)
        print(skibidi)
    else:
        amount = float(input("Enter your update amount: "))
        skibidi .set_gas(amount)
        print(skibidi)