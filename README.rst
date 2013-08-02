Python / MySQL example
----------------------
Used for a starting point or reference for any external scripts or python libraries that will access a 
MySQL database using class mappings

dev@scidentify.info

Install 
--------
* Run ``pip install -r requirements.txt``
* Run ``python setup.py install`` (as sudo or virtualenv)


Usage
-----
The ``db()`` class accepts the following arguments

* dbuser
* dbname
* dbpass
* dbhost
* auto = use this to automatically connect

The following sample shows how to use it as a module, or you can refer to tests.py

.. code-block:: python
	
	from dbaccess import *

	class DatabaseTableName(object):
		pass

	# connect!
	cl = db(host='x.x.x.x', dbuser='username', dbpass='passwd', dbname='name')
	cl.connect()

	# map the tables
	cl.map_table(DatabaseTableName, "sql_table_name")

	# search for something
	results = cl.select(DatabaseTableName).filter_by(user_id='64')

	# done, now close!
	cl.close()

	# show the results
	for i in results:
		print i.id




Testing
-------
Create a ``local_settings.py`` file and add the following variables

* DB_HOST = The host (blank will default to localhost)
* DB_USER = The database username
* DB_PASS = Password
* DB_NAME = Name of the database
