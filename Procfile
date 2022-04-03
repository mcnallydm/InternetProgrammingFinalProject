web: gunicorn --chdir ipfinal ipfinal.wsgi:application --log-file - --log-level debug
release: python ipfinal/manage.py migrate