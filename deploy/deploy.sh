create_deployment() {
  python3 -c "import deploy.github as gh; gh.create_deployment()"
}

update_status() {
  python3 -c "import deploy.github as gh; gh.update_status('$1', '$2')"
}

failure() {
  update_status "$DEPLOY_ID" "failure"
  echo "failure" >"$(tty)" # to override /dev/null redirection
  exit 1
}

############################################################
DEPLOY_ID=$(create_deployment)

# switch to project directory
cd "$(dirname "$0")"/.. 2>/dev/null || failure

git pull || failure

update_status "$DEPLOY_ID" "in_progress"

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

update_status "$DEPLOY_ID" "success"

# run gunicorn
gunicorn -b 0.0.0.0:59595 CollegeApp.wsgi || failure
