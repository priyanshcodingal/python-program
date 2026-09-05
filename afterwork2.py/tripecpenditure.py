def hotel_cost(nights):
    return 140 * nights

def plane_ride_Cost(city):
    if "Mumbai" == city:
        return 120
    elif "Delhi" == city:
        return 180
    elif "Kolkata" == city:
        return 190

def car_rental_cost(days):
    if days >=7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    
def total_trip_cost(city,days,spending_money):
    return car_rental_cost(days) + hotel_cost(days) + plane_ride_Cost(city) + spending_money

print("cost of car rent : ", car_rental_cost(5))

print("plane ride cost : ",plane_ride_Cost("Mumbai"))
print("cost of hotel for 7 nights : ",hotel_cost(7))
print("total cost of trip : ",total_trip_cost("Mumbai",7,10000))



    

    
    




   
