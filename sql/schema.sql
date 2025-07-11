CREATE DATABASE ia_farmacia;

USE ia_farmacia;

/*Register*/
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    cognom VARCHAR(255) NOT NULL,
    farmacia VARCHAR(255) NOT NULL,
    ubicacio VARCHAR(255) NOT NULL,
    correu_electronic VARCHAR(255) NOT NULL UNIQUE,
    contrasenya VARCHAR(255) NOT NULL
);
/*New Product*/
CREATE TABLE productes (
    id INT PRIMARY KEY,
    nom VARCHAR(100),
    quantitat INT,
    miligrams VARCHAR(50),
    preu DECIMAL(10,2),
    data_caducitat DATE,
    proveedor VARCHAR(100),
    categories VARCHAR(100)
);
