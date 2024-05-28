CREATE DATABASE  IF NOT EXISTS `codenames` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `codenames`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: codenames
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `asocijacija`
--

DROP TABLE IF EXISTS `asocijacija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asocijacija` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `zadataRec` varchar(50) DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `asocijacija_user_id_daa8f648_fk_korisnik_id` (`user_id`),
  CONSTRAINT `asocijacija_user_id_daa8f648_fk_korisnik_id` FOREIGN KEY (`user_id`) REFERENCES `korisnik` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asocijacija`
--

LOCK TABLES `asocijacija` WRITE;
/*!40000 ALTER TABLE `asocijacija` DISABLE KEYS */;
INSERT INTO `asocijacija` VALUES (1,'agaga',3),(2,'zastava',3),(3,'Love',4),(4,'dsa',4);
/*!40000 ALTER TABLE `asocijacija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add rec',6,'add_rec'),(22,'Can change rec',6,'change_rec'),(23,'Can delete rec',6,'delete_rec'),(24,'Can view rec',6,'view_rec'),(25,'Can add korisnik',7,'add_korisnik'),(26,'Can change korisnik',7,'change_korisnik'),(27,'Can delete korisnik',7,'delete_korisnik'),(28,'Can view korisnik',7,'view_korisnik'),(29,'Can add asocijacija',8,'add_asocijacija'),(30,'Can change asocijacija',8,'change_asocijacija'),(31,'Can delete asocijacija',8,'delete_asocijacija'),(32,'Can view asocijacija',8,'view_asocijacija'),(33,'Can add pogadjanje',9,'add_pogadjanje'),(34,'Can change pogadjanje',9,'change_pogadjanje'),(35,'Can delete pogadjanje',9,'delete_pogadjanje'),(36,'Can view pogadjanje',9,'view_pogadjanje'),(37,'Can add set reci',10,'add_setreci'),(38,'Can change set reci',10,'change_setreci'),(39,'Can delete set reci',10,'delete_setreci'),(40,'Can view set reci',10,'view_setreci');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_korisnik_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_korisnik_id` FOREIGN KEY (`user_id`) REFERENCES `korisnik` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=226 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (3,'2024-05-13 12:37:43.500502','1','Asocijacija object (1)',1,'[{\"added\": {}}]',8,3),(4,'2024-05-13 12:37:50.629369','2','Asocijacija object (2)',1,'[{\"added\": {}}]',8,3),(5,'2024-05-13 12:38:22.839732','1','Pogadjanje object (1)',1,'[{\"added\": {}}]',9,3),(6,'2024-05-13 12:38:25.454131','2','Pogadjanje object (2)',1,'[{\"added\": {}}]',9,3),(7,'2024-05-13 12:38:31.558508','3','Pogadjanje object (3)',1,'[{\"added\": {}}]',9,3),(8,'2024-05-13 12:38:34.562541','4','Pogadjanje object (4)',1,'[{\"added\": {}}]',9,3),(9,'2024-05-13 12:38:53.358464','3','admin',2,'[{\"changed\": {\"fields\": [\"Broj partija leader\", \"Broj pobeda leader\", \"Broj partija guesser\", \"Broj pobeda guesser\"]}}]',7,3),(10,'2024-05-13 14:11:23.610587','1','Rec object (1)',1,'[{\"added\": {}}]',6,3),(11,'2024-05-13 14:11:39.417190','1','SetReci object (1)',1,'[{\"added\": {}}]',10,3),(12,'2024-05-13 14:47:32.850139','7','Rec object (7)',3,'',6,3),(13,'2024-05-13 14:47:32.857883','6','Rec object (6)',3,'',6,3),(14,'2024-05-13 14:47:32.864535','5','Rec object (5)',3,'',6,3),(15,'2024-05-13 14:47:32.871886','4','Rec object (4)',3,'',6,3),(16,'2024-05-13 14:47:32.880891','3','Rec object (3)',3,'',6,3),(17,'2024-05-13 14:47:32.887670','2','Rec object (2)',3,'',6,3),(18,'2024-05-13 14:47:41.446384','207','Rec object (207)',3,'',6,3),(19,'2024-05-13 14:47:41.453258','206','Rec object (206)',3,'',6,3),(20,'2024-05-13 14:47:41.460463','205','Rec object (205)',3,'',6,3),(21,'2024-05-13 14:47:41.466806','204','Rec object (204)',3,'',6,3),(22,'2024-05-13 14:47:41.472949','203','Rec object (203)',3,'',6,3),(23,'2024-05-13 14:47:41.479254','202','Rec object (202)',3,'',6,3),(24,'2024-05-13 14:47:41.486250','201','Rec object (201)',3,'',6,3),(25,'2024-05-13 14:47:41.493527','200','Rec object (200)',3,'',6,3),(26,'2024-05-13 14:47:41.500316','199','Rec object (199)',3,'',6,3),(27,'2024-05-13 14:47:41.506251','198','Rec object (198)',3,'',6,3),(28,'2024-05-13 14:47:41.513254','197','Rec object (197)',3,'',6,3),(29,'2024-05-13 14:47:41.523150','196','Rec object (196)',3,'',6,3),(30,'2024-05-13 14:47:41.533147','195','Rec object (195)',3,'',6,3),(31,'2024-05-13 14:47:41.539651','194','Rec object (194)',3,'',6,3),(32,'2024-05-13 14:47:41.546156','193','Rec object (193)',3,'',6,3),(33,'2024-05-13 14:47:41.552968','192','Rec object (192)',3,'',6,3),(34,'2024-05-13 14:47:41.559970','191','Rec object (191)',3,'',6,3),(35,'2024-05-13 14:47:41.566972','190','Rec object (190)',3,'',6,3),(36,'2024-05-13 14:47:41.573973','189','Rec object (189)',3,'',6,3),(37,'2024-05-13 14:47:41.583975','188','Rec object (188)',3,'',6,3),(38,'2024-05-13 14:47:41.590976','187','Rec object (187)',3,'',6,3),(39,'2024-05-13 14:47:41.597979','186','Rec object (186)',3,'',6,3),(40,'2024-05-13 14:47:41.605852','185','Rec object (185)',3,'',6,3),(41,'2024-05-13 14:47:41.615859','184','Rec object (184)',3,'',6,3),(42,'2024-05-13 14:47:41.622863','183','Rec object (183)',3,'',6,3),(43,'2024-05-13 14:47:41.631928','182','Rec object (182)',3,'',6,3),(44,'2024-05-13 14:47:41.638253','181','Rec object (181)',3,'',6,3),(45,'2024-05-13 14:47:41.645251','180','Rec object (180)',3,'',6,3),(46,'2024-05-13 14:47:41.652252','179','Rec object (179)',3,'',6,3),(47,'2024-05-13 14:47:41.659254','178','Rec object (178)',3,'',6,3),(48,'2024-05-13 14:47:41.666238','177','Rec object (177)',3,'',6,3),(49,'2024-05-13 14:47:41.673038','176','Rec object (176)',3,'',6,3),(50,'2024-05-13 14:47:41.680041','175','Rec object (175)',3,'',6,3),(51,'2024-05-13 14:47:41.686043','174','Rec object (174)',3,'',6,3),(52,'2024-05-13 14:47:41.693253','173','Rec object (173)',3,'',6,3),(53,'2024-05-13 14:47:41.700242','172','Rec object (172)',3,'',6,3),(54,'2024-05-13 14:47:41.707077','171','Rec object (171)',3,'',6,3),(55,'2024-05-13 14:47:41.714055','170','Rec object (170)',3,'',6,3),(56,'2024-05-13 14:47:41.720057','169','Rec object (169)',3,'',6,3),(57,'2024-05-13 14:47:41.726952','168','Rec object (168)',3,'',6,3),(58,'2024-05-13 14:47:41.734092','167','Rec object (167)',3,'',6,3),(59,'2024-05-13 14:47:41.740955','166','Rec object (166)',3,'',6,3),(60,'2024-05-13 14:47:41.747253','165','Rec object (165)',3,'',6,3),(61,'2024-05-13 14:47:41.754216','164','Rec object (164)',3,'',6,3),(62,'2024-05-13 14:47:41.760256','163','Rec object (163)',3,'',6,3),(63,'2024-05-13 14:47:41.767255','162','Rec object (162)',3,'',6,3),(64,'2024-05-13 14:47:41.774258','161','Rec object (161)',3,'',6,3),(65,'2024-05-13 14:47:41.781261','160','Rec object (160)',3,'',6,3),(66,'2024-05-13 14:47:41.788220','159','Rec object (159)',3,'',6,3),(67,'2024-05-13 14:47:41.794258','158','Rec object (158)',3,'',6,3),(68,'2024-05-13 14:47:41.804223','157','Rec object (157)',3,'',6,3),(69,'2024-05-13 14:47:41.811227','156','Rec object (156)',3,'',6,3),(70,'2024-05-13 14:47:41.819916','155','Rec object (155)',3,'',6,3),(71,'2024-05-13 14:47:41.826256','154','Rec object (154)',3,'',6,3),(72,'2024-05-13 14:47:41.833258','153','Rec object (153)',3,'',6,3),(73,'2024-05-13 14:47:41.839260','152','Rec object (152)',3,'',6,3),(74,'2024-05-13 14:47:41.846241','151','Rec object (151)',3,'',6,3),(75,'2024-05-13 14:47:41.858256','150','Rec object (150)',3,'',6,3),(76,'2024-05-13 14:47:41.870849','149','Rec object (149)',3,'',6,3),(77,'2024-05-13 14:47:41.879356','148','Rec object (148)',3,'',6,3),(78,'2024-05-13 14:47:41.886267','147','Rec object (147)',3,'',6,3),(79,'2024-05-13 14:47:41.892432','146','Rec object (146)',3,'',6,3),(80,'2024-05-13 14:47:41.899130','145','Rec object (145)',3,'',6,3),(81,'2024-05-13 14:47:41.905263','144','Rec object (144)',3,'',6,3),(82,'2024-05-13 14:47:41.912264','143','Rec object (143)',3,'',6,3),(83,'2024-05-13 14:47:41.918851','142','Rec object (142)',3,'',6,3),(84,'2024-05-13 14:47:41.924800','141','Rec object (141)',3,'',6,3),(85,'2024-05-13 14:47:41.932264','140','Rec object (140)',3,'',6,3),(86,'2024-05-13 14:47:41.938258','139','Rec object (139)',3,'',6,3),(87,'2024-05-13 14:47:41.945263','138','Rec object (138)',3,'',6,3),(88,'2024-05-13 14:47:41.952265','137','Rec object (137)',3,'',6,3),(89,'2024-05-13 14:47:41.959267','136','Rec object (136)',3,'',6,3),(90,'2024-05-13 14:47:41.965267','135','Rec object (135)',3,'',6,3),(91,'2024-05-13 14:47:41.972097','134','Rec object (134)',3,'',6,3),(92,'2024-05-13 14:47:41.978633','133','Rec object (133)',3,'',6,3),(93,'2024-05-13 14:47:41.985268','132','Rec object (132)',3,'',6,3),(94,'2024-05-13 14:47:41.991247','131','Rec object (131)',3,'',6,3),(95,'2024-05-13 14:47:41.998268','130','Rec object (130)',3,'',6,3),(96,'2024-05-13 14:47:42.005270','129','Rec object (129)',3,'',6,3),(97,'2024-05-13 14:47:42.012273','128','Rec object (128)',3,'',6,3),(98,'2024-05-13 14:47:42.018259','127','Rec object (127)',3,'',6,3),(99,'2024-05-13 14:47:42.024260','126','Rec object (126)',3,'',6,3),(100,'2024-05-13 14:47:42.032267','125','Rec object (125)',3,'',6,3),(101,'2024-05-13 14:47:42.041270','124','Rec object (124)',3,'',6,3),(102,'2024-05-13 14:47:42.047271','123','Rec object (123)',3,'',6,3),(103,'2024-05-13 14:47:42.057774','122','Rec object (122)',3,'',6,3),(104,'2024-05-13 14:47:42.085778','121','Rec object (121)',3,'',6,3),(105,'2024-05-13 14:47:42.110260','120','Rec object (120)',3,'',6,3),(106,'2024-05-13 14:47:42.127272','119','Rec object (119)',3,'',6,3),(107,'2024-05-13 14:47:42.139274','118','Rec object (118)',3,'',6,3),(108,'2024-05-13 14:47:42.155476','117','Rec object (117)',3,'',6,3),(109,'2024-05-13 14:47:42.166281','116','Rec object (116)',3,'',6,3),(110,'2024-05-13 14:47:42.187271','115','Rec object (115)',3,'',6,3),(111,'2024-05-13 14:47:42.202462','114','Rec object (114)',3,'',6,3),(112,'2024-05-13 14:47:42.224263','113','Rec object (113)',3,'',6,3),(113,'2024-05-13 14:47:42.235247','112','Rec object (112)',3,'',6,3),(114,'2024-05-13 14:47:42.242254','111','Rec object (111)',3,'',6,3),(115,'2024-05-13 14:47:42.249255','110','Rec object (110)',3,'',6,3),(116,'2024-05-13 14:47:42.256257','109','Rec object (109)',3,'',6,3),(117,'2024-05-13 14:47:42.263259','108','Rec object (108)',3,'',6,3),(118,'2024-05-13 14:47:55.274511','107','Rec object (107)',3,'',6,3),(119,'2024-05-13 14:47:55.282829','106','Rec object (106)',3,'',6,3),(120,'2024-05-13 14:47:55.289519','105','Rec object (105)',3,'',6,3),(121,'2024-05-13 14:47:55.296519','104','Rec object (104)',3,'',6,3),(122,'2024-05-13 14:47:55.303011','103','Rec object (103)',3,'',6,3),(123,'2024-05-13 14:47:55.309436','102','Rec object (102)',3,'',6,3),(124,'2024-05-13 14:47:55.316432','101','Rec object (101)',3,'',6,3),(125,'2024-05-13 14:47:55.323078','100','Rec object (100)',3,'',6,3),(126,'2024-05-13 14:47:55.329863','99','Rec object (99)',3,'',6,3),(127,'2024-05-13 14:47:55.335866','98','Rec object (98)',3,'',6,3),(128,'2024-05-13 14:47:55.342871','97','Rec object (97)',3,'',6,3),(129,'2024-05-13 14:47:55.349876','96','Rec object (96)',3,'',6,3),(130,'2024-05-13 14:47:55.356848','95','Rec object (95)',3,'',6,3),(131,'2024-05-13 14:47:55.363787','94','Rec object (94)',3,'',6,3),(132,'2024-05-13 14:47:55.370884','93','Rec object (93)',3,'',6,3),(133,'2024-05-13 14:47:55.379310','92','Rec object (92)',3,'',6,3),(134,'2024-05-13 14:47:55.386314','91','Rec object (91)',3,'',6,3),(135,'2024-05-13 14:47:55.392947','90','Rec object (90)',3,'',6,3),(136,'2024-05-13 14:47:55.399701','89','Rec object (89)',3,'',6,3),(137,'2024-05-13 14:47:55.406059','88','Rec object (88)',3,'',6,3),(138,'2024-05-13 14:47:55.412437','87','Rec object (87)',3,'',6,3),(139,'2024-05-13 14:47:55.421440','86','Rec object (86)',3,'',6,3),(140,'2024-05-13 14:47:55.428444','85','Rec object (85)',3,'',6,3),(141,'2024-05-13 14:47:55.435316','84','Rec object (84)',3,'',6,3),(142,'2024-05-13 14:47:55.442626','83','Rec object (83)',3,'',6,3),(143,'2024-05-13 14:47:55.449020','82','Rec object (82)',3,'',6,3),(144,'2024-05-13 14:47:55.455614','81','Rec object (81)',3,'',6,3),(145,'2024-05-13 14:47:55.462028','80','Rec object (80)',3,'',6,3),(146,'2024-05-13 14:47:55.468590','79','Rec object (79)',3,'',6,3),(147,'2024-05-13 14:47:55.474438','78','Rec object (78)',3,'',6,3),(148,'2024-05-13 14:47:55.482013','77','Rec object (77)',3,'',6,3),(149,'2024-05-13 14:47:55.488432','76','Rec object (76)',3,'',6,3),(150,'2024-05-13 14:47:55.495035','75','Rec object (75)',3,'',6,3),(151,'2024-05-13 14:47:55.501874','74','Rec object (74)',3,'',6,3),(152,'2024-05-13 14:47:55.508875','73','Rec object (73)',3,'',6,3),(153,'2024-05-13 14:47:55.514881','72','Rec object (72)',3,'',6,3),(154,'2024-05-13 14:47:55.521880','71','Rec object (71)',3,'',6,3),(155,'2024-05-13 14:47:55.527880','70','Rec object (70)',3,'',6,3),(156,'2024-05-13 14:47:55.535197','69','Rec object (69)',3,'',6,3),(157,'2024-05-13 14:47:55.541889','68','Rec object (68)',3,'',6,3),(158,'2024-05-13 14:47:55.548404','67','Rec object (67)',3,'',6,3),(159,'2024-05-13 14:47:55.554755','66','Rec object (66)',3,'',6,3),(160,'2024-05-13 14:47:55.560896','65','Rec object (65)',3,'',6,3),(161,'2024-05-13 14:47:55.567433','64','Rec object (64)',3,'',6,3),(162,'2024-05-13 14:47:55.574442','63','Rec object (63)',3,'',6,3),(163,'2024-05-13 14:47:55.580800','62','Rec object (62)',3,'',6,3),(164,'2024-05-13 14:47:55.586803','61','Rec object (61)',3,'',6,3),(165,'2024-05-13 14:47:55.593465','60','Rec object (60)',3,'',6,3),(166,'2024-05-13 14:47:55.599466','59','Rec object (59)',3,'',6,3),(167,'2024-05-13 14:47:55.606932','58','Rec object (58)',3,'',6,3),(168,'2024-05-13 14:47:55.613720','57','Rec object (57)',3,'',6,3),(169,'2024-05-13 14:47:55.620298','56','Rec object (56)',3,'',6,3),(170,'2024-05-13 14:47:55.626432','55','Rec object (55)',3,'',6,3),(171,'2024-05-13 14:47:55.633414','54','Rec object (54)',3,'',6,3),(172,'2024-05-13 14:47:55.640029','53','Rec object (53)',3,'',6,3),(173,'2024-05-13 14:47:55.646310','52','Rec object (52)',3,'',6,3),(174,'2024-05-13 14:47:55.653030','51','Rec object (51)',3,'',6,3),(175,'2024-05-13 14:47:55.659592','50','Rec object (50)',3,'',6,3),(176,'2024-05-13 14:47:55.666035','49','Rec object (49)',3,'',6,3),(177,'2024-05-13 14:47:55.672564','48','Rec object (48)',3,'',6,3),(178,'2024-05-13 14:47:55.679044','47','Rec object (47)',3,'',6,3),(179,'2024-05-13 14:47:55.685539','46','Rec object (46)',3,'',6,3),(180,'2024-05-13 14:47:55.691659','45','Rec object (45)',3,'',6,3),(181,'2024-05-13 14:47:55.698661','44','Rec object (44)',3,'',6,3),(182,'2024-05-13 14:47:55.706666','43','Rec object (43)',3,'',6,3),(183,'2024-05-13 14:47:55.712637','42','Rec object (42)',3,'',6,3),(184,'2024-05-13 14:47:55.722588','41','Rec object (41)',3,'',6,3),(185,'2024-05-13 14:47:55.729564','40','Rec object (40)',3,'',6,3),(186,'2024-05-13 14:47:55.735421','39','Rec object (39)',3,'',6,3),(187,'2024-05-13 14:47:55.742631','38','Rec object (38)',3,'',6,3),(188,'2024-05-13 14:47:55.749568','37','Rec object (37)',3,'',6,3),(189,'2024-05-13 14:47:55.756574','36','Rec object (36)',3,'',6,3),(190,'2024-05-13 14:47:55.762576','35','Rec object (35)',3,'',6,3),(191,'2024-05-13 14:47:55.769882','34','Rec object (34)',3,'',6,3),(192,'2024-05-13 14:47:55.776582','33','Rec object (33)',3,'',6,3),(193,'2024-05-13 14:47:55.785586','32','Rec object (32)',3,'',6,3),(194,'2024-05-13 14:47:55.791587','31','Rec object (31)',3,'',6,3),(195,'2024-05-13 14:47:55.800883','30','Rec object (30)',3,'',6,3),(196,'2024-05-13 14:47:55.807596','29','Rec object (29)',3,'',6,3),(197,'2024-05-13 14:47:55.817599','28','Rec object (28)',3,'',6,3),(198,'2024-05-13 14:47:55.824601','27','Rec object (27)',3,'',6,3),(199,'2024-05-13 14:47:55.831117','26','Rec object (26)',3,'',6,3),(200,'2024-05-13 14:47:55.838586','25','Rec object (25)',3,'',6,3),(201,'2024-05-13 14:47:55.845475','24','Rec object (24)',3,'',6,3),(202,'2024-05-13 14:47:55.852593','23','Rec object (23)',3,'',6,3),(203,'2024-05-13 14:47:55.859596','22','Rec object (22)',3,'',6,3),(204,'2024-05-13 14:47:55.866445','21','Rec object (21)',3,'',6,3),(205,'2024-05-13 14:47:55.875382','20','Rec object (20)',3,'',6,3),(206,'2024-05-13 14:47:55.882385','19','Rec object (19)',3,'',6,3),(207,'2024-05-13 14:47:55.889390','18','Rec object (18)',3,'',6,3),(208,'2024-05-13 14:47:55.896392','17','Rec object (17)',3,'',6,3),(209,'2024-05-13 14:47:55.902901','16','Rec object (16)',3,'',6,3),(210,'2024-05-13 14:47:55.909890','15','Rec object (15)',3,'',6,3),(211,'2024-05-13 14:47:55.916893','14','Rec object (14)',3,'',6,3),(212,'2024-05-13 14:47:55.923895','13','Rec object (13)',3,'',6,3),(213,'2024-05-13 14:47:55.930247','12','Rec object (12)',3,'',6,3),(214,'2024-05-13 14:47:55.936894','11','Rec object (11)',3,'',6,3),(215,'2024-05-13 14:47:55.944206','10','Rec object (10)',3,'',6,3),(216,'2024-05-13 14:47:55.951206','9','Rec object (9)',3,'',6,3),(217,'2024-05-13 14:47:55.958383','8','Rec object (8)',3,'',6,3),(218,'2024-05-13 14:48:49.381598','2','SetReci object (2)',3,'',10,3),(219,'2024-05-14 16:13:08.300958','1','SetReci object (1)',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',10,3),(220,'2024-05-14 16:31:09.368875','1','SetReci object (1)',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',10,3),(221,'2024-05-14 16:59:10.360129','1','SetReci object (1)',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',10,3),(222,'2024-05-14 16:59:14.446985','1','SetReci object (1)',2,'[{\"changed\": {\"fields\": [\"Reci\"]}}]',10,3),(223,'2024-05-14 16:59:21.789120','1','SetReci object (1)',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',10,3),(224,'2024-05-16 10:21:30.382006','4','SetReci object (4)',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',10,3),(225,'2024-05-28 12:18:18.381647','4','djole123',2,'[{\"changed\": {\"fields\": [\"Broj partija leader\", \"Broj pobeda leader\", \"Broj partija guesser\"]}}]',7,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(8,'home','asocijacija'),(7,'home','korisnik'),(9,'home','pogadjanje'),(6,'home','rec'),(10,'home','setreci'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-05-13 11:12:00.826869'),(2,'contenttypes','0002_remove_content_type_name','2024-05-13 11:12:00.983277'),(3,'auth','0001_initial','2024-05-13 11:12:01.593605'),(4,'auth','0002_alter_permission_name_max_length','2024-05-13 11:12:01.762271'),(5,'auth','0003_alter_user_email_max_length','2024-05-13 11:12:01.772765'),(6,'auth','0004_alter_user_username_opts','2024-05-13 11:12:01.781771'),(7,'auth','0005_alter_user_last_login_null','2024-05-13 11:12:01.791987'),(8,'auth','0006_require_contenttypes_0002','2024-05-13 11:12:01.799069'),(9,'auth','0007_alter_validators_add_error_messages','2024-05-13 11:12:01.808985'),(10,'auth','0008_alter_user_username_max_length','2024-05-13 11:12:01.817995'),(11,'auth','0009_alter_user_last_name_max_length','2024-05-13 11:12:01.827812'),(12,'auth','0010_alter_group_name_max_length','2024-05-13 11:12:01.854496'),(13,'auth','0011_update_proxy_permissions','2024-05-13 11:12:01.865499'),(14,'auth','0012_alter_user_first_name_max_length','2024-05-13 11:12:01.890017'),(15,'home','0001_initial','2024-05-13 11:12:03.359280'),(16,'admin','0001_initial','2024-05-13 11:12:03.660048'),(17,'admin','0002_logentry_remove_auto_add','2024-05-13 11:12:03.672984'),(18,'admin','0003_logentry_add_action_flag_choices','2024-05-13 11:12:03.685531'),(19,'sessions','0001_initial','2024-05-13 11:12:03.766041'),(20,'home','0002_setreci_active','2024-05-13 13:37:47.911987'),(21,'home','0003_setreci_kreator','2024-05-14 17:18:28.066590');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('52w0dn565j3k2vdgdlnbatjf2i4un1eu','.eJxVjMEOwiAQRP-FsyGwCFk8evcbyLKAVA0kpT0Z_9026UFPk8x7M28RaF1qWEeew5TERRhx-u0i8TO3HaQHtXuX3NsyT1HuijzokLee8ut6uH8HlUbd1oz2bJVO3mcgRRzRa-YEtqBmICSjlPex4BZowQFBjs6pQoqN4yw-X90IN8Q:1sBvls:cQ-m8Il359Rsylamu4BiEvfiMVqADB45E8gdKzUPFBE','2024-06-11 12:17:40.138589'),('97a4gggblhaci53no96bx375ke0sf0s7','.eJxVjMEOwiAQRP-FsyGwCFk8evcbyLKAVA0kpT0Z_9026UFPk8x7M28RaF1qWEeew5TERRhx-u0i8TO3HaQHtXuX3NsyT1HuijzokLee8ut6uH8HlUbd1oz2bJVO3mcgRRzRa-YEtqBmICSjlPex4BZowQFBjs6pQoqN4yw-X90IN8Q:1s7ddY:G-S1CWAn5SE6G43yVVCD4glupOMVuWbM5KEPYh3nryc','2024-05-30 16:07:20.740263'),('f6ylnvunf67utoxd4s0c1k42cfbxg5oc','.eJxVjDsOwjAQBe_iGlkm6y8lfc5grb1rHECOFCcV4u4QKQW0b2beS0Tc1hq3zkucSFyEFqffLWF-cNsB3bHdZpnnti5TkrsiD9rlOBM_r4f7d1Cx128NAbQtUIodQJlg2Cs9gGVW4M5UgiVyoQAnDa5QztkbxeRRA6AzgcX7A8vYN8M:1sBID7:Og7IiiV4rhHC9Hsa0qV16NTFSt-3f4AR-aF8JKLIZkY','2024-06-09 18:03:09.607160'),('mdah76clwnsa7w9lxo8a0dqcztk6k7dy','.eJxVjMEOwiAQRP-FsyGwCFk8evcbyLKAVA0kpT0Z_9026UFPk8x7M28RaF1qWEeew5TERRhx-u0i8TO3HaQHtXuX3NsyT1HuijzokLee8ut6uH8HlUbd1oz2bJVO3mcgRRzRa-YEtqBmICSjlPex4BZowQFBjs6pQoqN4yw-X90IN8Q:1s7YMu:nicKUQQLpL5sAyg2AGEiBL2Qa_yhYa5J-wC4I9-4-60','2024-05-30 10:29:48.889088'),('ujui5bj9ezv85tnond9rhvuul8na78h4','.eJxVjMEOwiAQRP-FsyGwCFk8evcbyLKAVA0kpT0Z_9026UFPk8x7M28RaF1qWEeew5TERRhx-u0i8TO3HaQHtXuX3NsyT1HuijzokLee8ut6uH8HlUbd1oz2bJVO3mcgRRzRa-YEtqBmICSjlPex4BZowQFBjs6pQoqN4yw-X90IN8Q:1s6WmM:CcJ2Z6EdnKSCX2o8E8ZB22zBsLAcl8b7H4SR00z9r4o','2024-05-27 14:35:50.552954'),('upofo0qjii0uc0n8etlaee9yowzaposg','.eJxVjDsOwjAQBe_iGlkm6y8lfc5grb1rHECOFCcV4u4QKQW0b2beS0Tc1hq3zkucSFyEFqffLWF-cNsB3bHdZpnnti5TkrsiD9rlOBM_r4f7d1Cx128NAbQtUIodQJlg2Cs9gGVW4M5UgiVyoQAnDa5QztkbxeRRA6AzgcX7A8vYN8M:1s9TEi:Gqo_JxVvJ5x1nTI7NdLKoJFz4hf_98BF7WUwjOdDT-M','2024-06-04 17:25:16.070445'),('ygf9oghsglwj9nu56b50ziu3hyur7n2v','.eJxVjMEOwiAQRP-FsyGwCFk8evcbyLKAVA0kpT0Z_9026UFPk8x7M28RaF1qWEeew5TERRhx-u0i8TO3HaQHtXuX3NsyT1HuijzokLee8ut6uH8HlUbd1oz2bJVO3mcgRRzRa-YEtqBmICSjlPex4BZowQFBjs6pQoqN4yw-X90IN8Q:1s7YEk:AUDrbEZRwbtgNcf_BkasqFmT3PnC5CpQVRuUSk20pNw','2024-05-30 10:21:22.324362');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `broj_partija_leader` int NOT NULL,
  `broj_pobeda_leader` int NOT NULL,
  `broj_partija_guesser` int NOT NULL,
  `broj_pobeda_guesser` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (3,'pbkdf2_sha256$720000$N8e4bX8tNtD93o1Osz5qdu$ziPov+EPsCX+4cepaaEaCOrM/Pxdz9BPeaJVmIUnzSc=','2024-05-28 12:17:40.131586',1,'admin','','',1,1,'2024-05-13 12:24:22.000000','admin@gmail.com',7,4,5,2),(4,'pbkdf2_sha256$720000$hgQ6L2uSo6i1eYgZ0hKC2M$m10cWttSMjt3lKNDqFnjUTJI3uc/MkA8lbfBG5nbyQg=','2024-05-28 11:59:45.000000',0,'djole123','','',0,1,'2024-05-13 12:30:02.000000','djoleminecraft753@gmail.com',1,1,3,1),(5,'pbkdf2_sha256$720000$cyx6i3e3vvWPmTI85Hu99q$C22MLNKiV+/L5epC7o4PHwQsaHoEmuqrLJ1qIvZE9sk=',NULL,0,'teodorPC','','',0,1,'2024-05-13 12:30:03.520443','teodor.djelic@gmail.com',0,0,0,0),(6,'pbkdf2_sha256$720000$bPKEH41Hh6u4r853tBW6LM$v/CTihPo8ZrQCmG4hUXqRRi/rgFUvBH1s4n6valfBcE=',NULL,0,'solaja','','',0,1,'2024-05-13 12:30:04.147201','ekskurzija33@gmail.com',0,0,0,0),(7,'pbkdf2_sha256$720000$vvznQDKXs5nnL6WnXKyqSK$TZj5xNAr6rwUtxnddbwTq458uv9Gm4eRv3WcOaRr/Yg=','2024-05-16 10:18:27.222241',0,'tica12345','','',0,1,'2024-05-16 12:18:26.540321','tica@blabla.com',0,0,0,0),(8,'pbkdf2_sha256$720000$HobCLFlsjSFJBDzxftP8s4$2VAPatNldlGCTESXtzi9Hv4PZyjgCdy4rS8vXSqAras=','2024-05-17 16:11:46.553241',0,'eva','','',0,1,'2024-05-17 18:11:06.583300','stojanovskaeva01@gmail.com',0,0,0,0);
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik_groups`
--

DROP TABLE IF EXISTS `korisnik_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnik_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `korisnik_groups_korisnik_id_group_id_8c5ba7f0_uniq` (`korisnik_id`,`group_id`),
  KEY `korisnik_groups_group_id_639f924a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `korisnik_groups_group_id_639f924a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `korisnik_groups_korisnik_id_b99df0b8_fk_korisnik_id` FOREIGN KEY (`korisnik_id`) REFERENCES `korisnik` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik_groups`
--

LOCK TABLES `korisnik_groups` WRITE;
/*!40000 ALTER TABLE `korisnik_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `korisnik_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik_user_permissions`
--

DROP TABLE IF EXISTS `korisnik_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnik_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `korisnik_user_permission_korisnik_id_permission_i_f0bb31ce_uniq` (`korisnik_id`,`permission_id`),
  KEY `korisnik_user_permis_permission_id_ed48e217_fk_auth_perm` (`permission_id`),
  CONSTRAINT `korisnik_user_permis_permission_id_ed48e217_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `korisnik_user_permissions_korisnik_id_420accdf_fk_korisnik_id` FOREIGN KEY (`korisnik_id`) REFERENCES `korisnik` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik_user_permissions`
--

LOCK TABLES `korisnik_user_permissions` WRITE;
/*!40000 ALTER TABLE `korisnik_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `korisnik_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pogadjanje`
--

DROP TABLE IF EXISTS `pogadjanje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pogadjanje` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `poljeIndeks` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pogadjanje_user_id_2c250df0_fk_korisnik_id` (`user_id`),
  CONSTRAINT `pogadjanje_user_id_2c250df0_fk_korisnik_id` FOREIGN KEY (`user_id`) REFERENCES `korisnik` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pogadjanje`
--

LOCK TABLES `pogadjanje` WRITE;
/*!40000 ALTER TABLE `pogadjanje` DISABLE KEYS */;
INSERT INTO `pogadjanje` VALUES (1,3,3),(2,4,3),(3,11,3),(4,3,3),(5,2,4),(6,1,4),(7,1,4),(8,1,4),(9,2,4),(10,3,4),(11,22,4),(12,12,4),(13,21,4),(14,12,4),(15,23,4),(16,1,4),(17,2,4),(18,1,4),(19,0,4),(20,1,4),(21,2,4),(22,1,4),(23,2,4),(24,4,4),(25,2,4),(26,2,4),(27,2,4),(28,6,4),(29,22,4),(30,14,4),(31,21,4),(32,16,4),(33,17,4),(34,18,4),(35,19,4),(36,6,4),(37,16,4),(38,21,4),(39,22,4),(40,17,4),(41,19,4),(42,17,4),(43,12,4),(44,13,4),(45,11,4),(46,12,4),(47,6,4),(48,3,4),(49,4,4),(50,17,4),(51,18,4),(52,13,4),(53,21,4),(54,16,4),(55,5,4),(56,1,4),(57,2,4),(58,8,4);
/*!40000 ALTER TABLE `pogadjanje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rec`
--

DROP TABLE IF EXISTS `rec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rec` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rec` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=589 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rec`
--

LOCK TABLES `rec` WRITE;
/*!40000 ALTER TABLE `rec` DISABLE KEYS */;
INSERT INTO `rec` VALUES (461,'point'),(462,' sure'),(463,' build'),(464,' laced'),(465,' interpolate'),(466,' alike'),(467,' gloat'),(468,' stranger'),(469,' enrich'),(470,' blurt'),(471,' bound'),(472,' religious'),(473,' racer'),(474,' oval'),(475,' claws'),(476,' disease'),(477,' frank'),(478,' stink'),(479,' bad'),(480,' aside'),(481,' gape'),(482,' mollycoddle'),(483,' drama'),(484,' gross'),(485,' fall'),(486,' prevent'),(487,' fast'),(488,' vent'),(489,' shave'),(490,' suction'),(491,' taunt'),(492,' laugh'),(493,' love'),(525,'briny'),(526,' goon'),(527,' riot'),(528,' thee'),(529,' last'),(530,' salty'),(531,' wound'),(532,' shape'),(533,' crack'),(534,' caste'),(535,' hippo'),(536,' skirmish'),(537,' remember'),(538,' me'),(539,' havoc'),(540,' third'),(541,' cup'),(542,' timetable'),(543,' bane'),(544,' abuzz'),(545,' pork'),(546,' queue'),(547,' manner'),(548,' crime'),(549,' ditch'),(550,' mylar'),(551,' milky'),(552,' transportation'),(553,' nick'),(554,' left'),(555,' read'),(556,' bunny'),(557,'show'),(558,' ideal'),(559,' trunk'),(560,' cushy'),(561,' slow'),(562,' sweet'),(563,' office'),(564,' glide'),(565,' if'),(566,' nationalise'),(567,' play'),(568,' criminalize'),(569,' fore'),(570,' splay'),(571,' pet'),(572,' dusky'),(573,' cite'),(574,' mouse'),(575,' lust'),(576,' sealift'),(577,' woof'),(578,' weepy'),(579,' burn'),(580,' humble'),(581,' arraign'),(582,' evil'),(583,' dryer'),(584,' missing'),(585,' starch'),(586,' mind'),(587,' study'),(588,' dog');
/*!40000 ALTER TABLE `rec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setreci`
--

DROP TABLE IF EXISTS `setreci`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setreci` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `naziv` varchar(50) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `kreator_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `naziv` (`naziv`),
  KEY `setReci_kreator_id_864fe870_fk_korisnik_id` (`kreator_id`),
  CONSTRAINT `setReci_kreator_id_864fe870_fk_korisnik_id` FOREIGN KEY (`kreator_id`) REFERENCES `korisnik` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setreci`
--

LOCK TABLES `setreci` WRITE;
/*!40000 ALTER TABLE `setreci` DISABLE KEYS */;
INSERT INTO `setreci` VALUES (4,'Cool words',0,3),(5,'Djole\'s words',1,4),(6,'Evine reci',0,3);
/*!40000 ALTER TABLE `setreci` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setreci_reci`
--

DROP TABLE IF EXISTS `setreci_reci`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setreci_reci` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `setreci_id` bigint NOT NULL,
  `rec_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `setReci_reci_setreci_id_rec_id_a4214fb3_uniq` (`setreci_id`,`rec_id`),
  KEY `setReci_reci_rec_id_3195453b_fk_rec_id` (`rec_id`),
  CONSTRAINT `setReci_reci_rec_id_3195453b_fk_rec_id` FOREIGN KEY (`rec_id`) REFERENCES `rec` (`id`),
  CONSTRAINT `setReci_reci_setreci_id_ed8591f4_fk_setReci_id` FOREIGN KEY (`setreci_id`) REFERENCES `setreci` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=590 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setreci_reci`
--

LOCK TABLES `setreci_reci` WRITE;
/*!40000 ALTER TABLE `setreci_reci` DISABLE KEYS */;
INSERT INTO `setreci_reci` VALUES (462,4,461),(463,4,462),(464,4,463),(465,4,464),(466,4,465),(467,4,466),(468,4,467),(469,4,468),(470,4,469),(471,4,470),(472,4,471),(473,4,472),(474,4,473),(475,4,474),(476,4,475),(477,4,476),(478,4,477),(479,4,478),(480,4,479),(481,4,480),(482,4,481),(483,4,482),(484,4,483),(485,4,484),(486,4,485),(487,4,486),(488,4,487),(489,4,488),(490,4,489),(491,4,490),(492,4,491),(493,4,492),(494,4,493),(558,5,557),(559,5,558),(560,5,559),(561,5,560),(562,5,561),(563,5,562),(564,5,563),(565,5,564),(566,5,565),(567,5,566),(568,5,567),(569,5,568),(570,5,569),(571,5,570),(572,5,571),(573,5,572),(574,5,573),(575,5,574),(576,5,575),(577,5,576),(578,5,577),(579,5,578),(580,5,579),(581,5,580),(582,5,581),(583,5,582),(584,5,583),(585,5,584),(586,5,585),(587,5,586),(588,5,587),(589,5,588),(526,6,525),(527,6,526),(528,6,527),(529,6,528),(530,6,529),(531,6,530),(532,6,531),(533,6,532),(534,6,533),(535,6,534),(536,6,535),(537,6,536),(538,6,537),(539,6,538),(540,6,539),(541,6,540),(542,6,541),(543,6,542),(544,6,543),(545,6,544),(546,6,545),(547,6,546),(548,6,547),(549,6,548),(550,6,549),(551,6,550),(552,6,551),(553,6,552),(554,6,553),(555,6,554),(556,6,555),(557,6,556);
/*!40000 ALTER TABLE `setreci_reci` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-28 14:24:24
