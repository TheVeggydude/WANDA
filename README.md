# 1 WANDA
WANDA is a web-based application that takes a pre-defined JSON formatted tree structure with questions, answers and results and presents them to the user in a neatly formatted way.

# 1.1 Requirements
WANDA was made using Python 3.4 and Django 1.9. Therefore the requirements are quite simple. You system should have Python 3.4 (or higher) with the Django 1.9 (or higher) packages installed as well.

# 1.2 Setting the directories up
WANDA should be located somewhere on the server, with a folder 'data' on the same directory level as the WANDA folder. In the 'data' folder the JSON file containing the tree data should be located and called 'data.json', resulting in the following (simplified) directory structure:

someDirectory
	|
	|-- wanda
	|
	'-- data
		'-- data.json

# 1.3 Setting up the database
Now that the directories have been set up it is time to create the database. Depending on what type of database you want to use the process is different. Standard, WANDA (and Django in general) comes with a sqlite database. But as some people prefer other databases this can be changed.

As the standard sqlite database should suffice for most usages of WANDA we will not go into to much depth on changing the database used. However, note that settings.py is the location where the database used is specified and there is plenty of documentation on changing the database (https://docs.djangoproject.com/en/1.8/ref/settings/#databases for example).

# 1.4 Updating and filling the database
Now that WANDA is connected to some database (note that de database itself is not created yet in the case of sqlite - this will happen shortly when migrating) we can apply the migrations that create the required tables in the chosen database. In a terminal, cd to the location of 'manage.py' and run the following set of commands:

python manage.py makemigrations
python manage.py migrate
python manage.py load_data

Note that load_data can take some time based on the speed of the server and the size of the JSON file. After this the database will be set up and the data will be in there.

# 1.5 Running the server in debug mode
To run the server in debug mode make sure that in 'settings.py' DEBUG is set to TRUE. Note that if this is set Django will handle fileserving and display Django error messages in stead of any 404 or 500 pages.

Next, call 'python manage.py runserver' (without quotes) from the location where 'manage.py' is located and you will see a few lines stating that the serving is booting. The website can now be accessed on localhost:8000 (with standard settings).

# 1.6 Deploying WANDA
https://docs.djangoproject.com/en/1.9/howto/deployment/
