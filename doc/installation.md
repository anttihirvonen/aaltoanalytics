=========================
Installation instructions
=========================

These installation instructions cover the installation on *nix platform that already has Python 2.5 > pre-installed. If you want to try this on Windows, I strongly suggest you to install Ubuntu or some other distro in Virtualbox and run from there. You have been warned.

Using these instructions you'll end up with a standard development environment with SQLite database. Packages will be installed in a virtual Python environment to keep them isolated from system-level changes. 

1. Install pip, virtualenv and virtualenvwrapper. (``sudo easy_install pip virtualenv virtualenvwrapper``)
2. Pull code from github.
3. Move to project root directory.
4. Create new virtual Python environment. (``mkvirtualenv --no-site-packages aaltoanalytics``)
5. Install requirements using pip. (``pip install -r config/requirements && pip install -r config/development_requirements.txt``)
6. Copy template settings from ``config/template_local.py`` to ``aaltoanalytics/settings/local.py`` and modify as you wish.
7. Create the database. (``python manage.py syncdb && python manage.py migrate``)
8. Run the development server. (``python manage.py runserver``)
9. Navigate to ``http://127.0.0.1:8000/mobile/`` and app should be running.

If you eg. accidentally close the terminal, just run ``workon aaltoanalytics`` to activate the virtual environment and you'll be able to run the ``python manage.py`` commands again.