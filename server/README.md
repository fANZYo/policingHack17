# Backend Server

This directory contains the source code for the backend server.

## Endpoints

/createCrime - JSON POST, Required: *(string)* officer, *(string)* name, *(string)* description; Optional: *(string)* coords, *(string)* status

Creates a new crime report, returns the ID

* /updateCrime - JSON POST, Required: *(string)* crimeID, *(string)* name, *(string)* description, *(string)* status; Optional: *(FormData)* media, *(bool)* isVictim

Updates the crime progress. Media takes a list of filenames from the upload function.
isVictim shows if the post is by the victim, allowing them to add extra information (this is only useful while the officer's client version is under development)

* /updateMeta - JSON POST, Required: *(string)* crimeID; Optional: *(string)* officer, *(string)* name, *(string)* description

Allows you to update the meta information for a crime.

* /uploadMedia - FILE POST, Required: A file

Returns the filename.

* /deleteReport - JSON POST, Required: *(string)* crimeID, *(string)* uuid.

Removes an updated published on a report.

* /listReports - GET

Lists all the reports

* /report/<crimeId> - GET

Gets the document for a Crime.

## The Tracking

There is an SMS class for sending messages via Twilio, a script for watching updates via socket.io and one script to insert data in the database.
