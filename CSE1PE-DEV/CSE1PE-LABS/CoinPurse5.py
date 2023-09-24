# CSE1PE Week 5 Exercise: Coin Purse
# Define the CoinPurse class here
# 1 Constructor, 2 methods(add_coin, print_information)
# Constructor - Set name of purse owner and initalise coin value to 0.

class CoinPurse:
    def __init__(self, name):
        self.name = name
        self.total_value = 0
    def add_coin(self, value):
        self.total_value += value
    def print_information(self):
        print(f"{self.name} has {self.total_value} cents.")
name = input('Enter owner name: ')
purse = CoinPurse(name)
while True:
    value = int(input('Enter coin value (cents): '))
    if value <= 0:
        break
    purse.add_coin(value)
purse.print_information()

# WORST ONE YET - Gonna KMS
# Define the CoinPurse class here
class CoinPurse:
    def __init__(self, name):
        self.name = name
        self.total_value = 0
    def add_coin(self, value):
        self.total_value += value
    def print_information(self):
        print(str(self.name)+ " has " + str(self.total_value)+" cents")

name = input('Enter owner name: ')
purse = CoinPurse(name)
while True:
    value = int(input('Enter coin value (cents): '))
    if value <= 0:
        break
    purse.add_coin(value)
purse.print_information()