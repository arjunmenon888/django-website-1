1)Create a virtual environment in the same directory as src
2)Activate the virtual environment and install the all the dependencies from requirement.txt
3)Create a static_cdn and media folder inside src folder
4)Run migrations and collect static (run following command in cmd : python manage.py makemigration,python manage.py migrate, python manage.py collectstatic)
5)Finally runserver (run following command in cmd : python manage.py runserver)
