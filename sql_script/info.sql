CREATE DATABASE info;

USE info;

CREATE TABLE champion (
`name` VARCHAR(50),
`id` INT NOT NULL PRIMARY KEY
);

CREATE TABLE item (
`id` INT NOT NULL PRIMARY KEY,
`name` VARCHAR(50)
);

CREATE TABLE mastery (
`id` INT NOT NULL PRIMARY KEY,
`name` VARCHAR(50)
);

CREATE TABLE champion_item (
`champion_id` INT NOT NULL,
`item_name` VARCHAR(50) NOT NULL,
PRIMARY KEY(`champion_id`, `item_name`)
);

CREATE TABLE champion_mastery (
`champion_id` INT NOT NULL,
`mastery_name` VARCHAR(50) NOT NULL,
PRIMARY KEY(`champion_id`, `mastery_name`)
);
