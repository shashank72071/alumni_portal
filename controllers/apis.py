# -*- coding: utf-8 -*-
# try something like



def getAlumni():
    al=db(db.auth_user).select()
    return al

def getEvents():
    ev=db(db.eventlist).select()
    return ev

def getJobs():
    jobs=db(db.job).select()
    return jobs

def getERequests():
    er=db(db.e_request).select()
    return er

def search(val,stype):
    if stype == "job":
        rows=db(db.auth_user.job.contains(val.lower())).select()
    elif stype == "location":
        rows=db(db.auth_user.current_location.contains(val)).select()
    elif stype == "name":
        rows=db(db.auth_user.first_name.contains(val)|db.auth_user.last_name.contains(val)).select()
    elif stype == "bachof":
        rows=db(db.auth_user.year_of_joining.year.contains(val)).select()
    elif stype == "program":
        rows=db(db.auth_user.program.contains(val)).select()
    else:
        rows=None
    return rows


def getApplierListForEvent(e):
    appliers=db(db.applied_event.event_name==e).select()
    return appliers

def getApplierListForJob(c):
    appliers=db(db.applied_job.applied_com==c).select()
    return appliers
