import sqlite3

# If needed, the FMS_DB.db can be deleted and recreated on local. Please recreate all the databases by selecting one at a time menu options 1, 8, 12, 16, 22 and 24
# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:

  #Summary sql statements
  sql_count_pilot_schedule = """SELECT DISTINCT Pilot.PilotID, COUNT(Flight_Pilot.FlightID) as flight_count
    FROM Flight_Pilot
    INNER JOIN Pilot ON Flight_Pilot.PilotID = Pilot.PilotID
    GROUP BY Pilot.PilotID;"""
  
  #Status Table queries
  sql_create_table_status_firsttime = "CREATE TABLE IF NOT EXISTS Status (StatusID VARCHAR(2) NOT NULL PRIMARY KEY, StatusDesc VARCHAR(15));"
  sql_create_table_status = "CREATE TABLE Status (StatusID VARCHAR(2) NOT NULL, StatusDesc VARCHAR(15),PRIMARY KEY (StatusID));"
  sql_populate_status = """INSERT INTO Status (StatusID, StatusDesc)
    VALUES
    ('SC', 'Scheduled'),
    ('CN', 'Cancelled'),
    ('OT', 'On Time'),
    ('DE', 'Delayed'),
    ('AV', 'Arrived'),
    ('DP', 'Departed');"""
  sql_select_all_status_data = "SELECT * FROM Status;"

  #Schedule Table queries
  sql_create_table_schedule_firsttime = "CREATE TABLE IF NOT EXISTS Schedule (ScheduleID MEDIUMINT NOT NULL PRIMARY KEY, WeekDay VARCHAR(10) NOT NULL, DepartureTime DATE NOT NULL);"
  sql_create_table_schedule = "CREATE TABLE Schedule (ScheduleID MEDIUMINT NOT NULL,WeekDay VARCHAR(10) NOT NULL,DepartureTime DATE NOT NULL,PRIMARY KEY (ScheduleID));"
  sql_populate_schedule = """INSERT INTO Schedule (ScheduleID, WeekDay, DepartureTime)
    VALUES 
    (1, 'SUN', '14:30'),
    (2, 'MON', '10:30'),
    (3, 'TUE', '09:30'),
    (4, 'WED', '10:30'),
    (5, 'THU', '17:30'),
    (6, 'FRI', '15:30'),
    (7, 'SAT', '11:30'),
    (8, 'SAT', '20:30'),
    (9, 'SUN', '11:30'),
    (10, 'MON', '18:30'),
    (11, 'TUE', '08:30'),
    (12, 'WED', '17:30');"""
  sql_select_all_schedule_data = "SELECT * FROM Schedule;"
  sql_search_pilot_schedule = """SELECT Flight.FlightID, Flight.DepartureDate, Schedule.WeekDay, Schedule.DepartureTime
    FROM Schedule
    JOIN Flight ON Schedule.ScheduleID = Flight.ScheduleID
    JOIN Flight_Pilot ON Flight_Pilot.FlightID = Flight.FlightID
    JOIN Pilot ON Flight_Pilot.PilotID = Pilot.PilotID
    WHERE Pilot.PilotID = ?
    GROUP BY Schedule.WeekDay, Flight.DepartureDate
    ORDER BY Schedule.WeekDay;"""


  #Flight Pilot Table queries
  sql_create_flight_pilot_table_firsttime = "CREATE TABLE IF NOT EXISTS Flight_Pilot (PilotID MEDIUMINT, FlightID BIGINT, PRIMARY KEY (PilotID, FlightID));"
  sql_create_table_flight_pilot = "CREATE TABLE Flight_Pilot (PilotID MEDIUMINT, FlightID BIGINT,PRIMARY KEY (PilotID, FlightID), FOREIGN KEY(PilotID) REFERENCES Pilot(PilotID),FOREIGN KEY(FlightID) REFERENCES Flight(FlightID));"
  sql_populate_flight_pilot = """INSERT INTO Flight_Pilot (FlightID, PilotID)
    VALUES 
    (1, 1),
    (2, 1),
    (5, 8),
    (6, 10),
    (3, 14),
    (3, 15),
    (7, 2),
    (7, 8),
    (10, 10),
    (10, 14),
    (11, 11),
    (11, 5),
    (12, 9),
    (1, 15);"""
  sql_insert_flight_pilot_data = "INSERT INTO Flight_Pilot VALUES (?, ?);"
  sql_select_all_flight_pilot_data = "SELECT * FROM Flight_Pilot;"

  #Pilot Table queries
  sql_create_pilot_table_firsttime = "CREATE TABLE IF NOT EXISTS Pilot (PilotID MEDIUMINT NOT NULL PRIMARY KEY, PilotName VARCHAR(40) NOT NULL, PilotSeniority MEDIUMINT UNSIGNED NOT NULL);"
  sql_create_table_pilot = "CREATE TABLE Pilot (PilotID MEDIUMINT NOT NULL, PilotName VARCHAR(40) NOT NULL, PilotSeniority MEDIUMINT UNSIGNED NOT NULL, PRIMARY KEY (PilotID));"
  sql_populate_pilot = """INSERT INTO Pilot (PilotID, PilotName, PilotSeniority)
    VALUES 
    (1, 'Johnson, Trevor', 4),
    (2, 'Leibnitz, Kira', 4),
    (3, 'Donald, Scott', 2),
    (4, 'Freidrich, Larry', 4),
    (5, 'Lansky, Marina', 1),
    (6, 'Borisoff, Ilana', 4),
    (7, 'Mirsky, Konstantin', 3),
    (8, 'Levis, Alex', 1),
    (9, 'Johnson, Trevor', 4),
    (10, 'Bain, Sameera', 4),
    (11, 'Richardson, Kevin', 3),
    (12, 'Zhang, Li', 4),
    (13, 'Mirny, George', 2),
    (14, 'Pavicj, Maria', 4),
    (15, 'Jackson, Daniel', 1);"""
  sql_insert_pilot_data = "INSERT INTO Pilot VALUES (?, ?, ?);"
  sql_select_all_pilot_data = "SELECT * FROM Pilot;"
  sql_search_pilot = "SELECT * FROM Pilot where PilotID = ?;"

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
    ('SOU', 'Southampton Airport', 'Southampton', 'UK'),
    ('MAN', 'Manchester Airport', 'Manchester', 'UK'),
    ('HUY', 'Humberside Airport', 'Hull', 'UK'),
    ('EXT', 'Exeter Airport', 'Exeter', 'UK'),
    ('BRS', 'Bristol Airport', 'Bristol','UK'),
    ('BHX', 'BHX', 'Birmingham', 'UK'),
    ('EMA', 'Nottingham Airport', 'Nottingham', 'UK'),
    ('STN', 'London Stansted Airport', 'London', 'UK'),
    ('MME', 'Teesside International Airport', 'Middlesbrough', 'UK');"""
  sql_insert_destination_data = "INSERT INTO Destination VALUES (?, ?,	?, ?);"
  sql_select_all_destination_data = "SELECT * FROM Destination;"
  sql_search_destination = "SELECT * FROM Destination where DestinationID = ?;"

  #Flight Table queries
  sql_create_table_firsttime = "CREATE TABLE IF NOT EXISTS Flight (FlightID BIGINT NOT NULL PRIMARY KEY, OriginID VARCHAR(8) NOT NULL,DestinationID VARCHAR(8) NOT NULL, DepartureDate DATE NOT NULL, ScheduleID int NOT NULL, StatusID VARCHAR(2) NOT NULL);"
  #sql_drop_table = "DROP TABLE IF EXISTS Flight;"
  sql_create_table = "CREATE TABLE Flight (FlightID BIGINT NOT NULL,OriginID VARCHAR(8) NOT NULL REFERENCES Destination,DestinationID VARCHAR(8) NOT NULL REFERENCES Destination, DepartureDate DATE NOT NULL, ScheduleID int NOT NULL REFERENCES Schedule, StatusID VARCHAR(2) REFERENCES Status,PRIMARY KEY (FlightID));"
  sql_populate_flight = """INSERT INTO Flight (FlightID, OriginID, DestinationID, DepartureDate, ScheduleID, StatusID)
    VALUES 
    (1, 'BOH',	'NWI',	'2025-02-14', 6, 'SC'),
    (2, 'NWI',	'BOH',	'2025-02-15', 7, 'SC'),
    (3, 'BOH',	'LPL',	'2025-02-16', 1, 'SC'),
    (4, 'LPL',	'BOH',	'2025-02-17', 2, 'SC'),
    (5, 'BOH',	'CWL',	'2025-02-18', 3, 'SC'),
    (6, 'BOH',	'CRL',	'2025-02-19', 4, 'SC'),
    (7, 'CWL',	'BOH',	'2025-02-20', 5, 'SC'),
    (8, 'BOH',	'EDI',	'2025-02-21', 6, 'SC'),
    (9, 'CRL',	'BOH',	'2025-02-22', 7, 'SC'),
    (10, 'EDI',	'BOH',	'2025-02-23', 1, 'SC'),
    (11, 'BOH',	'GNB',	'2025-02-24', 2, 'SC'),
    (12, 'GNB',	'BOH',	'2025-02-25', 3, 'SC'),
    (13, 'BOH',	'BES',	'2025-02-25', 8, 'SC'),
    (14, 'BOH',	'LCY',	'2025-02-26', 4, 'SC'),
    (15, 'BES',	'BOH',	'2025-02-27', 5, 'SC'),
    (16, 'LCY',	'BOH',	'2025-02-28', 6, 'SC');"""

  sql_insert = "INSERT INTO Flight VALUES (?, ?,	?, ?, ?, ?);"
  sql_select_all = "SELECT * FROM Flight;"
  sql_search = "SELECT * FROM Flight where FlightID = ?;"
  sql_search_by_destination_city = "SELECT * FROM Flight JOIN Destination ON Flight.DestinationID = Destination.DestinationID WHERE Flight.DestinationID IN (SELECT Destination.DestinationID FROM Destination WHERE Destination.City = ?);"
  sql_search_by_destination_city_and_status_desc = """SELECT * FROM Flight JOIN Destination ON Flight.DestinationID = Destination.DestinationID WHERE Flight.DestinationID IN (SELECT Destination.DestinationID FROM Destination WHERE Destination.City = ?) AND
  Flight.StatusID IN (SELECT Status.StatusID FROM Status WHERE Status.StatusDesc = ?);"""
  sql_alter_data = ""
  sql_update_data = "UPDATE Flight SET StatusID = ? WHERE FlightID = ? ;"
  sql_delete_data = "DELETE FROM Flight WHERE FlightID = ?"
  sql_drop_table = "DROP TABLE IF EXISTS Flight;"

  #Status methods
  def __init_status__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
  
      self.cur.execute(self.sql_create_table_status_firsttime)
      self.conn.commit()
      self.cur.execute(self.sql_populate_status)
      self.conn.commit()
      self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
      print(self.cur.fetchall())
      print('Database input started')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def create_table_status(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table_status)
      self.cur.execute(self.sql_populate_status)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all_status_data(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all_status_data)
      result = self.cur.fetchall()

      # think how you could develop this method to show the records
      for row in result:
        print("Status ID = ", row[0])
        print("Status Description = ", row[1])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #Shedule methods
  #Initialise and populate the schedule table
  def __init_schedule__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
  
      self.cur.execute(self.sql_create_table_schedule_firsttime)
      self.conn.commit()
      self.cur.execute(self.sql_populate_schedule)
      self.conn.commit()
      self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
      print(self.cur.fetchall())
      print('Database input started')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def create_table_schedule(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table_schedule)
      self.cur.execute(self.sql_populate_schedule)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all_schedule_data(self):
    try:
      #connect to the database
      self.get_connection()
      #execute the sql statement
      self.cur.execute(self.sql_select_all_schedule_data)
      #collect all the rows into result
      result = self.cur.fetchall()

      # walking through each row and displaying the result row's attribute as row by row
      for row in result:
        print("Schedule ID = ", row[0])
        print("WeekDay = ", row[1])
        print("Departure Time = ", row[2])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def search_pilot_schedule(self):
    try:
      self.get_connection()
      pilotID = int(input("Enter Pilot ID, for example 1: "))
      self.cur.execute(self.sql_search_pilot_schedule, (pilotID,))
      result = self.cur.fetchall()
      for row in result:
        print("FlightID = ", row[0])
        print("Departure Date = ", row[1])
        print("WeekDay = ", row[2])
        print("Departure Time = ", row[3])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def __init_flight_pilot__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
  
      self.cur.execute(self.sql_create_flight_pilot_table_firsttime)
      self.conn.commit()
      self.cur.execute(self.sql_populate_flight_pilot)
      self.conn.commit()
      self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
      print(self.cur.fetchall())
      print('Database input started')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def create_table_flight_pilot(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table_flight_pilot)
      self.cur.execute(self.sql_populate_flight_pilot)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_flight_pilot_data(self):
    try:
      self.get_connection()

      flightPilot = FlightPilotInfo()
      flightPilot.set_flight_id(str(input("Enter Flight ID: ")))
      flightPilot.set_pilot_id(int(input("Enter Pilot ID: ")))
      #providing the input strings explicitly in place of question makrs of the sql query
      self.cur.execute(self.sql_insert_flight_pilot_data, (str(flightPilot.get_flight_id()),str(flightPilot.get_pilot_id())))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #display all assignments of pilots to flights
  def select_all_flight_pilot_data(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all_flight_pilot_data)
      result = self.cur.fetchall()

      # think how you could develop this method to show the records
      for row in result:
        print("Pilot ID = ", row[0])
        print("Flight ID = ", row[1])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #a method to count flights assigned per pilot
  def select_flight_counts_per_pilot(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_count_pilot_schedule)
      result = self.cur.fetchall()

      # think how you could develop this method to show the records
      for row in result:
        print("Pilot ID = ", row[0])
        print("Flight Count = ", row[1])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #Pilot methods
  def __init_pilot__(self):
    try:
      self.conn = sqlite3.connect("FMS_DB.db")
      self.cur = self.conn.cursor()
  
      self.cur.execute(self.sql_create_pilot_table_firsttime)
      self.conn.commit()
      self.cur.execute(self.sql_populate_pilot)
      self.conn.commit()
      self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
      print(self.cur.fetchall())
      print('Database input started')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def create_table_pilot(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table_pilot)
      self.cur.execute(self.sql_populate_pilot)
      self.conn.commit()
      print("Table created successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_pilot_data(self):
    try:
      self.get_connection()

      pilot = PilotInfo()
      pilot.set_pilot_id(int(input("Enter Pilot ID: ")))
      pilot.set_pilot_name(str(input("Enter Pilot name as 'Surname, Name': ")))
      pilot.set_pilot_seniority(int(input("Enter Pilot's seniority rung from 1 to 4 : ")))
  
      self.cur.execute(self.sql_insert_pilot_data, (str(pilot.get_pilot_id()),str(pilot.get_pilot_name()), str(pilot.get_pilot_seniority())))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all_pilot_data(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all_pilot_data)
      result = self.cur.fetchall()

      # think how you could develop this method to show the records
      for row in result:
        print("Pilot ID = ", row[0])
        print("Pilot Name = ", row[1])
        print("Pilot Seniority = ", row[2])

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def search_pilot_data(self):
    try:
      self.get_connection()
      pilotID = str(input("Enter PilotID: "))
      self.cur.execute(self.sql_search_pilot, (str(pilotID),))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Pilot ID: " + str(detail))
          elif index == 1:
            print("Pilot Name: " + str(detail))
          else:
            print("Pilot Seniority: " + str(detail))
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

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
      #create an object flight
      flight = FlightInfo()
      #set the attributes to the newly provided input values
      flight.set_flight_id(int(input("Enter FlightID: ")))
      flight.set_flight_origin(str(input("Enter Origin Airport IATA Code: ")))
      flight.set_flight_destination(str(input("Enter Destination Airport IATA Code: ")))
      flight.set_flight_departure_date(str(input("Enter Departure Date in a format YYYY-MM-DD: ")))
      flight.set_flight_schedule_id(str(input("Enter Schedule ID, please refer to the Schedule table, for example, 1: ")))
      flight.set_status(str(input("Enter Flight Status as 'SC' for Scheduled: ")))
      #using the tuple split to extract the individual strings from the object that was converted to strings
      self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))

      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #a method to display all the records from flight table
  def select_all(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all)
      result = self.cur.fetchall()
      #stepping through the fetched rows and converting their attributes into rows
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
            print("Flight Origin: " + str(detail))
          elif index == 2:
            print("Flight Destination: " + str(detail))
          elif index == 3:
            print("Flight Departure Date: " + str(detail))
          elif index == 4:
            print("Flight Schedule ID: " + str(detail))  
          else:
            print("Status: " + detail)
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  #a method to search the flight data by the name of the destination city, for example - Bournemouth or Edinburgh
  def search_data_by_destination_city(self):
    try:
      self.get_connection()
      city = str(input("Enter Destination City, for example London: "))
      self.cur.execute(self.sql_search_by_destination_city, (city,))
      result = self.cur.fetchall()
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
  
  #a method to search the flight data by the name of the destination city and by the status description, for example all fligths arriving to Edinburgh and have a status descriprtion Scheduled
  def search_data_by_destination_city_and_status_desc(self):
    try:
      self.get_connection()
      city = str(input("Enter Destination City, for example Bournemouth: "))
      status = str(input("Enter Status Description as per Status table, for example 'Scheduled': "))
      self.cur.execute(self.sql_search_by_destination_city_and_status_desc, (city, status))
      result = self.cur.fetchall()
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

  #a method to update flight status by providing status code such as OT for On Time, CN for Cancelled, AV for Arrived
  def update_data(self):
    try:
      self.get_connection()

      # Update statement
      flight = FlightInfo()
      flight.set_flight_id(int(input("Enter FlightID: ")))
      flight.set_status(str(input("Enter Flight Status as 'SC' for Scheduled or 'AV' for Arrived: ")))
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
        print("Departure Date = ", row[3])
        print("Schedule ID = ", row[4])
        print("Status = ", row[5])

    #this is a bug to resolve: the programign is complainting the list object has no attribute rowcount - todolist
      if result.rowcount != 0:
        print(str(self.cur.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corresponding record.

  def delete_data(self):
    try:
      self.get_connection()

      flightID = str(input("Enter FlightID: "))
      #fixed the bindings bug for the delete statement - however, now obtained a message ''NoneType' object has no attribute 'rowcount''
      self.cur.execute(self.sql_delete_data, (flightID,))
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
    self.flightDepartureDate = ''
    self.flightScheduleID = 0
    self.status = ''

  def set_flight_id(self, flightID):
    self.flightID = flightID

  # self.flight_origin was replaced with self.flightOrigin as specified in the declaration for the variables to fix the input bug
  def set_flight_origin(self, flightOrigin):
    self.flightOrigin = flightOrigin

  # self.flight_destination was replaced with self.flightDestination as specified in the declaration for the variables to fix the input bug
  def set_flight_destination(self, flightDestination):
    self.flightDestination = flightDestination
  
  def set_flight_departure_date(self, flightDepartureDate):
    self.flightDepartureDate = flightDepartureDate

  def set_flight_schedule_id(self, flightScheduleID):
    self.flightScheduleID = flightScheduleID

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
    return str(self.flightID) + "\n" + self.flightOrigin + "\n" + self.flightDestination + "\n" + self.flightDepartureDate + "\n" + str(self.flightScheduleID) + "\n" + str(self.status)


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

class PilotInfo:

  def __init_pilot__(self):
    self.pilotID = 0
    self.pilotName = ''
    self.pilotSeniority = 0

  def set_pilot_id(self, pilotID):
    self.pilotID = pilotID

  # self.flight_origin was replaced with self.flightOrigin as specified in the declaration for the variables to fix the input bug
  def set_pilot_name(self, pilotName):
    self.pilotName = pilotName

  # self.flight_destination was replaced with self.flightDestination as specified in the declaration for the variables to fix the input bug
  def set_pilot_seniority(self, pilotSeniority):
    self.pilotSeniority = pilotSeniority

  def get_pilot_id(self):
    return self.pilotID

  def get_pilot_name(self):
    return self.pilotName

  def get_pilot_seniority(self):
    return self.pilotSeniority

  def __str__(self):
    return str(self.pilotID) + "\n" + self.pilotName + "\n" + str(self.pilotSeniority)

class FlightPilotInfo:

  def __init_flight_pilot__(self):
    self.flightID = 0
    self.pilotID = 0

  def set_pilot_id(self, pilotID):
    self.pilotID = pilotID
  
  def set_flight_id(self, flightID):
    self.flightID = flightID

  def get_pilot_id(self):
    return self.pilotID
  
  def get_flight_id(self):
    return self.flightID

  def __str__(self):
    return str(self.flightID) + "\n" + str(self.pilotID)
  
class ScheduleInfo:

  def __init_schedule__(self):
    self.scheduleID = 0
    self.weekDay = ''
    self.departureTime = ''

  def set_schedule_id(self, scheduleID):
    self.scheduleID = scheduleID
  
  def set_week_day(self, weekDay):
    self.weekDay = weekDay
  
  def set_departure_time(self, departureTime):
    self.departureTime = departureTime

  def get_departure_time(self):
    return self.departureTime
  
  def get_schedule_id(self):
    return self.scheduleID
  
  def get_week_day(self):
    return self.weekDay

  def __str__(self):
    return str(self.sceduleID) + "\n" + str(self.weekDay)+ "\n" + str(self.departureTime)
    
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
  print(" 4. Search a flight by id")
  print(" 19. View flights for a particular destination city")
  print(" 20. View flights for a particular destination city and with a particular status description")
  print(" 5. Update data flight status")
  print(" 6. Delete data from flight by flight id")
  print("**********")
  print("DestinationInfo Menu")
  print(" 8. Create table Destination")
  print(" 9. Insert data into Destination")
  print(" 10. Select all data from Destination")
  print(" 11. Search a Destination")
  print("**********")
  print("PilotInfo Menu")
  print(" 12. Create table Pilot")
  print(" 13. Insert data into Pilot")
  print(" 14. Select all data from Pilot")
  print(" 15. Search a Pilot")
  print("**********")
  print("Pilot Flight Menu")
  print(" 16. Create table Flight_Pilot")
  print(" 17. Assigh Pilot to a Flight")
  print(" 18. View all Pilot-Flight assignments")
  print(" 21. View Pilot's Schedule")
  print("Schedule Menu")
  print(" 22. Create table Schedule")
  print(" 23. View all available airline's Schedules")
  print("Fligth Status Menu")
  print(" 24. Create table Status")
  print(" 25. View all descriptions for status codes")
  print("Summaries Menu")
  print(" 26. Display number of flights assigned per pilot")
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
    db_ops.search_pilot_data()
  elif __choose_menu == 12:
    db_ops.create_table_pilot()
  elif __choose_menu == 13:
    db_ops.insert_pilot_data()
  elif __choose_menu == 14:
    db_ops.select_all_pilot_data()
  elif __choose_menu == 15:
    db_ops.search_pilot_data()
  elif __choose_menu == 16:
    db_ops.create_table_flight_pilot()
  elif __choose_menu == 17:
    db_ops.insert_flight_pilot_data()
  elif __choose_menu == 18:
    db_ops.select_all_flight_pilot_data()
  elif __choose_menu == 19:
    db_ops.search_data_by_destination_city()
  elif __choose_menu == 20:
    db_ops.search_data_by_destination_city_and_status_desc()
  elif __choose_menu == 21:
    db_ops.search_pilot_schedule()
  elif __choose_menu == 22:
    db_ops.create_table_schedule()
  elif __choose_menu == 23:
    db_ops.select_all_schedule_data()
  elif __choose_menu == 24:
    db_ops.create_table_status()
  elif __choose_menu == 25:
    db_ops.select_all_status_data()
  elif __choose_menu == 26:
    db_ops.select_flight_counts_per_pilot()
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")
