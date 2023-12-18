# Read Me

This repository contains the code for the next test project:

### Test Task: Category and Product Management System

## Task Description:

## Database Structure:
	Design the database structure for storing categories and products.
	Categories have a tree-like structure with a maximum nesting level of 10.
	Categories are characterized by a name, and products are characterized by a name and a price.
	A product can belong to multiple categories.
## REST API:
## Implement a REST API with the following capabilities:
-	a. Create, update, and delete categories and products.
-	b. Change the parent category of a category.
-	c. For a given list of products, retrieve all categories containing these products.
-	d. For a given category, retrieve a list of all products present in this category and its descendant categories of all levels.
-	e. For a given list of categories, retrieve the count of product offerings in each category.
-	f. For a given list of categories, retrieve the total count of unique product offerings.
## OpenAPI/Swagger Specification:
	Provide a detailed specification of the API in OpenAPI/Swagger format.

## Python Web Framework:
	Implement the solution using a Python web framework of your choice.

## Test Data:
	Include a set of test data to demonstrate the functionality of your solution.
## Docker Compose Configuration:
	Provide a Docker Compose configuration for deploying your solution.

### Setup

Run in project root directory - [docker-compose up --build]

For admin user creation - [docker exec -it server python manage.py createsuperuser]

For set test data - [docker exec -it server python manage.py loaddata productapp_initial_data.json]