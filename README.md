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

CREATE DATABASE cycling;

### Tables

Let's create a table for this dataset.

CREATE TABLE hills (
    id,
    hill, 
    length,
    gain,
    avg_grade,
    max_grade
);

### Using SQL to Create, Read, Update, and Delete Records
### Adding records with the INSERT statement

### 
Let's create columns for each of our headers and a unique key.

Loader Python

Put into a database

Run queries

Creating a User Interface

Visualizing Data

Build a web frontend for it