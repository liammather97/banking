from pymysql import connect
import os
import sys

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utf8mb4'
)

print("Hello welcome to the bank! \n",
          "please select one of the options below: \n",
          "1. Create an account \n",
          "2. Deposit cash \n",
          "3. Withdraw cash \n",
          "4. Show account details \n",
          "5. Exit \n")

choice = input ("Enter choice: ")


    def create_account():
    
        firstname1= str(input("Enter your firstname: "))
        surname1= str(input("Enter your surname: "))
        gender1= str(input("Enter your gender: "))
        nationality1= str(input("Enter your nationality: "))
        address11= str(input("Enter your address line 1: "))
        address21= str(input("Enter your address line 2: "))
        county1= str(input("Enter your county: "))
        postcode1= str(input("Enter your postcode: "))
        salary1= float(input("Enter your salary: "))

    
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO bk_customer value(firstname1, surname1, gender1, nationality1, address11, address21, county1, postcode1, salary1)"
                cursor.execute(query)
            connection.commit()
                




if choice == "4":
    acc_num= input("Enter Account Number: ")
    
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM bk_customer WHERE customerID='{acc_num}';"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()
