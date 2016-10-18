CREATE TABLE `PasteFile` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `filename` VARCHAR(5000) NOT NULL,
  `filehash` VARCHAR(128) NOT NULL,
  `filemd5` VARCHAR(128) NOT NULL,
  `uploadtime` DATETIME NOT NULL ,
  `mimetype` VARCHAR(256) NOT NULL ,
  `size` INT(11) UNSIGNED NOT NULL ,
  PRIMARY KEY (`id`),
  UNIQUE KEY `filehash` (`filehash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;