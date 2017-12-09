#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime
# external dependencies
from flask import Flask, request, g
from pymongo import MongoClient

app = Flask(__name__)

# wrapper in case this gets changed in the future
def generateID(length):
    return os.urandom(length).encode('hex')

# preform database pooling with MongoDB
def get_db():
    if not hasattr(g, 'mongodb'):
        g.mongodb = MongoClient()
    return g.mongodb

# index page
@app.route('/')
def indexPage():
    return ''

"""
# /createReport

Creates a report to share information on.
"""
@app.route('/createCrime', methods=['POST'])
def createReport():
    try:
        # Get the data
        userData    = request.json
        uuid        = generateID(32)
        officer     = userData['officer']
        title       = userData['title']
        description = userData['description']
        # Store it in the Database
        client      = get_db()
        db          = client['policeDB']
        reports     = db.reports
        reports.insert_one({
            'uuid':uuid,
            'officer':officer,
            'title':title,
            'description':description,
            'status':[]
        })
    except:
        return json.dumps({'error':True})
    # Return the uuid so they can look it up instantly.
    return json.dumps({'uuid':uuid})

"""
# /updateCrime

Used to append to a report.
"""
@app.route('/updateCrime', methods=['POST'])
def updateReport():
    try:
        # Read the values in
        userData    = request.json
        uuid        = userData['uuid']
        title       = userData['title']
        description = userData['description']
        state       = userData['state']
        date        = datetime.now()
        item = {
            "uuid":generateID(32),
            "title":title,
            "description":description,
            "state":state,
            "date":date
        }
        # append this into the data structure
        client  = get_db()
        db      = client['policeDB']
        reports = db.reports
        reports.update(
            {'uuid':uuid},
            {"$push": {"status":item}}
        )
    except:
        return json.dumps({'error':True})
    
    return json.dumps({'uuid':uuid})

"""
# /updateMeta

Method to call when you want to update the title, description, officer or
status.

"""
@app.route('/updateMeta', methods=['POST'])
def updateReportMeta():
    client  = get_db()
    db      = client['policeDB']
    reports = db.reports

    try:
        form = {}
        userData    = request.json
        uuid        = userData['uuid']
        if 'officer' in userData:
            form['officer'] = userData['officer']
        if 'title' in userData:
            form['title'] = userData['title']
        if 'description' in userData:
            form['description'] = userData['description']
        if form != {}:
            reports.update(
                {'uuid':uuid},
                {'$set':form}
            )
    except:
        return json.dumps({'error':True})
    
    return json.dumps({'uuid':uuid})

"""
# /listReports

Lists reports managed by an Officer
"""
@app.route('/listReports')
def listReports():
    # connect to database
    client  = get_db()
    db      = client['policeDB']
    reports = db.reports

    # process the reports
    listOfReports = []
    for report in reports.find({}):
        # clean up mongos results so we can serialize it
        form = {
            'title':report['title'],
            'officer':report['officer'],
            'description':report['description']
        }
        listOfReports.append(form)

    return json.dumps({'reports':listOfReports})

"""
# /report/<id>

View a report in detail.
"""
@app.route('/report/<uuid>')
def fetchReport(uuid):
    client  = get_db()
    db      = client['policeDB']
    reports = db.reports
    
    report = reports.find_one({'uuid':uuid})
    if report == None:
        return json.dumps({'err':'cant find'})
    del report['_id']
    return json.dumps(report)

if __name__ == "__main__":
    app.run()
