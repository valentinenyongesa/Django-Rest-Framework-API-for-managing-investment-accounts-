1. Create a virtual environment to isolate the project from unintentional updates that can introduce vulnerabilities to the project. This is accomplished by the following command : python3 -m venv env
2. Activate the created virtual environment above to ensure use of the packages installed in the virtual environment.This is achieved by the following command : source env/bin/activate
3. Install the Django and Django Rest Framework. This is attained by this command : pip install django djangorestframework 
4. Create a new Django project. This is accomplished by the command: django-admin startproject investment_account_management_api .  The name of the project is : investment_account_management_api
5. Create an app which is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.This is achieved by the following command : python manage.py startapp investment
6. Configure DRF in Django Settings:Open investment_account_management_api/settings.py and add 'rest_framework' to the INSTALLED_APPS list:
Complete the models where models represent the structure of the database.
7. Django models are used to describe structure of database tables. Each Django model corresponds to a table in a database while each attribute is the column in the table.
8. Create Serializers which convert complex data types, such as Django QuerySets, into Python data types that can be easily rendered into JSON, XML, or other content types. They also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
8. Implement views and permissions to provide the logic for handling HTTP requests like GET, POST, PUT, and DELETE. In this case it shall be used to handle CRUD operations for the models.
Configure URLs to define the routing of the API endpoints.
Write Unit Tests
To get view only users use the curl command: curl -X GET http://localhost:8000/api/investment-accounts/ -H "Authorization: Token <view_only_user_token>"   Use the GET request to verify that the view-only user can access account data.
Use the POST request to confirm that the view-only user is restricted from creating new accounts. : curl -X POST http://localhost:8000/api/investment-accounts/ -H "Authorization: Token <view_only_user_token>" -d '{"name": "New Account", "details": "Details"}' -H "Content-Type: application/json"
10. Navigate to http://localhost:8000/admin/ in your web browser and log in using the superuser

