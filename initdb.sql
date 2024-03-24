CREATE DATABASE IF NOT EXISTS myappdb;
USE myappdb;

CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255) NOT NULL
);

INSERT INTO test_table (message) VALUES ('Hello, World!');
INSERT INTO test_table (message) VALUES ('Another test message');
