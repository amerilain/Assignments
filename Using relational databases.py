import mariadb

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game2',
         user='root',
         password='root123',
         autocommit=True
         )

# Part 1
icao = input("Enter IACO: ")
sql = "SELECT name, municipality FROM airport WHERE ident = '"+icao+"'"
cursor = connection.cursor()
cursor.execute(sql)
response = cursor.fetchall()
if cursor.rowcount >0:
    for row in response:
        print(f"Airport: {row[0]}\nLocation: {row[1]} ")

# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
# in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
code = input("Enter country code: ")
sql = "SELECT airport.name AS 'Airport Name', type AS 'Airport Type' FROM airport, country WHERE " \
      "airport.iso_country=country.iso_country and country.iso_country= '"+code+"' ORDER BY type asc; "
cursor = connection.cursor()
cursor.execute(sql)
response = cursor.fetchall()
if cursor.rowcount >0:
    for row in response:
        print(f"{row[0]}, {row[1]}")