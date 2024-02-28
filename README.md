# CRUD Django Course App

## Overview

This project demonstrates CRUD operations (Create, Read, Update, Delete) using Django and includes information about QuerySet, a powerful tool for interacting with the database through the Django Model API.

## CRUD Operations

### Create
- The project allows the creation of new records in the database.

### Read
- The Read operations involve retrieving records from the database.
- It utilizes the QuerySet concept in Django to represent collections of records.

### Update
- The Update operations enable modifying existing records in the database.

### Delete
- The Delete operations involve removing records from the database.

## QuerySet

QuerySet is a Django concept representing a collection of records in a database. In this project, QuerySet is utilized for reading objects using the Django Model API.

## Key Methods

### `all()`
- The `all()` method returns a QuerySet containing all the objects in the database.

### `filter()`
- The `filter()` method is used to narrow down the QuerySet based on specific criteria.
- It supports lookup parameters such as greater than, less than, contains, or is null.
- 
