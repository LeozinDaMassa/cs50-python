def main():
    time = str(input("What time is it?"))
    meal_time = convert(time)
    if 7.0 <= meal_time <= 8.0:
     print ("breakfast time")
    if 12.0 <= meal_time <= 13.0:
     print ("lunch time")
    if 18.0 <= meal_time <= 19.0:
     print ("dinner time")

def convert(time):
    # Check if 12h format
    if "a.m" in time or "p.m." in time:
     pre_time, am_pm = time.split(" ")
     hours, minutes = pre_time.split(":")
     hours = float(hours)
     minutes = float(minutes)
     if "p.m." in time:
          hours = hours + 12.0
    else:
       hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    meal_time = hours + (minutes / 60)
    return meal_time

if __name__ == "__main__":
        main()
