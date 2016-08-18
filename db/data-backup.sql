--
-- File generated with SQLiteStudio v3.1.0 on Tue Jul 26 14:39:56 2016
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: messages
CREATE TABLE messages(
	message_id INTEGER PRIMARY KEY AUTOINCREMENT,
	content TEXT(300),
	time_created TEXT(30),
	user_id INTEGER FOREIGN_KEY
);
INSERT INTO messages (message_id, content, time_created, user_id) VALUES (8, 'Hello', '2016-07-26 02:38:31', 13);
INSERT INTO messages (message_id, content, time_created, user_id) VALUES (9, 'Hello', '2016-07-26 02:38:31', 14);
INSERT INTO messages (message_id, content, time_created, user_id) VALUES (10, 'Hello', '2016-07-26 02:38:31', 15);

-- Table: users
CREATE TABLE users(
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT(30),
	password TEXT(64),
	first_name TEXT(64),
	last_name TEXT(20),
	email TEXT(50),
	photo BLOB(10000)
);
INSERT INTO users (user_id, username, password, first_name, last_name, email, photo) VALUES (13, 'tanya', 'test', 'Tanya', 'Gray', 'tanya@gathergather.co.nz', NULL);
INSERT INTO users (user_id, username, password, first_name, last_name, email, photo) VALUES (14, 'bob', 'password1', 'Bob', 'Jones', 'bob@gathergather.co.nz', NULL);
INSERT INTO users (user_id, username, password, first_name, last_name, email, photo) VALUES (15, 'james', 'jack2014', 'James', 'Black', 'james@gathergather.co.nz', NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
