import sys
import simplejson
from termprint import termprint
from unittest import TestCase, TestSuite, TextTestRunner
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

from dbaccess import *
import settings

class AssertionError:
    # simple assertion error output
    def __init__(self, msg, exit=False):
        termprint("ERROR", msg)
        if exit:
            sys.exit(1)

# sample database table
class UserProfile(object):
    pass

class TestDB(TestCase):
    """ Base test class for ami functionality that will be used """
    host = getattr(settings, "DB_HOST")
    password = getattr(settings, "DB_PASS")
    user = getattr(settings, "DB_USER")
    dbname = getattr(settings, "DB_NAME")

    def __connect(self):
        """ Internal helper method to instantiate teh
        class and connect. """
        cl = db(dbhost=getattr(self, "host"),
                dbuser=getattr(self, "user"),
                dbpass=getattr(self, "password"),
                dbname=getattr(self, "dbname"))
        return cl

    def test_map_table(self):
        """ Test the db() class. """
        cl = self.__connect()
        # bind the table
        cl.connect()
        cl.map_table(UserProfile, "mainweb_userprofile")
        termprint("INFO", "\nAttributes for UserProfile class\n%s" % dir(UserProfile))
        # Search for results
        results = cl.select(UserProfile).filter_by(user_id='64')
        termprint("WARNING", "\nAttributes for results \n%s" % dir(results))
        self.assertTrue(results)
        cl.disconnect()
        for i in results:
            cl.connect()
            termprint("ERROR", "Result Object Row\n %s" % i)
            termprint("ERROR", dir(i))
            termprint("INFO", "Result Row\n%s" % i.__dict__)
            cl.disconnect()




if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(TestDB("test_map_table"))
    TextTestRunner(verbosity=2).run(suite)


