-- MySQL dump 10.13  Distrib 9.0.1, for Linux (x86_64)
--
-- Host: localhost    Database: chat_application
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(150) NOT NULL,
  `is_received` tinyint(1) NOT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_messages_id` (`id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Hi backend',1,'2024-09-04 16:43:10',1),(2,'Hello postman',1,'2024-09-04 16:55:46',1),(3,'Hi frontend',0,'2024-09-04 16:56:09',1),(4,'Hi socket',0,'2024-09-04 17:10:25',1),(5,'Hi socket',1,'2024-09-04 17:10:26',1),(6,'Testing sender msg',0,'2024-09-04 17:11:01',1),(7,'Testing sender msg',1,'2024-09-04 17:11:01',1),(8,'hello there',0,'2024-09-04 17:49:38',1),(9,'hello there',1,'2024-09-04 17:49:38',1),(10,'Hello error',1,'2024-09-04 22:21:56',1),(11,'Hii socket',0,'2024-09-04 22:44:20',1),(12,'Hii socket',1,'2024-09-04 22:44:20',1),(13,'hi',0,'2024-09-04 22:54:20',1),(14,'hi',1,'2024-09-04 22:54:20',1),(15,'Hello user',0,'2024-09-04 22:54:31',1),(16,'Hello user',1,'2024-09-04 22:54:31',1),(17,'one',0,'2024-09-04 22:54:48',1),(18,'one',1,'2024-09-04 22:54:48',1),(19,'two',1,'2024-09-04 22:54:57',1),(20,'two',0,'2024-09-04 22:54:57',1),(21,'two',1,'2024-09-04 22:54:57',1),(22,'three',0,'2024-09-04 22:55:05',1),(23,'three',1,'2024-09-04 22:55:05',1),(24,'four',0,'2024-09-04 23:11:26',1),(25,'four',1,'2024-09-04 23:11:26',1),(26,'five',0,'2024-09-04 23:12:08',1),(27,'five',1,'2024-09-04 23:12:09',1),(28,'six',0,'2024-09-04 23:12:58',1),(29,'six',1,'2024-09-04 23:12:58',1),(30,'seven',0,'2024-09-04 23:15:08',1),(31,'seven',1,'2024-09-04 23:15:08',1),(32,'eiight',0,'2024-09-04 23:18:14',1),(33,'eiight',1,'2024-09-04 23:18:14',1),(34,'nine',0,'2024-09-04 23:18:57',1),(35,'nine',1,'2024-09-04 23:18:57',1),(36,'10',0,'2024-09-04 23:19:04',1),(37,'10',1,'2024-09-04 23:19:04',1),(38,'11',0,'2024-09-04 23:31:57',1),(39,'11',1,'2024-09-04 23:31:57',1),(40,'12',0,'2024-09-04 23:51:11',1),(41,'12',1,'2024-09-04 23:51:11',1),(42,'13',0,'2024-09-05 00:06:48',1),(43,'13',1,'2024-09-05 00:06:48',1),(44,'14',0,'2024-09-05 00:07:28',1),(45,'14',1,'2024-09-05 00:07:28',1),(46,'hii',0,'2024-09-05 10:03:28',1),(47,'hii',1,'2024-09-05 10:03:28',1),(48,'socket two',0,'2024-09-05 10:06:29',2),(49,'socket two',1,'2024-09-05 10:06:29',2);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'one@gmail.com','12345678'),(2,'two@gmail.com','two');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-05 13:25:16
