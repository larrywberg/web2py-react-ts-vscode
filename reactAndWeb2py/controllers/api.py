import requests
# import urllib

# -*- coding: utf-8 -*-
# try something like
def index():
    return dict(message="")

# ---- RESTfull API ----
# This really should require admin authentication
# @auth.requires_membership('admin')
# GET() examples:
#     http://127.0.0.1:8000/reactAndWeb2py/api/v1/entries/1883
#     http://127.0.0.1:8000/reactAndWeb2py/api/v1/entries/1883.json
#     http://127.0.0.1:8000/reactAndWeb2py/api/v1/entries/1883.xml
@request.restful()
def v1():

    def GET(tablename, id):
        if request.extension == 'xml':
            response.view = 'generic.xml'
        else:
            response.view = 'generic.json'
        if tablename == 'entries':
            return GET_entries(id)
        else:
            raise HTTP(400)

    def GET_entries(id):
        return dict(places = db.entries(id))

    def POST(tablename, **fields):
        # response.view = 'generic.json'
        if not tablename == 'entries':
            raise HTTP(400)
        retDict = dict()
        for key, value in fields.items():
            retDict.update({key : urllib.unquote(value)})
        return db.entries.validate_and_insert(**retDict)

    # def PUT(*args, **vars):
    #     return dict()

    # def DELETE(*args, **vars):
    #     return dict()

    return locals()



def testAPIPost():
    r = requests.post(URL('api','v1',scheme=True, host=True, args=['entries']),
             data = {'name':'Deschuttes Brewery',
                 'place':'Bend, OR',
                 'thing': 'brewery',
                 'description':'some good burgers.  Red Chair beer my favorite'
             })
    return dict(result=r)


def testAPIGet():
    response.view = 'generic.json'
    r = requests.get(URL('api','v1',scheme=True, host=True, args=['entries','1.json'], auth=('admin@example.com', 'password')))
    return dict(status_code =  r.status_code, headers = r.headers, content = r.content)
