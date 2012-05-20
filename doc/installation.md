=========================
Installation instructions
=========================

These installation instructions cover the installation on *nix platform that already has Python 2.5 > pre-installed.

1. Install pip, virtualenv and virtualenvwrapper. (sudo easy_install pip virtualenv virtualenvwrapper)
2. Pull code from github.
3. Move to project root directory.
4. Create new virtual Python environment. (mkvirtualenv --no-site-packages aaltoanalytics)
5. Install requirements using pip. (pip install -r config/requirements && pip install -r config/development_requirements.txt)
6. Copy template settings from "config/template_local.py" to "aaltoanalytics/settings/local.py" and modify as you wish.
7. Create database. (python manage.py syncdb && python manage.py migrate)
7. Run server. (python manage.py runserver)
8. Navigate to http://127.0.0.1:8000/mobile/ and app should be running.
