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

Connecting
-----------
You can connect by calling the main method ``db()`` with the arguments described above.
When calling the connection function, it returns ``session, metadata, connection``


Mapping Tables
--------------
When the table is mapped for you, it will add (or set) the mapped attribute to True so the rest
of your applications can easily know if there were any issues before making any database queries.

Required Arguments: ``map_table(metadata, obj, database_table, autoload=False, skip_tables=False)``

* metadata = This is the metadata value that is returned from db()
* TableClass = The class that will be used to map to a database table
* database_table = This is a string name of the table or a Table() object schema (with skip_tables set to True)
* autoload = Boolean to autoload table metadata or use supplied object Table()
* skip_tables = Set to true if you are passing a database_table object instead of a name(string)

``cl.map_table(metadata, TableClass, sqlalchemy.Table(...), autoload=False, skip_tables=True)``

You can map a class to a table with the example below. By default, it will autoload its meta data. 
To override this, you can pass ``autoload=False`` in the map_table() method. 
By using ``skip_tables=True``, you will pass the custom Table() class that you've created instead of a
table name string. See http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html#declare-a-mapping



See http://docs.sqlalchemy.org/en/latest/orm/mapper_config.html for more details on your table class

Sample Code 
-----------
The following sample shows how to use this as a module, or you can refer to ``tests.py``

.. code-block:: python
	
	from dbaccess import *

	# this is your class that will be mapped to a database table
	class DatabaseAutoLoad(object):
		# use this to autoload the schema from the database 
		pass

	class DatabaseNoAutoload(object):
		# will not autoload schema, explicitly set by Table()
		pass

	# use this with skip_table = True and pass this object instead of table name string
	# it will bind this Table() instance in with DatabaseTableName() instead
	table_object = Table("tbl", metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(60)),
            Column('age', Integer),)

	# connect!
	session, metadata, connection = db(host, user, passwd, name)
	
	# map the tables (autoloads meta data)
	map_table(metadata, DatabaseAutoload, "sql_table_name")

	# map the other table (does not autoload, and passes a Table() instance instead of a name)
	map_table(metadata, DatabaseNoAutoload, table_object, autoload=False, skip_table=True)

	# search for something (arguments: session, MappedClass, column_name, value)
	results = db_filter(session, DatabaseAutoload, "user_id", 64)

	# done, now close!
	db_disconnect(connection)

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
