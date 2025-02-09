DROP TABLE IF EXISTS Flight;

CREATE TABLE Flight (
    FlightID VARCHAR(5) NOT NULL,
    OriginID VARCHAR(8) NOT NULL REFERENCES Destination,
    DestinationID VARCHAR(8) NOT NULL REFERENCES Destination,
    DepartureDate DATE NOT NULL, 
    ScheduleID int NOT NULL REFERENCES Schedule, 
    StatusID VARCHAR(1) REFERENCES Status, 
    PRIMARY KEY (FlightID));


DROP TABLE IF EXISTS Pilot;

CREATE TABLE Pilot (
    PilotID MEDIUMINT NOT NULL,
    PilotName VARCHAR(40) NOT NULL,
    PilotSeniority MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (PilotID));


DROP TABLE IF EXISTS Flight_Pilot;

CREATE TABLE Flight_Pilot (
    PilotID MEDIUMINT,
    FlightID VARCHAR(30),
    PRIMARY KEY (PilotID, FlightID),
    FOREIGN KEY(PilotID) REFERENCES Pilot(PilotID),
    FOREIGN KEY(FlightID) REFERENCES Flight(FlightID)
    );


DROP TABLE IF EXISTS Schedule;

CREATE TABLE Schedule (
    ScheduleID MEDIUMINT AUTO_INCREMENT,
    WeekDay VARCHAR(10),
    DepartureTime DATE NOT NULL,
    PRIMARY KEY (ScheduleID));


DROP TABLE IF EXISTS Status;

CREATE TABLE Status (
    StatusID VARCHAR(2) NOT NULL,
    StatusDesc VARCHAR(15),
    PRIMARY KEY (StatusID));


DROP TABLE IF EXISTS Destination;

CREATE TABLE Destination (
    DestinationID VARCHAR(8) NOT NULL,
    Airport VARCHAR(30) NOT NULL,
    City VARCHAR(30) NOT NULL,
    Country VARCHAR(30) NOT NULL,
    PRIMARY KEY (DestinationID));