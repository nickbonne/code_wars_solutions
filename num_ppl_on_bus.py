
# https://www.codewars.com/kata/number-of-people-in-the-bus/train/python

def number(bus_stops):
    
    riders = 0
    
    for stop in bus_stops:

        riders = riders + stop[0] - stop[1]
        
    return riders