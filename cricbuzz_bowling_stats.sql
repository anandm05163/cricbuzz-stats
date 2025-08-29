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
-- Table structure for table `bowling_stats`
--

DROP TABLE IF EXISTS `bowling_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bowling_stats` (
  `bowling_stats_id` int NOT NULL AUTO_INCREMENT,
  `player_id` int NOT NULL,
  `match_id` int NOT NULL,
  `overs_bowled` decimal(4,1) NOT NULL,
  `wickets` int NOT NULL,
  `economy_rate` decimal(4,2) NOT NULL,
  PRIMARY KEY (`bowling_stats_id`),
  KEY `player_id` (`player_id`),
  KEY `match_id` (`match_id`),
  CONSTRAINT `bowling_stats_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`),
  CONSTRAINT `bowling_stats_ibfk_2` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bowling_stats`
--

LOCK TABLES `bowling_stats` WRITE;
/*!40000 ALTER TABLE `bowling_stats` DISABLE KEYS */;
INSERT INTO `bowling_stats` VALUES (1,1,2,5.0,3,3.20),(2,1,6,4.0,2,4.50),(3,1,7,6.0,4,2.80),(4,2,2,4.0,1,5.00),(5,2,6,5.0,3,3.60),(6,2,7,4.0,2,4.20),(7,3,8,4.0,5,2.50),(8,3,9,4.0,2,3.80),(9,3,2,5.0,3,3.00);
/*!40000 ALTER TABLE `bowling_stats` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-28 20:48:46
