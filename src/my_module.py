# I know this code isn't really organized in the most correct way,
# but since it's a small challenge I believe it makes it easier to a human read and
# make out it's logic by containing everything to only one file
class Hotel:
    def __init__(self, name, weekday_fees, weekend_fees, rating):
        self._name = name
        self._weekday_fees = weekday_fees
        self._weekend_fees = weekend_fees
        self._rating = rating

    @property
    def name(self):
        return self._name
    
    @property
    def weekday_fees(self):
        return self._weekday_fees

    @property
    def weekend_fees(self):
        return self._weekend_fees

    @property
    def rating(self):
        return self._rating

def get_cheapest_hotel(input):

    lakewood = Hotel('Lakewood', {"Regular": 110, "Rewards": 80}, {"Regular": 90, "Rewards": 80}, 3)
    bridgewood = Hotel('Bridgewood', {"Regular": 160, "Rewards": 110}, {"Regular": 60, "Rewards": 50}, 4)
    ridgewood = Hotel('Ridgewood', {"Regular": 220, "Rewards": 100}, {"Regular": 150, "Rewards": 40}, 5)

    hotels = [lakewood, bridgewood, ridgewood]

    weekdays = ['mon', 'tues', 'wed', 'thur', 'fri']

    customer_type = input.split(':')[0]
    customer_stay_dates = [date.strip() for date in input.split(':')[1].split(',')]

    num_weekdays = 0
    num_weekend = 0

    for stay_date in customer_stay_dates:
        if stay_date[stay_date.find("(")+1:stay_date.find(")")] in weekdays:
            num_weekdays += 1
        else:
            num_weekend += 1

    cheapest_hotel = {'name': None, "total_cost": 0, "rating": 0}

    for hotel in hotels:
        if hotels.index(hotel) == 0:
            cheapest_hotel['name'] = hotel.name
            cheapest_hotel['total_cost'] = hotel.weekday_fees[customer_type]*num_weekdays + hotel.weekend_fees[customer_type]*num_weekend
            cheapest_hotel['rating'] == hotel.rating
        
        current_cost = hotel.weekday_fees[customer_type]*num_weekdays + hotel.weekend_fees[customer_type]*num_weekend

        if current_cost < cheapest_hotel['total_cost']:
            cheapest_hotel['name'] = hotel.name
            cheapest_hotel['total_cost'] = current_cost

        if current_cost == cheapest_hotel['total_cost']:
            if hotel.rating > cheapest_hotel['rating']:
                cheapest_hotel['name'] = hotel.name
                cheapest_hotel['total_cost'] = current_cost
                cheapest_hotel['rating'] == hotel.rating
            pass

    return cheapest_hotel['name']