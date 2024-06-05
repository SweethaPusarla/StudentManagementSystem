CREATE DATABASE StudentManagementSystem;
USE StudentManagementSystem;


CREATE TABLE Dept (
    Dept_Id int PRIMARY KEY,
    Dept_Name varchar(50)
);


CREATE TABLE Course (
    Course_Id int PRIMARY KEY,
    Course_Name varchar(100),
    Faculty_Name varchar(100),
    Credits int,
    Type varchar(100),
    Slot varchar(100),
    Number_of_enrolled int
);


CREATE TABLE Faculty (
    Faculty_Id int AUTO_INCREMENT PRIMARY KEY,
    Faculty_Name varchar(255),
    Course int,
    Dept int,
    Class_room varchar(100),
    CONSTRAINT fk_FacDept1 FOREIGN KEY (Dept) REFERENCES Dept(Dept_Id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_FacCou2 FOREIGN KEY (Course) REFERENCES Course(Course_Id) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Student (
    Student_Id int AUTO_INCREMENT PRIMARY KEY,
    Student_Name varchar(255),
    Dept int,
    Year_of_study int,
    Course_A int,
    Course_B int,
    Course_C int,
    CONSTRAINT fk_StuDept1 FOREIGN KEY (Dept) REFERENCES Dept(Dept_Id) ON UPDATE CASCADE ON DELETE CASCADE
);


INSERT INTO Dept (Dept_Id, Dept_Name) VALUES
(1, 'Computer Science'),
(2, 'Electrical Engineering'),
(3, 'Mechanical Engineering');


INSERT INTO Course (Course_Id, Course_Name, Faculty_Name, Credits, Type, Slot, Number_of_enrolled) VALUES
(101, 'Data Structures', 'Dr. Smith', 3, 'Core', 'A1', 30),
(102, 'Electromagnetics', 'Dr. Johnson', 3, 'Core', 'B1', 25),
(103, 'Thermodynamics', 'Dr. Lee', 3, 'Core', 'C1', 20);


INSERT INTO Faculty (Faculty_Name, Course, Dept, Class_room) VALUES
('Dr. Smith', 101, 1, 'Room 101'),
('Dr. Johnson', 102, 2, 'Room 202'),
('Dr. Lee', 103, 3, 'Room 303');

INSERT INTO Student (Student_Name, Dept, Year_of_study, Course_A, Course_B, Course_C) VALUES
('Alice', 1, 2, 101, 102, NULL),
('Bob', 2, 1, 102, NULL, NULL),
('Charlie', 3, 3, 103, NULL, NULL);
