import requests
import urllib
from gluon.contrib.markdown import markdown2

# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- index page. Ask the user to login.  If logged in, show the reactPage ----
def index():
    if auth.is_logged_in():
        response.view='default/readme.html'
        return readme()
    else:
        redirect(URL("user"))

def readme():
  from os.path import join as pathjoin
  with open(pathjoin(request.folder,'private', 'README.md')) as f:
    data = f.read()
  return dict(data=markdown2.markdown(data))    
  

# Sample view that uses react
def reactExample():
    response.view='default/reactPage.html'
    props = {
        "first_name": auth.user.first_name, 
        "last_name": auth.user.last_name,
        "email": auth.user.email,
        "entries": __getEntries()
    }
    return dict(props=props, reactBundle="bundle.js")
    
# Builds an array of entries to pass to props
def __getEntries():
    rows = db(db.entries.id > 0).select()
    entries = []
    for row in rows:
        entries.append({
            "name": row.name,
            "place": row.place,
            "thing": row.thing,
            "description":row.description
        })
    return dict(entries=entries)

def gridExample():
    query = db.entries.userid == auth.user_id
    export_classes = dict(csv=True, json=True, html=False,
                          tsv=False, xml=True, csv_with_hidden_cols=False,
                          tsv_with_hidden_cols=False)
    return dict(grid=SQLFORM.grid(query, details=True, showbuttontext=False, 
        fields=[db.entries.name], exportclasses=export_classes, advanced_search=False, maxtextlength=40,
        ))

def addEntry():
    form = SQLFORM(db.entries, fields = ['name', 'place', 'thing','description' ])
    if form.process().accepted:
        response.flash = 'Entry Added'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'Fill out form to add a new place'
    return dict(form=form)

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables:
        return dict(error="Missing table or no table with that name. Use /tablename at end of url")
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


# ---- test email sending ----
# def test_email():
#     res=mail.send(to=['someone@somewhere.com'],
#           subject='hello',
#           # If reply_to is omitted, then mail.settings.sender is used
#           reply_to='support@artengines.com',
#           message='hi there')
#     return dict(res=res)
