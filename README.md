<p align="center">
 <img alt="logo" src="https://github.com/LeChat76/Projet10OC/assets/119883313/a0820c54-3c47-4f29-b81a-43990c58e9c5">
</p>

# Projet10OC
API creation with __Django Rest Framework__

--------------------------------------------------------------------------------------------------------------------------------------------------

## Installation
```sh
"git clone https://github.com/LeChat76/Projet10OC.git"
"cd Projet10OC"
Create virtual environment :
* "python -m venv .venv"
* activate environment :
    * for Linux "source .venv/bin/activate"
    * for Windows ".\.venv\Scripts\activate"
Install the necessary libraries by typing : "pip install -r requirements.txt"
Go in the folder of the projet : "cd project"
And run the webserver : "python manage.py runserver"

--------------------------------------------------------------------------------------------------------------------------------------------------

## Utilisation
The API provides the following endpoints.
- Base url is : [http://localhost:8000/api/](http://localhost:8000/api/)
1 ) create an user : user/
    * mandatory
    - `username=<username>` : username used to authenticate
    - `password=<password>` : password associated to username
    - `birthday=<birthday>` : birthday of the user, format dd/mm/yyyy
    * optionnal
    - `can_be_contaced`=<True> of <False> : user can be contacted?
    - `can_be_shared`=<True> of <False> : user's data can be shared?

