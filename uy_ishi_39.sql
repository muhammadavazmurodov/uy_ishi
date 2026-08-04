USE Talaba;
CREATE TABLE kitoblar (
    id INT PRIMARY KEY,
    muallif VARCHAR(100),
    nomi VARCHAR(100),
    janr VARCHAR(50),
    sotilgan_soni INT
);

INSERT INTO kitoblar VALUES (1, 'Alisher Navoiy', 'Xamsa', 'Doston', 1500);
INSERT INTO kitoblar VALUES (2, 'Alisher Navoiy', 'Lison ut-tayr', 'Doston', 1200);
INSERT INTO kitoblar VALUES (3, 'Alisher Navoiy', 'G''azallar', 'G''azal', 2000);
INSERT INTO kitoblar VALUES (4, 'Abdulla Qodiriy', 'O''tkan kunlar', 'Roman', 3000);
INSERT INTO kitoblar VALUES (5, 'Abdulla Qodiriy', 'Mehrobdan chayon', 'Roman', 2500);
INSERT INTO kitoblar VALUES (6, 'O''tkir Hoshimov', 'Dunyoning ishlari', 'Qissa', 1800);

SELECT DISTINCT janr 
FROM kitoblar 
WHERE muallif = 'Alisher Navoiy';

SELECT DISTINCT muallif, janr 
FROM kitoblar;

SELECT muallif, janr, COUNT(*) 
FROM kitoblar 
GROUP BY muallif, janr;

SELECT janr, COUNT(*) 
FROM kitoblar 
GROUP BY janr 
ORDER BY COUNT(*) DESC 
LIMIT 1;

SELECT muallif, janr, COUNT(*) 
FROM kitoblar 
GROUP BY muallif, janr 
ORDER BY COUNT(*) DESC;

SELECT muallif, SUM(sotilgan_soni) 
FROM kitoblar 
GROUP BY muallif 
ORDER BY SUM(sotilgan_soni) DESC 
LIMIT 1;