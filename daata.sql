CREATE DATABASE users;

USE users;

CREATE TABLE book_data (
  Book_Id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Title varchar(100),
  Author varchar(30),
  Description varchar(300) DEFAULT NULL,
  Published_Date date,
  Page_Count int,
  Status varchar(20) DEFAULT 'AVAILABLE'
));

CREATE TABLE user_details (
  id longtext(10),
  name varchar(100),
  email varchar(30)
));

INSERT INTO user_details VALUES ("5911","Awilda Brittingham","awid23@gmail.com");
INSERT INTO user_details VALUES ("3602","Belle Doig","bel34@gmail.com");
INSERT INTO user_details VALUES ("9593","Zula Avants","zula34@gmail.com");
INSERT INTO user_details VALUES ("5002","Maribel Mcquay","mari345@gmail.com");
INSERT INTO user_details VALUES ("7741","Evangelina Sommerville","evan234@gmail.com");
INSERT INTO user_details VALUES ("7285","Pamila Gaskill","pam34@gmail.com");
INSERT INTO user_details VALUES ("1400","Farah Zander","farah24@gmail.com");
INSERT INTO user_details VALUES ("9361","Keshia Stella","kesha34@gmail.com");
INSERT INTO user_details VALUES ("4651","Iesha Wray","iesha234@gmail.com");
INSERT INTO user_details VALUES ("9494","Lavinia Delia","lavin324@gmail.com");
INSERT INTO user_details VALUES ("7057","Sherlene Marko","sherlene32@gmail.com");
INSERT INTO user_details VALUES ("9520","Rosalina Walcott","rosa342@gmail.com");

CREATE TABLE book_data (
  trans_id int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  b_id int,
  m_id int,
  date_b date,
  dare_r date;
  fine float(5,2)
));


INSERT INTO `transaction` VALUES (1,2,3,"2021-03-01","2021-03-01",0.50);
INSERT INTO `transaction` VALUES (2,1,2,"2021-03-01","2021-03-01",0.40);
INSERT INTO `transaction` VALUES (3,3,2,"2021-03-01","2021-03-01",0.30);
INSERT INTO `transaction` VALUES (4,2,3,"2021-03-01","2021-03-01",0.20);
INSERT INTO `transaction` VALUES (5,4,4,"2021-03-01","2021-03-01",0.10);
INSERT INTO `transaction` VALUES (6,1,1,"2021-03-01","2021-03-01",0.00);
INSERT INTO `transaction` VALUES (7,2,3,"2021-03-01","2021-03-01",0.50);
