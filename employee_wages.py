import random
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="employee_waga.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")
logging.info("New Employee wage request came !")

# Displaying wecome message  to employee wage computation
print("\tWelcome to Emplopyee Waga Computation ")

# Use Case-1 checking employee is present or absent
random_number = random.randint(0, 1)
if random_number == 1:
    print("Employee is Present.....!")
else:
    print("Employee is Absent.....!")


# Use Case-2 calculate daily employee waga
try:
    day_hours = int(input(" Please enter working hours for one day ! : "))
    wage_per_hour = int(input(" Please enter wage for hour ! : "))
except Exception as massage:
    print("Please enter valid input , you need to enter number only......!")
    logging.info(massage)
else:
    total_wage = day_hours * wage_per_hour
    logging.info(total_wage)
    logging.info("new request process completed...!")
    print("Daily Employee wage  is : ", total_wage)
