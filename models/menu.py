# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('IIIT-H Alumni Networks'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.iiit.ac.in",
                  _id="iiit-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index') ),
    (T('Events'), False,'#',[ (T('Display Events'),False,URL('default', 'eventdisplay')),(T('Create Event'),False,URL('default', 'eventlist'))]),
    (T('Jobs'), False,'#',[ (T('Display Job'),False,URL('default', 'jobdisplay')),(T('Post Job'),False,URL('default', 'job'))]),
    (T('Members'), False, URL('default', 'members') ),
    (T('Gallery'), False, URL('default', 'index') ),
    (T('Alumni Assist'), False, URL('default', 'e_request')),
    (T('About Us'), False, URL('default', 'index') )

]



if "auth" in locals():
    auth.wikimenu()
