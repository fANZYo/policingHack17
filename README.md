Policing hackathon 2017

## The problem
The current system by which police officers communicate information to victims is painful and can lead to arguments going back and forth. This can often lead to degrading officer mental wellbeing.

## Our solution
A communication system to share updates on the investigation of a crime, combined with notifications, status and further information regarding the progress of the investigation and optional information explaining some of the reasoning behing the decisions made by the officer.

## Wireframe
![UI](https://i.imgur.com/hwGu6sg.jpg?1)

## Flowchart
![flowchart](https://i.imgur.com/C6IuE51.jpg?1)

JSON file:
```
{
  "crimeID": "000001",
  "name": "Kidnapping of doodle",
  "date": "2017-12-10T02:18:21.549358",
  "description": "Criminally good hackathon project",
  "status": "Investigating",
  "officer": "Somebody",
  "location": {},
  "timeline": [
    {
      "date": "2017-12-10T02:20:21.549358",
      "title": "Looking for evidence",
      "description": "",
      "state": "pending"
    },
    {
      "date": "2017-12-10T02:30:21.549358",
      "title": "Handed self administered interview forms",
      "description": "Used because of the large amount of witnesses",
      "state": "pending"
    },
    {
      "date": "2017-12-10T02:40:21.549358",
      "title": "Found doodle",
      "description": "Found doodle in the cookie jar",
      "state": "done",
      "media": [
        {
          "name": "Picture of doodle in the cookie jar",
          "content-type": "image/jpeg",
          "url": "https://placekitten.com/200/300"
        }
      ]
    }
  ]
}
```

## Scripts
To install the project:
```
$ npm install
```
To run the dev server:
```
$ npm start
```
To run the server:
```
FLASK_APP=server.py flask run
```

## Dependencies
For the backend server, you need the following Python dependencies: `flask`, `flask_cors`, `pymongo`, `socketIO_client`, `flask_socketio`
MongoDB is required for the backend.
