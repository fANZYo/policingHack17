# Backend Server

This directory contains the source code for the backend server.

## Endpoints

/createCrime - JSON POST, Required: officer, name, description; Optional: coords, status

Creates a new crime report, returns the ID

* /updateCrime - JSON POST, Required: crimeID, name, description, status; Optional: media, isVictim

Updates the crime progress. Media takes a list of filenames from the upload function.
isVictim shows if the post is by the victim, allowing them to add extra information

* /updateMeta - JSON POST, Required: crimeID; Optional:  officer, name, description

Allows you to update the meta information for a crime.

* /uploadMedia - FILE POST, Required: A file

Returns the filename.

* /deleteReport - JSON POST, Required: crimeID, uuid of update.

Removes an updated published on a report.

* /listReports - GET

Lists all the reports

* /report/<crimeId> - GET

Gets the document for a Crime.

## The Tracking

There is an SMS class for sending messages via Twilio, a script for watching
updates via socket.io and one script to insert data in the database.
