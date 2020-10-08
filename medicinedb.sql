
-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Company
-- ------------------------------------------------------
-- Server version   5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE=`+00:00` */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE=`NO_AUTO_VALUE_ON_ZERO` */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DEPARTMENT`
--
DROP DATABASE IF EXISTS `MEDICINE` ;
CREATE SCHEMA `MEDICINE`;
USE `MEDICINE`;
DROP TABLE IF EXISTS `medicines`;
create table medicines(
     UID int NOT NULL,
     company_name varchar (50) NOT NULL,
     medicine_name varchar (50) NOT NULL,
     cost int NOT NULL,
     date_of_manufacture MEDIUMTEXT NOT NULL,
     best_before int NOT NULL,
     expiry_date MEDIUMTEXT NOT NULL,
     type varchar(50));
ALTER TABLE medicines DROP COLUMN company_name;
ALTER TABLE medicines ADD PRIMARY KEY (UID);
ALTER TABLE medicines MODIFY COLUMN date_of_manufacture DATE;
ALTER TABLE medicines MODIFY COLUMN expiry_date DATE;
DROP TABLE IF EXISTS `company`;
CREATE TABLE company(
     company_name varchar (20) NOT NULL,
     PRIMARY KEY (company_name)
     );
DROP TABLE IF EXISTS `symptoms`;
CREATE TABLE symptoms( s_name varchar (50) NOT NULL, PRIMARY KEY (s_name));
DROP TABLE IF EXISTS `chemical`;
CREATE TABLE chemical ( chemical_name varchar (50) NOT  NULL, chemical_ID int NOT NULL, PRIMARY KEY (chemical_ID));
DROP TABLE IF EXISTS `disease`;
CREATE TABLE disease ( disease_namename varchar (50) NOT NULL, primary key(disease_namename));
DROP TABLE IF EXISTS `people_requests`;
CREATE TABLE people_requests ( mobilenumber int (10) NOT NULL, PRIMARY KEY (mobilenumber));
ALTER TABLE medicines ADD company_name varchar (50) NOT NULL;
ALTER TABLE medicines ADD FOREIGN KEY (company_name) REFERENCES company(company_name);
DROP TABLE IF EXISTS `made_of`;
create table made_of (medicine_ID int NOT NULL, used_chemical_id int NOT NULL);
ALTER TABLE made_of ADD FOREIGN KEY (medicine_ID) REFERENCES medicines(UID);
ALTER TABLE made_of ADD FOREIGN KEY (used_chemical_ID) REFERENCES chemical(chemical_ID);
DROP table IF EXISTS `uses`;
CREATE TABLE uses( m_ID int NOT NULL, ch_ID int NOT NULL, dis_name varchar (50) NOT NULL, symp_name varchar (50) NOT NULL);
ALTER TABLE uses ADD FOREIGN KEY (m_ID) REFERENCES medicines(UID);
ALTER TABLE uses ADD FOREIGN KEY (ch_ID) REFERENCES chemical(chemical_ID);
ALTER TABLE uses ADD FOREIGN KEY (dis_name) REFERENCES disease(disease_namename);
ALTER TABLE uses ADD FOREIGN KEY (symp_name) REFERENCES symptoms(s_name);
DROP TABLE IF EXISTS `cures`;
CREATE TABLE cures( medicine_ID int NOT NULL, disease_name varchar (50) NOT NULL, symptom_name varchar (50) NOT NULL);
ALTER TABLE cures ADD FOREIGN KEY (medicine_ID) REFERENCES medicines(UID);
ALTER TABLE cures ADD FOREIGN KEY (disease_name) REFERENCES disease(disease_namename);
ALTER TABLE cures ADD FOREIGN KEY (symptom_name) REFERENCES symptoms(s_name);
DROP TABLE IF EXISTS `symptoms_names`;
CREATE TABLE symptoms_names ( symptom_name varchar(50) NOT NULL, disease_name varchar(50) NOT NULL);
ALTER TABLE symptoms_names ADD FOREIGN KEY (disease_name) REFERENCES disease(disease_namename);
DROP TABLE IF EXISTS `details`;
CREATE TABLE details (name_customer varchar (50) NOT NULL, home_number varchar (50) NOT NULL, street varchar (50) NOT NULL, village varchar (50) NOT NULL, pincode varchar (50) NOT NULL, state varchar (50) NOT NULL, date_of_request DATE NOT NULL);
DROP TABLE IF EXISTS `rm_attributes`;
CREATE TABLE rm_attributes ( name varchar (50) NOT NULL, quantity int NOT NULL);
ALTER TABLE people_requests MODIFY COLUMN mobilenumber varchar (10);
DROP TABLE IF EXISTS `requested_medicines`;
CREATE TABLE requested_medicines( number varchar (10) NOT NULL);
ALTER TABLE requested_medicines ADD FOREIGN KEY (number) REFERENCES people_requests(mobilenumber);
ALTER TABLE details ADD p_number varchar (10) NOT NULL;
ALTER TABLE details ADD FOREIGN KEY (p_number) REFERENCES people_requests(mobilenumber);
ALTER TABLE rm_attributes ADD number varchar (10) NOT NULL;
ALTER TABLE rm_attributes ADD FOREIGN KEY (number) REFERENCES requested_medicines(number);
DROP TABLE IF EXISTS `chemical_cures`;
CREATE TABLE chemical_cures( c_ID int NOT NULL, d_name varchar (50) NOT NULL);
ALTER TABLE chemical_cures ADD FOREIGN KEY (c_ID) REFERENCES chemical(chemical_ID);
ALTER TABLE chemical_cures ADD FOREIGN KEY (d_name) REFERENCES disease(disease_namename);
LOCK TABLES `medicines` WRITE;
INSERT INTO `medicines` VALUES (1,'dolo 650',20,'2018-02-02',38,'2021-04-02','tablet','Micro Labs Limited'),(3,'eldoper',20,'2018-03-03',38,'2021-05-03','tablet','Micro Labs Limited'),(5,'digene',40,'2019-02-02',38,'2022-04-02','tablet','Abbott'),(7,'CPP',20,'2018-02-02',38,'2021-04-02','tablet','P & B pharmamaceuticals')
, (9,'Benadryl',50,'2018-02-02',38,'2021-04-02','tonic','Johnson & Johnson'),(11,'P650',20,'2018-02-02',38,'2021-04-02','tablet','Abbortt'),(13,'TT',18,'2018-02-02',36,'2021-02-02','injection','Avalon Pharma'),(15,'citrezine',80,'2019-02-10',38,'2022-04-10','tablet','Sun Pharma'),
(17,'Benadryl',120,'2020-02-02',38,'2023-04-02','tonic','Johnson & Johnson'),(19,'volini',202,'2020-09-09',48,'2024-09-09','ointment','volini ind.');
UNLOCK TABLES;
LOCK TABLES `chemical` WRITE;
INSERT INTO `chemical` VALUES('paracetamol',2),('loperamide hydrochloride',4),('Aluminium Hydroxide',6),('Diphenhydramine',8),('Tetanus Toxoid',10),('antihistamatic',12),('diclofenac diethylamine',14);
UNLOCK TABLES;
LOCK TABLES `company` WRITE;
INSERT INTO `company` VALUES ('Micro Labs Limited'),('MCL'),('Abbott'),('P & B pharmamaceuticals'),('Johnson & Johnson'),('volini ind.'),('Avalon Pharma'),('Sun Pharma');
UNLOCK TABLES;
LOCK TABLES `symptoms` WRITE;
INSERT INTO `symptoms` VALUES ('cold'),('fever'),('motions'),('sprain'),('headache'),('nasuea'),('cough'),('general'),('stomach pain'),('hurt and infection'),('sneezing'),('body pains');
UNLOCK TABLES;
LOCK TABLES `disease` WRITE;
INSERT INTO `disease` VALUES ('flu'),('diarea'),('gas'),('sprain'),('headache'),('nasuea'),('cough'),('general'),('viral fever'),('tetanus'),('allergy and cold'),('sprains');
UNLOCK TABLES;
LOCK TABLES `chemical_cures` WRITE;
INSERT INTO `chemical_cures` VALUES(2,'flu'),(2,'common fever'),(4,'diarea'),(6,'gas'),(8,'dry cough'),(2,'viral fever'),(10,'tetanus'),(12,'allergy and cold'),(14,'sprains');
UNLOCK TABLES;
LOCK TABLES `cures` WRITE;
INSERT INTO `cures` VALUES(1,'flu','cold'),(1,'common fever','headache'),(3,'diarea','motions'),(5,'gas','stomach pain'),(7,'flu','cold'),(9,'dry cough','cough'),(11,'viral fever','fever'),(13,'tetanus','hurt and infection'),(15,'allergy and cold','sneezing'),(17,'dry cough','cough'),(19,'sprain','body pains');
UNLOCK TABLES;
LOCK TABLES `details` WRITE;
INSERT INTO `details` VALUES('varun','10-48','near yadgiri teatre','gajwel','502311','Telangana','2019-02-02','8688366350'),('priya','23-11/6','near balaji temple','siddipet','500278','Telangana','2019-02-08','9856745678');
UNLOCK TABLES;
LOCK TABLES `made_of` WRITE;
INSERT INTO `made_of` VALUES(1,2),(3,4),(5,6),(7,2),(9,8),(11,2),(13,10),(15,12),(17,8),(19,14);
UNLOCK TABLES;
LOCK TABLES `people_requests` WRITE;
INSERT INTO `people_requests` VALUES('8688366350'),('9856745678');
UNLOCK TABLES;
LOCK TABLES `requested_medicines` WRITE;
INSERT INTO `requested_medicines` VALUES('8688366350'),('9856745678');
UNLOCK TABLES;
LOCK TABLES `rm_attributes` WRITE;
INSERT INTO `rm_attributes` VALUES('monocef',5,'8688366350'),('artivan',3,'9856745678'),('lecab xl',3,'9856745678');
UNLOCK TABLES;
LOCK TABLES `symptoms_names` WRITE;
INSERT INTO `symptoms_names` VALUES('headache','flu'),('cold','flu'),('motions','diarea'),('stomach pain','gas'),('cough','dry cough'),('fever','viral fever'),('hurt and infection','tetanus'),('allergy and cold','sneezing');
UNLOCK TABLES;
LOCK TABLES `uses` WRITE;
INSERT INTO `uses` VALUES(1,2,'flu','cold'),(3,4,'diarea','motions'),(5,6,'gas','stomach pain'),(7,2,'flu','cold'),(9,8,'dry cough','cough'),(11,2,'viral fever','fever'),(13,10,'tetanus','hurt and infected'),(15,12,'allergy and cold','sneezing'),(17,8,'dry cough','cough'),(19,14,'sprain','body pains');
UNLOCK TABLES;


