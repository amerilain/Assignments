import mariadb
from geopy import distance

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game2',
         user='root',
         password='root123',
         autocommit=True
         )

# part 1
icao = input("Enter IACO: ")
sql = "SELECT name, municipality FROM airport WHERE ident = '"+icao+"'"
cursor = connection.cursor()
cursor.execute(sql)
response = cursor.fetchall()
if cursor.rowcount >0:
    for row in response:
        print(f"Airport: {row[0]}\nLocation: {row[1]} ")

# part 2
code = input("Enter country code: ")
sql = "SELECT airport.name AS 'Airport Name', type AS 'Airport Type' FROM airport, country WHERE " \
      "airport.iso_country=country.iso_country and country.iso_country= '"+code+"' ORDER BY type asc; "
'''
SQL = "SELECT airport.iso_country, country.name, airport.type, count(*) FROM airport, country WHERE " \
      "airport.iso_country = country.iso_country AND airport.iso_country = 'FI' GROUP BY airport.type; "
'''

cursor = connection.cursor()
cursor.execute(sql)
response = cursor.fetchall()
if cursor.rowcount >0:
    for row in response:
        print(f"{row[0]}, {row[1]}")

'''
print(f"{row[1]} has ")
print(f"{row[3]} {row[2]}")
'''

# part 3
iaco1 = input("Enter IACO code of first airport: ")
iaco2 = input("Enter IACO code of second airport:")

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '"+iaco1+"';"
cursor = connection.cursor()
cursor.execute(sql)
response1 = cursor.fetchall()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '"+iaco2+"';"
cursor = connection.cursor()
cursor.execute(sql)
response2 = cursor.fetchall()

print(f"The distance between is: {distance.distance(response1, response2).km:.2f}km")


