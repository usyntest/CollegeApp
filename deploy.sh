# switch to project directory
cd "$(dirname "$0")" || {
  echo "failure"
  exit 1
}

echo "in_progress"

set -e
trap 'echo "failure"; exit 1' ERR
{
  # activate virtual environment
  source ./venv/bin/activate
  pip install -r requirements.txt

  # migrations
  python manage.py makemigrations
  python manage.py migrate

  # static
  python manage.py collectstatic --noinput

} >/dev/null 2>/dev/null

set +e
trap - ERR

echo "success"

# run gunicorn
gunicorn -b 0.0.0.0:59595 CollegeApp.wsgi
