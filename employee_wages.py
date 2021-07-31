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


# Use Case-2 calculate daily employee wage
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


# Use Case-3 calculate daily part_time employee wage
try:
    part_time_day_hours = int(input(
        " Please enter working 'PartTime' hours for  one day ! : "))
    wage_per_hour = int(input(" Please enter wage for hour ! : "))
except Exception as massage:
    print("Please enter valid input , you need to enter number only......!")
    logging.info(massage)
else:
    total_wage = part_time_day_hours * wage_per_hour
    logging.info(total_wage)
    logging.info("new request process completed...!")
    print("Part time Daily Employee wage  is : ", total_wage)


# Use Case 5 solving use case statement
print("\tWelcome to Employee Wage Computation ")

while True:
    try:
        print("you please choose below options to process : ")
        print("""1.daily employee Wage
                 2.daily wages for PartTime employee
                 3.exit
              """)
        option = int(input("you please enter your options to process : "))
        list_number = [1, 2, 3]

        if option not in list_number:
            print("you please enter valid input ")
            break
    except Exception as massage:
        print("you please enter valid input ")
        logging.exception(massage)
    else:
        if option == 1:
            random_number = random.randint(0, 1)
            if random_number == 1:
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
            else:
                print("Employee is Absent.....!")
                logging.info("Employee is Absent.....!")

        if option == 2:
            random_number = random.randint(0, 1)
            if random_number == 1:
                try:
                    part_time_day_hours = int(input(
                        " Please enter working 'PartTime' hours for  one day ! : "))
                    wage_per_hour = int(input(" Please enter wage for hour ! : "))
                except Exception as massage:
                    print("Please enter valid input , you need to enter number only......!")
                    logging.info(massage)
                else:
                    total_wage = part_time_day_hours * wage_per_hour
                    logging.info(total_wage)
                    logging.info("new request process completed...!")
                    print("Part time Daily Employee wage  is : ", total_wage)
            else:
                print("Employee is Absent.....!")
                logging.info("Employee is Absent.....!")

        else:
            logging.info(
                "New Employee wage  request processing completed.....!")
            break
print("Thanks for using our application .....!")


# Use Case-5 Calculating wages for a month
try:
    day_hours = int(input(" Please enter working hours for one day ! : "))
    wage_per_hour = int(input(" Please enter wage for hour ! : "))
    wage_per_month = 0
    work_days = int(input(" Please enter working days for month ! : "))
except Exception as massage:
    print("Please enter valid input , you need to enter number only......!")
    logging.info(massage)
else:
    total_wage = day_hours * wage_per_hour
    result = work_days * total_wage
    logging.info(result)
    logging.info("new request process completed...!")
    print("one month Employee wages  is : ", result)


