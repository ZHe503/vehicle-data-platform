Vehicle Data Platform

A Python and SQLite data engineering project that extracts vehicle specifications from CSV files, validates the data, and loads records into a database.

Overview

This project demonstartes a basic Pipeline using Python and SQL

Vehicle data is read from a CSV file, passes through dulication and validation checks, and is then stored in a SQLite database.

Technologies

-Python
-SQLite/SQL
-CSV
=Git & Github 

How it works
1. Read vehicle records from data/vehicles.csv
2. Converts numerical fields to integers and validates them
3. Checks for duplicates and inserts new, valid dat into SQLite
