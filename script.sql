DROP TABLE fruits

CREATE TABLE fruits (
    fruit_name VARCHAR(100) NOT NULL,
    amount INT NOT NULL
);

INSERT INTO fruits (fruit_name, amount) VALUES 
('apple', 3),
('banana', 5),
('pineapple', 1);