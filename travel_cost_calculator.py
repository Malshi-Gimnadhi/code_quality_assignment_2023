from csv import reader

# Create dictionaries to store the  data

hotelRates = {}
exchangeRates = {}
flightCosts = {}

# Load data from CSV files into the dictionaries

def loadHotelRates(file):
    with open(file) as hotelFile:
        csv_reader = reader(hotelFile)
        for row in csv_reader:
            hotelRates[row[0]] = float(row[1])

def load_exchangeRates(file):
    with open(file) as exchangeFile:
        csv_reader = reader(exchangeFile)
        for row in csv_reader:
            exchangeRates[row[0].upper()] = float(row[1])

def load_flightCosts(file):
    with open(file) as flightFile:
        csv_reader = reader(flightFile)
        for row in csv_reader:
            flightCosts[row[0]] = float(row[1])

def main():

    # Load data from CSV files into the dictionaries

H('data/hotelRates.csv')
    load_exchangeRates('data/exchangeRates.csv')
    load_flightCosts('data/flightCosts.csv')

    # Get user input for destination,duration

    destination = input("Enter your destination: ").upper()
    flight_cost = flightCosts.get(destination, 0.0)
    hotel_cost_per_day = hotelRates.get(destination, 0.0)

    days = int(input("Enter your stay duration in days: "))
    hotel_cost = hotel_cost_per_day * days
    total_cost = flight_cost + hotel_cost

    print(f"Flight cost: USD {flight_cost:.2f}")
    print(f"Hotel cost for {days} days: USD {hotel_cost:.2f}")
    print(f"Total: USD {total_cost:.2f}")

    # Get user input for the currency selection

    currencies = ', '.join(exchangeRates.keys())
    selected_currency = input(f"Select your currency for final price estimation ({currencies}): ")

    exchange_rate = exchangeRates.get(selected_currency, 1.0)
    price_in_selected_currency = total_cost * exchange_rate
    print(f"Total in {selected_currency}: {price_in_selected_currency:.2f}")

if __name__ == "__main__":
    main()
