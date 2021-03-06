import random
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="employee_waga.log",
                    level=logging.INFO,
                    format=log_format,
                    datefmt="%d/%m/%y %I:%M:%S:%p")
logging.info("New Employee wage request came !")

# Displaying welcome message  to employee wage computation
print("\tWelcome to Employee Wage Computation ")

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


# Use Case-4 solving use case statement
print("\tWelcome to Employee Wage Computation ")

while True:
    try:
        print("you please choose below options to process : ")
        print("""\t1.daily employee Wages
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


# Use Case-6 Calculate wages till a condition of total working days and hours reached for a month
try:
    max_days = int(input("enter 'max working days' for month :"))
    max_hours = int(input("enter 'max working  hours' in month :"))
    day_hours = max_hours // max_days
except Exception as message:
    print("please enter valid input...! you need to enter only number !")
    logging.exception(message)
else:
    wage_per_hour = 20
    max_days_count = 0
    max_hours_cont = 0
    total_wage = 0

    while True:
        if max_hours_cont == max_hours and max_days_count == max_days:
            print("max days and hours reached ")
            break

        total_wage += day_hours * wage_per_hour
        max_hours_cont += day_hours
        max_days_count += 1

    print("The total wages for", max_days, "days and ", max_hours, "hours is : ", total_wage)
    logging.info(total_wage)


# Use Case-7 refactor the code to write a function to get work hours
def get_hours():
    try:
        day_hours = int(input(" Please enter working hours for one day less than or equal to 10 ! : "))
        total_hours = 0
    except Exception as message:
        print(message)
        logging.info(message)
    else:
        if day_hours <= 10:
            present_count = 0
            absent_count = 0
            for day in range(30):
                random_number = random.randint(0, 1)
                if random_number == 1:
                    total_hours += day_hours
                    present_count += 1
                else:
                    absent_count += 1
            logging.info(total_hours)
            print("number of days employee 'Absent' in one month : ", absent_count)
            print("number of days employee 'Present' in  one month : ", present_count)
            print("the total working hours an employee for a month :", total_hours)
        else:
            print("Please enter working  hours less than or equal to 10 only.....!  ")


print(get_hours())


# Use Case-8 Store the Daily Wage along with the Total Wage
def month_wage():
    while True:
        try:
            day_hours = int(input(
                " Please enter working hours for one day less than or equal to 10 ! : "))
            wage_per_hour = int(input(" Please enter wage for hour ! : "))
        except Exception as message:
            print("Please enter valid input , you need to enter number only......!")
            logging.info(message)
        else:
            dictionary = {}
            daily_wage = day_hours * wage_per_hour
            present_count = 0
            absent_count = 0
            if day_hours <= 10:
                for day in range(1, 31):
                    random_number = random.randint(0, 1)
                    if random_number == 1:
                        present_count += 1
                    else:
                        absent_count += 1
            else:
                print("Please enter working  hours less than or equal to 10 only.....!  ")
                daily_wage = 0

            total_wage = present_count * daily_wage
            dictionary['absent_days'] = absent_count
            dictionary['present_days'] = present_count
            dictionary['daily_wage'] = daily_wage
            dictionary['monthly_wage'] = total_wage
            for key, value in dictionary.items():
                print('\t', key, '\t', value)
        break


print(month_wage())


# Use Case-9 Store the Daily Wage and day wage along with the Total month Wages
# define a function to display Daily Wage and day wage along with the Total month Wages
def month_wage():
    # until condition False we run this while loop
    while True:
        try:
            # taking input from the user and handle exceptions
            day_hours = int(input(
                " Please enter working hours for one day less than or equal to 10 ! : "))
            wage_per_hour = int(input(" Please enter wage for hour ! : "))
        except Exception as message:
            print("Please enter valid input , you need to enter number only......!")
            logging.info(message)
        # if there is no exception else block will run
        else:
            # define one empty dictionary to store employee wage details
            dictionary = {}
            # calculating daily wage
            daily_wage = day_hours * wage_per_hour
            present_count = 0
            absent_count = 0
            # counting employee  present days and absent days
            if day_hours <= 10:
                # days counting in one month
                for day in range(1, 31):
                    random_number = random.randint(0, 1)
                    if random_number == 1:
                        present_count += 1
                    else:
                        absent_count += 1
            else:
                # if user enter more than 10 hours one day else block will execute
                print("Please enter working  hours less than or equal to 10 only.....!  ")
                daily_wage = 0
            # calculating total wage in month
            total_wage = present_count * daily_wage
            # storing employee details in dictionary by using keys
            dictionary['absent_days'] = absent_count
            dictionary['present_days'] = present_count
            dictionary['daily_wage'] = daily_wage
            dictionary['monthly_wage'] = total_wage
            # printing key values by using dictionary items method
            for key, value in dictionary.items():
                print('\t', key, '\t', value)
        break


# function calling
print(month_wage())

