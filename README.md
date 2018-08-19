# StackOverFlow_lite    [![Build Status](https://travis-ci.org/belio39/StackOverFlow_lite.svg?branch=Challenge2)](https://travis-ci.org/belio39/StackOverFlow_lite) [![Coverage Status](https://coveralls.io/repos/github/belio39/StackOverFlow_lite/badge.svg)](https://coveralls.io/github/belio39/StackOverFlow_lite)
StackOverflow-lite is a platform where people can ask questions and provide answers

# Usage

- Home page
- Create an account
- Login into your account
- Post a question
- Fetch all questions
- Fetch a single question
- Edit a specific question
- Delete a specific question
- Post an answer to a question

# Prerequisities
  - Python 3.6 version
 
# Installation
Downlaod / clone the project to your local computer by:

- Download the zip file of this repository.
- Unzip it and navigate into the StackOverflow-lite directory.

# Virtual environment
Create a virtual environment
> $ virtualenv venv

Activate the environment

>  $ venv/bin/activate 

# Dependencies
Install package requirements to your environment
>$ pip install -r requirements.txt 

# Env
Create a.env file in your StackOverflow-lite root directory and add:

>$ venv/bin/activate
>$ export FLASK_APP="run.py"
>$ export SECRET="any-character-or-STRING-YOU-PREFER"
>$ export APP_SETTINGS="development"

# Testing
To set up testing environment
>$ pip install nose
>$ pip install coverage

# Testing API endpoints
<table> 
<tr>
<th>Test</th>
<th>Endpoints</th>
<th>HTTP VERBS</th>
</tr>
<tr>
<td>Post a question</td>
<td>/api/v1/questions</td>
<td>POST</td>
</tr>
<tr>
<td>View all question</td>
<td>/api/v1/questions</td>
<td>GET</td>
</tr>
<tr>
<td>Get single question</td>
<td>/api/v1/questions/<questions_id></td>
<td>GET</td>
</tr>
<tr>
<td>Post an answer to a question </td>
<td>/api/v1/questions/<question_id>/answers</td>
<td>POST</td>
</tr>
</table>

# Resources
The API is hosted on [Heroku](https://stackoverflow-lite-app.herokuapp.com/)

# Authors
> [Dennis rotich Belio](https://github.com/belio39)

# Acknowledgement
Andela Bootcamp - cohort 31
