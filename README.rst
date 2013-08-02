Python / MySQL example
----------------------
Used for a starting point or reference for any external scripts or python libraries that will access a 
MySQL database using class mappings

dev@scidentify.info

Usage
-----
The ``db()`` class accepts the following arguments

* dbuser
* dbname
* dbpass
* dbhost
* auto = use this to automatically connect


Testing
-------
Create a ``local_settings.py`` file and add the following variables

* DB_HOST = The host (blank will default to localhost)
* DB_USER = The database username
* DB_PASS = Password
* DB_NAME = Name of the database