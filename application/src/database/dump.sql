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
  `title` varchar(255) NOT NULL,
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
(1,1,1,'static/images/user/user1.jpeg','static/file/CV_1.pdf',415,'Expert Tutor for CSC 415: Operating System Principles',35.00,
 'Struggling with CSC 415? I simplify concepts like memory management, file systems, and synchronization to help you excel. Flexible scheduling and tailored sessions.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(2,2,1,'static/images/user/user2.jpeg','static/file/CV_2.pdf',520,'Expert Guidance for CSC 520: Theory of Computing',42.00,
 'CSC 520 can be tough. I provide clear explanations of automata, Turing machines, and NP-complete problems to ensure you understand and succeed.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(3,3,1,'static/images/user/user3.jpeg','static/file/CV_3.pdf',600,'CSC 600 Tutoring: Unlocking Programming Paradigms',38.00,
 'Need help with CSC 600? I’ll clarify programming paradigms like OOP, functional programming, and logic programming to strengthen your skills.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(4,4,1,'static/images/user/user4.jpeg','static/file/CV_4.pdf',645,'CSC 645 Computer Networks Tutoring by Industry Professional',45.00,
 'Master CSC 645 with focused sessions on protocols, routing, and network security. Real-world examples to bridge theory and practice.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(5,5,1,'static/images/user/user5.jpeg','static/file/CV_5.pdf',668,'Advanced OOP Tutoring for CSC 668 Students',43.00,
 'Struggling with design patterns and UML in CSC 668? I’ll guide you through advanced OOP concepts to build robust and scalable applications.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(6,6,1,'static/images/user/user6.jpeg','static/file/CV_6.pdf',675,'Mastering Databases: CSC 675 Tutoring Services',40.00,
 'Simplify database systems in CSC 675. I focus on SQL, normalization, and transaction management to help you grasp complex concepts.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(7,7,1,'static/images/user/user7.jpeg','static/file/CV_7.pdf',690,'CSC 690 Project Guidance: From Concept to Completion',50.00,
 'Need guidance for your capstone project in CSC 690? I offer support in planning, coding, and testing to ensure project success.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(8,1,1,'static/images/user/user1.jpeg','static/file/CV_1.pdf',780,'Mobile App Development Tutoring for CSC 780',48.00,
 'Learn mobile app development in CSC 780. I focus on building responsive and optimized apps for iOS and Android platforms.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(9,2,1,'static/images/user/user2.jpeg','static/file/CV_2.pdf',831,'Level Up in CSC 831: Multiplayer Game Development Tutoring',55.00,
 'Excel in CSC 831 by mastering multiplayer game development. I cover real-time networking, game logic, and synchronization.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(10,3,1,'static/images/user/user3.jpeg','static/file/CV_3.pdf',846,'CSC 846 Tutoring: Mastering Software Metrics',45.00,
 'Understand software metrics in CSC 846. I focus on analysis, predictive models, and process improvement techniques to help you succeed.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00');
 INSERT INTO `tutor_posting` VALUES
(11,8,2,'static/images/user/user8.jpeg','static/file/CV_8.pdf',226,'Calculus I Tutoring: Master MATH 226 Concepts',35.00,
 'Struggling with limits, derivatives, or integrals in MATH 226? I simplify key concepts and help you prepare for exams with confidence.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(12,9,2,'static/images/user/user9.jpeg','static/file/CV_9.pdf',227,'Master Integration and Series in MATH 227',37.00,
 'Need help with integration techniques or series? I make complex Calculus II topics like sequences and convergence tests easy to understand.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(13,10,2,'static/images/user/user10.jpeg','static/file/CV_10.pdf',324,'Excel in Probability and Statistics: MATH 324 Tutoring',40.00,
 'Struggling with probability and statistics? I’ll guide you through distributions, hypothesis testing, and real-world data analysis.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(14,11,2,'static/images/user/user11.jpeg','static/file/CV_11.pdf',400,'MATH 400 Tutoring: Master Numerical Analysis',42.00,
 'Need help with numerical methods? I cover root-finding, interpolation, and solving ODEs with clear explanations and practical examples.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(15,12,2,'static/images/user/user12.jpeg','static/file/CV_12.pdf',325,'Linear Algebra Tutoring for MATH 325',38.00,
 'Master matrices, vector spaces, and eigenvalues in MATH 325. I offer straightforward explanations and problem-solving techniques.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(16,13,2,'static/images/user/user13.jpeg','static/file/CV_13.pdf',370,'Real Analysis Tutoring for MATH 370',45.00,
 'Struggling with sequences, continuity, and integration? I simplify real analysis concepts and help you build strong problem-solving skills.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00');
INSERT INTO `tutor_posting` VALUES
(17,9,3,'static/images/user/user9.jpeg','static/file/CV_9.pdf',214,'Improve Your Writing for ENGL 214',30.00,
 'Enhance your writing skills for ENGL 214. I help with essay structure, grammar, and research to make your writing clear and impactful.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(18,10,3,'static/images/user/user10.jpeg','static/file/CV_10.pdf',419,'Literature and Culture Tutoring for ENGL 419',35.00,
 'I help students analyze literary texts, explore cultural themes, and write compelling essays to succeed in ENGL 419.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(19,11,3,'static/images/user/user11.jpeg','static/file/CV_11.pdf',530,'Advanced Composition Tutoring for ENGL 530',40.00,
 'Refine your academic writing skills in ENGL 530. I focus on clarity, precision, research techniques, and polished final drafts.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00');
INSERT INTO `tutor_posting` VALUES
(20,12,4,'static/images/user/user12.jpeg','static/file/CV_12.pdf',230,'BIOL 230 Tutoring: Introductory Biology',35.00,
 'I simplify cell biology, genetics, and lab techniques for BIOL 230 to help you understand concepts and succeed in exams.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(21,13,4,'static/images/user/user13.jpeg','static/file/CV_13.pdf',240,'BIOL 240 Tutoring: Ecology and Evolution',37.00,
 'Struggling with ecosystems or evolutionary principles? I’ll clarify BIOL 240 concepts and help you prepare for tests and projects.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(22,14,4,'static/images/user/user14.jpeg','static/file/CV_14.pdf',355,'BIOL 355 Tutoring: Genetics Made Easy',40.00,
 'Need help with Mendelian genetics or DNA replication? I provide clear explanations and lab guidance for BIOL 355.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(23,8,4,'static/images/user/user8.jpeg','static/file/CV_8.pdf',380,'BIOL 380 Tutoring: Master Ecology Concepts',38.00,
 'Learn about ecosystems, population models, and conservation in BIOL 380. I make ecological concepts clear and relatable.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00');
INSERT INTO `tutor_posting` VALUES
(24,9,5,'static/images/user/user9.jpeg','static/file/CV_9.pdf',300,'Effective Business Communication Tutoring',35.00,
 'Improve your business writing, presentation skills, and communication techniques to excel in BUS 300.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(25,10,5,'static/images/user/user10.jpeg','static/file/CV_10.pdf',350,'Simplified Marketing Concepts for BUS 350',38.00,
 'Learn marketing strategies, case analysis, and core concepts to master BUS 350. I simplify complex topics for easy understanding.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00'),
(26,11,5,'static/images/user/user11.jpeg','static/file/CV_11.pdf',440,'BUS 440 Financial Management Tutoring',42.00,
 'Struggling with financial analysis, budgeting, or time value of money? I help you excel in BUS 440 with clear explanations.',1,'2024-06-09 12:00:00','2024-06-09 12:00:00');

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
(1,'jsmith@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','John Smith',0,'2024-10-18 08:13:36','2024-10-18 08:44:37'),
(2,'djane@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Jane Doe',0,'2024-10-18 08:42:58','2024-10-18 08:42:58'),
(3,'jrock@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Jack Rock',0,'2024-10-18 09:33:05','2024-10-18 09:33:05'),
(4,'prussel@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Paul Russel',0,'2024-10-18 09:33:34','2024-10-18 09:33:34'),
(5,'tma@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Tony Ma',0,'2024-10-18 09:34:01','2024-10-18 09:34:01'),
(6,'sjobless@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Steve Jobless',0,'2024-10-23 23:01:34','2024-10-23 23:01:34'),
(7,'asouza@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Ant Souza',0,'2024-10-25 06:12:33','2024-10-25 06:12:33'),
(8,'mbrown@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Michael Brown',0,'2024-11-10 12:00:00','2024-11-10 12:00:00'),
(9,'ljohnson@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Laura Johnson',0,'2024-11-10 12:05:00','2024-11-10 12:05:00'),
(10,'cwilson@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Chris Wilson',0,'2024-11-10 12:10:00','2024-11-10 12:10:00'),
(11,'smiller@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Sarah Miller',0,'2024-11-10 12:15:00','2024-11-10 12:15:00'),
(12,'klopez@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Kevin Lopez',0,'2024-11-10 12:20:00','2024-11-10 12:20:00'),
(13,'rgarcia@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Rachel Garcia',0,'2024-11-10 12:25:00','2024-11-10 12:25:00'),
(14,'bsmith@sfsu.edu','$2b$12$ONs5cF4m09fwzh96NBC45efu6Z2fh/.yClN.0XI0iuH16no9Xh6A6','Brian Smith',0,'2024-11-10 12:30:00','2024-11-10 12:30:00'),
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
