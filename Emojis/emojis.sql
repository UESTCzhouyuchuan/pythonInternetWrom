/*
Navicat MySQL Data Transfer

Source Server         : Tencent
Source Server Version : 50728
Source Host           : 49.233.169.5:3306
Source Database       : study

Target Server Type    : MYSQL
Target Server Version : 50728
File Encoding         : 65001

Date: 2020-02-26 18:34:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for emojis
-- ----------------------------
DROP TABLE IF EXISTS `emojis`;
CREATE TABLE `emojis` (
  `number` int(10) unsigned NOT NULL,
  `code` varchar(255) NOT NULL,
  `bighead` varchar(255) NOT NULL,
  `bighead_url` varchar(255) NOT NULL,
  `mediumhead` varchar(255) NOT NULL,
  `mediumhead_url` varchar(255) NOT NULL,
  `browser` varchar(255) NOT NULL,
  `apple` longtext,
  `google` longtext,
  `facebook` longtext,
  `windows` longtext,
  `twitter` longtext,
  `joy` mediumtext NOT NULL,
  `sams` longtext,
  `gmail` longtext,
  `sb` longtext,
  `dcm` longtext,
  `kddi` longtext,
  `cldr_short_name` varchar(255) NOT NULL,
  `andr` longtext,
  PRIMARY KEY (`code`,`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
