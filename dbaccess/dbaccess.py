from sqlalchemy import create_engine, MetaData, Table, and_, Column, ForeignKey, \
Integer, String, DateTime
from sqlalchemy.orm import mapper, sessionmaker

# Authored Marcos Lopez / dev@scidentify.info


def db(dbhost, dbuser, dbpass, dbname):
    """ Connect to the database. Returns session, metadata, connection """
    engine = create_engine('mysql://%s:%s@%s/%s' % (
        dbuser, dbpass, dbhost, dbname
    ), echo=False)
    metadata = MetaData(engine)
    connection = engine.connect()
    sess = sessionmaker(bind=engine)
    session = sess()
    return session, metadata, connection

def map_table(metadata, cls, tbl, autoload=True, skip_table=False):
    """ Map the table to a class. skip_table will skip creating the 
    Table() object in this method, assuming its already provided 
    in the tbl argument. Additionally, set the mapped attribute on the 
    class object to true for testing purposes."""
    if not skip_table:
        tblobj = Table(tbl, metadata, autoload=autoload)
    else:
        tblobj = tbl
    mapper(cls, tblobj)
    # set it to mapped
    setattr(cls, "mapped", True)
    return cls

def db_disconnect(connection):
    """ Disconnect the connection """
    return connection.close()

def db_select(session, cls):
    """ perform a select query """
    return session.query(cls)

def db_filter(session, cls, col, value):
    """ Perform a select by query. """
    filters = {col: value}
    return session.query(cls).filter_by(**filters).all()

def db_update(session, cls, value, filterby):
    """Update the database by filterby and update with value.
    Required Arguments:
     - session = The session
     - cls = The mapped class table that you want to update
     - value = The kwarg values (dictionary) to update
     - filterby = The kwarg data to select the row to update.
    """
    return session.query(cls).filter_by(**filterby).update(**value)


    
