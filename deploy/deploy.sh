create_deployment() {
  python -c "import deploy.github as gh; gh.create_deployment()"
}

update_status() {
  python -c "import deploy.github as gh; gh.update_status('$1', '$2')"
}

failure() {
  update_status "$DEPLOY_ID" "failure"
  exit 1
}

############################################################
# if first two commands (i.e., cd and source) fail then
# no deployment will be created and the script will simply
# exit. This is due to the fact that creating a deployment
# requires the virtualenv to be activated, therefore a
# chicken and the egg problem arises.

# switch to project directory
cd "$(dirname "$0")"/.. 2>/dev/null || exit

{
  # activate virtual environment
  source ./venv/bin/activate || exit

  # get deployment id
  DEPLOY_ID=$(create_deployment)
  update_status "$DEPLOY_ID" "in_progress"

  git pull || failure
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
