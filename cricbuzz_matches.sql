CREATE DATABASE  IF NOT EXISTS `cricbuzz` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cricbuzz`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cricbuzz
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `matches`
--

DROP TABLE IF EXISTS `matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matches` (
  `match_id` int NOT NULL AUTO_INCREMENT,
  `match_description` varchar(255) DEFAULT NULL,
  `team1_id` int DEFAULT NULL,
  `team2_id` int DEFAULT NULL,
  `venue_id` int DEFAULT NULL,
  `match_date` date DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `match_type` varchar(50) DEFAULT NULL,
  `winner_id` int DEFAULT NULL,
  PRIMARY KEY (`match_id`),
  KEY `team1_id` (`team1_id`),
  KEY `team2_id` (`team2_id`),
  KEY `venue_id` (`venue_id`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`team1_id`) REFERENCES `teams` (`team_id`),
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`team2_id`) REFERENCES `teams` (`team_id`),
  CONSTRAINT `matches_ibfk_3` FOREIGN KEY (`venue_id`) REFERENCES `venues` (`venue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matches`
--

LOCK TABLES `matches` WRITE;
/*!40000 ALTER TABLE `matches` DISABLE KEYS */;
INSERT INTO `matches` VALUES (2,'1st ODI',2,4,1,'2025-08-01','Win','ODI',2),(6,'1st Test',4,5,1,'2025-07-15','Draw','Test',NULL),(7,'2nd T20I',3,5,1,'2025-08-10','Loss','T20I',5),(8,'3rd ODI',13,10,1,'2025-08-15','Win','ODI',13),(9,'1st Test',6,12,1,'2025-07-20','Win','Test',6);
/*!40000 ALTER TABLE `matches` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-28 20:48:45
