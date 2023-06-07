CREATE TABLE identification (
  id INT NOT NULL AUTO_INCREMENT,
  token VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO identification (token) VALUES ('motion115');
INSERT INTO identification (token) VALUES ('root');

select token from identification;