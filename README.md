A dummy project to recreate https://github.com/carljm/django-model-utils/issues/142

To hit the bug,

./manage.py migrate
./manage.py createsuperuser
./manage.py runserver

Then login to admin and navigate to http://127.0.0.1:8000/admin/bug/foo/add/
