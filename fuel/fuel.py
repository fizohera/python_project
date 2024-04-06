
"""
HarvardX: CS50's Introduction to Programming with Python PROBLEM SET 5

In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""

import sys

def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    gauge(percentage)

def convert(fraction):
    while True:
        try:
            if "/" in fraction:
                available_fuel = fraction.split("/")
                if len(available_fuel) == 2:
                    available_fuel = [int(i) for i in available_fuel]
                    numerator, denomenator =[*available_fuel]
                    if denomenator == 0:
                        raise ZeroDivisionError()
                    elif numerator > denomenator:
                        raise ValueError()
                    else:
                        percentage = int((numerator/denomenator)*100)
                        if(percentage % 10) > 5:
                            return percentage + 1
                        else:
                            return percentage
        except ValueError:
            raise
        except ZeroDivisionError:
            raise

def gauge(percentage):
    
    if  percentage <= 1 :
         return "E"
    elif percentage >= 99:
         return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()


