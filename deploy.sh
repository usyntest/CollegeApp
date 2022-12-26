# switch to project directory
cd "$(dirname "$0")" || exit 1

# activate virtual environment
source ./venv/bin/activate
pip install -r requirements.txt

# migrations
python manage.py makemigrations
python manage.py migrate

# static
python manage.py collectstatic

# run gunicorn
gunicron -b 0.0.0.0:59595 CollegeApp.wsgi
