from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

# table class mappings
class SampleTable(object):
	pass

class UserProfile(object):
	pass

# database class 
class db(object):
	engine = None
	metadata = None

	dbuser = None
	dbpass = None
	dbname = None
	dbhost = None

	def __init__(self, dbuser=None, dbpass=None, dbname=None, dbhost=None, localhost=False):
		""" initialize connection parameters if passed """
		if dbuser:
			self.dbuser = dbuser
		if dbpass:
			self.dbpass = dbpass
		if dbname:
			self.dbname = dbname
		if dbhost:
			self.dbhost = dbhost

		if localhost:
			self.dbhost = 'localhost'
		
		if not self.connect():
			print 'Database connection error'
			exit

		# map the tables
		sampletable = Table('sampletable', self.metadata, autoload=True)
		userprofile = Table('userprofile', self.metadata, autoload=True)
		mapper(SampleTable, sampletable)
		mapper(UserProfile, userprofile)

		session = sessionmaker(bind=self.engine)
		self.session = session()

	def connect(self):
		self.engine = create_engine('mysql://%s:%s@%s/%s' % (
			self.dbuser, self.dbpass, self.dbhost, self.dbname
		), echo=False)
		self.metadata = MetaData(self.engine)
		return self.metadata

	def disconnect(self):
		self.engine.disconnect()
		
	
		
if __name__ == '__main__':
	# c = db()
	
