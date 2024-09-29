def liters_100km_to_miles_gallon(liters):
    # Convert liters per 100 km to miles per gallon using the formula
    return 235.215 / liters

def miles_gallon_to_liters_100km(miles):
    # Convert miles per gallon to liters per 100 km using the formula
    return 235.215 / miles

# Test the functions
print(liters_100km_to_miles_gallon(3.9))  # Expected around 60.31
print(liters_100km_to_miles_gallon(7.5))  # Expected around 31.36
print(liters_100km_to_miles_gallon(10.))  # Expected around 23.52
print(miles_gallon_to_liters_100km(60.3)) # Expected around 3.90
print(miles_gallon_to_liters_100km(31.4)) # Expected around 7.49
print(miles_gallon_to_liters_100km(23.5)) # Expected around 10.00
