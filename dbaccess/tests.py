import sys
import simplejson
from termprint import termprint
from unittest import TestCase, TestSuite, TextTestRunner

from dbaccess import *
import settings

class AssertionError:
    # simple assertion error output
    def __init__(self, msg, exit=False):
        termprint("ERROR", msg)
        if exit:
            sys.exit(1)

# this is your class that will be mapped to a database table
class DatabaseAutoload(object):
    # use this to autoload the schema from the database 
    pass

class DatabaseNoAutoload(object):
    # will not autoload schema, explicitly set by Table()
    pass

# use this with skip_table = True and pass this object instead of table name string
# it will bind this Table() instance in with DatabaseTableName() instead
table_object = Table("mainweb_userprofile", MetaData(),
        Column('id', Integer, primary_key=True),
        Column('user_id', Integer),
        Column('zip', String(10)),
        Column('city', String(60)),)




class TestDB(TestCase):
    """ Base test class for ami functionality that will be used """
    host = getattr(settings, "DB_HOST")
    password = getattr(settings, "DB_PASS")
    user = getattr(settings, "DB_USER")
    dbname = getattr(settings, "DB_NAME")


    def __connect(self):
        """ Internal helper method to instantiate teh
        class and connect. """
        session, metadata, connection = db(dbhost=getattr(self, "host"),
                dbuser=getattr(self, "user"),
                dbpass=getattr(self, "password"),
                dbname=getattr(self, "dbname"))
        return session, metadata, connection


    def test_map_table(self):
        """ Test the db() methods. """
        # connect!
        session, metadata, connection = self.__connect()
        self.assertTrue(connection)
        
        # map the tables (autoloads meta data)
        user_profile_auto = map_table(metadata, DatabaseAutoload, "mainweb_userprofile")
        # map the other table (does not autoload, and passes a Table() instance instead of a name)
        user_profile = map_table(metadata, DatabaseNoAutoload, table_object, autoload=False, skip_table=True)

        # search for something (arguments: session, MappedClass, column_name, value)
        results_auto = db_filter(session, user_profile_auto, "user_id", '64')
        results = db_filter(session, user_profile, "user_id", '64')

        termprint("INFO", "Printing the results....\n")
        # show the results
        for i in results_auto:
            termprint("WARNING", "\t- %s" % i.id)

        for i in results:
            termprint("ERROR", "\t- %s" % i.id)

        # done, now close!
        db_disconnect(connection)


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(TestDB("test_map_table"))
    TextTestRunner(verbosity=2).run(suite)


