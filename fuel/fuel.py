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


