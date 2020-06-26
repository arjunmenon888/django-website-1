Create a virtual environment in the same directory as src
Activate the virtual environment and install the all the dependencies from requirement.txt
Create a static_cdn folder inside src folder
do migrations and collect static (run following command in cmd : python manage.py makemigration,python manage.py migrate, python manage.py collectstatic)
Finally runserver (run following command in cmd : python manage.py runserver)
