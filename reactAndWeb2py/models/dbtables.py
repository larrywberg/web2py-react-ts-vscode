# -*- coding: utf-8 -*-
from gluon.contrib.appconfig import AppConfig

# from gluon.tools import Auth
# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# db.define_table('mytable', Field('myfield', 'string'))

# This is a sample table.  Replace for your app
db.define_table('entries',
    Field('userid', 'reference auth_user', default=auth.user_id, update=auth.user_id, writable=False ),
    Field('name', default=''),
    Field('place','string'),
    Field('thing','string'),
    Field('description','text')
)

# Run once with this uncommented to regenerate the sample data for the entries table
# db.entries.truncate()

# If there is no data yet let's reinitialize it
rows = db(db.entries.userid > 0).select()
if len(rows) < 1:
    db.entries.truncate()
    db.entries.insert(userid=1, name="Paris", place="France", thing="city", description="The city of lights must be visited once in your lifetime." )
    db.entries.insert(userid=1, name="Frog", place="Swamp", thing="Amphibian", description="There is nothing more interesting than frogs." )
    db.entries.insert(userid=1, name="Chora Church", place="Istanbul, Turkey", thing="Church", description="One of the most beautiful small churches in the world.  The mosaics are so old they look soft." )
    db.commit()
