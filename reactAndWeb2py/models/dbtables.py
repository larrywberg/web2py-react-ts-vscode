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
