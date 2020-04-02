CREATE DATABASE products;
use products;

CREATE TABLE products_name ( id VARCHAR(20), name VARCHAR(20) );

INSERT INTO products_name
  (id, name)
VALUES
  ('1', 'Apple'),
  ('2', 'Mango'),
  ('3', 'Pineapple'),
  ('4', 'Plum'),
  ('5', 'Dragon Fruit');
