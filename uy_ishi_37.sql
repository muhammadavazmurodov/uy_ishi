CREATE DATABASE computer_shop;
USE computer_shop;

CREATE TABLE computers (
    brand VARCHAR(50),
    model VARCHAR(50),
    cpu VARCHAR(50),
    frequency FLOAT,
    ram INT,
    os VARCHAR(50),
    price INT
);

INSERT INTO computers (brand, model, cpu, frequency, ram, os, price) VALUES
('Apple', 'MacBook Pro', 'Intel Core i7', 2.6, 16, 'macOS', 2400),
('Apple', 'MacBook Air', 'Apple M1', 3.2, 8, 'macOS', 999),
('ASUS', 'ZenBook', 'Intel Core i7', 2.8, 8, 'Windows 10', 950),
('ASUS', 'VivoBook', 'AMD Ryzen 5', 2.1, 8, 'Windows 10', 550),
('ASUS', 'ROG Strix', 'Intel Core i7', 2.6, 16, 'Windows 11', 1500),
('HP', 'Pavilion', 'AMD Ryzen 5', 2.1, 8, 'Windows 10', 600),
('HP', 'Envy', 'Intel Core i5', 2.4, 16, 'Windows 11', 899),
('Lenovo', 'ThinkPad', 'Intel Core i7', 3.0, 16, 'Windows 10', 1899),
('Lenovo', 'IdeaPad', 'AMD Ryzen 3', 2.6, 4, 'Ubuntu 20.04', 450),
('Dell', 'XPS', 'Intel Core i7', 2.8, 16, 'Windows 11', 1450),
('Dell', 'Inspiron', 'Intel Core i5', 2.4, 8, 'Ubuntu 20.04', 650),
('Acer', 'Aspire', 'Intel Core i5', 2.4, 8, 'Windows 10', 520),
('MSI', 'Modern', 'Intel Core i5', 2.5, 8, 'Windows 10', 700),
('Apple', 'MacBook Pro', 'Apple M1', 3.2, 16, 'macOS', 1200),
('HP', 'Spectre', 'Intel Core i7', 2.8, 16, 'Windows 11', 1799),
('Lenovo', 'Legion', 'AMD Ryzen 7', 3.2, 16, 'Windows 11', 1250),
('Dell', 'G15 Gaming', 'AMD Ryzen 7', 3.2, 16, 'Windows 11', 1100),
('Acer', 'Swift', 'AMD Ryzen 7', 2.0, 8, 'Windows 10', 680),
('Acer', 'Nitro', 'Intel Core i5', 2.5, 8, 'Windows 11', 799),
('ASUS', 'TUF Gaming', 'AMD Ryzen 5', 3.0, 8, 'Windows 11', 850);

SELECT * FROM computers 
ORDER BY price DESC 
LIMIT 1;

SELECT * FROM computers 
ORDER BY price ASC 
LIMIT 1;

SELECT frequency FROM computers 
WHERE price >= 400 AND price <= 1000 AND cpu LIKE '%Intel%';

SELECT COUNT(*) FROM computers 
WHERE brand = 'Apple';

SELECT * FROM computers 
WHERE brand = 'ASUS' AND os LIKE '%Windows%' AND ram = 8 
ORDER BY price ASC;
