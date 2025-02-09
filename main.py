import sqlite3

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:
  sql_create_table_firsttime = "CREATE TABLE IF NOT EXISTS Flight (FlightID INT AUTO_INCREMENT PRIMARY KEY,OriginID VARCHAR(8) NOT NULL,DestinationID VARCHAR(8) NOT NULL,DepartureDate DATE NOT NULL,ScheduleID INT NOT NULL,StatusID VARCHAR(2) NOT NULL);"

  sql_create_table = "CREATE TABLE Flight (FlightID INT AUTO_INCREMENT,OriginID VARCHAR(8) NOT NULL REFERENCES Destination,DestinationID VARCHAR(8) NOT NULL REFERENCES Destination,DepartureDate DATE NOT NULL,ScheduleID INT NOT NULL REFERENCES Schedule,StatusID VARCHAR(2) REFERENCES Status,PRIMARY KEY (FlightID)); INSERT INTO Flight (OriginID, DestinationID, DepartureDate, ScheduleID, StatusID) VALUES ('BOH',	'NWI',	'2025-02-14', 6, 'SC'),('BOH',	'2025-02-15', 7, 'SC'),('BOH',	'LPL',	'2025-02-16', 1, 'SC'),('LPL',	'BOH',	'2025-02-17', 2, 'SC'),('BOH',	'CWL',	'2025-02-18', 3, 'SC'),('BOH',	'CRL',	'2025-02-19', 4, 'SC'),('CWL',	'BOH',	'2025-02-20', 5, 'SC'),('BOH',	'EDI',	'2025-02-21', 6, 'SC'),('CRL',	'BOH',	'2025-02-22', 7, 'SC'),('EDI',	'BOH',	'2025-02-23', 1, 'SC'),('BOH',	'GNB',	'2025-02-24', 2, 'SC'),('GNB',	'BOH',	'2025-02-25', 3, 'SC'),('BOH',	'BES',	'2025-02-25', 8, 'SC'),('BOH',	'LCY',	'2025-02-26', 4, 'SC'),('BES',	'BOH',	'2025-02-27', 5, 'SC'),('LCY',	'BOH',	'2025-02-28', 6, 'SC');"

  sql_insert = "INSERT INTO Flight (FlightID, OriginID, DestinationID, DepartureDate, ScheduleID, StatusID) VALUES (?, '?',	'?',	'?', ?, '?');"
              

  sql_select_all = "SELECT * FROM Flight"
  sql_search = "SELECT * FROM Flight where FlightID = ?"
  sql_alter_data = ""
  sql_update_data = ""
  sql_delete_data = ""
  sql_drop_table = "DROP TABLE IF EXISTS Flight;"

  def __init__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
      self.cur.execute(self.sql_create_table_firsttime)
      self.conn.commit()
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
      flight.set_flight_departure_date(str(input("Enter Departure Date in format YYYY-MM-DD: ")))
      flight.set_flight_schedule_id(int(input("Enter Schedule ID: ")))
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
        print("Departure Date = ", row[3])
        print("Schedule ID = ", row[4])
        print("Status = ", row[5])

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
            print("Flight Origin: " + detail)
          elif index == 2:
            print("Flight Destination: " + detail)
          else:
            print("Status: " + str(detail))
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

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
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
    self.flightDepartureDate = ''
    self.flightScheduleID = 0
    self.status = ''

  def set_flight_id(self, flightID):
    self.flightID = flightID

  def set_flight_origin(self, flightOrigin):
    self.flight_origin = flightOrigin

  def set_flight_destination(self, flightDestination):
    self.flight_destination = flightDestination
  
  def set_flight_departure_date(self, flightDepartureDate):
    self.flight_departure_date = flightDepartureDate

  def set_flight_schedule_id(self, flightScheduleID):
    self.flight_schedule_id = flightScheduleID

  def set_status(self, status):
    self.status = status

  def get_flight_id(self):
    return self.flightID

  def get_flight_origin(self):
    return self.flightOrigin

  def get_flight_destination(self):
    return self.flightDestination
  
  def get_flight_departure_date(self):
    return self.flightDepartureDate

  def get_flight_schedule_id(self):
    return self.flightScheduleID
  
  def get_status(self):
    return self.status

  def __str__(self):
    return str(
      self.flightID
    ) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + str(self.flightDepartureDate) + "\n" + self.flightScheduleID + "\n" + str(
      self.status)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Create table FlightInfo")
  print(" 2. Insert data into FlightInfo")
  print(" 3. Select all data from FlightInfo")
  print(" 4. Search a flight")
  print(" 5. Update data some records")
  print(" 6. Delete data some records")
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
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")
