def main():
    time = str(input("What time is it?"))
    # calls convert function
    meal_time = convert(time)
    # checks if converted input fits
    if 7.0 <= meal_time <= 8.0:
     print ("breakfast time")
    if 12.0 <= meal_time <= 13.0:
     print ("lunch time")
    if 18.0 <= meal_time <= 19.0:
     print ("dinner time")

def convert(time):
    # splits user input into two variables
    hours, minutes = time.split(":")
    # set variables as float
    hours = float(hours)
    minutes = float(minutes)
    # converts minutes into decimal
    meal_time = hours + (minutes / 60)
    return meal_time

if __name__ == "__main__":
        main()
