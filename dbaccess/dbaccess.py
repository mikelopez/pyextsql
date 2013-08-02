from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

# Authored Marcos Lopez / dev@scidentify.info

# table class mappings
class SampleTable(object):
    pass

class UserProfile(object):
    pass

# custom exceptions
class NoConnection(BaseException):
    pass

# database class 
class db(object):
    """ Main Database class. """
    engine = None
    metadata = None
    dbuser = None
    dbpass = None
    dbname = None
    dbhost = None
    connection = None

    def __init__(self, **kwargs):
        """ initialize connection parameters if passed """
        self.__set_kwargs(kwargs)
        if kwargs.get('auto', None):
            if not self.connect():
                raise NoConnection("Database connection error")
                exit
        self.start_session()

    def __set_kwargs(self, kwargs):
        """ Set the keyword arguments for init() """
        for k, v in kwargs.items():
            setattr(self, k, v)
        if kwargs.get('localhost', False) or not self.dbhost:
            setattr(self, "dbhost", "localhost")

    def map_table(self, cls, tbl):
        """ Map the table to a class """
        tblobj = Table(tbl, self.metadata, autoload=True)
        mapper(cls, tblobj)
        return cls

    def start_session(self):
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def connect(self):
        """ connects to the engine, returns database metadata """
        self.engine = create_engine('mysql://%s:%s@%s/%s' % (
            self.dbuser, self.dbpass, self.dbhost, self.dbname
        ), echo=False)
        self.metadata = MetaData(self.engine)
        self.connection = self.engine.connect()
        return self.engine, self.metadata

    def disconnect(self):
        return self.connection.close()

    def select(self, cls):
        """ erform a select query """
        return self.session.query(cls)

    
