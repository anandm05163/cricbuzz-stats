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
-- Table structure for table `batting_stats`
--

DROP TABLE IF EXISTS `batting_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batting_stats` (
  `batting_stats_id` int NOT NULL AUTO_INCREMENT,
  `player_id` int NOT NULL,
  `match_id` int NOT NULL,
  `innings_id` int NOT NULL,
  `batting_position` int NOT NULL,
  `runs` int NOT NULL,
  `team_id` int NOT NULL,
  PRIMARY KEY (`batting_stats_id`),
  KEY `player_id` (`player_id`),
  KEY `match_id` (`match_id`),
  KEY `team_id` (`team_id`),
  CONSTRAINT `batting_stats_ibfk_1` FOREIGN KEY (`player_id`) REFERENCES `players` (`player_id`),
  CONSTRAINT `batting_stats_ibfk_2` FOREIGN KEY (`match_id`) REFERENCES `matches` (`match_id`),
  CONSTRAINT `batting_stats_ibfk_3` FOREIGN KEY (`team_id`) REFERENCES `teams` (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batting_stats`
--

LOCK TABLES `batting_stats` WRITE;
/*!40000 ALTER TABLE `batting_stats` DISABLE KEYS */;
INSERT INTO `batting_stats` VALUES (1,1,2,1,1,60,2),(2,2,2,1,2,70,3),(3,3,6,2,1,80,4),(4,4,6,2,2,75,5),(5,5,7,1,1,90,5),(6,6,7,1,2,65,4),(7,7,8,1,3,50,3),(8,8,9,2,4,60,2),(9,9,2,1,3,45,3);
/*!40000 ALTER TABLE `batting_stats` ENABLE KEYS */;
UNLOCK TABLES;
