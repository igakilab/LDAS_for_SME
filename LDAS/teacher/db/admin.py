#!/usr/bin/env python
import pymongo

host = 'localhost'
port = 27017
db = 'admin'
client = pymongo.MongoClient(host, port)

client[db].add_user(
  'admin',
  'password',
  roles=[
    {
      'role': 'userAdminAnyDatabase',
      'db': db,
    },
  ],
)
