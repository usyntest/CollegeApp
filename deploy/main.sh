failure() {
  echo "failure" >"$(tty)" # to override /dev/null redirection
  exit 1
}

# switch to project directory
cd "$(dirname "$0")"/.. 2>/dev/null || failure

echo "in_progress"

{
  # activate virtual environment
  source ./venv/bin/activate || failure
  pip install -r requirements.txt || failure

  # migrations
  python manage.py makemigrations || failure
  python manage.py migrate || failure

  # static
  python manage.py collectstatic --noinput || failure

} >/dev/null 2>/dev/null

echo "success"

# run gunicorn
gunicorn -b 0.0.0.0:59595 CollegeApp.wsgi || failure
