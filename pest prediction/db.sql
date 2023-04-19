/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - pest detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pest detection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pest detection`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `F_id` int(11) DEFAULT NULL,
  `ex_id` int(11) DEFAULT NULL,
  `Complaint` varchar(200) DEFAULT NULL,
  `Reply` varchar(200) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Comp_id`,`F_id`,`ex_id`,`Complaint`,`Reply`,`Date`) values 
(1,4,2,'That is not the correct pest','sorry ','2023-03-28');

/*Table structure for table `crop` */

DROP TABLE IF EXISTS `crop`;

CREATE TABLE `crop` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_name` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `crop` */

insert  into `crop`(`c_id`,`crop_name`,`description`) values 
(2,'corn','best crop in India');

/*Table structure for table `doubt` */

DROP TABLE IF EXISTS `doubt`;

CREATE TABLE `doubt` (
  `D_id` int(11) NOT NULL AUTO_INCREMENT,
  `F_id` int(11) DEFAULT NULL,
  `ex_id` int(11) DEFAULT NULL,
  `Doubt` varchar(200) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Reply` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`D_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `doubt` */

insert  into `doubt`(`D_id`,`F_id`,`ex_id`,`Doubt`,`Date`,`Reply`) values 
(1,4,2,'Is this fertilizer is suitable?','2023-03-28','yes');

/*Table structure for table `expert` */

DROP TABLE IF EXISTS `expert`;

CREATE TABLE `expert` (
  `ex_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `First_name` varchar(200) DEFAULT NULL,
  `Last_name` varchar(200) DEFAULT NULL,
  `Phone_no` varchar(200) DEFAULT NULL,
  `Place` varchar(200) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Pin` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`ex_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `expert` */

insert  into `expert`(`ex_id`,`l_id`,`First_name`,`Last_name`,`Phone_no`,`Place`,`Age`,`Pin`) values 
(1,2,'Ashique','Ash','9874563211','Wayanad',23,670731);

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `F_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `First_name` varchar(200) DEFAULT NULL,
  `Last_name` varchar(200) DEFAULT NULL,
  `Place` varchar(200) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Pin` bigint(20) DEFAULT NULL,
  `Phone_no` bigint(25) DEFAULT NULL,
  PRIMARY KEY (`F_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `farmer` */

insert  into `farmer`(`F_id`,`l_id`,`First_name`,`Last_name`,`Place`,`Age`,`Pin`,`Phone_no`) values 
(1,4,'Yusra','Yasar','Nadapuram',22,673503,9562918880),
(2,5,'Nusreen','Fathima','Kallachi',22,673504,2147483647),
(3,6,'Rabeeh','Rahman','Vengara',22,614257,9632145872),
(4,7,'Nihad','Abdulla','Wayanad',21,673503,9630852741);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `Feed_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `Feedback` varchar(200) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Feed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`Feed_id`,`l_id`,`Feedback`,`Date`) values 
(1,4,'Godd website','2023-03-28');

/*Table structure for table `fertilizer` */

DROP TABLE IF EXISTS `fertilizer`;

CREATE TABLE `fertilizer` (
  `Fert_id` int(11) NOT NULL AUTO_INCREMENT,
  `ex_id` int(11) DEFAULT NULL,
  `Fertilizer name` varchar(200) DEFAULT NULL,
  `Description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Fert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer` */

insert  into `fertilizer`(`Fert_id`,`ex_id`,`Fertilizer name`,`Description`) values 
(1,1,'cow dung manuare','best fertilizer ');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `Type` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`Type`) values 
(1,'admin','admin','agriculture officer'),
(2,'ashiq','123456','expert'),
(3,'niala','niala@123','expert'),
(4,'yus','yus@123','farmer'),
(5,'nuchii','nuchi@1234','farmer'),
(6,'Rabee','rabe@123','farmer'),
(7,'Nihad','nihu@123','reject');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `N_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `Notification` varchar(200) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`N_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`N_id`,`l_id`,`Notification`,`Date`) values 
(1,1,'no notification','2023-03-28');

/*Table structure for table `tips` */

DROP TABLE IF EXISTS `tips`;

CREATE TABLE `tips` (
  `Tip_id` int(11) NOT NULL AUTO_INCREMENT,
  `ex_id` int(11) DEFAULT NULL,
  `Tips` varchar(200) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Tip_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tips` */

insert  into `tips`(`Tip_id`,`ex_id`,`Tips`,`Date`) values 
(1,1,'check for cracks and gaps','2023-03-28');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
