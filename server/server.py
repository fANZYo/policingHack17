#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime
# external dependencies
from flask import Flask, request, send_from_directory, g
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit
from werkzeug.utils import secure_filename
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, resources='/')
app.config['UPLOAD_FOLDER'] = './temp/'
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
#app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, supports_credentials=True)
socketio = SocketIO(app)

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



@app.route('/files/<filename>')
def uploaded_file(filename):
    client  = get_db()
    db      = client['policeDB']
    images  = db.images
    imageMeta = images.find_one({'filename':filename})
    mimetype = imageMeta['content-type']
    return send_from_directory(app.config['UPLOAD_FOLDER'],
        filename, mimetype=mimetype)

"""
# /createReport

Creates a report to share information on.

"""
@app.route('/createCrime', methods=['POST'])
def createReport():
    try:
        # Get the data
        userData    = request.json
        crimeID     = generateID(32)
        officer     = userData['officer']
        name        = userData['name']
        description = userData['description']
        date        = datetime.now().isoformat()
        if 'coords' in userData:
            coords = userData['coords']
        if 'status' in userData:
            status = userData['status']
        else:
            status = 'Started'
        # Store it in the Database
        client      = get_db()
        db          = client['policeDB']
        reports     = db.reports
        form = {
            'crimeID':crimeID,
            'officer':officer,
            'name':name,
            'description':description,
            'date':date,
            'status':status,
            'location':{
            },
            'timeline':[]
        }
        if 'coords' in userData:
            form['location']['coords'] = coords
        reports.insert_one(form)
    except:
        return json.dumps({'error':True})
    # Return the crimeID so they can look it up instantly.
    return json.dumps({'crimeID':crimeID})

"""
# /updateCrime

Used to append to a report.

"""
@app.route('/updateCrime', methods=['POST'])
def updateReport():
    try:
        # Read the values in
        userData    = request.json
        crimeID     = userData['crimeID']
        name        = userData['title']
        description = userData['description']
        status      = userData['status']
        date        = datetime.now().isoformat()
        item = {
            "uuid":generateID(32),
            "title":name,
            "description":description,
            "status":status,
            "date":date
        }
        if 'isVictim' in userData:
            item['isVictim'] = userData['isVictim']
        # append this into the data structure
        client  = get_db()
        db      = client['policeDB']
        images  = db.images
        reports = db.reports
        if 'media' in userData:
            allMedia = []
            for image in images.find({'filename':{'$in':userData['images']}}):
                del image['_id']
                allMedia.append(image)
            item['media'] = allMedia
        reports.update(
            {'crimeID':crimeID},
            {"$push": {"timeline":item}}
        )
    except:
        return json.dumps({'error':True})
    socketio.emit(crimeID,{"updated":item})
    return json.dumps({'crimeID':crimeID})

"""
# /updateMeta

Method to call when you want to update the name, description, officer or
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
        crimeID    = userData['crimeID']
        if 'officer' in userData:
            form['officer'] = userData['officer']
        if 'name' in userData:
            form['name'] = userData['name']
        if 'description' in userData:
            form['description'] = userData['description']
        if form != {}:
            reports.update(
                {'crimeID':crimeID},
                {'$set':form}
            )
    except:
        return json.dumps({'error':True})
    
    return json.dumps({'crimeID':crimeID})

"""
# /uploadMedia

Allows you to upload files. These can then be added to a file.
"""
@app.route("/uploadMedia", methods=['POST'])
def uploadMedia():
    if 'file' not in request.files:
        return ''
    file = request.files['file']
    if file.filename == '':
        return ''
    filename = generateID(16)
    client  = get_db()
    db      = client['policeDB']
    images  = db.images
    filetype = file.content_type
    url = "http://192.168.1.34:5000/files/"+filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    images.insert_one(
    {
        'filename':filename,
        'content-type':filetype,
        'url':url
    })
    try:
        crimeID = request.form.get('crimeID')
        name = request.form.get('title')
        description = request.form.get('description')
        status = "on"
        date = datetime.now().isoformat()
        item = {
            "uuid":generateID(32),
            "title":name,
            "description":description,
            "status":status,
            "date":date
        }
        if 'isVictim' in request.form:
            item['isVictim'] = request.form.get('isVictim')
        # append this into the data structure
        client  = get_db()
        db      = client['policeDB']
        images  = db.images
        reports = db.reports
        allMedia = []
        print "AA"
        for image in images.find({'filename':filename}):
            del image['_id']
            allMedia.append(image)
        item['media'] = allMedia
        reports.update(
            {'crimeID':crimeID},
            {"$push": {"timeline":item}}
        )
    except:
        return json.dumps({})
    socketio.emit(crimeID,{"updated":item})
    return json.dumps({'filename':filename})


"""
# /deleteReport

Takes an ID of a report and deletes it.

"""
@app.route("/deleteReport", methods=['POST'])
def deleteReport():
    client  = get_db()
    db      = client['policeDB']
    reports = db.reports
    
    try:
        userData    = request.json
        crimeID     = userData['crimeID']
        reports.delete_one({'crimeID':crimeID})
    except:
        return json.dumps({'error':True})

    return json.dumps({'crimeID':crimeID})

"""
# /deleteUpdate

Takes an ID of a item in the state and removes it

"""
@app.route("/deleteState", methods=['POST'])
def deleteState():
    client  = get_db()
    db      = client['policeDB']
    reports = db.reports
    
    try:
        userData    = request.json
        crimeID     = userData['crimeID']
        uuidState   = userData['uuidState']
        reports.update(
            {'crimeID':crimeID},
            {'$pull':{'timeline':{'uuid':uuidState}}}
        )
    except:
        return json.dumps({'error':True})
    
    return json.dumps({'error':False})

"""
# /listReports

Lists reports managed by an Officer.

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
            'name':report['name'],
            'officer':report['officer'],
            'description':report['description'],
            'crimeID':report['crimeID']
        }
        listOfReports.append(form)

    return json.dumps({'reports':listOfReports})

"""
# /report/<id>

View a report in detail.

"""
@app.route('/report/<crimeID>')
def fetchReport(crimeID):
    client  = get_db()
    db      = client['policeDB']
    reports = db.reports
    
    report = reports.find_one({'crimeID':crimeID})
    if report == None:
        return json.dumps({'err':'cant find'})
    del report['_id']
    return json.dumps(report)

if __name__ == "__main__":
    socketio.run(app)
