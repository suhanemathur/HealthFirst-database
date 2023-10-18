DROP SCHEMA IF EXISTS HealthFirst;
CREATE SCHEMA HealthFirst;
USE HealthFirst;

CREATE TABLE Adminn (
	admin_ID int NOT NULL AUTO_INCREMENT,
	admin_name varchar(255) NOT NULL,
	admin_username varchar(255) NOT NULL UNIQUE,
	admin_password varchar(255) NOT NULL,
        
	PRIMARY KEY(admin_ID)
);

CREATE TABLE Customer (
	customer_ID int NOT NULL AUTO_INCREMENT,
    f_name varchar(200),
    l_name varchar(200),
    dob varchar(20),
    
    PRIMARY KEY(customer_ID)
);

CREATE TABLE Phone_Number(
	phone_number varchar(30),
    customer_ID int NOT NULL,
    
    FOREIGN KEY( customer_ID) REFERENCES Customer(customer_ID)
    );
    
CREATE TABLE Address(
	customer_ID int,
    address varchar(200) NOT NULL,
    
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID)
    );
    
CREATE TABLE Illness(
	illness_ID int NOT NULL AUTO_INCREMENT,
    illness_name varchar(200) NOT NULL,
    
    PRIMARY KEY(illness_ID)
    );
    
CREATE TABLE Product_Category(
	category_name varchar(100) NOT NULL,
    category_ID int NOT NULL AUTO_INCREMENT,
    customer_ID int,
    
    PRIMARY KEY(category_ID),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID)
    );
    
CREATE TABLE Product(
	product_name varchar(200) NOT NULL,
    product_ID int NOT null AUTO_INCREMENT,
    product_availability varchar(255) NOT NULL,
    product_price varchar(200) NOT NULL,
    product_expiry varchar(30) NOT NULL,
    product_manufacture varchar(30) NOT NULL,
    customer_ID int,
    category_ID int,
    
    PRIMARY KEY(product_ID),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(category_ID) REFERENCES Product_Category(category_ID)
    
    );
    
CREATE TABLE Supplier(
	supplier_name varchar(100) NOT NULL,
    supplier_ID int NOT NULL AUTO_INCREMENT,
    
    PRIMARY KEY(supplier_ID)
    
    );
    
CREATE TABLE Payment(
	payment_ID int NOT NULL AUTO_INCREMENT,
    payment_discount varchar(100),
    customer_ID int,
    
    PRIMARY KEY(payment_ID),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID)
    );
    
CREATE TABLE Payment_Date(
	payment_ID int,
    payment_date varchar(30) NOT NULL,
    
    FOREIGN KEY(payment_ID) REFERENCES Payment(payment_ID)
    );
    
CREATE TABLE Payment_Dicount(
	payment_ID int,
    payment_discount varchar(100),
    
    FOREIGN KEY(payment_ID) REFERENCES Payment(payment_ID)
    );
	
CREATE TABLE Supplier_Address(
	supplier_ID int NOT NULL AUTO_INCREMENT,
    supplier_address varchar(200),
    
    FOREIGN KEY(supplier_ID) REFERENCES Supplier(supplier_ID)
    );
    
CREATE TABLE Order_(
	order_date varchar(30) NOT NULL,
    order_account varchar(100) NOT NULL,
    customer_ID int,
    order_number int NOT NULL AUTO_INCREMENT,
    
    PRIMARY KEY(order_number),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID)
    );
    
CREATE TABLE Tracking_Order(
	tracking_ID int NOT NULL AUTO_INCREMENT,
    delivery_name varchar(200) NOT NULL,
    
    PRIMARY KEY(tracking_ID)
    );
    
CREATE TABLE proceeds_to(
	customer_ID int,
    order_number int,
    product_ID int,
    admin_ID int,
    
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(order_number) REFERENCES Order_(order_number),
    FOREIGN KEY(product_ID) REFERENCES Product(product_ID),
    FOREIGN KEY(admin_ID) REFERENCES Adminn(admin_ID)
    );
    
CREATE TABLE recommends(
	customer_ID int,
    illness_ID int,
    product_ID int,
    category_ID int,
    
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(illness_ID) REFERENCES Illness(illness_ID),
    FOREIGN KEY(product_ID) REFERENCES Product(product_ID),
    FOREIGN KEY(category_ID) REFERENCES Product_Category(category_ID)
    );
    
CREATE TABLE opens(
	payment_ID int,
    customer_ID int,
    order_number int,
    
    FOREIGN KEY(payment_ID) REFERENCES PAYMENT(payment_ID),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(order_number) REFERENCES Order_(order_number)
    );
    
CREATE TABLE added(
	admin_ID int,
    customer_ID int,
    product_ID int,
    
    FOREIGN KEY(admin_ID) REFERENCES Adminn(admin_ID),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(product_ID) REFERENCES Product(product_ID)
    );
    
CREATE TABLE manufactures(
	product_ID int,
    supplier_ID int,
    
    FOREIGN KEY(product_ID) REFERENCES Product(product_ID),
    FOREIGN KEY(supplier_ID) REFERENCES Supplier(supplier_ID)
    );
    
CREATE TABLE access(
	customer_ID int,
    product_ID int,
    tracking_ID int,
    payment_ID int,
    category_ID int,
    admin_ID int,
    
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(product_ID) REFERENCES Product(product_ID),
    FOREIGN KEY(tracking_ID) REFERENCES Tracking_Order(tracking_ID),
    FOREIGN KEY(payment_ID) REFERENCES Payment(payment_ID),
    FOREIGN KEY(category_ID) REFERENCES Product_Category(category_ID),
    FOREIGN KEY(admin_ID) REFERENCES Adminn(admin_ID)
    );
    
CREATE TABLE Cart_Product(
	cart_size varchar(200),
    customer_ID int,
    
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID)
    );
    
CREATE TABLE Website(
	website_url int NOT NULL AUTO_INCREMENT,
    website_name varchar(200),
    admin_ID int,
    
    PRIMARY KEY(website_url),
    FOREIGN KEY(admin_ID) REFERENCES Adminn(admin_ID)
    );
    
CREATE TABLE order_dispatch(
	tracking_ID int,
    customer_ID int,
    payment_ID int,
    transaction_success varchar(20) NOT NULL,
    
    FOREIGN KEY(tracking_ID) REFERENCES Tracking_Order(tracking_ID),
    FOREIGN KEY(customer_ID) REFERENCES  Customer(customer_ID),
    FOREIGN KEY(payment_ID) REFERENCES Payment(payment_ID)
    );
    
CREATE TABLE Order_Tracking(
	order_number int,
    customer_ID int,
    payment_ID int,
    tracking_ID int,
    admin_ID int,
    
    FOREIGN KEY(order_number) REFERENCES Order_(order_number),
    FOREIGN KEY(customer_ID) REFERENCES Customer(customer_ID),
    FOREIGN KEY(payment_ID) REFERENCES Payment(payment_ID),
    FOREIGN KEY(tracking_ID) REFERENCES Tracking_Order(tracking_ID),
    FOREIGN KEY(admin_ID) REFERENCES Adminn(admin_ID)
    );
    
    
    
    
	
    
    
    
    
    

    

    

	
    
    
	
