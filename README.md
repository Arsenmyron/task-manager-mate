# Task Management App

## About TaskManager

Powered by Django TaskManager is wonderful app for tracking your tasks.
And actually not only yours! By using TaskManager you can create tasks, assign them to other team members and work together to find the best solution and after that mark them as **completed**!

### Features:

1.  Create, Read, Update, Delete operations for Tasks, Workers, TaskTypes & Tags
2. Assigning tasks to different workers
3. Tag assigning system for better task definition
4. Simple task status update(Completed/Incompleted)
5. Comfortable way for tracking tasks for each member of the team

## [TaskManager (Deployed on Render)](https://task-manager-53a5.onrender.com)

### Test user credentials
Login:
````
user
````
Password:
````
user12345
````

# Project Set Up
## Prerequisite
### - Python (>= 3.10)

## Follow these steps to run project locally

1. Clone the repository:
    ````
   git clone -b develop https://github.com/Arsenmyron/task-manager-mate
   cd task-manager-mate
   ````
2. Set up a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Linux/MacOS use `source venv/bin/activate`
   ```
3. Install requirements:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```sh
   python manage.py createsuperuser
   ```
   or load fixture with pre-made records:
    ```sh
    python manage.py loaddata dump.json
    ```
   and use username: <strong>arsen</strong> & password: <strong>test12345</strong> to log in
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

