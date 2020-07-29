CREATE TABLE `sensordaten` (
  `PM25` decimal(4,2) DEFAULT NULL,
  `PM10` decimal(4,2) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `Temperature` decimal(4,2) DEFAULT NULL,
  `Humidity` decimal(4,2) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
