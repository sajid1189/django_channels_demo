# A quick demonstration on how to integrate django channels to enable websockets in a django project 

## Setup

### 1. Clone the repository
### 2. inside the project directory (django_channels_demo) create a virtual environment
```
virtualenv venv
```
### 3. Activate the virtual environment
```
source venv/bin/activate
``` 
(on Mac/Linux)

### 4. Install the dependencies
```
 pip install -r requirements.txt 
```

### 5. Run database migrations

```
 ./manage.py migrate
```

### 5. Run the development server

```
 ./manage.py runserver
```

## Send/receive messages

### open http://127.0.0.1:8000/ on your browser

### type in a desired username: (let's say max) and submit

### You will be redirected to http://127.0.0.1:8000/private/?user=max
At this point your browser tab is connected to three websockets 
```
1.  ws://127.0.0.1:8000/ws/private/max/  <--  max = the username that you typed in
2.  ws://127.0.0.1:8000/ws/open-room/
3.  ws://127.0.0.1:8000/ws/tasks/
```

### Open 3 terminal windows and ```cd``` to the project root dir (django_channels_demo) in each window
### On each window activate the virtual environment
```
source venv/bin/activate
```
### On window 1 run:
```python run_tasks.py```
On your browser window, you should be able to see messages like :

task 1 submitted

task 1 being executed

task 1 finished

### On window 2 run:
```python send_open_messages.py```
type a message on the prompt
Under 'Open messages from WS ' header, on your browser window , you should be able to see the message you just typed.

### On window 3 run:
```python send_private_messages.py```
type the username. In this case you will type ```max``` because you want to send a message explicitly to max. 
Type the message in the next prompt.
Only max (http://127.0.0.1:8000/private/?user=max) can see this message. On other browser tabs e.g., http://127.0.0.1:8000/private/?user=john
won't see this message.
Under 'Private messages from WS ' header, on your browser window (http://127.0.0.1:8000/private/?user=max), you should be able to see the message you just typed.



