""" Enter the first odometer reading (miles): 30462
    Enter the second odometer reading (miles): 30810
    Enter the amount of fuel used (gallons): 11.2
    31.1 miles per gallon
    7.57 liters per 100 kilometers"""

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return (end_miles-start_miles)/amount_gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return 235.215/mpg
    
def main():
    s_odometer = float(input("Enter the first odometer reading (miles): "))
    f_odometer = float(input("Enter the second odometer reading (miles): "))
    fuel = float(input("Enter the amount of fuel used (gallons): "))
    
    
    
    mpg = miles_per_gallon(s_odometer,f_odometer,fuel)

    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{round(mpg,1)} miles per gallon.\n{round(lp100k,2)} liters per 100 kilometers.")    
    
main()