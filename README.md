# Perfectétude

Perfectétude is a website designed for music teachers to view and manage their students' practice recordings and statistics. 

## Code Structure 

We used Django for our web framework. Our Models.py file corresponds with our SQL database. It is the relationship with our data, and contains everything related to data access and validation. The Views.py file relates to the Controller in the MVC pattern and handles all the business logic that throws back to the respective templates. Our templates relate to the View in the MVC pattern. It is the presentation layer that handles the presentation logic in the framework and basically controls what should be displayed and how it should be displayed to the user. Urls.py contains all of our various web urls. 

We stress-tested our database to achieve proof of concept. See StressTest.jpg in our main repo.


## Compiling, setting up, deployment

Our project utilizes fake data that we created using a Python script. (See the data_production.py module contained in our zip file)

This module was created and used to build a fake dataset that corresponds to our current schema as well as all of the constraints we have on this data due to the nature of the platform.

Inside the module, each function represents a distinct table. Under the main, one can choose the number of members in the dataset, the number of those members which are teachers and the number of days to have recording data for.

Currently it is set at 10 members, 3 teachers and 10 days. Upon run, the output is saved to a (created) file named 'generated_inserts.sql' which includes around 550 insert statements that should be manually uploaded to the database within the docker mysql container environment..

The data is successfully in there and the files we used to populate our database are as follows:

1. create.sql - creates the tables and concurs with the correct schema

2. generated_inserts.sql - contains all the insert statements created by data_production.py

In order to compile, set up, and deploy our website locally, you will need to utilize Django and Docker. 

First, download and set up Docker: https://docs.docker.com/docker-for-mac/install/

Next, download and set up Django: 

```bash
python -m pip install Django
```
In the same directory as the project, run "docker-compose build" to create the docker image.

Next, run "docker-compose up" to start running things. 

Use "docker ps -a" to view ports that are running on and to obtain the "container ID" for the mysql container.

Using the container ID, enter "docker exec -it [container ID] bash". You are now inside of the docker database container.

Now, you can load the SQL database. First, open a terminal shell.

Run "docker ps -a" to get the mySQL container ID. Then you can run "docker exec -it [container ID] bash".

Enter "mysql -u root -p". This will prompt you for a password. Type in "example".

Open a new terminal shell. Cd to the local github repo.

Run "docker cp inserts.sql *container ID*:/tmp" and "docker cp create.sql *container ID*:/tmp".

Navigate back to your old terminal shell. Type "use development", and then "\\. /tmp/create.sql" and "\\. /tmp/inserts.sql". 

The database should now be loaded.

You should now be able to view the site locally by pointing a web browser to "localhost:3000/music."


## Limitations in our current implementation

In some ways, our project differs from our initial goals. Firstly, our audio recordings do not auto-combine, as we had initially planned to implement. We also do not have a student portal to interact with our teacher app, which was the other half of our broad concept. 
