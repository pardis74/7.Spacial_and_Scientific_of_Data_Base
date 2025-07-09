
--CREATE EXTENSION postgis.--This one is for spatial_ref_sys 

CREATE TABLE Customer (
    MobileNumber VARCHAR(20) PRIMARY KEY,
	C_Coordinator GEOMETRY(POINT)
);

-- Create the IndividualCustomer table, inheriting from Customer
CREATE TABLE IndividualCustomer (
    MobileNumber VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HomeAddress VARCHAR(100),
    PaymentIdentifier VARCHAR(50),
    C_Coordinator GEOMETRY(POINT),
    FOREIGN KEY (MobileNumber) REFERENCES Customer(MobileNumber)
);

-- Create the BusinessCustomer table, inheriting from Customer
CREATE TABLE BusinessCustomer (
    MobileNumber VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    HomeAddress VARCHAR(100),
    PaymentIdentifier VARCHAR(50),
	DiscountRate FLOAT,
    C_Coordinator GEOMETRY(POINT),
    FOREIGN KEY (MobileNumber) REFERENCES Customer(MobileNumber)
);

CREATE TABLE Company (
    Accreditation_Code VARCHAR(20) PRIMARY KEY,
    Company_Name VARCHAR(50),
    Address VARCHAR(100)
);

CREATE TABLE Assign (
    MobileNumber VARCHAR(20),
    Accreditation_Code VARCHAR(20),
	PRIMARY KEY (MobileNumber, Accreditation_Code),
    FOREIGN KEY (MobileNumber) REFERENCES Customer(MobileNumber),
	FOREIGN KEY (Accreditation_Code) REFERENCES Company(Accreditation_Code)
);

CREATE TABLE Car (
  PlateNumber VARCHAR(10) NOT NULL,
  NumLuggage INT,
  NumSeats INT,
  MPG FLOAT,
  model VARCHAR(50),
  make VARCHAR(50),
  Car_year INT,
  PRIMARY KEY (PlateNumber)
);

CREATE TABLE Call_T (
  MobileNumber VARCHAR(15) NOT NULL,
  callTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PlateNumber VARCHAR(10) NOT NULL,
  PRIMARY KEY (MobileNumber, PlateNumber),
  FOREIGN KEY (MobileNumber) REFERENCES Customer(MobileNumber),
  FOREIGN KEY (PlateNumber) REFERENCES Car(PlateNumber)
);

CREATE TABLE Driver (
    DriverLicenseNumber varchar(20) PRIMARY KEY,
    Driver_Name varchar(50),
    YearsOfExperience int,
    ExpectedMpg FLOAT,
    TaxiGoesPaymentIdentifier varchar(20)
);

CREATE TABLE TaxiLocation (
    TCoordinator GEOMETRY(POLYGON),
    PickUp varchar(100),
    DropOff varchar(100),
    StartTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    EndTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TheRoute varchar(200),
    PRIMARY KEY (TCoordinator)
);

CREATE TABLE DriveBy (
    PlateNumber varchar(20),
    SelfDriver Boolean,
    DriverLicenseNumber varchar(20),
    PRIMARY KEY (PlateNumber, DriverLicenseNumber),
    FOREIGN KEY (PlateNumber) REFERENCES Car(PlateNumber),
	FOREIGN KEY (DriverLicenseNumber) REFERENCES Driver
);

CREATE TABLE TaxiHas (
    PlateNumber varchar(20),
    TCoordinator GEOMETRY(POLYGON),
    FOREIGN KEY (PlateNumber) REFERENCES Car(PlateNumber),
	FOREIGN KEY (TCoordinator) REFERENCES TaxiLocation
);

CREATE TABLE Region (
  RCoordinator GEOMETRY(POLYGON),
  district VARCHAR(50),
  PRIMARY KEY (RCoordinator)
);

CREATE TABLE AssignSource (
  TCoordinator GEOMETRY(POLYGON),
  RCoordinator GEOMETRY(POLYGON),
  FOREIGN KEY (TCoordinator) REFERENCES TaxiLocation,
  FOREIGN KEY (RCoordinator) REFERENCES Region
);
