import random

class Seedes():
    def __init__(self, name, type, plantMonths, harvestMonths, growthTime, price, globalSupply, globalDemand):
        self.name = name
        self.type = type
        self.plantMonths = plantMonths
        self.harvestMonths = harvestMonths
        self.growhthTime = growthTime
        self.price = price
        self.globalSupply = globalSupply
        self.globalDemand = globalDemand
        
    def priceChange(self, sellBuyAmount):
        self.price = self.price * (self.globalDemand-(self.globalSupply * sellBuyAmount))/self.globalDemand
        