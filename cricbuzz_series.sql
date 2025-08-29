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
-- Table structure for table `series`
--

DROP TABLE IF EXISTS `series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `series` (
  `series_id` int NOT NULL AUTO_INCREMENT,
  `series_name` varchar(255) DEFAULT NULL,
  `host_country` varchar(100) DEFAULT NULL,
  `match_type` varchar(50) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `total_matches` int DEFAULT NULL,
  PRIMARY KEY (`series_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10841 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `series`
--

LOCK TABLES `series` WRITE;
/*!40000 ALTER TABLE `series` DISABLE KEYS */;
INSERT INTO `series` VALUES (7572,'ICC Cricket World Cup League Two 2023-27',NULL,NULL,'2024-02-15',NULL),(8788,'South Africa tour of England, 2025',NULL,NULL,'2025-09-02',NULL),(8802,'England tour of Ireland, 2025',NULL,NULL,'2025-09-17',NULL),(9107,'The Ashes, 2025-26',NULL,NULL,'2025-11-21',NULL),(9551,'West Indies tour of South Africa, 2026',NULL,NULL,'2026-01-27',NULL),(9596,'India tour of Australia, 2025',NULL,NULL,'2025-10-19',NULL),(9602,'South Africa tour of Australia, 2025',NULL,NULL,'2025-08-10',NULL),(9629,'West Indies tour of India, 2025',NULL,NULL,'2025-10-02',NULL),(9638,'South Africa tour of India, 2025',NULL,NULL,'2025-11-14',NULL),(9686,'India tour of Bangladesh, 2025 (Called off)',NULL,NULL,'2025-08-17',NULL),(10091,'West Indies vs Nepal in UAE, 2025',NULL,NULL,'2025-09-27',NULL),(10102,'New Zealand tour of India, 2026',NULL,NULL,'2026-01-11',NULL),(10201,'Australia tour of New Zealand, 2025',NULL,NULL,'2025-10-01',NULL),(10212,'England tour of New Zealand, 2025',NULL,NULL,'2025-10-18',NULL),(10223,'West Indies tour of New Zealand, 2025',NULL,NULL,'2025-11-05',NULL),(10234,'South Africa tour of New Zealand, 2026',NULL,NULL,'2026-03-15',NULL),(10267,'Sri Lanka tour of Zimbabwe, 2025',NULL,NULL,'2025-08-29',NULL),(10504,'South Africa tour of Namibia 2025',NULL,NULL,'2025-10-11',NULL),(10532,'India tour of England, 2026',NULL,NULL,'2026-07-01',NULL),(10559,'New Zealand tour of England, 2026',NULL,NULL,'2026-06-04',NULL),(10565,'Pakistan tour of England 2026',NULL,NULL,'2026-08-19',NULL),(10576,'Sri Lanka tour of England, 2026',NULL,NULL,'2026-09-15',NULL),(10587,'Asia Cup 2025',NULL,NULL,'2025-09-09',NULL),(10625,'ICC Mens T20 World Cup East Asia Pacific Qualifier 2025',NULL,NULL,'2025-10-08',NULL),(10642,'United Arab Emirates T20I Tri-Series 2025',NULL,NULL,'2025-08-29',NULL),(10647,'Netherlands tour of Bangladesh 2025',NULL,NULL,'2025-08-30',NULL),(10746,'Belgium tour of Austria 2025',NULL,NULL,'2025-08-23',NULL),(10774,'England tour of Sri Lanka 2026',NULL,NULL,'2026-01-22',NULL),(10790,'Eastern Europe Cup 2025',NULL,NULL,'2025-08-29',NULL),(10801,'Guernsey Tri-Nation T20I Series 2025',NULL,NULL,'2025-08-29',NULL),(10812,'Sweden tour of Isle Of Man 2025',NULL,NULL,'2025-09-06',NULL),(10840,'Afghanistan vs Bangladesh in UAE 2025',NULL,NULL,'2025-10-02',NULL);
/*!40000 ALTER TABLE `series` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-28 20:48:47
