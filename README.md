# meetup.com-clone

### Introduction

Web application built using flask that lets user create an account, login/logout and organize a meetup. This is a very simple clone. I have built this app to learn flask as django contains all the batteries in place for **migrations, urls, and independent applications.**

Since Flask is a micro framework - You are implementing **everthing from scratch and learning why specific file was created** like urls.py to handle the routing, models.py to create models in the database. 

With flask you get to learn many things like How do you handle imports and avoid circular imports or How do you hash the passwords in the database and compare with entered password?



### Features
- User can Register 
- User can Login/Logout
- Create Meetups and Join Meetups 
- Meetups and attendees are displyed when you click on specific post. 

### Nice to have 
- Adding a location feature that lets user to choose locations from a list (probably google maps) 
- Letting user add events to their Google Calendar

### Areas of Improvement
- Using elastic search users and meetups (posts) from database
- I feel the way "attendees" are stored in database is not the right way. I am just storing the 'user_id' of the attendees as a 'string' with spaces. Then, convert back these user_ids to integer to query users from database,  which takes up a lot of extra code and creates an over head. One approach would be creating a proper relationship in the database. This is not a scalable approach. 

### Instructions to run (Python 3.7)

  - **Create a Virtual Environment**

    ``virtualenv -p python3 meetup_env``
    `source meetup_env/source/bin/activate`

  - **Install the Required Packages** 

    `pip install -r requirments.txt`

  - **Create a db (migrate) using python repl**

    `python`
    
    ***import the database***
    
    `from meetup_app.models import db`

    ***Delete old tables***

    `db.drop_all()`

    ***Create new tables***

    `db.create_all()`

 - ### Run the app

    ``python run.py``

