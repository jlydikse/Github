# Overview

I wanted to create a follow-up to my CRUD project that goes over the Dagee game, but this time I attempted to create a webapp of a blog so that people who are playing Dagee could post and talk about it. This opportunity afforded me a lot of really cool learning experiences, and while it is not pretty, nor perfect, it still functions and it was lots of fun learning about it.

Working within the Django / Python framework was interesting and was a lot of bouncing between directories and creating new ones. Something that I struggled with on this was making sure that the files were all connected and everything functioned. The way you start is by making a directory in your command prompt with "django-admin startproject my_project_name" and then you run the command "python manage.py startapp my_app_name". Once your project is actually created and you've fleshed it out a little bit, you run the server with the following command, "python manage.py runserver". You then go to your internet browser and type in "localhost:8000" which will load your webapp.

The reason I created this was to learn more about webapps and see if I liked creating them. I learned about how to link all of these different files and how to troubleshoot through the process.



[Software Demo Video](https://youtu.be/Q0rhdbjh8Bg)

# Web Pages

There are a total of 3 webpages within this web application.

## Post_list page
### Dynamic Content: List of blog posts retrieved from the database

## Post_edit page
### Dynamic Content: provides a form to input blog post title and content

## Post_description page.
### Dynamic Content: Title and content of a specific blog post


# Development Environment

I used Django to run the server and to develop the software. I used python within that framework to create the different files such as the views, models, forms, urls, etc. I created various templates with html

Within the python programs I created, I imported things from django.db and django itself to import models and forms.


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [RealPython.com](https://realpython.com/python-django-blog/)
* [Medium.com](https://medium.com/@bobbykboseoffice/create-customized-user-input-with-django-forms-in-simple-steps-c4375c4df355)

# Future Work

* I need to create a style sheet that functions properly, so that the web app looks much nicer.
* I want to connect this project with my previous Dagee CRUD operations project.
* I could add more functionality, like logging in to the web app, and verifying the user is valid.