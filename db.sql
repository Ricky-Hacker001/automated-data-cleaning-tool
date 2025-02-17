CREATE DATABASE IF NOT EXISTS data_cleaning;

USE data_cleaning;

CREATE TABLE IF NOT EXISTS file_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    cleaned_at DATETIME NOT NULL
);
