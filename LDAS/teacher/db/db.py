#!/usr/bin/env python
import pymongo

host = 'localhost'
port = 27017
db = 'db'
client = pymongo.MongoClient(host, port)

client[db].add_user(
  'Database Administrator',
  'admin',
  roles=[
    {
      'role': 'userAdmin',
      'db': db,
    },
  ],
)

client[db].add_user(
  'Read and write User',
  'write',
  roles=[
    {
      'role': 'readWrite',
      'db': db,
    },
  ],
)

client[db].add_user(
  'ROM User',
  'read',
  roles=[
    {
      'role': 'read',
      'db': db,
    },
  ],
)
