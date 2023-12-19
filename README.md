# Test Task: Category and Product Management System

## Task Description:

####  Database Structure:
Design the database structure for storing categories and products - Category and product models.
Categories have a tree-like structure with a maximum nesting level of 10 - valid_nested_parent_level 
pre-save signal.
Categories are characterized by a name, and products are characterized by a name and a price.
A product can belong to multiple categories.
#### REST API:
##### Implement a REST API with the following capabilities:
- a. Create, update, and delete categories and products. - CRUD endpoints
- b. Change the parent category of a category.
	Patch (/category/{id}/)
- c. For a given list of products, retrieve all categories containing these products.
	GET (/category-of-product-list/?product_ids=1&product_ids=2)
- d. For a given category, retrieve a list of all products present in this category and its descendant categories of all levels.
	I believe it should be two separate endpoint:
	1. For a given category, retrieve a list of all products present in this category
		GET (product-by-category-list/<int:category_id>/)
	2. Its descendant categories of all levels
		GET (category-parents-list/<int:category_id>/)
- e. For a given list of categories, retrieve the count of product offerings in each category.
	GET (/category-product-offering-count-apiview/?category_ids=1&category_ids=2)
- f. For a given list of categories, retrieve the total count of unique product offerings.
	GET (/category-product-total-offering-count-apiview/?category_ids=1&category_ids=2)
#### OpenAPI/Swagger Specification:
Provide a detailed specification of the API in OpenAPI/Swagger format - /swagger

#### Python Web Framework:
Implement the solution using a Python web framework of your choice - Django/DRF

#### Test Data:
Include a set of test data to demonstrate the functionality of your solution - json file and command in readme
#### Docker Compose Configuration:
Provide a Docker Compose configuration for deploying your solution - server, db and nginx containers


#### Setup:
##### Run in project root directory:
	docker-compose up --build

##### For admin user creation:
	docker exec -it server python manage.py createsuperuser

##### For set test data:
	docker exec -it server python manage.py loaddata productapp_initial_data.json

##### Create .env file:
	copy sample_env .env

##### Fow access to site:
	0.0.0.0

##### Fow access to admin part:
	0.0.0.0/admin

##### Fow access to swagger documentation:
	0.0.0.0/swager
