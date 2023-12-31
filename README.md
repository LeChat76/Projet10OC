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
    * for Windows `.\.venv\Scripts\activate`  
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
- **PATCH** method:
    - Modify specif user: `localhost:8000/api/user/<int:pk>/`
    * mandatory body options:  
        - `password=<password>`: to modify password (<font color="red">password is mandatory even empty because hashed in any cases</font>)
    * optionnals body options: 
        - `username=<username>`: to modify username  
        - `birthday=<birthday>`: to modify birthday, format dd-mm-yyyy (less than 15 years old will be rejected)  
        - `can_be_contacted=<1 or O>` to modify 'can_be_contacted' field 
        - `can_data_be_shared=<1 or O>`  to modify 'can_data_be_shared' field  

<img alt="rgpd" src="https://github.com/LeChat76/Projet10OC/assets/119883313/1cf0bf05-38a8-4652-a24f-d78e096e13e7">   

- **DEL** method: `localhost:8000/api/user/<int:pk>/`  
<font color="red">RGPD rules require that account deleted is fully destroyed. But all records created (project, issue, comments and access right in contributor) keep in database to allow users to continue to work with.</font>

Note : account admin / password Toto1234 has been created to access to the webadmin page of the DRF

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

<img alt="create_project" src="https://github.com/LeChat76/Projet10OC/assets/119883313/d321fee1-bb98-430a-9dd7-4d2edc52b45b">

#### Optionnals features for **project**:
- **GET** method:
    <span style="color:red">Note : to respect <span style="color:green">"green coding"</span>, result of this request will display minimal informations, for detailed informations, show specific project with second request</span>
    - Show project(s) created by authenticated user: `localhost:8000/api/project/`  
    - Show specific project if author or contributor: `localhost:8000/api/project/<int:pk>/`  
- **DEL** method (when deleting project, delation of record in contributor table by cascade):  
    - Delete specific project if author: `localhost:8000/api/project/<int:pk>/`  
    Note : delete a project will delete all issues and comments associated to
- **PATCH** method:  
    - modify specific project if author: `localhost:8000/api/project/<int:pk>/`  
        - field you can modify : __description__, __title__ and __type__  
 
----------------------------------------------------------------------------------

### 4 - Manage contributor with **POST** method: `localhost:8000/api/contributor/`
You can add contributor for specific user and project:  
* mandatory body options:  
    - `project=<project:pk>`: pk of the project to which to add a user  
    - `user=<user:pk>`: pk of the user to add to the project  

<img alt="create_issue" src="https://github.com/LeChat76/Projet10OC/assets/119883313/22e71067-d9cc-4b7d-8f73-3411e583daac">

Note : for security reason, only author of projects can add users its projects. And author can not add himself
because already authorized on its own projects.

#### Optionnals features for **contributor**:  
- **GET** method:
    - Show all contributors for specific project if you are the author: `localhost:8000/api/project/<int:pk>/contributor/`
- **DEL** method:
    - You can delete specific contributor if author of the associated project: `localhost:8000/api/contributor/<int:pk>/` 

----------------------------------------------------------------------------------

### 5 - Create Issue(s) with **POST** method: `localhost:8000/api/issue/`
Note : you can create issues only for project you are contributor or author  
* mandatory body options:  
    - `priority=<low, medium, high>`: priority level  
    - `title=<title>`: title of this issue(100 characters max)  
    - `type=<bug, feature, task>`: type of issue  
    - `project=<project_id>`: project ID  
    - `assigned_user=<user_id>`: user id of the user to assign this issue (default=authenticated user)
* optionnal body options:  
    - `description=<description>`: description of the project(500 characters max)  
    - `statut=<todo, inprogress, finished>`: statut of the issue(default= todo )  

<img alt="create_issue" src="https://github.com/LeChat76/Projet10OC/assets/119883313/27be523b-ef15-44bb-b2e5-be081f95d37c">

#### Optionnals features for **issue**:  
- **GET** method:  
    <font color="red">Note : to respect <font color="green">"green coding"</font>, result of the first two requests will display minimal informations, for detailed informations, show specific issue with third request</font>  
    - Show issue(s) associated to an project you are contributor or author: `localhost:8000/api/project/<int:pk>/issue/`  
    - Show specific issue if you are contributor or author of the associated project: `localhost:8000/api/issue/<int:pk>/`  
- **PATCH** method:
    - You can modify specific issue only if the issue is assigned to you: `localhost:8000/api/issue/<int:pk>/` 
        - field you can modify : __statut__=<todo, inprogress, finished>
- **DEL** method:
    - You can delete specific issue only if you are the author of the issue: `localhost:8000/api/issue/<int:pk>/` 
    Note : delete an issue will delete comments associated to

----------------------------------------------------------------------------------

### 6 - Create Comment(s) with **POST** method: `localhost:8000/api/comment/`
Note : you can create comments only for project you are contributor or author
* mandatory body options:
    - `issue=<issue_id>`: issue ID to associate comment with
    - `description=<description>`: description of the project(500 characters max)

<img alt="create_comment" src="https://github.com/LeChat76/Projet10OC/assets/119883313/28f35951-bf20-4af8-8ad8-3592ad52748d">

#### Optionnals features for **comment**:  
- **GET** method:  
    <font color="red">Note : to respect <font color="green">"green coding"</font>, result of the first two requests will display minimal informations, for detailed informations, show specific comment with third request</font>  
    - Show comment(s) associated to an project you are contributor or author: `localhost:8000/api/project/<int:pk>/issue/<int:pk>/comment/`  
    - Show specific comment if you are contributor or author of the associated project: `localhost:8000/api/comment/<int:pk>/`  
- **PATCH** method:
    - You can modify specific comment only if you are author: `localhost:8000/api/comment/<int:pk>/`  
        - field you can modify : __description__
- **DEL** method:
    - Delete specific comment only if you are the author: `localhost:8000/api/comment/<int:pk>/` 

----------------------------------------------------------------------------------

### - Diagram

<img alt="create_comment" src="https://github.com/LeChat76/Projet10OC/assets/119883313/62de1ec3-800d-46ab-a6a0-02f03844319e">