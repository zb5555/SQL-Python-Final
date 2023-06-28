#query project2 database 
import mysql.connector

def get_employees_per_region(mycursor):
    print("-------- VIEW Employees Per Region ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter region name to see the number of employees in that region or enter 'All' for number of employees in all regions: ")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM EmployeesPerRegion;"
    else:
        sql_query = f"select *  from EmployeesPerRegion where region_name = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There are no employees in {user_option}\n")
    else:
        for record in query_result:
            print(f"Region: {record[0]}\nNumber of Employees: {record[1]}")
    
    return

def managers_in_department(mycursor):
    print("-------- VIEW Managers Per Department ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter department name to see the number of managers in that department or enter 'all' for managers in each department: ")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT department_name, COUNT(first_name) FROM managers GROUP BY department_name; "
    else:
        sql_query = f"SELECT department_name, COUNT(first_name) FROM managers WHERE department_name = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There are no managers in {user_option}\n")
    else:
        for record in query_result:
            print(f"Department: {record[0]}\nNumber of Managers: {record[1]}")
    
    return

def departmnts_with_most_dependents(mycursor):
    print("-------- VIEW Dependents Per Department ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter department name to see the number of dependents in that department or enter 'all' for dependents in each department: ")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM DependentsByDepartment;"
    else:
        sql_query = f"SELECT * FROM DependentsByDepartment WHERE department_name = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There are no dependents in {user_option}\n")
    else:
        for record in query_result:
            print(f"Department: {record[0]}\nNumber of Dependents: {record[1]}")
    
    return

def employees_hired_1997(mycursor):
    print("-------- VIEW Number of Hires Per Year ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter the year to see the number of employees hired that year or enter 'all' for all years an employee was hired: ")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM HiresByYear;"
    else:
        sql_query = f"SELECT * FROM HiresByYear WHERE Year = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There are no hires in {user_option}\n")
    else:
        for record in query_result:
            print(f"Year: {record[0]}\nNumber of Hires: {record[1]}")
    
    return

def total_salary_in_finance(mycursor):
    print("-------- VIEW Salary Per Department ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter department name to see the total salary in that department or enter 'all' for total salary in each department: ")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM SalaryByDepartment;"
    else:
        sql_query = f"SELECT * FROM SalaryByDepartment WHERE department_name = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There is no department {user_option}\n")
    else:
        for record in query_result:
            print(f"Department: {record[0]}\nTotal Salary: {record[1]}")
    
    return

def total_salary_by_jobTitle(mycursor):
    print("-------- VIEW Salary by job title ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter Job Title to view Salary of that job title or enter 'all' to see the salary for all job titles:")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM SalaryByJobTitle;"
    else:
        sql_query = f"SELECT * FROM SalaryByJobTitle WHERE job_title = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There is no job title {user_option}\n")
    else:
        for record in query_result:
            print(f"Job Title: {record[0]}\nSalary: {record[1]}")
    
    return

def employee_dependents(mycursor):
    print("-------- VIEW Dependents of job Employees ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter employee last name to see the dependent data for that employee or enter 'all' to see all dependent data by employee:")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM EmployeeDependents;"
    else:
        sql_query = f"SELECT * FROM EmployeeDependents WHERE last_name = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There is no employee with last name {user_option}\n")
    else:
        for record in query_result:
            print(f"First Name: {record[0]}\nLastName: {record[1]}\nEmail: {record[2]}\nPhone Number:{record[3]}\nNumber of Dependents: {record[4]} ")
    
    return

def countries_with_no_locations(mycursor):
    print("-------- VIEW location data by country ---------")
    #ask user for input: Can enter "all" to view all managers or city to view managers from a particular city
    user_option = input("\nEnter employee country name to see the number of locations for that country or enter 'all' to see all country locations:")


    #create query
    if user_option.upper() == "ALL":
        sql_query = "SELECT * FROM CountryLocation;"
    else:
        sql_query = f"SELECT * FROM CountryLocation WHERE country_name = '{user_option}';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    if(len(query_result) == 0):
        print(f"There is no country {user_option}\n")
    else:
        for record in query_result:
            print(f"Country: {record[0]}\nNumber of Locations: {record[1]}")
    
    return

def add_dependent(mycursor):
    print("\n-------- Add Dependent --------\n")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    relationship = input("Enter relationship: ")
    employee_id = input("Enter employee_id: ")

    sql_query = f"INSERT INTO dependents(first_name, last_name, relationship, employee_id) VALUES('{first_name}', '{last_name}', '{relationship}', '{employee_id}')"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: {mycursor.rowcount} records inserted in dependents table")
    except:
        print(f"Failure to add dependent to dependents table")
    return

def add_job(mycursor):
    print("\n-------- Add Job --------\n")

    job_title = input("Enter job title: ")
    min_salary= input("Enter minimum salary with two decimal places: ")
    max_salary = input("Enter maximum salary with two decimal places: ")

    sql_query = f"INSERT INTO jobs(job_title, min_salary, max_salary) VALUES('{job_title}', '{min_salary}', '{max_salary}')"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: {mycursor.rowcount} records inserted into the jobs table")
    except:
        print(f"Failure to add job to jobs table")
    return

def delete_employee(mycursor):
    print("\n-------- Delete Employee --------\n")

    employee_id = input("Enter the employee id you'd like to delete: ")

    sql_query = f"DELETE FROM employees WHERE employee_id = {employee_id}"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: Employee {employee_id} has been deleted from employees table ")
    except:
        print(f"Failure to delete employee {employee_id} from the employees table, please make sure the employee_id is correct.")
    return

def delete_dependent(mycursor):
    print("\n-------- Delete Dependent --------\n")

    dependent_id = input("Enter the dependent id you'd like to delete: ")

    sql_query = f"DELETE FROM dependents WHERE dependent_id = {dependent_id}"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: Dependent {dependent_id} has been deleted from the dependents table ")
    except:
        print(f"Failure to delete dependent {dependent_id} from the dependent table, please make sure the dependent_id is correct.")
    return

def update_employee_firstName(mycursor):
    print("\n-------- Update Employee First Name --------\n")

    employee_id = input("Enter the employee id you'd like to update: ")
    employee_firstName = input("What is his updated first name: ")

    sql_query = f"UPDATE employees SET first_name = '{employee_firstName}' WHERE employee_id = {employee_id}"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: Employee {employee_id} has been updated  with the first name {employee_firstName} ")
    except:
        print(f"Failure to update employee {employee_id} with the first name {employee_firstName}")
    return

def update_employee_lastName(mycursor):
    print("\n-------- Update Employee Last Name --------\n")

    employee_id = input("Enter the employee id you'd like to update: ")
    employee_lastName = input("What is his updated last name: ")

    sql_query = f"UPDATE employees SET last_name = '{employee_lastName}' WHERE employee_id = {employee_id}"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: Employee {employee_id} has been updated  with the last name {employee_lastName} ")
    except:
        print(f"Failure to update employee {employee_id} with the first name {employee_lastName}")
    return   

def update_job_minSalary(mycursor):
    print("\n-------- Update Job Minimum Salary --------\n")

    job_id = input("Enter the job id you'd like to update: ")
    job_min = input("What is his updated minimum salary (two decimals): ")

    sql_query = f"UPDATE jobs SET min_salary = '{job_min}' WHERE job_id = {job_id}"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: Job {job_id} has been updated  with the minimum salary {job_min} ")
    except:
        print(f"Failure to update job {job_id} with the minimum salary {job_min}")
    return 

def update_job_maxSalary(mycursor):
    print("\n-------- Update Job Maximum Salary --------\n")

    job_id = input("Enter the job id you'd like to update: ")
    job_max = input("What is his updated maximum salary (two decimals): ")

    sql_query = f"UPDATE jobs SET max_salary = '{job_max}' WHERE job_id = {job_id}"

    try:
        #execute query
        mycursor.execute(sql_query)
        print(f"Success: Job {job_id} has been updated  with the minimum salary {job_max} ")
    except:
        print(f"Failure to update job {job_id} with the minimum salary {job_max}")
    return                 

def print_menu():
    print("Choose an option")
    print("-----------------")
    print("---- VIEW DATA ----")
    print("1. View employee count data per region")
    print("2. View manager count by department")
    print("3. View dependent data per department")
    print("4. View hiring data by year")
    print("5. View salary data by department")
    print("6. View Salary data by job title")
    print("7. View dependent data by employee")
    print("8. View location data by country")
    print("----  ADD DATA ----")
    print("9. Add a dependent")
    print("10. Add a job")
    print("---- DELETE DATA ----")
    print("11. Delete an employee")
    print("12. Delete a dependent")
    print("---- UPDATE DATA ----")
    print("13. Update employee first name")
    print("14. Update employee last name")
    print("15. Update job minimum salary")
    print("16. Update job maximum salary")
    print("---- Exit Application ----")
    print("17. Exit Application")
    return

def get_user_choice():
    print_menu()
    while True:
        try:
            choice = (input("Enter Choice: "))
            if choice.isdigit():
                choice = int(choice)
            else:  
                raise ValueError()
            if 1<= choice <=17:
                break    
        except ValueError:
            print("Please enter a number between 1 and 17.")
            break

    return choice 

    

def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        user_choice = get_user_choice()
        if(user_choice == 1):
            #call the function to query the managers
            get_employees_per_region(mycursor)
        elif(user_choice == 2):
            managers_in_department(mycursor)
        elif(user_choice == 3):
            departmnts_with_most_dependents(mycursor)
        elif(user_choice == 4):
            employees_hired_1997(mycursor)
        elif(user_choice == 5):
            total_salary_in_finance(mycursor)
        elif(user_choice == 6):
            total_salary_by_jobTitle(mycursor)
        elif(user_choice == 7):
            employee_dependents(mycursor)
        elif(user_choice == 8):
            countries_with_no_locations(mycursor)
        elif(user_choice == 9):
            add_dependent(mycursor)
            mydb.commit()
        elif(user_choice == 10):
            add_job(mycursor)
            mydb.commit()
        elif(user_choice == 11):
            delete_employee(mycursor)
            mydb.commit()
        elif(user_choice == 12):
            delete_dependent(mycursor)
            mydb.commit()
        elif(user_choice == 13):
            update_employee_firstName(mycursor)
            mydb.commit()
        elif(user_choice == 14):
            update_employee_lastName(mycursor)
            mydb.commit()
        elif(user_choice == 15):
            update_job_minSalary(mycursor)
            mydb.commit()
        elif(user_choice == 16):
            update_job_maxSalary(mycursor)
            mydb.commit()
        elif(user_choice == 17):
            print("Bye Bye!!!")
            break

main()