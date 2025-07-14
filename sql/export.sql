/*registration*/ 
SELECT * FROM users
INTO OUTFILE '/tmp/pharmacy_users.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/*New Product*/
SELECT * FROM productes
INTO OUTFILE 'productes.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';
