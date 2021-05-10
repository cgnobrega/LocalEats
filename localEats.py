import sqlite3
import random

### First, initialize a connection
db_name = "localEats.db"
connection = sqlite3.connect(db_name)
cur = connection.cursor()

def validTable(name):
    
    # This function checks to make sure a user input table name is actually there 
    
    if(name=="alert" or name=="driver" or name=="menu" or name=="orders" or name=="restaurant" or name=="users"):
        valid = True
    else:
        valid = False
        
    return(valid)
def driver():
    
    #This function is string formating for SQL Statements in the "driver" table
    print()
    query = "(" + str(random.randrange(201,999)) + ", '"
    name = input("Please enter a name: ")
    query = query + name + "', '"
    make = input("Enter a car make: ")
    query = query + make + "', '"
    model = input("Enter a car model: ")
    query = query + model + "', '"
    license = input("Enter a license plate number (405ZX2): ")
    query = query +"')"
    
    return query
    
def alert():
    
    #This function is string formating for SQL Statements in the "alert" table
    
    print()
    query = "(" + str(random.randrange(100301, 100900))
    query = query +", '"
    deliveredBy = input("Enter who delivered this order (driverID): ")
    query = query + deliveredBy + "', '"
    alertTime = input("Enter an alert time (13:55): ")
    query = query + alertTime+ "', '"
    pickupTime = input("Enter a pickup time (14:27): ")
    query = query + pickupTime + "')"
    
    return query

def menu():
    
    # This function is string formating for SQL Statements in the "menu" table
    
    print()
    query = "(" + str(random.randrange(201,999)) + ", '"
    typE = input("Enter a menu type (All Day, Breakfast, Lunch, or Dinner): ")
    query = query + typE + "', "
    price = input("Enter a price (7.34): ")
    query = query + price + ", "
    query = query  + str(random.randrange(1000,9999)) + ", "
    restID = input("Enter restaurantID: ")
    query = query + restID +")"
    
    print(query)
    return query

def orders():
    
    # This function is string formating for SQL Statements in the "orders" table
    
    print()
    query = "(" + str(random.randrange(100301,109999)) + ", "
    ordred = input("Enter the ID of the customer who ordered this: ")
    query = query + ordred + ", '"
    delTime = input("Enter a delivery time (12:47): ")
    query = query + delTime + "', '"
    orderTime = input("Enter order time (12:34): ")
    query = query + orderTime + "', "
    itemID = input("Enter itemID of the item ordered(2087): ")
    query = query + itemID + ", "
    price = input("Enter the price of the above item: ")
    query = query + price +", "
    quant = input("Enter the quantity: ")
    query = query + quant + ", "
    extendedPrice = str(int(quant)*float(price))
    query = query + extendedPrice + ", "
    ful = input("Enter your restaurantID: ")
    query = query + ful + ")"
    
    return query

def restaurant():
    
    # This function is string formating for SQL Statements in the "restaurant" table
    
    print()
    query = str(random.randrange(101,999)) + ", '"
    addr = input("Enter address: ")
    query = query + addr + "', '"
    cat = input("Enter restaurant category: ")
    query = query + cat + "', '"
    name = input("Enter name: ")
    query = query + name +"')"
    
    return query

def users():
    
    # This function is string formating for SQL Statements in the "users" table
    
    query = "(" + str(random.randrange(201,999)) + ", '"
    addr = input("Enter address: ")
    query = query + addr + "', '"
    name = input("Enter user name: ")
    query = query + name + "')"
    
    return query

def printTable():
    
    # This function prints out an entire table
    
    global connection
    global cur
    
    print("\n")
    print("+-----------------------------------------+")
    print("Which table would you like to see?")
    print("Please enter the name of the table you wish to look at.")
    choice = input("Your input: ")
    valid = validTable(choice)
    print()
    
    if (valid == True):
        query = "SELECT * FROM "
        query = query + choice
        
        cur.execute(query)
        
        names = cur.description
        
        for name in names:
            print("{: <30}".format(name[0]), end="")
        print()
        
        for row in cur.fetchall():
            for item in row:
                if item != None:
                    print("{: <30}".format(item), end="")
                else:
                    print("{: ,30}".format("None"), end="")
            print()
        print()
    
    else:
        print()
        print("Invalid table name. Exiting to main menu...")
        print()
            
    
def insert():
    
    # This function allows the user to insert into any valid table
    global connection
    global cur
    
    print()
    table = input("Enter the table you want to insert into: ")
    valid = validTable(table)
    
    
    if (valid == True):
        query = "INSERT INTO " + table
        
        if (table == "alert"):
            q2 = alert()
            query = query + "('orderID', 'deliveredBy', 'alertTime', 'pickupTime') VALUES " +q2 + "; "
        elif (table == "driver"):
            q2 = driver()
            query = query + "('ID', 'name', 'carMake', 'carModel', 'license') VALUES " +q2 + "; "
            print(query)
        elif (table == "menu"):
            q2 = menu()
            query = query + "('menuID', 'type', 'price', 'itemID', 'restaurantID') VALUES " +q2 + "; "
        elif (table == "orders"):
            q2 = orders()
            query = query + "('orderID', 'orderedBy', 'delieveryTime', 'orderTime', 'itemID', 'price', 'quantity', 'extendedPrice', 'fulfilledBy') VALUES " + q2 + "; "
        elif (table == "restaurant"):
            q2 = restaurant()
            query = query + "('ID', 'address', 'category', 'name') VALUES (" + q2 + "; "
        elif (table == "users"):
            q2 = users()
            query = query + "('ID', 'address', 'name') VALUES " + q2 + "; "
        try:
            cur.execute(query)
        except sqlite3.OperationalError as e:
            print(e)        
    else:
        print()
        print("Invalid table name. Exiting to main menu...")
        print()
        
    connection.commit()
    print()
    print("Insertion committed")
    print()
    
def deletion():
    
    # this function allows the user to delete from any valid table
    global connection
    global cur    
    print()
    table = input("Enter the table you want to delete from: ")
    valid = validTable(table)
    
    if (valid == True):
        query = "DELETE FROM " + table + " WHERE "
        
        where = input("Enter a WHERE clause argument(s): ")
        query = query + where  
        
        
        cur.execute(query)  
    else:
        print()
        print("Invalid table name. Exiting to main menu...")
        print()
        
    connection.commit()
    print()
    print("Deletion committed")
    print() 
    
def update():
    
    # This function allows the user to update any valid database
    
    global connection
    global cur
    
    print()
    table = input("Enter a table you want to update: ")
    valid = validTable(table)
    if (valid == True):
        
        query = "UPDATE " + table
        setClause = input("Enter a SET clause argument(s): ")
        query = query + " SET " + setClause + " WHERE "
        where = input("Enter a WHERE clause argument(s): ")
        query = query + where
            
        cur.execute(query)
        
    else:
        print()
        print("Bad input, kicking you back to main menu...")
        print()
    connection.commit()
    print()
    print("Update committed")
    print()

def customSQL():
    
    # This function allows for more personalization of a report for a user
    
    global connection
    global cur    
    
    print()
    print("Please enter an SQL Command")
    query = input("Enter command here: ")
    
    try:
        cur.execute(query)
    except sqlite3.OperationalError as e:
        print(e)
    
    results = cur.fetchall()
    print()
    
    names = cur.description
    for name in names:
        print("{: <30}".format(name[0]), end="")
    print()

    for row in results:
        for item in row:
            print("{: <30}".format(item), end="")
        print()
    print()    
    
def topTen():
    
    # This function has a hard coded SQL query that gets the top 10 most popular restaurants 
    global connection
    global cur
    
    print()
    print("Here are the top 10 most popular restaurants")
    print()
    query = "SELECT COUNT(orders.fulfilledBy) AS orderCount, restaurant.name AS restaurantName FROM orders, restaurant WHERE orders.fulfilledBy = restaurant.ID GROUP BY orders.fulfilledBy ORDER BY orderCount DESC LIMIT 10 "
    cur.execute(query)
    
    results = cur.fetchall()
    print()
    
    # Print out results
    names = cur.description
    for name in names:
        print("{: <30}".format(name[0]), end="")
    print()
    
    for row in results:
        for item in row:
            print("{: <30}".format(item), end="")
        print()
    print()
    
def joinSQL():
    
    # This function has a set SQL statement for a statistics option in the menu. It reports all users who have an account but have not ordered anything. 
    # Please note: This is used as our "join feature" however, SQL Lite does not have ANTI JOIN needed to complete this query so a work around has been found. 
    
    global connection
    global cur
    
    print()
    print("Here are all the users who have an account, but have not ordered anything")
    print()
    #    ANTI JOIN is not supported by SQL Lite, so NOT IN has been used to do the same thing.
    query = "SELECT users.ID AS customerID, users.name AS customerName FROM users WHERE users.ID NOT IN (SELECT orders.orderedBy FROM orders) " 
    cur.execute(query)
    
    results = cur.fetchall()
    print()
    names = cur.description
    
    # Print out results
    for name in names:
        print("{: <30}".format(name[0]), end="")
    print()
    
    for row in results:
        for item in row:
            print("{: <30}".format(item), end="")
        print()
    print()

def mostPop():
    
    #This function has a set SQL statement to generate a report of the top 10 most popular restaurnt categories in the database. 
    
    global connection
    global cur
    
    print()
    print("Here are the top 10 most popular restaurant categories")
    print()
    query = "SELECT COUNT(orders.fulfilledBy) as orderCount, restaurant.category FROM orders, restaurant WHERE orders.fulfilledBy = restaurant.ID GROUP BY restaurant.category ORDER BY orderCount DESC LIMIT 10 "
    
    cur.execute(query)
    
    results = cur.fetchall()
    print()
    names = cur.description
    
    #Print out the results
    for name in names:
        print("{: <30}".format(name[0]), end="")
    print()
    
    for row in results:
        for item in row:
            print("{: <30}".format(item), end="")
        print()
    print()
    
def statsMenu():
    # This functions as the statistics menu
    print()
    print("+-----------------------------------------+")
    print("This is the statistics menu!")
    print("Enter 1 for the top 10 restaurants that fulfilled the most orders")
    print("Enter 2 to look at all the users that have an account, but have not ordered anything")
    print("Enter 3 to look at the top 10 most popular restaurant categories")
    print("Enter 4 to enter a custom SQL query")
    print("+-----------------------------------------+")
    
    choice = int(input("Your Choice: "))
    
    #Go through user choice
    if (choice ==1):
        topTen()
    elif(choice ==2):
        joinSQL()
    elif(choice ==3):
        mostPop()
    elif(choice ==4):
        customSQL()
    
    
    print()
def main():
    
    # --------------- Main ---------------
    # This functions as the main menu for interaction
    
    global connection
    global cur
    
    print()
    print("+-----------------------------------------+")
    print("Welcome to the LocalEats Database!")
    print("What would you like to do today?")
    print("+-----------------------------------------+")
    print()
    
    choice = 1
    while choice > 0:
        print("+-----------------------------------------+")
        print("Main Menu: ")
        print("Enter 0 to exit")
        print("Enter 1 to print out a table")
        print("Enter 2 to insert/delete/update into a table")
        print("Enter 3 to enter a custom SQL command")
        print("Enter 4 to go to the statistics menu")
        print("+-----------------------------------------+")
        choice = int(input("Your input: "))
    
        #Go through user choice
        if (choice == 1):
            printTable()
        
        elif (choice == 2):
            valid = True
            while (valid == True):
                print()
                num = int(input("Enter 1 for insert, 2 for delete, and 3 for update: "))
                if (num ==1):
                    insert()
                    valid = False
                elif (num ==2):
                    deletion()
                    valid = False
                elif (num == 3):
                    update()
                    valid = False
        elif (choice == 3):
            customSQL()
    
        elif (choice ==4):
            statsMenu()
    
    print()
    print("Exiting...")
    
main()
# Save our changes and then close
# connection.rollback()    # this will undo any changes since the last commit
connection.commit()
connection.close()