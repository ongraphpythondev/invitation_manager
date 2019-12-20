# Project Setup

Please read all the instructions carefully and follow step by step.

## Prerequisites:

You will need the following programs properly installed on your system.

* [Python](https://www.python.org/) 3.7

* [Virtual Environment](https://docs.python.org/3/library/venv.html)

* [RabbitMQ](https://www.rabbitmq.com/)


## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/invitation_manager.git

cd invitation_manager
```
#### Note:-

Open settings.py in the project directory and update database settings and email settings.


EMAIL_HOST_USER = "your_email"

EMAIL_HOST_PASSWORD = "your_password"


```
# Install required packages for the project to run
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

# Run Celery worker to work in the background
celery -A invitation_manager worker -l info

```

#### API Endpoints:-
* [For authentication APIs please follow this link](https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html)

1. URL: http://127.0.0.1:8000/api/invitations/

   
       METHOD: GET
       HEADER: Authorization Token <token>
       Response:
       data:[
         {
              'id': <str>, 
              'createdTime': <str iso 8601 format>,
              'seconds': <int> The time since the invitation has been created in seconds
              'email': <str>,
              'used': <bool>
              'creatorEmail': <str>, 
              'creatorFullname': <str> Example: John Oliver,
          },
              ...
         ]
      
      
       METHOD: POST
       HEADER: Authorization Token <token>
        Body:
              {
                "email": "asd@example.com"
               }
       Response:
             {
              'id': <str>, 
              'createdTime': <str iso 8601 format>,
              'seconds': <int> The time since the invitation has been created in seconds
              'email': <str>,
              'used': <bool>
              'creatorEmail': <str>, 
              'creatorFullname': <str> Example: John Oliver,
          }

2. URL: http://127.0.0.1:8000/api/invitations/{id}

        METHOD: PATCH
        HEADER: Authorization Token <token>
        Request Body:
          {
            "email": "asd_updated@example.com",
            "used": true/false
           }
        
        Response:
        <id>
        

        METHOD: DELETE
        HEADER: Authorization Token <token>
        Response:
        <id>

