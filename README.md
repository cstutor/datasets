# Working With Datasets in Python

## Setup

Need Python installed first.

## Parsing a CSV file with Python

```
import csv

with open('vashon-hills.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print row
```

Get the headers, map to data

## Creating a database in SQLite

For simplicity, we will use SQLite. Start with a GUI. sqlitebrowser.

### Databases

First we'll want to create a database to store our data. We will name this database 'cycling' since it will store cycling data.

```
CREATE DATABASE cycling;
```

### Tables

A relational database contains one or more tables that hold records. A table has columns to define the attributes of each record. Let's create a table for our dataset. We can create a database column for each heading in our CSV file. We will also create an `id` field that will be the table's primary key. This is a unique number that corresponds to that record.

```
CREATE TABLE hills (
    id INT PRIMARY KEY NOT NULL,
    hill REAL NOT NULL, 
    length REAL NOT NULL,
    gain REAL NOT NULL,
    avg_grade REAL NOT NULL,
    max_grade REAL NOT NULL
);
```

### Using SQL to Create, Read, Update, and Delete Records

### Creating records with the INSERT statement

```
INSERT INTO hills (hill, length, gain, avg_grade, max_grade) 
VALUES ('Vashon Ferry hill 1', 0.7 , 354, 9.2, 18.1);
```

### Reading records with the SELECT statement

```
SELECT id, hill, length, gain, avg_grade, max_grade 
FROM hills;
```

```
SELECT * FROM hills;
```

### Updating records with the UPDATE statement

```
UPDATE hills SET hill = 'Vashon Ferry Hill' WHERE hill = 'Vashon Ferry Hill 1';
```

### Deleting records with the DELETE statement

#### Deleting a record by ID

```
DELETE FROM hills WHERE id = 1;
```

#### Deleting multiple records

```
DELETE FROM hills WHERE max_grade < 10;
```

### Using Python to execute SQL queries

We will not type an INSERT statement for each record. What if the dataset had a million records? We will use Python to parse our CSV file and generate an INSERT statement for each record.

## Visualizing Data 

### Building a Web Frontend

