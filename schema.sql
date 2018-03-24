-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: 35.227.38.69    Database: sosapp
-- ------------------------------------------------------
-- Server version	5.7.14-google-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED='d0dc6914-2f19-11e8-a525-42010a8e0082:1-6023';

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patientID` int(11) DEFAULT NULL,
  `doctorID` int(11) DEFAULT NULL,
  `appointmentDate` datetime DEFAULT NULL,
  `appointmentType` varchar(255) DEFAULT NULL,
  `reason` text,
  `results` text,
  `extradetails` text,
  `privatenotes` text,
  PRIMARY KEY (`id`),
  KEY `IDX_appointments_patientID` (`patientID`),
  KEY `IDX_appointments_doctorID` (`doctorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `basicmedicaldatahsitory`
--

DROP TABLE IF EXISTS `basicmedicaldatahsitory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basicmedicaldatahsitory` (
  `userid` int(11) DEFAULT NULL,
  `appointmentID` int(11) DEFAULT NULL,
  `recordType` int(11) DEFAULT NULL,
  `recordValue` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='for height, weight, blood pressure';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `emergencylog`
--

DROP TABLE IF EXISTS `emergencylog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emergencylog` (
  `rowid` int(11) NOT NULL AUTO_INCREMENT,
  `patientID` varchar(255) DEFAULT NULL,
  `calltime` datetime DEFAULT NULL,
  `locationlatitude` decimal(10,0) DEFAULT NULL,
  `locationlongitude` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`rowid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medication`
--

DROP TABLE IF EXISTS `medication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medication` (
  `medID` int(11) NOT NULL AUTO_INCREMENT,
  `patientID` int(11) DEFAULT NULL,
  `medicationType` int(11) DEFAULT NULL,
  `dosage` int(11) DEFAULT NULL,
  `dosageunits` int(11) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `frequencyunit` int(11) DEFAULT NULL,
  PRIMARY KEY (`medID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `testinformation`
--

DROP TABLE IF EXISTS `testinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testinformation` (
  `testID` int(11) NOT NULL AUTO_INCREMENT,
  `doctorID` int(11) DEFAULT NULL,
  `patientID` int(11) DEFAULT NULL,
  `testType` varchar(255) DEFAULT NULL,
  `testDate` datetime DEFAULT NULL,
  `result` text,
  `privatenotes` text,
  `appoitmentID` int(11) DEFAULT NULL,
  PRIMARY KEY (`testID`),
  KEY `IDX_testinformation_doctorID` (`doctorID`),
  KEY `IDX_testinformation_patientID` (`patientID`),
  KEY `IDX_testinformation_appoitment` (`appoitmentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `useremail` varchar(255) DEFAULT NULL,
  `userpassword_salt` varchar(8) DEFAULT NULL,
  `userpassword_hash` varchar(255) DEFAULT NULL,
  `usertype` tinyint(4) DEFAULT NULL,
  `userbirthday` date DEFAULT NULL,
  `bloodtype` varchar(4) DEFAULT NULL,
  `emergencycontactname` varchar(255) DEFAULT NULL,
  `emergencycontactphone` varchar(255) DEFAULT NULL,
  `doctorType` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-24  1:55:23
