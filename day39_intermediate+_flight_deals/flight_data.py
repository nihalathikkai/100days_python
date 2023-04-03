class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, flyFrom, flyTo, cityFrom, cityTo, local_arrival, local_departure):
        self.price = price
        self.flyFrom = flyFrom
        self.flyTo = flyTo
        self.cityFrom = cityFrom
        self.cityTo = cityTo
        self.local_arrival = local_arrival
        self.local_departure = local_departure