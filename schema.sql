CREATE TABLE `sensordaten` (
  `PM25` decimal(4,2) DEFAULT NULL,
  `PM10` decimal(4,2) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `Temperature` decimal(4,2) DEFAULT NULL,
  `Humidity` decimal(4,2) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB;
CREATE USER 'sensor'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON feinstaub.* TO sensor@'localhost';