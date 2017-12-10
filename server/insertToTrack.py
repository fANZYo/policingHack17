import sys
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client['policeDB']
    reports = db.reportsToTrack
    reports.insert_one({'id':sys.argv[1]})
