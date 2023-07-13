<p align="center">
 <img alt="logo" src="https://github.com/LeChat76/Projet10OC/assets/119883313/a0820c54-3c47-4f29-b81a-43990c58e9c5">
</p>

# Projet10OC
API creation with __Django Rest Framework__

## Installation

* Clone repository: `git clone https://github.com/LeChat76/Projet10OC.git`  
* Enter in created folder: `cd Projet10OC`  
* Create virtual environment: `python -m venv .venv`  
* Activate environment:  
    * for Linux `source .venv/bin/activate`  
    * for Windows `.\\.venv\Scripts\activate`  
* Install the necessary libraries: `pip install -r requirements.txt`  
* Go in the folder of the projet: `cd project`  
* And run the webserver: `python manage.py runserver`  

## Utilisation
The API provides the following endpoints.
All endpoints have been tested with Postman.

----------------------------------------------------------------------------------

### 1 - Create an user with **POST** method: `localhost:8000/api/user/`
* mandatory body options:
    - `username=<username>`: username used to authenticate
    - `password=<password>`: password associated to username
    - `birthday=<birthday>`: birthday of the user, format dd-mm-yyyy (less than 15 years old will be rejected)
* optionnal body options
    - `can_be_contacted=<1 or O>` for True of False: user can be contacted? (default = False)
    - `can_data_be_shared=<1 or O>`  for True of False: user's data can be shared? (default = False)

 <img alt="create_user" src="https://github.com/LeChat76/Projet10OC/assets/119883313/669f4860-cea7-40b6-b870-25419a76ca69">

----------------------------------------------------------------------------------

### 2 - generate token with **POST** method: `localhost:8000/api/token/`
* mandatory body options:
    - `username=<username>`: existing username
    - `password=<password>`: password of this username

<img alt="generate_token" src="https://github.com/LeChat76/Projet10OC/assets/119883313/91cc8beb-c5d8-431c-be0d-7e93e5aaa9e8">

#### Optionnals features for **user**
- **GET** method:
    - Show all users (except superuser): `localhost:8000/api/user/`
    - Show specific user: `localhost:8000/api/user/<int:pk>/`
- **DEL** method:
    - Delete specific user: `localhost:8000/api/user/<int:pk>/`
- **PUT** method:
    - modify specific user: `localhost:8000/api/user/<int:pk>/`
        - mandatory body options:
            - `username=<username>`: username used to authenticate
            - `password=<password>`: password associated to username
            - `birthday=<birthday>`: birthday of the user, format dd-mm-yyyy (less than 15 years old will be rejected)

----------------------------------------------------------------------------------

### 3 - create project with **POST** method: `localhost:8000/api/project/`
<font color="red">**At this point, all request without Token will be rejected**</font>
* mandatory body options:
    - `type=<frontend, frontend, ios, android>`: select type of project
    - `title=<title>`: title of this project(100 characters max)
* optionnal body options:
    - `description=<description>`: description of the project(500 characters max)  

Note : When creating a project, the authenticated user is automaticaly the author and the contributor.

<img alt="create_project" src="https://github.com/LeChat76/Projet10OC/assets/119883313/38d52c73-e50e-4a63-b8f2-9695c5b94e6b">

#### Optionnals features for **project**
- **GET** method:
    - Show project(s) for current user: `localhost:8000/api/project/`
    - Show specific project if authorized: `localhost:8000/api/project/<int:pk>/`
- **DEL** method (when deleting project, delation of record in contributor table by cascade):
    - Delete specific project: `localhost:8000/api/project/<int:pk>/`

----------------------------------------------------------------------------------

### 4 - Create Issue(s) with **POST** method: `localhost:8000/api/issue/`
Note : you can create only issue for project you are author, contributor can only read
* mandatory body options:
    - `priority=<low, medium, high>`: priority level
    - `title=<title>`: title of this issue(100 characters max)
    - `type=<bug, feature, task>`: type of issue
    - `project=<project_id>`: project ID
* optionnal body options:
    - `description=<description>`: description of the project(500 characters max)
    - `statut=<todo, inprogress, finished>`: statut of the issue(default= todo )

<img alt="create_issue" src="https://github.com/LeChat76/Projet10OC/assets/119883313/07def0fc-ddc0-4026-b3f6-df265879e4c5">



