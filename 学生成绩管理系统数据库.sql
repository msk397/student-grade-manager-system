-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: python
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `grade`
--

DROP TABLE IF EXISTS `grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `grade` (
  `num` varchar(20) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `class` varchar(20) NOT NULL,
  `course1` double(5,2) DEFAULT '-1.00',
  `course2` double(5,2) DEFAULT '-1.00',
  `course3` double(5,2) DEFAULT '-1.00',
  `sum` double(5,2) DEFAULT '0.00',
  PRIMARY KEY (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade`
--

LOCK TABLES `grade` WRITE;
/*!40000 ALTER TABLE `grade` DISABLE KEYS */;
INSERT INTO `grade` VALUES ('110203','周元恺','四年级一班',90.00,83.00,80.70,253.70),('110204','钱鸿风','四年级一班',71.00,75.00,67.40,213.40),('110205','孙智勇','四年级一班',98.00,77.00,74.90,249.90),('110206','郑鸿晖','四年级一班',63.00,76.00,60.50,199.50),('110207','李德明','四年级一班',94.00,77.00,68.60,239.60),('110208','钱德华','四年级一班',92.00,86.00,76.60,254.60),('110209','钱良材','四年级一班',93.00,88.00,75.80,256.80),('110210','赵成和','四年级一班',92.00,77.00,52.90,221.90),('110211','李涵意','四年级一班',96.00,80.00,63.60,239.60),('110212','赵正祥','四年级一班',0.00,78.00,62.00,140.00),('110213','王玉成','四年级一班',72.00,78.00,0.00,150.00),('110214','孙弘致','四年级一班',60.00,76.00,66.30,202.30),('110215','孙浩波','四年级一班',80.00,75.00,63.00,218.00),('110216','赵和畅','四年级一班',73.00,77.00,68.20,218.20),('110217','钱子濯','四年级一班',0.00,0.00,0.00,0.00),('110218','周子轩','四年级一班',76.00,69.00,60.50,205.50),('110219','郑天空','四年级一班',79.00,73.00,60.10,212.10),('110220','吴力行','四年级一班',82.00,83.00,67.00,232.00),('110221','吴星驰','四年级一班',97.00,86.00,87.40,270.40),('110222','郑德庸','四年级一班',82.00,73.00,78.80,233.80),('110223','李俊誉','四年级一班',96.00,82.00,73.70,251.70),('110224','周博易','四年级一班',0.00,64.00,60.40,124.40),('110225','周天华','四年级一班',62.00,73.00,0.00,135.00),('110226','郑鹏运','四年级一班',94.00,87.00,80.30,261.30),('110227','郑思敏','四年级一班',88.00,78.00,82.10,248.10),('110228','钱含香','四年级一班',100.00,93.00,94.70,287.70),('110229','王芳泽','四年级一班',68.00,67.00,0.00,135.00),('110230','吴高洁','四年级一班',86.00,82.00,82.30,250.30),('110231','李韦柔','四年级一班',100.00,76.00,83.80,259.80),('110232','王初雪','四年级一班',100.00,90.00,87.60,277.60),('110233','李妙旋','四年级一班',84.00,81.00,64.90,229.90),('110234','周觅海','四年级一班',89.00,70.00,60.20,219.20),('110235','马晗蕾','四年级二班',87.60,89.50,84.60,261.70),('110236','马恺歌','四年级二班',82.20,90.90,64.30,237.40),('110237','马香天','四年级二班',84.60,79.70,65.00,229.30),('110238','马永言','四年级二班',78.00,84.60,81.10,243.70),('110239','马云梦','四年级二班',68.40,72.70,65.70,206.80),('110240','马杰秀','四年级二班',87.00,65.00,72.00,224.00),('110241','马晗玥','四年级二班',82.00,60.10,74.80,216.90),('110242','马怡宁','四年级二班',81.60,76.90,72.70,231.20),('110243','马元瑶','四年级二班',75.80,67.80,68.50,212.10),('110244','马家馨','四年级二班',70.60,79.00,65.70,215.30),('110245','林依秋','四年级二班',82.20,67.80,68.50,218.50),('110246','林弘文','四年级二班',79.60,60.80,60.80,201.20),('110247','林格格','四年级二班',85.20,62.90,71.10,219.20),('110248','林宾白','四年级二班',75.40,88.80,60.10,224.30),('110249','林嘉勋','四年级二班',81.80,77.60,0.00,159.40),('110250','林新翰','四年级二班',86.40,65.70,0.00,152.10),('110251','林雅可','四年级二班',60.20,80.40,65.70,206.30),('110252','林初然','四年级二班',84.00,79.70,62.90,226.60),('110253','林冷梅','四年级二班',71.80,74.10,0.00,145.90),('110254','林明旭','四年级二班',68.40,63.50,67.80,199.70),('110255','陈慧丽','四年级二班',67.80,72.00,60.60,200.40),('110256','陈香蝶','四年级二班',84.60,73.40,0.00,158.00),('110257','陈从波','四年级二班',71.40,63.60,60.10,195.10),('110258','陈碧菡','四年级二班',84.60,70.60,66.40,221.60),('110259','陈兰芝','四年级二班',79.80,0.00,87.40,167.20),('110260','陈鸿风','四年级二班',77.60,62.20,80.40,220.20),('110261','陈陶然','四年级二班',82.80,62.20,78.30,223.30),('110262','陈怜雪','四年级二班',69.60,0.00,82.50,152.10),('110263','陈涵易','四年级二班',77.40,76.20,80.40,234.00),('110264','陈芷荷','四年级二班',75.20,76.90,83.90,236.00),('110265','孔子凡','四年级二班',66.00,66.40,74.10,206.50),('110266','孔小雨','四年级二班',68.40,78.80,78.30,225.50),('110267','孔俊材','四年级二班',74.20,75.60,66.40,216.20);
/*!40000 ALTER TABLE `grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `root`
--

DROP TABLE IF EXISTS `root`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `root` (
  `username` varchar(15) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `root`
--

LOCK TABLES `root` WRITE;
/*!40000 ALTER TABLE `root` DISABLE KEYS */;
INSERT INTO `root` VALUES ('root','123'),('root1','123');
/*!40000 ALTER TABLE `root` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stud`
--

DROP TABLE IF EXISTS `stud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stud` (
  `username` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `pass` varchar(30) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud`
--

LOCK TABLES `stud` WRITE;
/*!40000 ALTER TABLE `stud` DISABLE KEYS */;
/*!40000 ALTER TABLE `stud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student` (
  `username` varchar(20) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `password` varchar(20) NOT NULL DEFAULT '123456',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('110203','周元恺','123456'),('110204','钱鸿风','123456'),('110205','孙智勇','123456'),('110206','郑鸿晖','123456'),('110207','李德明','123456'),('110208','钱德华','123456'),('110209','钱良材','123456'),('110210','赵成和','123456'),('110211','李涵意','123456'),('110212','赵正祥','123456'),('110213','王玉成','123456'),('110214','孙弘致','123456'),('110215','孙浩波','123456'),('110216','赵和畅','123456'),('110217','钱子濯','123456'),('110218','周子轩','123456'),('110219','郑天空','123456'),('110220','吴力行','123456'),('110221','吴星驰','123456'),('110222','郑德庸','123456'),('110223','李俊誉','123456'),('110224','周博易','123456'),('110225','周天华','123456'),('110226','郑鹏运','123456'),('110227','郑思敏','123456'),('110228','钱含香','123456'),('110229','王芳泽','123456'),('110230','吴高洁','123456'),('110231','李韦柔','123456'),('110232','王初雪','123456'),('110233','李妙旋','123456'),('110234','周觅海','123456'),('110235','马晗蕾','123456'),('110236','马恺歌','123456'),('110237','马香天','123456'),('110238','马永言','123456'),('110239','马云梦','123456'),('110240','马杰秀','123456'),('110241','马晗玥','123456'),('110242','马怡宁','123456'),('110243','马元瑶','123456'),('110244','马家馨','123456'),('110245','林依秋','123456'),('110246','林弘文','123456'),('110247','林格格','123456'),('110248','林宾白','123456'),('110249','林嘉勋','123456'),('110250','林新翰','123456'),('110251','林雅可','123456'),('110252','林初然','123456'),('110253','林冷梅','123456'),('110254','林明旭','123456'),('110255','陈慧丽','123456'),('110256','陈香蝶','123456'),('110257','陈从波','123456'),('110258','陈碧菡','123456'),('110259','陈兰芝','123456'),('110260','陈鸿风','123456'),('110261','陈陶然','123456'),('110262','陈怜雪','123456'),('110263','陈涵易','123456'),('110264','陈芷荷','123456'),('110265','孔子凡','123456'),('110266','孔小雨','123456'),('110267','孔俊材','123456');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `teacher` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL DEFAULT '123456',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('teacher','123'),('teacher1','1234'),('teacher2','123'),('teacher3','123');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `up`
--

DROP TABLE IF EXISTS `up`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `up` (
  `sno` varchar(15) NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `up`
--

LOCK TABLES `up` WRITE;
/*!40000 ALTER TABLE `up` DISABLE KEYS */;
/*!40000 ALTER TABLE `up` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-18 10:17:23
