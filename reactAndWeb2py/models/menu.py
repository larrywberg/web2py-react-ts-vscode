# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
response.menu = [
   (T('Example'), False, URL('default', 'index'), [
      (T('readme'), False, URL('default', 'readme')),
      (T('reactExample'), False, URL('default', 'reactExample')),
      (T('gridExample'), False, URL('default', 'gridExample')),
      (T('api test json'), False, URL('api', 'v1')+'/entries/1.json'),
      (T('api test xml'), False, URL('api', 'v1')+'/entries/1.xml')
      ])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------
if not configuration.get('app.production'):
   _app = request.application
   if auth.has_membership('admin'):
      response.menu += [
         (T('Admin'), False, '',
            [
               (T('This App Panel'), False, URL('admin', 'default', 'design')+'/'+request.application),
               (T('Web2py Admin Panel'), False, URL('admin', 'default', 'site')),
               (  '------------------', False, ''),
               (T('Compile Typescript/React: npm run-script dev'), False, URL('dev', 'builddev')),
               (T('Install npm modules'), False, URL('dev', 'npminstall'))
            ]
         )
      ]
