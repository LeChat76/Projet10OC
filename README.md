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

**Note: dependabot is enabled on this project. A pull request will be automatically created if a security flaw is discovered. This way, dependencies will always be secure.**

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

#### Optionnals features for **user**:
- **GET** method:
    - Show all users (except superuser): `localhost:8000/api/user/`
    - Show specific user: `localhost:8000/api/user/<int:pk>/`

### <font color="red">RGPD rules:</font>
- Modify `can_be_contacted` and `can_data_be_shared` and all others field with **PATCH** method: `localhost:8000/api/user/<int:pk>/`
* mandatory body options:  
    - `password=<password>`: to modify password (<font color="red">password is mandatory even empty because hashed in any cases</font>)
* optionnals body options: 
    - `username=<username>`: to modify username  
    - `birthday=<birthday>`: to modify birthday, format dd-mm-yyyy (less than 15 years old will be rejected)  
    - `can_be_contacted=<1 or O>` to modify 'can_be_contacted' field 
    - `can_data_be_shared=<1 or O>`  to modify 'can_data_be_shared' field  


<img alt="rgpd" src="https://github.com/LeChat76/Projet10OC/assets/119883313/1cf0bf05-38a8-4652-a24f-d78e096e13e7">   

- Delete specific user with **DEL** method: `localhost:8000/api/user/<int:pk>/`  
<font color="red">RGPD rules require that a deleted user also deletes all traces of his activity SO all projects, issues and comments he has created will be deleted.</font>

----------------------------------------------------------------------------------

### 2 - generate token with **POST** method: `localhost:8000/api/token/`
* mandatory body options:
    - `username=<username>`: existing username
    - `password=<password>`: password of this username

<img alt="generate_token" src="https://github.com/LeChat76/Projet10OC/assets/119883313/91cc8beb-c5d8-431c-be0d-7e93e5aaa9e8">

----------------------------------------------------------------------------------

### 3 - create project with **POST** method: `localhost:8000/api/project/`
<font color="red">**At this point, all request without Token will be rejected**</font>
* mandatory body options:
    - `type=<backend, frontend, ios, android>`: select type of project
    - `title=<title>`: title of this project(100 characters max)
* optionnal body options:
    - `description=<description>`: description of the project(500 characters max)  

Note : for better project management, identical titles are refused

<img alt="create_project" src="https://github.com/LeChat76/Projet10OC/assets/119883313/3380790e-9632-4610-b98b-87b640541fce">

#### Optionnals features for **project**:
- **GET** method:
    - Show project(s) for current user: `localhost:8000/api/project/`  
    <font color="red">To respect <font color="green">"green coding"</font>, result of this request will display minimal informations, for detailed informations, show specific project bellow</font>
    - Show specific project if author: `localhost:8000/api/project/<int:pk>/`  
- **DEL** method (when deleting project, delation of record in contributor table by cascade):  
    - Delete specific project if author: `localhost:8000/api/project/<int:pk>/`  
- **PATCH** method:  
    - modify project if author: `localhost:8000/api/project/<int:pk>/`  

----------------------------------------------------------------------------------

### 4 - Manage contributor with **POST** method: `localhost:8000/api/contributor/`
You can add contributor for specific user and project:  
* mandatory body options:  
    - `project=<project:pk>`: pk of the project to which to add a user  
    - `user=<user:pk>`: pk of the user to add to the project  

<img alt="create_issue" src="https://github.com/LeChat76/Projet10OC/assets/119883313/f8b641ec-5a6a-47ce-a1ae-9576195e72f9">

Note : for security reason, only author of projects can add users its projects. And author can not add himself
because already authorized on its own projects.

#### Optionnals features for **contributor**:  
- **DEL** method:
    - You can delete specific contributor: `localhost:8000/api/contributor/<int:pk>/` 

----------------------------------------------------------------------------------

### 5 - Create Issue(s) with **POST** method: `localhost:8000/api/issue/`
Note : you can create issues only for project you are contributor or author  
* mandatory body options:  
    - `priority=<low, medium, high>`: priority level  
    - `title=<title>`: title of this issue(100 characters max)  
    - `type=<bug, feature, task>`: type of issue  
    - `project=<project_id>`: project ID  
* optionnal body options:  
    - `description=<description>`: description of the project(500 characters max)  
    - `statut=<todo, inprogress, finished>`: statut of the issue(default= todo )  

<img alt="create_issue" src="https://github.com/LeChat76/Projet10OC/assets/119883313/b9e18196-ed9f-47d3-bff4-a874ae741c31">

#### Optionnals features for **issue**:  
- **GET** method:  
    - Show all issues for current user: `localhost:8000/api/issue/`  
    <font color="red">To respect <font color="green">"green coding"</font>, result of this request will display minimal informations, for detailed informations, show specific issue bellow</font>
    - Show specific issue if authorized: `localhost:8000/api/issue/<int:pk>/`  
- **PATCH** method:
    - You can modify specific issue if authorized: `localhost:8000/api/issue/<int:pk>/` 
        - field you can modify : __priority__, __title__, __description__, __type__ and __statut__
- **DEL** method:
    - You can delete specific issue if authorized: `localhost:8000/api/issue/<int:pk>/` 

----------------------------------------------------------------------------------

### 6 - Create Comment(s) with **POST** method: `localhost:8000/api/comment/`
Note : you can create comments only for project you are contributor or author
* mandatory body options:
    - `issue=<issue_id>`: issue ID to associate comment with
    - `description=<description>`: description of the project(500 characters max)

<img alt="create_comment" src="https://github.com/LeChat76/Projet10OC/assets/119883313/cc81f63e-0e38-49ef-b7ae-e0720c22f7ac">

#### Optionnals features for **comment**:  
- **GET** method:  
    - Show all comments for current user: `localhost:8000/api/comment/`  
    <font color="red">To respect <code style='color : green'>"green coding"</code>, result of this request will display minimal informations, for detailed informations, show specific comment bellow</font>
    - Show specific comment if authorized: `localhost:8000/api/comment/<int:pk>/`  
- **PATCH** method:
    - You can modify specific comment if authorized: `localhost:8000/api/comment/<int:pk>/`  
        - field you can modify : __description__
- **DEL** method:
    - Delete specific comment if authorized: `localhost:8000/api/comment/<int:pk>/` 

----------------------------------------------------------------------------------
