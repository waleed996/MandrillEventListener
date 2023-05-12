# Event Listener For Mandrill 3rd Party Email Service

### Tech Used
1. Django
2. Django Rest Framework (For Webhook)
3. SQLAlchemy ORM
4. Django Channels (For Websockets)
5. Daphne (A webserver supporting http and websocket protocols)
6. SQLite3 relational database for persistent storage
7. Mandrill 3rd party service for sending test events

### How To Run?

Follow the steps below to get the project up and running on your local machine

1. Create a virtual environment
```python3 -m venv my_env```

2. Activate the virtual environment
```source my_env/bin/activate```

3. Install all requirements from requirements.txt
```pip install -r requirements.txt```

4. Create run configuration using IDE and set these env variables
```commandline
PYTHONUNBUFFERED=1
DJANGO_SETTINGS_MODULE=mandrill_event_listener_config.settings.local
SECRET_KEY={INSERT_YOUR_SECRET_KEY_HERE}
```

5. Set the working directory to the project directory

6. Run the following command to start the daphne ASGI server
```commandline
{path_to_my_env}/bin/daphne mandrill_event_listener_config.asgi:application --port 8000
```

7. When the server is running, go to http://127.0.0.1:8000 to see the html view where updates will be sent through
websocket in realtime.

### Mandrill Testing
Install, setup and run `ngrok` by following instructions on their website. When `ngrok` is running
it will temporarily (for 2 hours) connect our system with the internet and generate a public url.
We can use this public url as the base url for our webhook url that we need to register
with mandrill so they can send updates to our application.

```https://8734-2407-d000-f-fb08-95f2-6181-6b4b-8572.eu.ngrok.io -> http://localhost:8000```

The webhook url to be registered with mandrill will be something like the following (base_url + webhook_url)

```https://8734-2407-d000-f-fb08-95f2-6181-6b4b-8572.eu.ngrok.io/mandrill_event_listener/api/v1/user_email_action_updates```

### Note: You will need to create a mailchimp account to login to mandrill for testing 
