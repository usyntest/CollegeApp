# GGSocial

## Running the project
Run these commands in the project directory  

Create a virtual environment
```
$ virtualenv venv
```
Activate the virtual enviornment
```
$ venv\Scripts\activate
```
Install Django
```
$ pip install -r requirements.txt
```
Make tables
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Run it
```
python manage.py runserver
```

## Documentation
### Types of Alerts
- **Normal Post** - No Different Styling
- **Special Post 1** - Post with a pink border and background
- **Special Post 2** - Only can be made by me
- **Special Post 3** - Small alerts like someone joined