-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for osx10.18 (arm64)
--
-- Host: 13.57.185.95    Database: CSC648
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booking_request`
--

DROP TABLE IF EXISTS `booking_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booking_request` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tutor_posting_id` int NOT NULL,
  `sender_id` int NOT NULL,
  `description` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `booking_request_ibfk_3_idx` (`tutor_posting_id`),
  CONSTRAINT `booking_request_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `user` (`id`),
  CONSTRAINT `booking_request_ibfk_3` FOREIGN KEY (`tutor_posting_id`) REFERENCES `tutor_posting` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_request`
--

LOCK TABLES `booking_request` WRITE;
/*!40000 ALTER TABLE `booking_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `booking_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idnew_table_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES
(1,'(CSC) Computer Science'),
(2,'(MATH) Mathematics'),
(3,'(ENG) English'),
(4,'(BIOL) Biology'),
(5,'(BUS) Business');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutor_posting`
--

DROP TABLE IF EXISTS `tutor_posting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tutor_posting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `profile_picture_url` varchar(255) DEFAULT NULL,
  `cv_url` varchar(255) DEFAULT NULL,
  `class_number` int NOT NULL,
  `title` varchar(45) NOT NULL,
  `pay_rate` decimal(6,2) NOT NULL,
  `description` text NOT NULL,
  `approved` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `post_ibfk_2_idx` (`subject_id`),
  CONSTRAINT `tutor_posting_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `tutor_posting_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutor_posting`
--

LOCK TABLES `tutor_posting` WRITE;
/*!40000 ALTER TABLE `tutor_posting` DISABLE KEYS */;
INSERT INTO `tutor_posting` VALUES
(1,1,1,'static/images/user/user1.jpeg','static/file/CV.pdf',648,'Welcome to 648',35.50,'new tutor',1,'2024-10-18 08:16:40','2024-11-21 02:11:04'),
(2,1,2,'static/images/user/user1.jpeg','static/file/CV.pdf',210,'Join my 210 session',25.50,'enjoy',1,'2024-10-18 08:36:56','2024-11-21 02:11:04'),
(3,2,1,'static/images/user/user2.jpg','static/file/CV.pdf',675,'Data structures is my life!',40.50,'data structures/ MYSQL',1,'2024-10-18 08:43:47','2024-11-21 02:11:04'),
(4,3,3,'static/images/user/user1.jpeg','static/file/CV.pdf',208,'Lets learn english',24.00,'Grammar for Writing--Multilingual',1,'2024-10-18 09:37:55','2024-11-21 02:11:04'),
(5,4,1,'static/images/user/user1.jpeg','static/file/CV.pdf',510,'Lets learn algorithms',50.00,'Analysis of Algorithms I',1,'2024-10-18 09:38:59','2024-11-21 02:11:04'),
(6,5,1,'static/images/user/user1.jpeg','static/file/CV.pdf',615,'Unix is fun!',75.00,'UNIX Programming',1,'2024-10-18 09:40:02','2024-11-21 02:11:04'),
(7,3,2,'static/images/user/user1.jpeg','static/file/CV.pdf',226,'Calculus is amazing!',34.50,'Calculus I ',1,'2024-10-18 09:42:29','2024-11-21 02:11:04'),
(8,2,4,'static/images/user/user2.jpg','static/file/CV.pdf',230,'Lets learn Biology!',32.00,'Introductory Biology I ',1,'2024-10-18 09:43:59','2024-11-21 02:11:04'),
(9,5,5,'static/images/user/user1.jpeg','static/file/CV.pdf',350,'Lets get into Business',45.00,'Introduction to Entrepreneurship ',1,'2024-10-18 09:44:57','2024-11-21 02:11:04'),
(10,6,3,'static/images/user/user1.jpeg','static/file/CV.pdf',200,'Lets learn alphabets',10.00,'Elementary Alphabets',1,'2024-10-23 23:03:40','2024-11-21 02:11:04'),
(11,7,4,'static/images/user/user1.jpeg','static/file/CV.pdf',210,'Im the best Bio tutor!',1.11,'best bio teacher',1,'2024-10-25 06:13:31','2024-11-21 02:11:04'),
(12,7,5,'static/images/user/user1.jpeg','static/file/CV.pdf',111,'',100.00,'greatest business course',1,'2024-10-25 06:14:22','2024-10-30 01:10:01');
/*!40000 ALTER TABLE `tutor_posting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `is_banned` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,'jsmith@sfsu.edu','12345','John Smith',0,'2024-10-18 08:13:36','2024-10-18 08:44:37'),
(2,'djane@sfsu.edu','12345','Jane Doe',0,'2024-10-18 08:42:58','2024-10-18 08:42:58'),
(3,'jrock@sfsu.edu','12345','Jack Rock',0,'2024-10-18 09:33:05','2024-10-18 09:33:05'),
(4,'prussel@sfsu.edu','12345','Paul Russel',0,'2024-10-18 09:33:34','2024-10-18 09:33:34'),
(5,'tma@sfsu.edu','12345','Tony Ma',0,'2024-10-18 09:34:01','2024-10-18 09:34:01'),
(6,'sjobless@sfsu.edu','12345','Steve Jobless',0,'2024-10-23 23:01:34','2024-10-23 23:01:34'),
(7,'asouza@sfsu.edu','12345','Ant Souza',0,'2024-10-25 06:12:33','2024-10-25 06:12:33'),
(23,'test@test.com','password','Test User',0,'2024-11-08 06:51:27','2024-11-08 06:51:27');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-21 16:21:21
