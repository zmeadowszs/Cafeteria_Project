-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS cafeteria;

-- Usar o banco de dados
USE cafeteria;

-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

-- Inserção de dados de exemplo
INSERT INTO users (username, password) VALUES ('user1', 'password123');
INSERT INTO users (username, password) VALUES ('user2', 'password456');
