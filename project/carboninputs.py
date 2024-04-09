class Inputs:

    def __init__(self, energy, waste, travel):
        self.energy = energy
        self.waste = waste
        self.travel = travel


    def energy_usage():

        while True:
            try:
                electricity_bill = int(input("please inter the amount of electricity bill per a month min 0 max 50 : "))
                assert 0<= electricity_bill <= 50 , "the electricity bill must be between 0 and 50 : "

                gas_bill = int(input("please inter the amount of gas bill per a month min 0 max 50 : "))
                assert  0 <= gas_bill <=50, "careful the input should be at the range"

                fuel_bill = int(input("please inter the amount of fuel bill per a month min 0 max 500 : "))
                assert 0 <= fuel_bill<= 500, "mind the conditions"


                months = 12
                energy = electricity_bill*months*0.0005 + gas_bill*months*0.0053 + fuel_bill*months*2.32
                return int(energy)

            except ValueError:
                print("your input has to be integer")
            except AssertionError as instruction:

                print("please re enter your input",instruction)


    def wastes():
        while True:
            try:
                generated = int(input("please enter the amount of generated material per a month between 0 and 100 in pound : "))
                assert 0 <= generated <=100, "please read the range"
                recycled = int(input("please enter the amount of recycled material between 0 to 100 per a month : "))
                assert 0 <= recycled <=100, "please read the range"
                composed = int(input("please enter the amount of composed material from 0 to 100 per a month : "))
                assert 0 <= composed <=100, "please read the range"
                months = 12
                waste = generated*months*0.57 - recycled+composed
                return int(waste)
            except ValueError:
                print("your inputs have to be integer please try again")
            except AssertionError as message:
                print("try again", message)
            

    def business_travel():
        while True:
            try:
                km_travels = int(input("please enter the amount of traveled km from 0 to 100 : "))
                assert 0 <= km_travels <=100, "plesae read the range of km travels"
               
                fuel_in_100km = int(input("please enter the amount of fuel bill per 100km from 0 to 100 : "))
                assert 0 <= fuel_in_100km <=100, "please read the range of fuel in 100km"
                if km_travels and fuel_in_100km != 0:
                    formula = km_travels*1/fuel_in_100km * 2.31
                    return int(formula)
                else:
                    return 0
            except ValueError:
                print("watch out for your inputs it must be integer")
            except AssertionError as caution:
                print("try again!", caution)
