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
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `playing_role` varchar(50) DEFAULT NULL,
  `batting_style` varchar(50) DEFAULT NULL,
  `bowling_style` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'Rehan Ahmed','England',NULL,NULL,NULL),(2,'Prashant Veer','India',NULL,NULL,NULL),(3,'MD Nidheesh','India',NULL,NULL,NULL),(4,'Shreyas Gopal','India',NULL,NULL,NULL),(5,'Money Grewal','India',NULL,NULL,NULL),(6,'Akhil Scaria','India',NULL,NULL,NULL),(7,'Rohan Kunnummal','India',NULL,NULL,NULL),(8,'Tejasvi Dahiya','India',NULL,NULL,NULL),(9,'Rituraj Sharma','India',NULL,NULL,NULL),(10,'Ackeem Auguste','West Indies',NULL,NULL,NULL),(11,'Joe Root','England','Batsman','Right-hand bat','Right-arm offbreak'),(12,'Virat Kohli','India','Batsman','Right-hand bat',NULL),(13,'Pat Cummins','Australia','Bowler',NULL,'Right-arm fast'),(14,'Kane Williamson','New Zealand','Batsman','Right-hand bat',NULL),(15,'Rashid Khan','Afghanistan','Bowler','Right-hand bat','Right-arm legbreak'),(103,'Sameer Rizvi','India',NULL,NULL,NULL),(104,'Sanju Samson','India',NULL,NULL,NULL),(105,'Mohammad Amir','Pakistan',NULL,NULL,NULL),(106,'Jan Frylinck','Namibia',NULL,NULL,NULL),(107,'Rehan Ahmed','England',NULL,NULL,NULL),(108,'Prashant Veer','India',NULL,NULL,NULL),(109,'MD Nidheesh','India',NULL,NULL,NULL),(110,'Shreyas Gopal','India',NULL,NULL,NULL),(111,'Money Grewal','India',NULL,NULL,NULL),(112,'Akhil Scaria','India',NULL,NULL,NULL);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
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
