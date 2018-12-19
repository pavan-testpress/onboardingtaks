# Onboarding Tasks

This Project involves in doing multiple apps which covers so many features that django is providing to us.
Tasks/Apps to complete in order to complete Onboarding tasks.
- [x] Bookmarks app
- [x] Places app
- [x] Pages app
- [x] Events app
- [x] Invitations app
- [x] Bootstrap
- [x] User Authentication
- [ ] User Accounts
- [ ] Email
- [ ] Password Change and Reset
- [ ] Forms
- [ ] Custom User Model
- [ ] Movies app
- [ ] Music app
- [ ] People app
- [ ] Books app
- [ ] Message Board app
- [ ] Blog app
- [ ] Newspaper app
- [ ] Permissions and Authorizations
- [ ] Comments
- [ ] social image bookmarking website

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing.

### Prerequisites

- **Python 3.6.6**
- **Django 2.1.3**
- **taggit**
- **django-bootstrap4**


### Installing

- Download & install Python by following this [offical page instructions](https://www.python.org/downloads/release/python-366/)
- Command to install django `pip install django` [instructions](https://docs.djangoproject.com/en/2.1/topics/install/)
- Command to install taggit `pip install django-taggit`
- Command to install bootstrap `pip install django-bootstrap4`

### Steps to run the project
- Clone the project to local machine after installing above softwares
- Go to the sub-directory where you can see *manage.py* file
- Open Command prompt or Terminal from this directory
- Execute Command: `python manage.py runserver` for Unix and `py manage.py runserver`
- Open the displayed link in browser and use the project.

## Usage
### 1. Bookmarks app

```
In Bookmarks app we can add an URL with name, url, description and tag it particular folder it belongs.
If folder you want to tag is not found then you can create new folder form left side menu and select it later.
You can Edit, Delete and tag an URL after saving as well.
You can filter url's by folders.
```

### 2. Places app
```
In Places app you can add a new place by filling all required fields given in the form.
After creating places you select the place to see the details of the place.
You can filter the places list by selecting the city.
```

### 3. Pages app
```
In Pages app you can add a new page by giving title, html content, and order you can to display in
the navigation bar.
After submitting the page you can see the title of your page added to the navigation bar.
By clicking title name in navigation bar you will see the rendered html of your page.
```

### 4. Events app
```
In Events app you can add an event by selecting the places which are created through the Places app.
If you want to create a new place then click on add place, add it and then select the place.
you can filter events based on weekday, month, specific date.
```

### 5. Invitation app
```
In Invitation app you can invite your friends by their email id.
To use this app first you need to add an email and password to onboardingtasks>settings.py>
EMAIL_HOST_USER = '123@gmail.com' <<replace with your mail, use mail with less secure setting enabled(https://myaccount.google.com/u/0/lesssecureapps?)
EMAIL_HOST_PASSWORD = 'password' <<replace with your password
Once you invite both of you will get an email saying that you invited.
Once the invitee registered the app, you will get a notification mail saying the invitee is registered.
```
