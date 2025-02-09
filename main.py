import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:

  #Destination Table queries
  sql_create_destination_table_firsttime = "CREATE TABLE IF NOT EXISTS Destination (DestinationID VARCHAR(8) NOT NULL PRIMARY KEY, Airport VARCHAR(30) NOT NULL, City VARCHAR(30) NOT NULL,Country VARCHAR(30) NOT NULL);"
  sql_create_table_destination = "CREATE TABLE Destination (DestinationID VARCHAR(8) NOT NULL,Airport VARCHAR(30) NOT NULL,City VARCHAR(30) NOT NULL,Country VARCHAR(30),PRIMARY KEY (DestinationID));"
  sql_populate_destination = """INSERT INTO Destination (DestinationID, Airport, City, Country)
    VALUES 
    ('BOH', 'Bournemouth Airport', 'Bournemouth', 'UK'),
    ('NWI', 'Norwich Airport', 'Norwich', 'UK'),
    ('LPL', 'Liverpool John Lennon Airport', 'Liverpool', 'UK'),
    ('CWL', 'Cardiff Airport', 'Cardiff', 'Wales'),
    ('CRL', 'Brussels South Charleroi Airport', 'Charleroi','Belgium'),
    ('EDI', 'Edinburgh Airport', 'Edinburgh', 'UK'),
    ('GNB', 'Alpes-Isere Airport', 'Grenoble', 'France'),
    ('BES', 'Brest Bretagne Airport', 'Brest', 'France'),
    ('LCY', 'London City Airport', 'London', 'UK');"""
  sql_insert_destination_data = "INSERT INTO Destination VALUES (?, ?,	?, ?);"
  sql_select_all_destination_data = "SELECT * FROM Destination;"
  sql_search_destination = "SELECT * FROM Destination where DestinationID = ?;"
  sql_delete_destination_data = "DELETE FROM Destination WHERE DestinationID = ?;"

  #Flight Table queries
  sql_create_table_firsttime = "CREATE TABLE IF NOT EXISTS Flight (FlightID BIGINT NOT NULL PRIMARY KEY, OriginID VARCHAR(8) NOT NULL,DestinationID VARCHAR(8) NOT NULL,StatusID VARCHAR(2) NOT NULL);"
  #sql_drop_table = "DROP TABLE IF EXISTS Flight;"
  sql_create_table = "CREATE TABLE Flight (FlightID BIGINT NOT NULL,OriginID VARCHAR(8) NOT NULL REFERENCES Destination,DestinationID VARCHAR(8) NOT NULL REFERENCES Destination,StatusID VARCHAR(2) REFERENCES Status,PRIMARY KEY (FlightID));"
  sql_populate_flight = """INSERT INTO Flight (FlightID, OriginID, DestinationID, StatusID)
    VALUES 
    (1, 'BOH',	'NWI', 'SC'),
    (2, 'NWI',	'BOH', 'SC'),
    (3, 'BOH',	'LPL', 'SC'),
    (4, 'LPL',	'BOH', 'SC'),
    (5, 'BOH',	'CWL', 'SC'),
    (6, 'BOH',	'CRL', 'SC'),
    (7, 'CWL',	'BOH', 'SC'),
    (8, 'BOH',	'EDI', 'SC');"""

  sql_insert = "INSERT INTO Flight VALUES (?, ?,	?, ?);"
  sql_select_all = "SELECT * FROM Flight;"
  sql_search = "SELECT * FROM Flight where FlightID = ?;"
  sql_alter_data = ""
  sql_update_data = "UPDATE Flight SET StatusID = ? WHERE FlightID = ? ;"
  sql_delete_data = "DELETE FROM Flight WHERE FlightID = ?"
  sql_drop_table = "DROP TABLE IF EXISTS Flight;"

  def __init_destination__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
  
      self.cur.execute(self.sql_create_destination_table_firsttime)
      self.conn.commit()
      self.cur.execute(self.sql_populate_destination)
      self.conn.commit()
      self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
      print(self.cur.fetchall())
      print('Database input started')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def create_table_destination(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table_destination)
      self.cur.execute(self.sql_populate_destination)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_destination_data(self):
    try:
      self.get_connection()

      destination = DestinationInfo()
      destination.set_destination_id(str(input("Enter Destination Airport IATA Code: ")))
      destination.set_destination_airport(str(input("Enter Airport name: ")))
      destination.set_destination_city(str(input("Enter Airport's City name: ")))
      destination.set_destination_country(str(input("Enter Airport's country name: ")))
  
      #challenge encountered - the split of the tuple did not work for the destination data possibly due to the delimiter choice - this was resolved with supplying the input as four strings already split
      #self.cur.execute(self.sql_insert_destination_data, tuple(str(destination).split("\n")))
      self.cur.execute(self.sql_insert_destination_data, (str(destination.get_destination_id()),str(destination.get_destination_airport()), str(destination.get_destination_city()), str(destination.get_destination_country())))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all_destination_data(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all_destination_data)
      result = self.cur.fetchall()

      # think how you could develop this method to show the records
      for row in result:
        print("DestinationID = ", row[0])
        print("Airport = ", row[1])
        print("City = ", row[2])
        print("Country = ", row[3])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def search_destination_data(self):
    try:
      self.get_connection()
      destinationID = str(input("Enter DestinationID: "))
      self.cur.execute(self.sql_search_destination, (str(destinationID),))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Destination Code: " + str(detail))
          elif index == 1:
            print("Destination Airport: " + str(detail))
          elif index == 2:
            print("Destination City: " + str(detail))
          else:
            print("Destination Country: " + str(detail))
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def __init__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
      #self.cur.execute(self.sql_drop_table)
      self.cur.execute(self.sql_create_table_firsttime)
      self.conn.commit()
      self.cur.execute(self.sql_populate_flight)
      self.conn.commit()
      self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
      print(self.cur.fetchall())
      print('Database input started')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_connection(self):
    self.conn = sqlite3.connect("FMS_DB.db")
    self.cur = self.conn.cursor()

  def create_table(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table)
      self.cur.execute(self.sql_populate_flight)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_data(self):
    try:
      self.get_connection()

      flight = FlightInfo()
      flight.set_flight_id(int(input("Enter FlightID: ")))
      flight.set_flight_origin(str(input("Enter Origin Airport IATA Code: ")))
      flight.set_flight_destination(str(input("Enter Destination Airport IATA Code: ")))
      flight.set_status(str(input("Enter Flight Status as 'SC' for Scheduled: ")))
  
      self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))

      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all)
      result = self.cur.fetchall()

      # think how you could develop this method to show the records
      for row in result:
        print("FlightID = ", row[0])
        print("Origin = ", row[1])
        print("Destination = ", row[2])
        #print("Departure Date = ", row[3])
        #print("Schedule ID = ", row[4])
        print("Status = ", row[3])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def search_data(self):
    try:
      self.get_connection()
      flightID = int(input("Enter FlightID: "))
      self.cur.execute(self.sql_search, tuple(str(flightID)))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Flight ID: " + str(detail))
          elif index == 1:
            print("Flight Origin: " + str(detail))
          elif index == 2:
            print("Flight Destination: " + str(detail))
          else:
            print("Status: " + detail)
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def update_data(self):
    try:
      self.get_connection()

      # Update statement
      flight = FlightInfo()
      flight.set_flight_id(int(input("Enter FlightID: ")))
      flight.set_status(str(input("Enter Flight Status as 'SC' for Scheduled: ")))
      flightID = flight.get_flight_id()
      statusID = flight.get_status()
      data = (statusID, flightID)

      #self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))
      self.cur.execute(self.sql_update_data, data)
      self.conn.commit()
      print('Updated data successfully')

      result = self.cur.fetchall()
      for row in result:
        print("FlightID = ", row[0])
        print("Origin = ", row[1])
        print("Destination = ", row[2])
        print("Status = ", row[3])

    #this is a bug to resolve: the programign is complainting the list object has no attribute rowcount - todolist
      if result.rowcount != 0:
        print(str(self.cur.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.

  def delete_data(self):
    try:
      self.get_connection()

      flightID = int(input("Enter FlightID: "))

      self.cur.execute(self.sql_delete_data, tuple(str(flightID)))
      self.conn.commit()
      result = self.cur.fetchone()

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


class FlightInfo:

  def __init__(self):
    self.flightID = 0
    self.flightOrigin = ''
    self.flightDestination = ''
    #self.flightDepartureDate = 
    #self.flightScheduleID = 0
    self.status = ''

  def set_flight_id(self, flightID):
    self.flightID = flightID

  # self.flight_origin was replaced with self.flightOrigin as specified in the declaration for the variables to fix the input bug
  def set_flight_origin(self, flightOrigin):
    self.flightOrigin = flightOrigin


  # self.flight_destination was replaced with self.flightDestination as specified in the declaration for the variables to fix the input bug
  def set_flight_destination(self, flightDestination):
    self.flightDestination = flightDestination
  
  # def set_flight_departure_date(self, flightDepartureDate):
  #   self.flight_departure_date = flightDepartureDate

  # def set_flight_schedule_id(self, flightScheduleID):
  #   self.flight_schedule_id = flightScheduleID

  def set_status(self, status):
    self.status = status

  def get_flight_id(self):
    return self.flightID

  def get_flight_origin(self):
    return self.flightOrigin

  def get_flight_destination(self):
    return self.flightDestination
  
  def get_status(self):
    return self.status

  def __str__(self):
    return str(self.flightID) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(self.status)


class DestinationInfo:
  def __init_destination__(self):
    self.destinationID = ''
    self.airport = ''
    self.city = ''
    self.country = ''

  def set_destination_id(self, destinationID):
    self.destinationID = destinationID

  # self.flight_origin was replaced with self.flightOrigin as specified in the declaration for the variables to fix the input bug
  def set_destination_airport(self, airport):
    self.airport = airport

  # self.flight_destination was replaced with self.flightDestination as specified in the declaration for the variables to fix the input bug
  def set_destination_city(self, city):
    self.city = city
  
  def set_destination_country(self, country):
    self.country = country

  def get_destination_id(self):
    return self.destinationID

  def get_destination_airport(self):
    return self.airport

  def get_destination_city(self):
    return self.city
  
  def get_destination_country(self):
    return self.country

  def __str_dest__(self):
    return str(self.destinationID) + "\n" + str(self.airport) + "\n" + str(self.city) + "\n" + str(self.country)

# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print("FlightInfo Menu")
  print(" 1. Create table Flight")
  print(" 2. Insert data into FlightInfo")
  print(" 3. Select all data from FlightInfo")
  print(" 4. Search a flight")
  print(" 5. Update data some records")
  print(" 6. Delete data some records")
  print("**********")
  print("DestinationInfo Menu")
  print(" 8. Create table Destination")
  print(" 9. Insert data into Destination")
  print(" 10. Select all data from Destination")
  print(" 11. Search a Destination")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 8:
    db_ops.create_table_destination()
  elif __choose_menu == 9:
    db_ops.insert_destination_data()
  elif __choose_menu == 10:
    db_ops.select_all_destination_data()
  elif __choose_menu == 11:
    db_ops.search_destination_data()
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")
