# flask-website

This is a blog website created with Flask features on Python.

## Preview
![preview gif](https://raw.githubusercontent.com/PooWoox/python-flask-website/master/flask_blog_preview.gif)

## Running locally

For running it, clone the repository and run the file "run.py" to execute everything that is on the "website" package and access using your browser on localhost:5000. You will have to set your own environment variables for using the reset password email funcitonality if you want. You can change it on config.py file.

--------------------------------------------------------------

## A bit about the functionality

The webapp is entirely organized in directories. Besides static stuff and html templates, I used blueprints for all others for better organization and ease on adding functionalities later.

Speaking of functionalities, below I will list them and talk about each with more details. First, here is a list of the modules I used for the making (if I forgot some and remember later I'll add it here):
- From flask: current_app, render_template, redirect, url_for, request, Blueprint, flash, abort;
- os as I stored some environment variables on my computer;
- datetime for creating a "date_posted" value on the Posts table;
- Flask-WTF / WTForms for forms;
- SQLAlchemy with SQLite for database connection;
- flask_login for useful things like 'current_user', 'login_user', 'logout_user' and 'login_required';
- itsdangerous for generating a token to authenticate the user on the password reset email;
- bcrypt for encrypting passwords before saving them to the db;
- PIL for handling profile pictures;
- secrets for generating a random hex that I used to name the profile pictures saved on the db;
- flask_mail for sending the password reset email.

## Features live
1. Register/Login:
  Both registering and logging in works with forms, information is received and saved on the db. I created one table for users, called 'Users', for storing an id, username, email and profile picture (there is also a relationship to the Posts table with the name 'author', to relate users to their posts). When registering all fields are validated according to the rules set, emails are checked to be valid ones, username cannot already exist and the password confirmation has to be equal to the password typed.
2. View/Edit user profile page:
  User profile page is simple, there's actually just the username and profile picture displayed there for now. On this page you can edit the username, email and profile pic. When changing the username or email a verification on the db to check if there are no equal values already existent will happen. Profile page and only be viewed and accessed when logged in.
3. Create/Edit/Delete posts:
  When logged in there is a 'New Post' option on the navbar. You can create a post with a title and content that will be saved on the second table I created on SQLite, called Posts. This Posts table has the columns id, title, date_posted, content and author. After posting, your post will be displayed on the top of the page. When viewing a post on the home page you can click the post title to go to its individual page or click the author(username) to go to a page where you will be able to see all of this user's posts. If you click on your own post title, you will be able to edit or delete your post. If you try to access another user's post edit function via url you will get access denied.
4. Home page and user posts pagination:
  Not much to say about it, I used a paginate function on both pages to make it look cleaner, only 5 posts per page are shown.
5. Password reset e-mail:
  This feature was nice building. On the Login page you will find the "Forgot your password?" link. When clicking there you will be redirected to a page where you confirm your e-mail. The function behind it will verify if the email typed exists on the db, if it doesn't you will be flashed with an error message. If your email exists, 'itsdangerous' module will generate a token that lasts for 30 minutes. This token will be concatenated to an url that is sent to your email and if you click it within the 30 minutes, you will be able to reset your password. If you don't use the link in 30 minutes, it will just expire and nothing will happen.

--------------------------------------------------------------

Thanks again for reading through this explanation, any doubts can be sent to me and tips are always welcome so I can improve my code. 
