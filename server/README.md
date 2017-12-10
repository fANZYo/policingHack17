# Backend Server

This directory contains the source code for the backend server.

## Endpoint

/createCrime - JSON POST, Required: officer, title, description; Optional: coords

Creates a new crime report, returns the ID

* /updateCrime - JSON POST, Required: crimeid, name, description, state; Optional: media

Updates the crime progress. Media takes a list of filenames from the upload function.

* /updateMeta - JSON POST, Required: CrimeID; Optional:  officer, title, description

Allows you to update the meta information for a crime.

* /uploadMedia - FILE POST, Required: A file

Returns the filename.

* /deleteReport - JSON POST, Required: crimeID, uuid of update.

Removes an updated published on a report.

* /listReports - GET

Lists all the reports

* /report/<crimeId> - GET

Gets the document for a Crime.

