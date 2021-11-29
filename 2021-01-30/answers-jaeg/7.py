class FruitStand:
    def __init__(self, fruit_count, money, location):
        self.fruit_count = fruit_count
        self.money = money
        self.location = location
    
    def output(self):
        #prints all information about the fruit stand
        print(f"the fruit stand has {self.fruit_count} fruits")
        print(f"the fruit stand has {self.money} money")
        print(f"the fruit stand is located {self.location}")

    def sell_fruit(self, fruit_to_sell):
        #the function redefines the self.money variable by adding 5 times the amount of fruit there is to be sold, since fruit cost 5 money per
        self.money = self.money + (fruit_to_sell * 5)
    
    def recieve_fruit(self, amount_acquired):
        #adds the amount of fruit acquired to the self.fruit_count variable
        self.fruit_count = self.fruit_count + amount_acquired
        #subtracts the cost of the amount of fruit acquired from self.money
        self.money = self.money - (amount_acquired * 2)

    def change_location(self, new_location):
        #changes the self.location variable to the input of the method
        self.location = new_location

itu_fruitstand = FruitStand(50, 1000, 'next to itu')
itu_fruitstand.output()
print("the fruit stand now sells some fruit, buys some fruit, and changes location")
itu_fruitstand.sell_fruit(20)
itu_fruitstand.recieve_fruit(40)
itu_fruitstand.change_location('by amagerbro station')
itu_fruitstand.output()