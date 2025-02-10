-- This is a sandbox for testing the queries using the test database FMS_DB_TEST.db

--fectching all the flights
SELECT * from Flight;

--fectching all the pilots
SELECT * from Pilot;

--get the pilot's schedule for a specific Pilot ID
SELECT Flight.FlightID, Flight.DepartureDate, Schedule.WeekDay, Schedule.DepartureTime
FROM Schedule
JOIN Flight ON Schedule.ScheduleID = Flight.ScheduleID
JOIN Flight_Pilot ON Flight_Pilot.FlightID = Flight.FlightID
JOIN Pilot ON Flight_Pilot.PilotID = Pilot.PilotID
where Pilot.PilotID = 15
GROUP BY Schedule.WeekDay, Flight.DepartureDate
ORDER BY Schedule.WeekDay;

SELECT Flight.FlightID, Flight.DepartureDate, Schedule.WeekDay, Schedule.DepartureTime
FROM Schedule
JOIN Flight ON Schedule.ScheduleID = Flight.ScheduleID
JOIN Flight_Pilot ON Flight_Pilot.FlightID = Flight.FlightID
JOIN Pilot ON Flight_Pilot.PilotID = Pilot.PilotID
where Pilot.PilotID = 1
GROUP BY Schedule.WeekDay, Flight.DepartureDate
ORDER BY Schedule.WeekDay;


-- show all the schedules for pilots flying the same schedule - pilot caben crew
SELECT DISTINCT Pilot.PilotID, Flight.FlightID, Flight.DepartureDate, Schedule.WeekDay, Schedule.DepartureTime
FROM Schedule
JOIN Flight ON Schedule.ScheduleID = Flight.ScheduleID
JOIN Flight_Pilot ON Flight_Pilot.FlightID = Flight.FlightID
JOIN Pilot ON Flight_Pilot.PilotID = Pilot.PilotID
WHERE Pilot.PilotID IN (
    SELECT DISTINCT PilotID 
    FROM Flight_Pilot)
GROUP BY Pilot.PilotID, Schedule.WeekDay, Flight.DepartureDate
ORDER BY Pilot.PilotID, Schedule.WeekDay;

--fectching all the aiports destinations
SELECT * from Destination;

--fectching all the aiports destinations in the UK
SELECT * FROM Destination
WHERE Destination.Country = 'UK';

--fectching all the aiports destinations outside of the UK
SELECT * FROM Destination
WHERE Destination.Country NOT IN ('UK');

--count the aiports destinations outside of the UK
SELECT COUNT (DISTINCT Destination.Airport)
FROM Destination
WHERE Destination.Country NOT IN ('UK');

--show all the flights with the status Scheduled
SELECT Flight.FlightID, Flight.DepartureDate, Status.StatusDesc
FROM Flight
JOIN Status ON Flight.StatusID = Status.StatusID
WHERE Flight.StatusID IN ('SC');