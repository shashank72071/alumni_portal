# -*- coding: utf-8 -*-
db.define_table('newsroom',
               Field('title',requires=IS_NOT_EMPTY()),
               Field('body','text',requires=IS_NOT_EMPTY()),
               auth.signature
               )
db.define_table('news_comment',
                Field('newsroom','reference newsroom'),
                Field('post_comment',requires=IS_NOT_EMPTY()),
                auth.signature)

db.define_table('job',
    Field('Company_Name', 'string'),
    Field('Description', 'string'),
    Field('LastDate', 'datetime'),
    Field('em'))

db.define_table('applied_job',
    Field('rec_email','string'),
    Field('applier_name','string'),
    Field('applier_email','string'),
    Field('applied_com','string'),
    Field('description','string'))

db.define_table('eventlist',
    Field('event_name', 'string'),
    Field('description', 'string'),
    Field('event_date', 'date'),
	Field('venue','string'))

db.define_table('applied_event',
    Field('event_name','string'),
    Field('description','string'),
    Field('applier_email','string'),
    Field('applier_name','string'))

db.define_table('e_request',
    Field('request_type'),
    Field('description','string'),
    Field('request_date','datetime'),
    Field('applier_email','string'),
    Field('applier_name','string'))
