CREATE SCHEMA `community_old` ;

use community_old;

CREATE TABLE IF NOT EXISTS `staff` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `account` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `status` int DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='工作人员表';
INSERT INTO `staff` (`id`,`name`,`account`,`password`,`status`) VALUES (1,'管理员','admin','123456',1);

CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL COMMENT '姓名',
  `sex` int DEFAULT '0' COMMENT '0-男 1-女',
  `birth_place_code` varchar(45) DEFAULT NULL COMMENT '籍贯',
  `area_code` varchar(45) DEFAULT NULL COMMENT '居住地编号（精确到区县）',
  `area_detail` varchar(200) DEFAULT NULL COMMENT '详细地址',
  `phone` varchar(45) DEFAULT NULL COMMENT '电话',
  `emergency_contact_name` varchar(45) DEFAULT NULL COMMENT '紧急联络人姓名',
  `emergency_contact_phone` varchar(45) DEFAULT NULL COMMENT '紧急联络人电话',
  `emergency_contact_relationship` varchar(45) DEFAULT NULL COMMENT '与紧急联络人关系',
  `is_marry` int DEFAULT '0' COMMENT '婚姻状况：0-未婚 1-已婚',
  `is_live_alone` int DEFAULT '0' COMMENT '是否独居：0-否 1-是',
  `is_disability` int DEFAULT '0' COMMENT '是否残疾：0-否 1-是',
  `diseases_history` varchar(200) DEFAULT NULL COMMENT '疾病史 JSON数组',
  `major_diseases_history` varchar(200) DEFAULT NULL COMMENT '重大疾病史 JSON数组',
  `status` int DEFAULT '1' COMMENT '账号状态：0-禁用 1-有效',
  `birthday` date DEFAULT NULL COMMENT '出生年月日',
  `care_level` int DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='用户表';

CREATE TABLE IF NOT EXISTS `dict_area` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` varchar(45) NOT NULL,
  `p_code` varchar(45) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='地区字典表';

CREATE TABLE IF NOT EXISTS `dict_video_cate` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `status` int DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='视频分类';
INSERT INTO `dict_video_cate` (`id`,`name`,`status`) VALUES (1,'文娱',1);
INSERT INTO `dict_video_cate` (`id`,`name`,`status`) VALUES (2,'健康',1);

CREATE TABLE IF NOT EXISTS `dict_news_cate` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `status` int DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='新闻分类';
INSERT INTO `dict_news_cate` (`id`,`name`,`status`) VALUES (1,'文娱',1);
INSERT INTO `dict_news_cate` (`id`,`name`,`status`) VALUES (2,'健康',1);

CREATE TABLE IF NOT EXISTS `appointment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `type` int DEFAULT 1 COMMENT '1-家政服务 2-医疗检查 3-药品配送 4-代买购物',
  `detail` varchar(200) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `status` int DEFAULT '1',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='预约表';

CREATE TABLE IF NOT EXISTS `video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cate_id` int DEFAULT NULL,
  `title` varchar(80) DEFAULT NULL,
  `img_url` varchar(160) DEFAULT NULL,
  `video_url` varchar(160) DEFAULT NULL,
  `content` longtext,
  `status` int DEFAULT '1',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='视频资讯';

CREATE TABLE IF NOT EXISTS `fav_video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `video_id` int DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='视频收藏表';

CREATE TABLE IF NOT EXISTS `news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cate_id` int DEFAULT NULL,
  `title` varchar(80) DEFAULT NULL,
  `content` longtext,
  `status` int DEFAULT '1',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='新闻资讯';

CREATE TABLE IF NOT EXISTS `fav_news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `news_id` int DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='新闻收藏表';

CREATE TABLE IF NOT EXISTS `instant_call` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `status` int DEFAULT '1',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='一件呼救';

CREATE TABLE IF NOT EXISTS `message_board` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `status` int DEFAULT '1',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB COMMENT='留言板';



