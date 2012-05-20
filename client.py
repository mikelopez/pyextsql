#!/usr/bin/env python

# Marcos Lopez - dev@scidentify.info
import os, sys

sys.path.append('/home/mike')

from dbaccess import *
import time

# set the db class
d = db()

"""check if its already running 
you can comment this out if run time of this script is less
than the frequency of time to run this script at
(exectime < run-frequency)
"""
for i in os.popen('ps aux | grep client.py').readlines():
  if 'python client.py' in i and not str(os.getpid()) in i:
    print 'Currently running in the background, waiting...'
    sys.exit()



print '===========================\n\n\nStarting\n\n\n'
print '===========================\n\n\n'

from client_utils import *

# search for something in user table - pass table class mapping to query()
# getting all active users
results = d.session.query(UserProfile).filter_by(status='active')


for i in results:
  print i.user_id
  # get single object by its pk
  results_get = d.session.query(UserProfile).get(i.id)

  # update an entry - will set status to inactive
  update_data = {'status': 'inactive'}
  d.session.query(UserProfile).filter_by(id=id).update(update_data)
  # commit the changes!
  d.session.commit()

  print 'Inactivated user id: %s' % (i.user_id)

