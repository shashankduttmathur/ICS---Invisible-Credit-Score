
CREATE TABLE users(id SERIAL PRIMARY KEY, phone VARCHAR(20));
CREATE TABLE scores(user_id INT, score INT);
