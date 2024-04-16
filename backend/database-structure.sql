-- MariaDB dump 10.19  Distrib 10.5.23-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: db-seguimiento-alumnos
-- ------------------------------------------------------
-- Server version	10.5.23-MariaDB

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
-- Table structure for table `Alumnos`
--

DROP TABLE IF EXISTS `Alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Alumnos` (
  `Matricula` varchar(8) NOT NULL,
  `Nombre` varchar(70) NOT NULL,
  `Activo` bit(1) DEFAULT b'1',
  PRIMARY KEY (`Matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Calificaciones`
--

DROP TABLE IF EXISTS `Calificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Calificaciones` (
  `Matricula` varchar(8) NOT NULL,
  `MateriaId` int(11) NOT NULL,
  `GrupoId` int(11) NOT NULL,
  `CalificacionFinal` decimal(10,0) NOT NULL,
  `Intento` int(11) DEFAULT 0,
  `Fecha` datetime NOT NULL,
  `Estado` int(11) NOT NULL,
  PRIMARY KEY (`Matricula`,`MateriaId`,`GrupoId`),
  KEY `Calificaciones_EstadoAlumno_FK` (`Estado`),
  KEY `Calificaciones_Grupos_FK` (`GrupoId`),
  KEY `Calificaciones_Materias_FK` (`MateriaId`),
  CONSTRAINT `Calificaciones_Alumnos_FK` FOREIGN KEY (`Matricula`) REFERENCES `Alumnos` (`Matricula`),
  CONSTRAINT `Calificaciones_EstadoAlumno_FK` FOREIGN KEY (`Estado`) REFERENCES `EstadoAlumno` (`Id`),
  CONSTRAINT `Calificaciones_Grupos_FK` FOREIGN KEY (`GrupoId`) REFERENCES `Grupos` (`Id`),
  CONSTRAINT `Calificaciones_Materias_FK` FOREIGN KEY (`MateriaId`) REFERENCES `Materias` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `EstadoAlumno`
--

DROP TABLE IF EXISTS `EstadoAlumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EstadoAlumno` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Estado` varchar(15) DEFAULT NULL,
  `Activo` bit(1) DEFAULT b'1',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grupos`
--

DROP TABLE IF EXISTS `Grupos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grupos` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Grupo` varchar(25) NOT NULL,
  `Activo` bit(1) DEFAULT b'1',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=235 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Materias`
--

DROP TABLE IF EXISTS `Materias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Materias` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `NombreMateria` varchar(80) NOT NULL,
  `Activo` bit(1) DEFAULT b'1',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `UltimaActualizacion`
--

DROP TABLE IF EXISTS `UltimaActualizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UltimaActualizacion` (
  `Fecha` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-16 11:05:26
