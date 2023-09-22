import csv

# Create dictionaries to store data

discounts = {}
taxRates = {}
promotions = {}
currencyRates = {}
inventory = {}

# Load discount data from CSV file

def loadDiscounts(file):
    with open(file) as discountFile:
        reader = csv.reader(discountFile)
        for row in reader:
            discounts[row[0].upper()] = float(row[1])

# Load tax rate data from CSV file

def loadTaxRates(file):
    with open(file) as taxFile:
        reader = csv.reader(taxFile)
        for row in reader:
            taxRates[row[0].upper()] = float(row[1])

# Load promotion data from CSV file

def loadPromotions(file):
    with open(file) as promotionFile:
        reader = csv.reader(promotionFile)
        for row in reader:
            promotions[row[0]] = float(row[1])

# Load currency rate data from CSV file

def loadCurrencyRates(file):
    with open(file) as currencyFile:
        reader = csv.reader(currencyFile)
        for row in reader:
            currencyRates[row[0].upper()] = float(row[1])

# Load inventory data from CSV file

def loadInventory(file):
    with open(file) as inventoryFile:
        reader = csv.reader(inventoryFile)
        for row in reader:
            inventory[row[0].upper()] = int(row[1])

def main():

    # Load data from CSV files into dictionaries

    loadDiscounts('data/discounts.csv')
    loadTaxRates('data/taxRates.csv')
    loadPromotions('data/promotions.csv')
    loadCurrencyRates('data/currencyRates.csv
