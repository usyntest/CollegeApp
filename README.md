# GGSocial
<img width="1440" alt="Screenshot 2024-04-29 at 7 05 12 PM" src="https://github.com/usyntest/CollegeApp/assets/68940203/8ae71176-7477-4b8d-a146-0c48743e6427">
<img width="1440" alt="Screenshot 2024-04-29 at 7 06 19 PM" src="https://github.com/usyntest/CollegeApp/assets/68940203/2d9bfd2e-0e61-4ad7-9eea-79133919652c">

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
