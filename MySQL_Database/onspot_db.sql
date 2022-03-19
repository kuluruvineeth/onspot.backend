--
-- Host: localhost    Database: onspot
-- ------------------------------------------------------
-- Server version	ubuntu0.18.04.1

--
-- Table structure for table `__authorities__`
--

DROP TABLE IF EXISTS `__authorities__`;
CREATE TABLE `__authorities__` (
  `authority_id` varchar(50) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `photo_url` text NOT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`authority_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `__authorities__`
--

LOCK TABLES `__authorities__` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `__authority_zones__`
--

DROP TABLE IF EXISTS `__authority_zones__`;
CREATE TABLE `__authority_zones__` (
  `authority_id` varchar(50) NOT NULL,
  `zipcode` varchar(10) NOT NULL,
  PRIMARY KEY (`authority_id`,`zipcode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `__authority_zones__`
--

LOCK TABLES `__authority_zones__` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `__public_users__`
--

DROP TABLE IF EXISTS `__public_users__`;
CREATE TABLE `__public_users__` (
  `user_id` varchar(50) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `badge` varchar(100) NOT NULL,
  `photo_url` text NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `__public_users__`
--

LOCK TABLES `__public_users__` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `__report_comments__`
--

DROP TABLE IF EXISTS `__report_comments__`;
CREATE TABLE `__report_comments__` (
  `user_type` varchar(50) NOT NULL,
  `comment_id` varchar(100) NOT NULL,
  `comment_text` text NOT NULL,
  `case_id` varchar(50) NOT NULL,
  `comment_date_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `__report_comments__`
--

LOCK TABLES `__report_comments__` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `__reports__`
--

DROP TABLE IF EXISTS `__reports__`;
CREATE TABLE `__reports__` (
  `case_id` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `imageURL` text NOT NULL,
  `latitude` varchar(50) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  `severity` int(2) NOT NULL,
  `userId` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_date` varchar(50) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `address` varchar(1000) DEFAULT NULL,
  `location_point` point DEFAULT NULL,
  PRIMARY KEY (`case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `__reports__`
--

LOCK TABLES `__reports__` WRITE;
UNLOCK TABLES;

-- Dump completed on 2022-03-18 20:07:57
