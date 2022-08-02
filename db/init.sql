CREATE DATABASE thesis;
use thesis;

CREATE TABLE client_access (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    ip_address VARCHAR(100), 
    random_str VARCHAR(100),
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP
);