
INSERT INTO Flight (FlightID, OriginID, DestinationID, DepartureDate, ScheduleID, StatusID)
VALUES 
  ('TYCV', 'BOH',	'NWI',	'2025-02-14', 6, 'SC'),
  ('T25V', 'NWI',	'BOH',	'2025-02-15', 7, 'SC'),
  ('1KOR', 'BOH',	'LPL',	'2025-02-16', 1, 'SC'),
  ('RTY2', 'LPL',	'BOH',	'2025-02-17', 2, 'SC'),
  ('CVNE', 'BOH',	'CWL',	'2025-02-18', 3, 'SC'),
  ('WERT', 'BOH',	'CRL',	'2025-02-19', 4, 'SC'),
  ('VGP8', 'CWL',	'BOH',	'2025-02-20', 5, 'SC'),
  ('128I', 'BOH',	'EDI',	'2025-02-21', 6, 'SC'),
  ('W7YT', 'CRL',	'BOH',	'2025-02-22', 7, 'SC'),
  ('B78Y', 'EDI',	'BOH',	'2025-02-23', 1, 'SC'),
  ('Q7XC', 'BOH',	'GNB',	'2025-02-24', 2, 'SC'),
  ('9YFI', 'GNB',	'BOH',	'2025-02-25', 3, 'SC'),
  ('V7YT', 'BOH',	'BES',	'2025-02-25', 8, 'SC'),
  ('8YT6', 'BOH',	'LCY',	'2025-02-26', 4, 'SC'),
  ('A5CV', 'BES',	'BOH',	'2025-02-27', 5, 'SC'),
  ('19UY', 'LCY',	'BOH',	'2025-02-28', 6, 'SC');


INSERT INTO Pilot (PilotID, PilotName, PilotSeniority)
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
  (15, 'Jackson, Daniel', 1);


INSERT INTO Flight_Pilot (FlightID, PilotID)
VALUES 
  ('TYCV', 1),
  ('TYCV', 15);


INSERT INTO Schedule (ScheduleID, WeekDay, DepartureTime)
VALUES
  (1, 'SUN', '14:30'),
  (2, 'MON', '10:30'),
  (3, 'TUE', '09:30'),
  (4, 'WED', '10:30'),
  (5, 'THU', '17:30'),
  (6, 'FRI', '15:30'),
  (7, 'SAT', '11:30'),
  (8, 'SAT', '20:30');

INSERT INTO Status (StatusID, StatusDesc)
VALUES
  ('SC', 'Scheduled'),
  ('CN', 'Cancelled'),
  ('OT', 'On Time'),
  ('DE', 'Delayed'),
  ('AV', 'Arrived'),
  ('DP', 'Departed');


INSERT INTO Destination (DestinationID, Airport, City, Country)
VALUES 
  ('BOH', 'Bournemouth Airport', 'Bournemouth', 'UK'),
  ('NWI', 'Norwich Airport', 'Norwich', 'UK'),
  ('LPL', 'Liverpool John Lennon Airport', 'Liverpool', 'UK'),
  ('CWL', 'Cardiff Airport', 'Cardiff', 'Wales'),
  ('CRL', 'Brussels South Charleroi Airport', 'Charleroi','Belgium'),
  ('EDI', 'Edinburgh Airport', 'Edinburgh', 'UK'),
  ('GNB', 'Alpes-Isere Airport', 'Grenoble', 'France'),
  ('BES', 'Brest Bretagne Airport', 'Brest', 'France'),
  ('LCY', 'London City Airport', 'London', 'UK');