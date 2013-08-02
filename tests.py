import sys
import simplejson
from termprint import termprint
from unittest import TestCase, TestSuite, TextTestRunner
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

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
        self.assertTrue(cl.connect())
        self.assertTrue(cl.disconnect())
        return cl

    def test_map_table(self):
        """ Test the db() class. """
        cl = self.__connect()
        # bind the table
        cl.map_table(UserProfile, "mainweb_userprofile")
        termprint("WARNING", dir(UserProfile))
        results = cl.session.query(UserProfile).filter_by(status='active')
        termprint("WARNING", results)
        self.assertTrue(len(results))




if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(TestDB("test_map_table"))
    TextTestRunner(verbosity=2).run(suite)


